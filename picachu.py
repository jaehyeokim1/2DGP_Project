from pico2d import *

# 캔버스 열기
open_canvas()

# 스프라이트 시트 이미지 로드
sprite_sheet = load_image('sprite_sheet.png')  # sprite_sheet.png 파일을 지정하세요.

# 피카츄의 클립 영역 (가정: 피카츄의 가로 크기: 100, 세로 크기: 100, 시작 위치: (0, 0))
pikachu_x = 130  # 스프라이트 시트에서 피카츄의 x 좌표
pikachu_y = 550  # 스프라이트 시트에서 피카츄의 y 좌표
pikachu_width = 70  # 피카츄의 가로 크기
pikachu_height = 70  # 피카츄의 세로 크기

# 배경색 설정 (선택 사항)
clear_canvas()

# 피카츄 그리기
sprite_sheet.clip_draw(pikachu_x, pikachu_y, pikachu_width, pikachu_height, 400, 50)  # 화면 중앙에 피카츄 그리기

# 화면 업데이트
update_canvas()

# 잠시 대기 (5초)
delay(1)

# 캔버스 닫기
close_canvas()
