import pygame

pygame.init() #초기화(반드시 해줘야함)

#게임 화면 크기 설정
screen_width = 480 # 가로 
screen_height= 640 # 세로

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Ball Game") # Name of the game . 

# import background image

background = pygame.image.load("C:\\Python_Project\\project1\\PYTHON_PROJECT1\\pygame_basic\\background.png")


# Event Loop 
running = True # Is the game on the process? 
while running:
    for event in pygame.event.get(): # What kind of evnet happened? 
        if event.type== pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False 
    #screen.fill((0,0,255)) -> Filling the background color not using png. image 
    screen.blit(background, (0,0)) # drawing background 

    pygame.display.update()  # Drawing backround again. 

# pygaem ended 
pygame.quit()