import pygame
import random
import math

pygame.init()

bg_x = 0
player_x = 0
bullet_x = 0
player_speed = 2
speed = 12
is_jump = False
mouse_pos = 0
jump_count = 20
bullet_count = 0
bullet_have = 5
zombie_speed = 8
gameplay = True
heal_have = 10
go_sound = False
zombie_count = [ ]
box_count = 0
box_pos = 2048
shit_count = 0
shit_pos = 2048
shit_have = 0
heal_count = 0
heal_pos = 2048
bullet_y = 793
bullet_y1 = 0
dron_count = 0
dron_x = 2005
dron_y = 200
mouse = pygame.mouse.get_pos()
mouse_y = mouse[1]

screen = pygame.display.set_mode((600,300))
clock = pygame.time.Clock()
bg1 = pygame.image.load("images/bg1.jpg")
magazine = pygame.image.load("images/magazine.png")
tank = pygame.image.load("images/tank.png")
bullet1 = pygame.image.load("images/bullet.png")
zombie = pygame.image.load("images/zombie.png")
heart = pygame.image.load("images/heart.png")
box = pygame.image.load("images/box.png")
heal = pygame.image.load("images/heal.png")
shit1 = pygame.image.load("images/shit1.png")
shit11 = pygame.image.load("images/shit.png")
aim = pygame.image.load("images/aim.png")
dron1 = pygame.image.load("images/dron.png")
bg_sound = pygame.mixer.Sound("sounds/bg.mp3")
udar_sound = pygame.mixer.Sound("sounds/udar.mp3")
damage = pygame.mixer.Sound("sounds/damage.mp3")
zombie_sound = pygame.mixer.Sound("sounds/zombie.mp3")
box_sound = pygame.mixer.Sound("sounds/box.mp3")
game_over = pygame.mixer.Sound("sounds/gameover.mp3")
get_sound = pygame.mixer.Sound("sounds/get.mp3")
dron_sound = pygame.mixer.Sound("sounds/dron.mp3")
font = pygame.font.Font("fonts/font/font.ttf",75)
bullet_label = font.render(str(bullet_have),False,(255,0,0))
heal_label = font.render(str(heal_have),False,(255,0,0))
game_over_label = font.render("Game Over",False,(255,0,0))
restart_label = font.render("restart",False,(255,0,0),(255,255,255))


new_width = bullet1.get_width() // 3.5
new_height = bullet1.get_height() // 3.5
bullet = pygame.transform.scale(bullet1, (new_width, new_height))

new_width1 = shit11.get_width() // 1.5
new_height1 = shit11.get_height() // 1.5
shit = pygame.transform.scale(shit11, (new_width1, new_height1))

new_width2 = dron1.get_width() // 1.5
new_height2 = dron1.get_height() // 1.5
dron = pygame.transform.scale(dron1, (new_width2, new_height2))


bg_sound.play( )


zombie_x =  bg_x + 2000

zombie_timer = pygame.USEREVENT + 1
box_timer = pygame.USEREVENT + 2
shit_timer = pygame.USEREVENT + 3
heal_timer = pygame.USEREVENT + 4
dron_timer = pygame.USEREVENT + 5
pygame.time.set_timer(zombie_timer,random.randint(3000,6000))
pygame.time.set_timer(box_timer,random.randint(12000,18000))
pygame.time.set_timer(shit_timer,random.randint(18000,24000))
pygame.time.set_timer(heal_timer,random.randint(24000,30000))
pygame.time.set_timer(dron_timer,random.randint(10000,15000))


running = True
while running:
    keys =pygame.key.get_pressed() 
    for event in pygame.event.get():
            if keys[pygame.K_BACKSPACE] :  
                pygame.quit() 
                running = False
            if event.type == zombie_timer:
                zombie_count.append(zombie.get_rect(topleft=(2048,726)))
            if event.type == shit_timer and shit_count == 0:
                shit_count += 1
                shit_pos = 2048
            if event.type == box_timer and box_count == 0:
                box_count += 1
                box_pos = 2048        
            if event.type == heal_timer and heal_count == 0:
                heal_count += 1
                heal_pos = 2048        
            if event.type == dron_timer and dron_count == 0:
                dron_count += 1
                dron_x  = 2050
                dron_y = 200        
            
    
    restart_label_rect = restart_label.get_rect(topleft =(730,600)) 
    
        
           
    screen.blit(bg1,(bg_x,0))
    
    if gameplay:
        screen.blit(bg1,(bg_x + 2000,0))
        screen.blit(bg1,(bg_x - 2000,0))
        screen.blit(magazine,(0,20))
        screen.blit(heart,(1700,20))
        screen.blit(tank,(player_x + 100,680))
        screen.blit(bullet_label,(150,40))
        screen.blit(heal_label,(1850,40))
        player_rect = tank.get_rect(topleft=(player_x + 100, 680))
        mouse = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        if shit_have > 0:
        	screen.blit(shit1,(1500,20))
        
        if bullet_count > 0:
            screen.blit(bullet1,(bullet_x,bullet_y))
            bullet_rect = bullet.get_rect(topleft = (bullet_x,bullet_y))
#            pygame.draw.rect(screen,"Red",(bullet_x,793,73,25))
        if box_count > 0:
             screen.blit(box,(box_pos,800))
             box_rect = box.get_rect(topleft = (box_pos,800))
             if box_pos < -10:
                 box_count = 0
             if player_rect.colliderect(box_rect):
                 box_sound.play()
                 box_count = 0
                 box_pos = 2048
                 if bullet_have <= 14:
                     bullet_have += 6
                 else:
                 	bullet_have = 20
        
        if shit_count > 0 and shit_have == 0:
             screen.blit(shit,(shit_pos,800))
             shit_rect = shit.get_rect(topleft = (shit_pos,800))
             if shit_pos < -10:
                 shit_count = 0
             if player_rect.colliderect(shit_rect):
                 get_sound.play()
                 shit_count = 0
                 shit_pos = 2048
                 shit_have = 1
        
        if heal_count > 0:
             screen.blit(heal,(heal_pos,800))
             heal_rect = heal.get_rect(topleft = (heal_pos,800))
             if heal_pos < -10:
                 heal_count = 0
             if player_rect.colliderect(heal_rect):
                 get_sound.play()
                 heal_count = 0
                 heal_pos = 2048
                 if heal_have <= 5:
                     heal_have += 5
                 else:
                 	heal_have = 10
        if dron_count > 0:
             screen.blit(dron,(dron_x,dron_y))
             dron_rect = dron.get_rect(topleft = (dron_x,dron_y))
             dron_x -= 20
             if dron_x < 1300:
             	dron_y += 10
             if dron_x < -10:
                 dron_count = 0
             if player_rect.colliderect(dron_rect):
                 damage.play()
                 dron_count = 0
                 if shit_have == 0:
                    	if heal_have > 5:
                    		heal_have -= 5
                    	else:
                    		damage.play()
                    		heal_have = 0
                    		gameplay = False
                 else:
                    	shit_have = 0
                           
#            pygame.draw.rect(screen,"Red",(bullet_x,793,73,25))
        screen.blit(aim,(1800,mouse[1] - 32))
             
        
        if zombie_count:
            for el in zombie_count:
                screen.blit(zombie,el)
                el.x -= zombie_speed
                            
                                                
                if player_rect.colliderect(el):
                    damage.play()
                    if shit_have == 0:
                    	if heal_have >= 3:
                    		heal_have -= 3
                    	else:
                    		heal_have = 0
                    else:
                    	shit_have = 0
                    zombie_count.pop(0)
                    if heal_have == 0:
                        gameplay = False
  

        
        if bullet_count > 0 and zombie_count:
            if bullet_rect.colliderect(zombie_count[0]):
                zombie_sound.play()
                bullet_count = 0
                zombie_count.pop(0)
                    
        if bullet_count > 0 and dron_count > 0:
                if bullet_rect.colliderect(dron_rect):
                    dron_sound.play()
                    bullet_count = 0
                    dron_count = 0
                
#    pygame.draw.rect(screen,"Red",(player_x + 100,680,256,256))
        zombie_rect = zombie.get_rect(topleft=(zombie_x,726))
#    pygame.draw.rect(screen,"Red",(zombie_x,726,135,200))
        
        bullet_label = font.render(str(bullet_have),False,(255,0,0))
        heal_label = font.render(str(heal_have),False,(255,0,0))
		        
           
           
        if bg_x < -2000:
            bg_x = 0
        elif bg_x > 2000:
            bg_x = 0
    
    
        
        if keys[pygame.K_RIGHT]:        
            speed = 12
            zombie_speed = 14
        elif keys[pygame.K_LEFT]:
            speed = -6
            zombie_speed = 2
        else:
        	speed = 0
        	zombie_speed = 6
                            
            
        if mouse_y>793:
            bullet_y1 = (mouse_y - 793)
            bullet_y += bullet_y1/72
        if mouse_y<793:
            bullet_y1 = (793 - mouse_y)
            bullet_y -= bullet_y1/72
        if bullet_x > 2000:
             bullet_count = 0
                
        if pygame.mouse.get_pressed()[0] and bullet_count == 0 and bullet_have != 0:
             bullet_x = player_x + 325
             bullet_y = 793
             bullet_count += 1
             bullet_have -= 1
             mouse_y = mouse[1]
             if mouse_y > 793:
                 angel = math.degrees(math.atan2(-bullet_y1,1800))
             elif mouse_y < 793:
                 angel = math.degrees(math.atan2(bullet_y1,1800))
             
             
             udar_sound.play()
             bullet1 = pygame.transform.rotate(bullet,angel)
             
        
        bg_x -= speed
        box_pos -= speed
        shit_pos -= speed
        heal_pos -= speed

                  
        bullet_x += 20 
                         
    else:
        screen.fill((20,20,20))
        screen.blit(game_over_label,(680,500))
        screen.blit(restart_label,(730,600))
        bg_sound.stop()
        go_sound += 1
        player_x = 0
        
        
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
             gameplay = True
             go_sound = 0
             bg_sound.play()
             zombie_count.clear()
             bullet_have = 5
             heal_have = 10
             box_pos = 2048
             box_count = 0
             shit_have = 0
             shit_count = 0
             heal_count = 0
             bg1 = pygame.image.load("images/bg1.jpg")
        
        
        if go_sound == 1:
            game_over.play()
      
    pygame.display.update()
    clock.tick(50)