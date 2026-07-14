import os
import time
import random
import sys

# Windows에서 키 입력을 확인하기 위한 라이브러리
try:
    import msvcrt
except ImportError:
    print("이 게임은 Windows 환경의 콘솔에 최적화되어 있습니다.")
    sys.exit()

# 게임 설정
WIDTH = 20
HEIGHT = 15
PLAYER_CHAR = "A"
ALIEN_CHAR = "W"
BULLET_CHAR = "|"
EMPTY_CHAR = " "

class Game:
    def __init__(self):
        self.player_x = WIDTH // 2
        self.bullets = []
        self.aliens = []
        self.score = 0
        self.game_over = False
        self.alien_direction = 1  # 1은 오른쪽, -1은 왼쪽
        self.move_counter = 0     # 외계인 이동 타이밍을 계산하는 카운터
        self.total_aliens = 0     # 초기 외계인 수 (속도 계산용)
        self.spawn_aliens()

    def spawn_aliens(self):
        """외계인 부대를 생성합니다."""
        self.aliens = []
        for y in range(1, 4):
            for x in range(2, WIDTH - 2, 2):
                self.aliens.append([x, y])
        self.total_aliens = len(self.aliens)

    def draw(self):
        """화면을 그립니다."""
        # 화면 초기화 (Windows: cls, Mac/Linux: clear)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"Score: {self.score} | Controls: A(Left), D(Right), W(Shoot), Q(Quit)")
        print("-" * (WIDTH + 2))

        for y in range(HEIGHT):
            line = "|"
            for x in range(WIDTH):
                if x == self.player_x and y == HEIGHT - 1:
                    line += PLAYER_CHAR
                elif [x, y] in self.aliens:
                    line += ALIEN_CHAR
                elif [x, y] in self.bullets:
                    line += BULLET_CHAR
                else:
                    line += EMPTY_CHAR
            line += "|"
            print(line)
        
        print("-" * (WIDTH + 2))

    def update(self):
        """게임 로직을 업데이트합니다."""
        # 총알 이동
        for bullet in self.bullets[:]:
            bullet[1] -= 1
            if bullet[1] < 0:
                self.bullets.remove(bullet)
            else:
                # 충돌 체크
                for alien in self.aliens[:]:
                    if bullet == alien:
                        self.aliens.remove(alien)
                        if bullet in self.bullets: self.bullets.remove(bullet)
                        self.score += 10
                        break

        if self.aliens:
            # 남은 외계인 수에 따라 속도 결정 (외계인이 적을수록 move_delay가 작아짐)
            # 기본 15프레임마다 이동 -> 외계인이 줄어들면 최소 2프레임까지 빨라짐
            move_delay = max(2, int(15 * (len(self.aliens) / self.total_aliens)))
            
            self.move_counter += 1
            if self.move_counter >= move_delay:
                self.move_counter = 0
                
                move_down = False
                # 화면 끝에 닿았는지 확인
                for alien in self.aliens:
                    next_x = alien[0] + self.alien_direction
                    if next_x < 0 or next_x >= WIDTH:
                        move_down = True
                        break
                
                if move_down:
                    # 방향을 바꾸고 한 칸 아래로 내려옴
                    self.alien_direction *= -1
                    for alien in self.aliens:
                        alien[1] += 1
                else:
                    # 옆으로 이동
                    for alien in self.aliens:
                        alien[0] += self.alien_direction

        # 3. 게임 오버 조건 체크
        for alien in self.aliens:
            if alien[1] >= HEIGHT - 1: # 외계인이 바닥에 닿으면
                self.game_over = True

        # 외계인이 다 사라지면 새로 생성
        if not self.aliens:
            self.spawn_aliens()

    def run(self):
        """메인 게임 루프"""
        while not self.game_over:
            self.draw()
            self.update()

            # 키 입력 처리 (비동기)
            if msvcrt.kbhit():
                try:
                    # decode 시 errors='ignore'를 추가하여 에러를 방지합니다.
                    key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                except UnicodeDecodeError:
                    key = "" # 디코딩 실패 시 무시
                    
                if key == 'a' and self.player_x > 0:
                    self.player_x -= 1
                elif key == 'd' and self.player_x < WIDTH - 1:
                    self.player_x += 1
                elif key == 'w':
                    self.bullets.append([self.player_x, HEIGHT - 2])
                elif key == 'q':
                    print("Game Quit!")
                    break

            time.sleep(0.05) # 게임 속도 조절

        self.draw() # 마지막 화면 출력
        print("💥 GAME OVER! 외계인이 침공했습니다! 💥")
        print(f"Final Score: {self.score}")

if __name__ == "__main__":
    game = Game()
    game.run()