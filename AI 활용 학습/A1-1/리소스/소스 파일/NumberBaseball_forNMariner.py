import random

def play_game():
    # 1~9 사이의 서로 다른 숫자 3개 생성
    numbers = random.sample(range(1, 10), 3)
    print("숫자 야구 게임을 시작합니다!")

    # 시도 횟수를 기록할 변수 초기화
    attempts = 1

    while True:
        guess = input(f"[{attempts}회차] 3자리 숫자를 입력하세요 (예: 123): ")

        # 입력 유효성 검사
        if len(guess) != 3 or not guess.isdigit():
            print("잘못된 입력입니다. 3자리 숫자를 입력해주세요.")
            continue

        guess_list = [int(d) for d in guess]
        strike = 0
        ball = 0

        # 스트라이크, 볼 판정
        for i in range(3):
            if guess_list[i] == numbers[i]:
                strike += 1
            elif guess_list[i] in numbers:
                ball += 1

        if strike == 3:
            print(f"3 스트라이크! {attempts}번 만에 정답을 맞추셨습니다.")
            break
        else:
            print(f"{strike} 스트라이크, {ball} 볼")
            attempts += 1

if __name__ == "__main__":
    play_game()