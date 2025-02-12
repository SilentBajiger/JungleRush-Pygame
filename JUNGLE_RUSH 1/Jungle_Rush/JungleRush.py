import pygame
import random
from pygame import mixer
pygame.mixer.init()
pygame.init()
screen_x=1900
screen_y=1000
clock = pygame.time.Clock()
FPS = 120#frame per second
gamewindow = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("GAMING")
introwindow = pygame.display.set_mode((screen_x,screen_y))
scorewindow = pygame.display.set_mode((screen_x,screen_y))
gameoverwindow = pygame.display.set_mode((screen_x,screen_y))
welcome = pygame.transform.scale(pygame.image.load("Image/welcome.jpg"),(screen_x,screen_y))
score_img = pygame.transform.scale(pygame.image.load("Image/score.jpg"),(screen_x,screen_y))
gameover_img = pygame.transform.scale(pygame.image.load("Image/gameover.jpg"),(screen_x,screen_y))
font = pygame.font.SysFont('impact',200)
SOUNDS = [pygame.mixer.Sound("sound/jump.mp3"),
          pygame.mixer.Sound("sound/player_shoot.mp3"),
          pygame.mixer.Sound("sound/coin.mp3"),
          pygame.mixer.Sound("sound/kill.mp3"),
          pygame.mixer.Sound("sound/blast.mp3")]
MUSIC = ["sound/intro.mp3","sound/game_music.mp3","sound/game_over.mp3","sound/new_score.mp3"]
music = pygame.mixer.music

def game_over_window():
    SOUNDS[1].stop()
    music.stop()
    music.unload()
    if not screenscore.new_high_score:  
        music.load(MUSIC[2])
        music.play(-1)
    exits = False
    if screenscore.new_high_score:    
        screenscore.update_score()
        screenscore.new_high_score = False
        music.load(MUSIC[2])
        music.play(-1)
    while not exits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exits = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    music.stop()
                    music.unload()
                    new_game()
                    intro_window()
                    exits = True
        gameoverwindow.blit(gameover_img,(0,0))
        gameoverwindow.blit(font.render(str(screenscore.total_score),True,"white"),[900,700])
        pygame.display.update()
        clock.tick(FPS)

def intro_window():
    SOUNDS[0].stop()
    if not music.get_busy():
        music.load(MUSIC[0])
        music.play(-1)
    exits = False
    while not exits:
        introwindow.blit(welcome,(0,0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exits = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score_window()
                    exits = True
                if event.key == pygame.K_RETURN:
                    SOUNDS[0].stop()
                    music.stop()
                    music.unload()
                    gameloop()
                    exits = True
        
class High_score():
    def __init__(self):
        self.list = []
        self.font = pygame.font.SysFont('impact',100)
    def fetch_score(self):
        with open("score1.txt","r") as obj:
            string = obj.read()
        print(string)
        obj.close()
        splitted = string.split(" ",5)
        self.list = [[splitted[0],splitted[1]],[splitted[2],splitted[3]],[splitted[4],splitted[5]]]
    
    def display_score(self):
        screen_text = self.font.render(str(self.list[0][0]),True,("white"))
        screen_text_score = self.font.render(str(self.list[0][1]),True,("white"))
        scorewindow.blit(screen_text,[600,370])
        scorewindow.blit(screen_text_score,[1200,370])
        screen_text = self.font.render(self.list[1][0],True,("white"))
        screen_text_score = self.font.render(str(self.list[1][1]),True,("white"))
        scorewindow.blit(screen_text,[600,518])
        scorewindow.blit(screen_text_score,[1200,518])
        screen_text = self.font.render(self.list[2][0],True,("white"))
        screen_text_score = self.font.render(str(self.list[2][1]),True,("white"))
        scorewindow.blit(screen_text,[600,659])
        scorewindow.blit(screen_text_score,[1200,659])
        screen_text = font.render("PRESS ESC TO GO HOME PAGE",True,("white"))

def score_window():
    exits = False
    highscore.fetch_score()
    while not exits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exits = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    intro_window()
                    exits = True
        scorewindow.blit(score_img,(0,0))
        highscore.display_score()
        pygame.display.update()
        clock.tick(FPS)
    

class Screen_Score():
    def __init__(self):
        self.new_high_score = False
        with open("score1.txt","r") as obj:
            text = obj.read()
        self.highscore = text.split(" ",5)
        self.total_score = 0
    
    def display_score_on_game_screen(self):

        self.total_score = collision.enemy_kill_score + collision.coin_score
        curent_score = ((pygame.font.SysFont('agencyfb',100)).render(str("score: " +str(self.total_score)),True,"yellow"))    
        gamewindow.blit((curent_score),[100,50])
        if int(self.highscore[1]) > self.total_score:
            high_score = pygame.font.SysFont('agencyfb',100).render(str("Highscore: " +self.highscore[1]),True,"yellow")
            gamewindow.blit((high_score),[600,50])
        if self.total_score > int(self.highscore[5]):
            self.new_high_score = True

    def update_score(self):
        music.load(MUSIC[3])
        if not music.get_busy():
            music.play(-1)
        name = ''
        highscore = str(self.total_score)
        base_font = pygame.font.Font(None,100)
        screen_text = font.render("ENTER YOUR NAME AND PRESS ENTER",True,("yellow"))
        screen_score_text = (pygame.font.SysFont("rogfonts",150)).render(highscore,True,("red"))
        scorewindow.blit(screen_text,[100,100])
        exits = False 
        flag = 1
        newnamewindow = pygame.display.set_mode((screen_x,screen_y))
        while not exits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.KEYDOWN:   
                    if event.key == pygame.K_RETURN and name != '':
                        exits = True
                        flag = 0
                        music.stop()
                        music.unload()
                    if event.key == pygame.K_BACKSPACE :
                        name = name[:-1]
                    else:
                        if flag == 1 and len(name)<10:
                            tag = event.unicode
                            if ('A' <= tag and tag <= 'Z') or ('a' <= tag and tag <= 'z'):
                                name += tag 
            newnamewindow.blit(pygame.transform.scale(pygame.image.load("Image/new_score.jpg"),(screen_x,screen_y)),(0,0))
            text_surface = (pygame.font.SysFont("rogfonts",60)).render(name,True,(0,0,0))
            newnamewindow.blit(screen_score_text,(1100,390))
            newnamewindow.blit(text_surface,(760,715))
            pygame.display.update()
        with open("score1.txt","r") as obj:
            string = obj.read()
        obj.close()
        splitted = string.split(" ",5)
        list =[[splitted[0],splitted[1]],[splitted[2],splitted[3]],[splitted[4],splitted[5]]]
        num = self.total_score
        if num > int(splitted[5]):
            screenscore.new_high_score = False
            list[2] = [name,str(num)]
        for i in range(3):
            for j in range (2):
                if int(list[j][1]) < int(list[j+1][1]):
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp
        with open ("score1.txt","w") as obj1:
            obj1.write(list[0][0]+" "+list[0][1]+" "+list[1][0]+" "+list[1][1]+" "+list[2][0]+" "+list[2][1])
        obj1.close()

class Enemy():
    def __init__(self):
        self.enemy_list = []
        self.enemy_bullet_list = []
        self.img_enemy_list = [pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry1.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/angry2.png"),(100,70)),
                               pygame.transform.scale(pygame.image.load("Image/enemy_fire.png"),(100,70)),
                               ]
        self.img_enemy_bullet = pygame.transform.scale(pygame.image.load("Image/enemy_bullet.png"),(20,20))
        self.enemy_img_fire = pygame.transform.scale(pygame.image.load("Image/enemy_fire.png"),(100,70))
        self.enemy_bullet_rect = self.img_enemy_bullet.get_rect()
        self.bullet_width = self.img_enemy_bullet.get_width()
        self.bullet_height = self.img_enemy_bullet.get_height()
        self.enemy_rect = self.img_enemy_list[0].get_rect()
        self.enemy_speedx = -2
        self.enemy_width = self.img_enemy_list[0].get_width()
        self.enemy_height = self.img_enemy_list[0].get_height()
        self.enemy_img_count = 0
        self.enemy_fire_flag = False
        self.enemy_bullet_speedx = 5
        
    def new_enemy(self):
        self.enemy_fire_flag = True
        if not (collision.game_over_flag or player.game_over_flag):
            fdy = random.randint(100,screen_y-200)
            img_index = 0
            self.enemy_list.append([1900,fdy,self.enemy_width,self.enemy_height,img_index,False,0])

    def update_enemy(self):
        flag = 0
        for enemy in self.enemy_list:
            self.enemy_rect.x = enemy[0]
            self.enemy_rect.y = enemy[1]
            if self.enemy_rect.x > 0:        
                if enemy[5] == True:   
                    enemy[6] += 1
                    enemy[4] = 17
                    if enemy[6] >= 15:
                        enemy[5] = False
                        enemy[6] = 0
                gamewindow.blit(self.img_enemy_list[enemy[4]],self.enemy_rect)
                if not collision.game_over_flag:
                    if player.img_rect.x >screen_x/2:
                        enemy[0] += (self.enemy_speedx - 10) 
                    else:
                        enemy[0] += self.enemy_speedx
                    self.enemy_img_count+=1
                    enemy[4] += 1
                    if enemy[4] == 18 or enemy[4] >= 24:
                        enemy[4] = 0
                        self.enemy_fire_flag = False
            else:
                flag = 1
        if flag == 1:
            del self.enemy_list[0]
    
    def enemy_fire(self):
        if not (collision.game_over_flag or player.game_over_flag): 
            if len(self.enemy_list):
                index = random.randint(0,len(self.enemy_list)-1)
                self.enemy_fire_flag = True
                self.enemy_list[index][5] = True
                self.enemy_bullet_list.append([self.enemy_list[index][0]-20,self.enemy_list[index][1]+40,self.bullet_width,self.bullet_height])

    def enemy_bullet_update(self):
        for bullet_index in range(len(self.enemy_bullet_list)):
            if not collision.game_over_flag:
                if player.img_rect.x >(screen_x/2):
                    self.enemy_bullet_list[bullet_index][0] -= self.enemy_bullet_speedx + 10
                else:
                    self.enemy_bullet_list[bullet_index][0] -= self.enemy_bullet_speedx
            gamewindow.blit(self.img_enemy_bullet,self.enemy_bullet_list[bullet_index])
        
        if len(self.enemy_bullet_list):
            if self.enemy_bullet_list[0][0] < 0:
                del self.enemy_bullet_list[0]

class Player_Bullets():
    def __init__(self):
        self.player_bullet_list = []
        self.img_bullet = pygame.transform.scale(pygame.image.load("Image/goli.png"),(50,12))
        self.img_bullet_left = pygame.transform.flip(self.img_bullet,True,False)
        self.bullet_rect = self.img_bullet.get_rect()
        self.width = self.img_bullet.get_width()
        self.height = self.img_bullet.get_height()

    def player_fire(self,x,y):
        if not (collision.game_over_flag or player.game_over_flag):
            SOUNDS[1].play()
            if player.right_direction:
                self.player_bullet_list.append([x+75,y+35,self.width,self.height,player.right_direction])
            else:
                self.player_bullet_list.append([x,y+35,self.width,self.height,player.right_direction])

    def update(self):
        flag = 0
        bullet_image = self.img_bullet
        for x in range(len(self.player_bullet_list)):
            if self.player_bullet_list[x][4]:
                self.player_bullet_list[x][0]+=15
                bullet_image = self.img_bullet
            else:
                self.player_bullet_list[x][0]-=15
                bullet_image = self.img_bullet_left
            if self.player_bullet_list[x][0]>screen_x or self.player_bullet_list[x][0]<0:
                flag=1
            gamewindow.blit(bullet_image,(self.player_bullet_list[x][0],self.player_bullet_list[x][1]))
        if flag==1:
            del self.player_bullet_list[0] 

    def player_bullet_with_tiles(self):
        player_bullet_flag = 0
        bullet_index = 0
        for bullet in range(len(self.player_bullet_list)):
            bullet_rect = pygame.Rect(self.player_bullet_list[bullet][0],self.player_bullet_list[bullet][1],self.player_bullet_list[bullet][2],self.player_bullet_list[bullet][3])
            for tile in Bg.platform_list:
                tile_rect = pygame.Rect(tile[1].x,tile[1].y,100,100)
                if tile_rect.colliderect(bullet_rect):
                    player_bullet_flag = 1
                    bullet_index = bullet
        if player_bullet_flag == 1:
            del self.player_bullet_list[bullet_index]
            player_bullet_flag = 0

class Collision():
    def __init__(self):
        self.enemy_kill_score = 0
        self.coin_score = 0
        self.game_over_flag = False
        self.flag = False

    def player_bullet_with_enemy(self):
        enemy_flag = 0
        bullet_flag = 0
        delete_enemy_index = 0
        delete_bullet_index = 0
        for bullet in range(len(player_bullet.player_bullet_list)):
            for enemy_index in range(len(enemy.enemy_list)):
                enemy_rect = pygame.Rect(enemy.enemy_list[enemy_index][0],enemy.enemy_list[enemy_index][1],enemy.enemy_list[enemy_index][2],enemy.enemy_list[enemy_index][3])
                bullet_rect = pygame.Rect(player_bullet.player_bullet_list[bullet][0],player_bullet.player_bullet_list[bullet][1],player_bullet.player_bullet_list[bullet][2],player_bullet.player_bullet_list[bullet][3])
                if enemy_rect.colliderect(bullet_rect):
                    SOUNDS[3].play()
                    enemy_flag = 1
                    bullet_flag = 1
                    delete_enemy_index = enemy_index
                    delete_bullet_index = bullet
                    self.enemy_kill_score += 2
            if enemy_flag == 1:
                del enemy.enemy_list[delete_enemy_index]
                enemy_flag = 0
        if bullet_flag == 1:
            del player_bullet.player_bullet_list[delete_bullet_index]
            bullet_flag = 0
    
    def player_with_enemy(self):
        player_rect = pygame.Rect(player.img_rect.x,player.img_rect.y,player.rect_width,player.rect_height)
        for Enemy in enemy.enemy_list:
            enemy_rect = pygame.Rect(Enemy[0],Enemy[1],Enemy[2],Enemy[3])
            if player_rect.colliderect(enemy_rect):
                self.game_over_flag = True 

    def player_with_enemy_bullet(self):
        player_rect = pygame.Rect(player.img_rect.x,player.img_rect.y,player.rect_width,player.rect_height)
        for bullet in enemy.enemy_bullet_list:
            bullet_rect = pygame.Rect(bullet[0],bullet[1],bullet[2],bullet[3])
            if player_rect.colliderect(bullet_rect):
                #pass
                self.game_over_flag = True

    def player_with_coin(self):
        coin_flag = 0
        coin_index = 0
        player_rect = pygame.Rect(player.img_rect.x,player.img_rect.y,player.rect_width,player.rect_height)
        for coin in range(len(Bg.coin_list)):
            coin_rect = pygame.Rect(Bg.coin_list[coin])
            if player_rect.colliderect(coin_rect):
                SOUNDS[2].play()
                self.coin_score += 1
                coin_flag = 1
                coin_index = coin
        if coin_flag == 1:
            del Bg.coin_list[coin_index]
            coin_flag = 0

class Player():
    def __init__(self):
        self.image_list = [pygame.transform.scale(pygame.image.load("Image/renu1.png"),(80,100)),
                           pygame.transform.scale(pygame.image.load("Image/renu2.png"),(80,100)),
                           pygame.transform.scale(pygame.image.load("Image/renu3.png"),(80,100)),
                           pygame.transform.scale(pygame.image.load("Image/renu4.png"),(80,100)),
                           pygame.transform.scale(pygame.image.load("Image/renu5.png"),(80,100)),
                           pygame.transform.scale(pygame.image.load("Image/renu6.png"),(80,100))]
        self.image_list_left = [pygame.transform.flip(self.image_list[0],True,False),
                                pygame.transform.flip(self.image_list[1],True,False),
                                pygame.transform.flip(self.image_list[2],True,False),
                                pygame.transform.flip(self.image_list[3],True,False),
                                pygame.transform.flip(self.image_list[4],True,False),
                                pygame.transform.flip(self.image_list[5],True,False)]
        self.blast_img_list = [pygame.transform.scale(pygame.image.load("Image/fire1.png"),(100,100)),
                               pygame.transform.scale(pygame.image.load("Image/fire2.png"),(100,100)),
                               pygame.transform.scale(pygame.image.load("Image/fire3.png"),(100,100)),
                               pygame.transform.scale(pygame.image.load("Image/fire4.png"),(100,100))]
        self.image_stable = pygame.transform.scale(pygame.image.load("Image/stable.png"),(80,100))
        self.image_stable_left = pygame.transform.flip(self.image_stable,True,False)
        self.image_jump = pygame.transform.scale(pygame.image.load("Image/jump.png"),(80,100))
        self.image_jump_left = pygame.transform.flip(self.image_jump,True,False)
        self.image_fire = pygame.transform.scale(pygame.image.load("Image/shoot.png"),(80,100))
        self.image_fire_left = pygame.transform.flip(self.image_fire,True,False)
        self.img_rect = self.image_list[0].get_rect()
        self.rect_width = self.image_list[0].get_width()
        self.rect_height = self.image_list[0].get_height()
        self.img_rect.x = 500
        self.img_rect.y = 200
        self.img_index = 0
        self.speed_x = 10
        self.vel_y = 0
        self.acc_y = 30
        self.jump_height = 300
        self.current_height = 0
        self.jump = False
        self.next_jump_on = True
        self.animation_on = False
        self.right_direction = True
        self.game_over_flag = False
        self.player_is_on_tile = True
        self.curr_image = self.image_list[0]
        self.blast_img_index = 0
        self.change_fire_img_cnt = 0
        self.blast_play = False
        self.i = 0
        self.stable = 0
        self.img_index_count = 0
        self.jump_count = 0
        self.y =0 
        self.fire = False
        self.below_y = False

    def update(self):
        dx = 0
        dy = 0 
        run = False
        if not collision.game_over_flag and  not player.game_over_flag:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                dx += self.speed_x
                self.animation_on = True
                run = True
                self.right_direction = True
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                dx -= self.speed_x
                self.animation_on = True
                run = True
                self.right_direction = False
            if key[pygame.K_SPACE] and self.jump == False and self.next_jump_on == True and self.player_is_on_tile == True or key[pygame.K_w]:
                if self.i == 0 :
                    SOUNDS[0].play()
                    self.jump = True
                    self.vel_y = -50
                    self.next_jump_on = False
                    self.player_is_on_tile = False
                self.i += 1 
            else:
                if self.jump == False and self.next_jump_on == True and self.player_is_on_tile == True:
                    self.i = 0
            if self.jump == True:
                if self.vel_y >0:
                    self.jump = False
            self.y +=1
            if self.y == 2:
                self.vel_y += 3
            if self.vel_y > 0:
                self.vel_y = 18
            if self.y == 2:
                dy += self.vel_y
                self.y = 0
        for tile in Bg.platform_list:
            if tile[1].colliderect(self.img_rect.x + dx ,self.img_rect.y,self.rect_width,self.rect_height):
                dx=0
            if tile[1].colliderect(self.img_rect.x,self.img_rect.y+dy,self.rect_width,self.rect_height):
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.img_rect.top
                    self.vel_y = 0
                    self.player_is_on_tile = True
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.img_rect.bottom
                    self.vel_y=0
                    self.next_jump_on = True
                    self.jump = False
                    self.player_is_on_tile = True
                else:
                    self.player_is_on_tile = False
        if self.animation_on == True:
            self.img_index_count += 1
            if self.img_index_count == 5:
                self.img_index_count = 0
                self.img_index += 1
            self.animation_on = False
        if self.img_index == 6:
            self.img_index = 0
        if self.img_rect.x + dx < 0:
            dx = 0
        if self.img_rect.bottom + dy > screen_y:
            dy = 0
            self.game_over_flag = True
            self.below_y = True
        self.img_rect.x += dx
        self.img_rect.y += dy
        if not collision.game_over_flag and  not player.game_over_flag:
            if self.jump:
                if self.right_direction:
                    gamewindow.blit(self.image_jump,self.img_rect)
                    self.curr_image = self.image_jump
                else:
                    gamewindow.blit(self.image_jump_left,self.img_rect)
                    self.curr_image = self.image_jump_left
            elif self.fire == True:
                self.fire = False
                if self.right_direction == True:
                    gamewindow.blit(self.image_fire,self.img_rect)
                else:
                    gamewindow.blit(self.image_fire_left,self.img_rect)
            else:
                if run:
                    if self.right_direction:
                        gamewindow.blit(self.image_list[self.img_index],self.img_rect)
                        self.curr_image = self.image_list[self.img_index]
                    else:
                        gamewindow.blit(self.image_list_left[self.img_index],self.img_rect)
                        self.curr_image = self.image_list_left[self.img_index]
                else:
                    if self.right_direction:
                        gamewindow.blit(self.image_stable,self.img_rect)
                        self.curr_image = self.image_stable
                        self.stable = 1
                    else:
                        gamewindow.blit(self.image_stable_left,self.img_rect)
                        self.curr_image = self.image_stable_left
                        self.stable = 1         
        else:
            if not self.below_y:
                if not self.blast_play:
                    SOUNDS[4].play()
                    self.blast_play = True
                gamewindow.blit(self.blast_img_list[self.blast_img_index],self.img_rect)
                self.change_fire_img_cnt +=1
                if self.change_fire_img_cnt == 5:
                    self.blast_img_index +=1
                    if self.blast_img_index == 3:
                        self.blast_img_index = 0
                    self.change_fire_img_cnt = 0

class Background():
    
    def __init__(self,platform):
        self.platform_list = []
        self.img_coin_list = [pygame.transform.scale(pygame.image.load("Image/coin1.png"),(100,100)),
                              pygame.transform.scale(pygame.image.load("Image/coin2.png"),(100,100)),
                              pygame.transform.scale(pygame.image.load("Image/coin3.png"),(100,100)),
                              pygame.transform.scale(pygame.image.load("Image/coin4.png"),(100,100)),
                              ]
        self.coin_list = []
        self.coin_img_index = 0   
        self.coin_rotate_time = 0 
        row_count = 0
        col_count = 0
        self.tile_size = 100 
        self.distance = 0
        tile_image = pygame.transform.scale(pygame.image.load("Image/tile_m.png"),(self.tile_size,self.tile_size))
        #grass_image = pygame.transform.scale(pygame.image.load("Image/grass.jpg"),(self.tile_size,self.tile_size))
        for i in platform:
            col_count=0
            for j in i:
                if j==1:
                    img_rect = tile_image.get_rect()
                    img_rect.x = col_count*self.tile_size
                    img_rect.y = row_count*self.tile_size
                    tile = (tile_image,img_rect)
                    self.platform_list.append(tile)
                if j==3:
                    img_rect = self.img_coin_list[0].get_rect()
                    img_rect.x = col_count*self.tile_size
                    img_rect.y = row_count*self.tile_size
                    self.coin_list.append(img_rect)
                col_count +=1
            row_count +=1    

    def draw_platform(self):
        for tile in self.platform_list:
            gamewindow.blit(tile[0],tile[1])
        for coin in self.coin_list:
            gamewindow.blit(self.img_coin_list[self.coin_img_index],coin)
        self.coin_rotate_time+=1
        if self.coin_rotate_time > 3:
            self.coin_img_index +=1
            if self.coin_img_index > 3:
                self.coin_img_index = 0
            self.coin_rotate_time = 0
        if player.img_rect.x >(screen_x/2):
            player.img_rect.x = screen_x /2
            for tile in self.platform_list:
                tile[1].x -= 7
            for coin in self.coin_list:
                coin.x -= 7
        if len(self.coin_list) and self.coin_list[0].x <400:
            del self.coin_list[0]

platform = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,3,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,1,1,0,0,1,1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,3,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,3,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,3,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,3,3,3,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,3,0,1,3,0,0,0,3,3,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,3,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,3,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1,0,0,0,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,3,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,3,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,3,0,0,0,0,0,3,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

def new_game():
    global Bg 
    Bg = Background(platform)
    global player
    player = Player()
    global collision 
    collision = Collision()
    global player_bullet 
    player_bullet= Player_Bullets()
    global enemy 
    enemy = Enemy()
    global highscore 
    highscore = High_score()
    global screenscore 
    screenscore = Screen_Score()

def gameloop():
    game_over_count = 0
    if not music.get_busy():
        music.load(MUSIC[1])
        music.play(-1)
    exits = False
    bullet_count = 0
    enemy_bullet_count = 0
    allow_bullet = True
    enemy_count = 0
    while not exits:
        bullet_count +=1
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exits =  True
            if (event.type == pygame.KEYDOWN):    
                if (event.key == pygame.K_RETURN) and allow_bullet:
                    player.fire = True
                    if bullet_count > 8 and  len(player_bullet.player_bullet_list)<4:
                        player_bullet.player_fire(player.img_rect.x,player.img_rect.y)
                        bullet_count = 0
        gamewindow.blit((pygame.transform.scale(pygame.image.load("Image/bg.png"),(screen_x,screen_y))),(0,0))
        Bg.draw_platform()
        player.update()
        if enemy_count > 150:
            enemy.new_enemy()
            enemy_count = 0
        if enemy_bullet_count > 120:
            enemy.enemy_fire()
            enemy_bullet_count = 0
        collision.player_bullet_with_enemy()
        player_bullet.update()
        enemy.update_enemy()
        collision.player_with_enemy()
        if collision.game_over_flag or player.game_over_flag:
            if game_over_count>60:
                game_over_window()
                exits = True
                collision.game_over_flag = False
            game_over_count+=1
        enemy.enemy_bullet_update()
        player_bullet.player_bullet_with_tiles()
        collision.player_with_coin()
        collision.player_with_enemy_bullet()
        screenscore.display_score_on_game_screen()
        pygame.display.update()
        enemy_count += 1
        enemy_bullet_count += 1
        clock.tick(FPS)
    pygame.quit()

new_game()
intro_window()