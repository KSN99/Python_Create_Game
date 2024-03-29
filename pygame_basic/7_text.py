import pygame

pygame.init() #초기화(반드시 해줘야함)

#게임 화면 크기 설정
screen_width = 480 # 가로 
screen_height= 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Ball Game") # Name of the game . 

# FPS
clock = pygame.time.Clock()

# import background image
background = pygame.image.load("C:\\Python_Project\\project1\\PYTHON_PROJECT1\\pygame_basic\\background.png")

#import sprite (Character)
character = pygame.image.load("C:\\Python_Project\\project1\\PYTHON_PROJECT1\\pygame_basic\\character.png")
character_size = character.get_rect().size # size of image
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)  #  the size of widht of screen
character_y_pos = screen_height - character_height # 화면 세로 키그 가장 아래

# 이동할 좌표 설정. 
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# Enemy character
enemy = pygame.image.load("C:\\Python_Project\\project1\\PYTHON_PROJECT1\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size # size of image
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width/2)  #  the size of widht of screen
enemy_y_pos = (screen_height/2) - (enemy_height/2)

# 폰트 정의 
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 ( 폰트 , 크기 )

#총 시간
total_time = 10 

#시작 시간
start_ticks= pygame.time.get_ticks() #시작 tick 을 받아옴 

# Event Loop 
running = True # Is the game on the process? 
while running:
    dt = clock.tick(60) # 초당 프레임 수 . 

# 캐릭터가 100 만큼 이동을 해야함. 
    for event in pygame.event.get(): # What kind of evnet happened? 
        if event.type== pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False 
    
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽으로 
                to_x -=character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x +=character_speed
            elif event.key== pygame.K_UP: 
                to_y -=character_speed
            elif event.key == pygame.K_DOWN:
                to_y +=character_speed

        if event.type== pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_y = 0 
   
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt 

    if character_x_pos <0:
        character_x_pos = 0
    
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리 
    if character_y_pos <0:
        character_y_pos = 0 
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌처리를 위한 rect 정보 업데이트 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요.")
        running = False 
    

    screen.blit(background, (0,0)) # drawing background   
    screen.blit(character, (character_x_pos, character_y_pos)) #캐맅터 그리기 
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) #적그리기

    # 타이머 집어 넣기
    #경과 시간 계산 
    elapsed_time = (pygame.time.get_ticks()- start_ticks) /1000 #경과 시간을 1000으로 나ㅜㄴ어 초단위로 표시 
    timer = game_font.render(str(int(total_time - elapsed_time)), True,(255, 255, 2555))
    #출력할 글자, tRUE, 글자 색상
    screen.blit(timer,(10,10))

    #만약 시간이 0 이하면 게임 종료. 
    if total_time - elapsed_time <=0:
        print("Time out")
        running = False

    pygame.display.update()  # Drawing backround again. 

# 잠시 대기
pygame.time.delay(2000)    
# pygame ended 
pygame.quit()