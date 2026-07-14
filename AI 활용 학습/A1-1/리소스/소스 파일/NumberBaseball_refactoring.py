import random

class NumberBaseball:
    def __init__(self, digit_count=3):
        self.digit_count = digit_count
        self.target_numbers = self._generate_numbers()

    def _generate_numbers(self):
        """중복 없는 랜덤 숫자 생성"""
        return random.sample(range(1, 10), self.digit_count)

    def validate_input(self, user_input):
        """사용자 입력값 검증"""
        if not user_input.isdigit() or len(user_input) != self.digit_count:
            return False, f"{self.digit_count}자리 숫자를 입력해야 합니다."
        if len(set(user_input)) != self.digit_count:
            return False, "중복된 숫자는 사용할 수 없습니다."
        return True, ""

    def check_score(self, guess_str):
        """스트라이크와 볼 개수 계산"""
        guess = [int(d) for d in guess_str]
        strike = sum(1 for g, t in zip(guess, self.target_numbers) if g == t)
        # 전체 겹치는 숫자 개수에서 스트라이크를 빼면 볼의 개수
        ball = len(set(guess) & set(self.target_numbers)) - strike
        return strike, ball

    def start(self):
        print(f"--- {self.digit_count}자리 숫자 야구 게임을 시작합니다! [회차/아웃/홈런] ---")
        attempts = 0
        out_count = 0  # 아웃 카운트 변수 추가

        while True:
            user_input = input(f"[{attempts + 1}/{out_count}/0] 숫자를 입력하세요: ").strip()
            is_valid, error_msg = self.validate_input(user_input)
            
            if not is_valid:
                print(f"[오류] {error_msg}")
                continue

            attempts += 1
            strike, ball = self.check_score(user_input)

            if strike == self.digit_count:
                print(f"축하합니다! 총 {attempts}번 만에 맞추셨습니다! 🏠🏃")
                break

            # 아웃 처리
            if attempts % 3 == 0:
                out_count += 1

                # 전체 3칸 중 아웃된 만큼 🔴, 나머지는 ⚪
                # 예: 1아웃 -> 🔴⚪⚪ / 2아웃 -> 🔴🔴⚪ / 3아웃 -> 🔴🔴🔴
                scoreboard = "🔴" * out_count + "⚪" * (3 - out_count)
                # if out_count < 3:
                print(f"⚠️ 3번 시도 후 아웃! 현재 아웃: {scoreboard}")
            
            print(f"결과: {strike} Strike, {ball} Ball")

            # 게임 오버 판정
            if out_count == 3:
                print("\n" + "="*30)
                print(f"😱 3아웃! GAME OVER")
                print(f"정답은 {self.target_numbers}였습니다. 다음에 다시 도전하세요!")
                print("="*30)
                break

if __name__ == "__main__":
    game = NumberBaseball(3) # 4자리로 변경하고 싶으면 4를 넣으면 됩니다.
    game.start()