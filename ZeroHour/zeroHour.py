# pygame template - skeleton for new games

import pygame, sys
import random
import os
game = False
menu = True
ships = False
shipSpeed = 1
shipType = 'small'
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
font_folder = os.path.join(game_folder, 'font')
snd_folder = os.path.join(game_folder, 'snd')

killed = False
WIDTH = 800
HEIGHT = 700
#pygame stuff
pygame.init()
pygame.mixer.init()
os.getcwd()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ZeroHour")
clock = pygame.time.Clock()
scroll = -1024
scroll1 = 1024
FPS = 30
font = pygame.font.Font(os.path.join(font_folder,'font.ttf'), 30)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
mark = 1
cash = 10000
hyper = 0
turretLevel = 1
lives = 1
#############################################################ALL ASSETS#############################################################
background = pygame.image.load(os.path.join(img_folder,'space.png'))
background_rect = background.get_rect()
background1 = pygame.image.load(os.path.join(img_folder,'space.png'))
background1_rect = background1.get_rect()
background2 = pygame.image.load(os.path.join(img_folder,'hanger.jpg'))
background2_rect = background2.get_rect()

logo = pygame.image.load(os.path.join(img_folder,'logo.png'))
logo_rect = logo.get_rect()
sship1 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Small/body_01.png'))
sship1_rect = sship1.get_rect()
sship2 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Small/body_02.png'))
sship2_rect = sship2.get_rect()
sship3 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Small/body_03.png'))
sship3_rect = sship3.get_rect()

mship1 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Medium/body_01.png'))
mship1_rect = mship1.get_rect()
mship2 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Medium/body_02.png'))
mship2_rect = mship2.get_rect()
mship3 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Medium/body_03.png'))
mship3_rect = mship3.get_rect()

bship1 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Big/body_01.png'))
bship1_rect = bship1.get_rect()
bship2 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Big/body_02.png'))
bship2_rect = bship2.get_rect()
bship3 = pygame.image.load(os.path.join(game_folder, 'assets/Ships/Big/body_03.png'))
bship3_rect = bship3.get_rect()

c1 = pygame.image.load(os.path.join(game_folder, 'assets/Weapons/Small/Cannon/turret_01_mk1.png'))
c1_rect = c1.get_rect()
c2 = pygame.image.load(os.path.join(game_folder, 'assets/Weapons/Small/Cannon/turret_01_mk2.png'))
c2_rect = c2.get_rect()
c3 = pygame.image.load(os.path.join(game_folder, 'assets/Weapons/Small/Cannon/turret_01_mk3.png'))
c3_rect = c3.get_rect()

meteorite = pygame.image.load(os.path.join(img_folder, 'Meteorite.png'))
meteorite_rect = meteorite.get_rect()
red = pygame.image.load(os.path.join(img_folder, 'beam.png'))
alert = pygame.image.load(os.path.join(img_folder, 'alert.png'))
alert = pygame.transform.scale(alert,(50,50))
alert_rect = alert.get_rect()
alert1_rect = alert.get_rect()
alert2_rect = alert.get_rect()
alert_rect.center = (WIDTH/3, 70)
alert1_rect.center = (WIDTH/2,70)
alert2_rect.center = ((WIDTH *2)/3,70)
alertS = pygame.mixer.Sound(os.path.join(snd_folder,'alertS.wav'))
laser = pygame.mixer.Sound(os.path.join(snd_folder,'laser.wav'))
lifeLos = pygame.mixer.Sound(os.path.join(snd_folder,'lifeLos.wav'))
level = 4
shipx = 0
shipy = 0
#############################################################ALL ASSETS#############################################################
selShip = sship1
selTur = c1
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = selShip
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        if shipType == 'small':
            self.rect.bottom = HEIGHT - 10 
        self.speedx = 0
        self.speedy = 0
        self.lives = 1
    def update(self):
        if shipType != 'small' and mark != 1:
            self.image = selShip
        if shipType == 'medium':
            self.rect.bottom = HEIGHT - 65
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x += -shipSpeed
        if keystate[pygame.K_RIGHT]:
            self.rect.x += shipSpeed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <0:
            self.rect.left = 0
        shipx = self.rect.centerx
        shipy = self.rect.centery
    def shoot(self):
        if shipType == 'small' or shipType == 'medium' or shipType == 'big':
            if turretLevel == 2:
                bullet = Bullet(self.rect.centerx + 20, self.rect.top)
                bullet1 = Bullet(self.rect.centerx - 20, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                all_sprites.add(bullet1)
                bullets.add(bullet1)
            if turretLevel == 3:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet1 = Bullet(self.rect.centerx - 20, self.rect.top)
                bullet2 = Bullet(self.rect.centerx + 20, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                all_sprites.add(bullet1)
                bullets.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet2)
            if turretLevel == 4:
                bullet = Bullet(self.rect.centerx + 20, self.rect.top)
                bullet1 = Bullet(self.rect.centerx - 20, self.rect.top)
                bullet2 = Bullet(self.rect.centerx + 40, self.rect.top)
                bullet3 = Bullet(self.rect.centerx - 40, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                all_sprites.add(bullet1)
                bullets.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet2)
                all_sprites.add(bullet3)
                bullets.add(bullet3)
                
            if turretLevel > 4:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet1 = Bullet(self.rect.centerx - 20, self.rect.top)
                bullet2 = Bullet(self.rect.centerx + 20, self.rect.top)
                bullet3 = Bullet(self.rect.centerx + 40, self.rect.top)
                bullet4 = Bullet(self.rect.centerx - 40, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                all_sprites.add(bullet1)
                bullets.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet2)
                all_sprites.add(bullet3)
                bullets.add(bullet3)
                all_sprites.add(bullet4)
                bullets.add(bullet4)
            else:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
            


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteorite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, level)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if killed:
            self.kill()
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20: #Goes past edge of bottom of screen
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = red
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.attack = turretLevel

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

bgm = pygame.mixer.music.load(os.path.join(snd_folder,("bgm.mp3")))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

gameStart = font.render('Play', True, WHITE) 
gameButton = gameStart.get_rect()
gameButton.center = (WIDTH/2,440)

shipSel = font.render('Ship',True, WHITE)
shipButton = shipSel.get_rect()
shipButton.center = (WIDTH/2,500)

back = font.render('Back', True, WHITE) 
backButton = back.get_rect()
backButton.center = (55,HEIGHT - 30)

upgradeTurret = font.render('Upgrade Turrets', True, WHITE) 
turretButton = upgradeTurret.get_rect()
turretButton.center = (WIDTH/2,300)

upgradeShip = font.render('Upgrade Ship', True, WHITE) 
ushipButton = upgradeShip.get_rect()
ushipButton.center = (WIDTH/2,340)

upgradeShield = font.render('Upgrade Shield', True, WHITE) 
shieldButton = upgradeShield.get_rect()
shieldButton.center = (WIDTH/2,380)

upgradeThrusters = font.render('Upgrade Thrusters', True, WHITE) 
thrustersButton = upgradeThrusters.get_rect()
thrustersButton.center = (WIDTH/2,420)

upgradeAmmo = font.render('Upgrade Ammunition', True, WHITE) 
ammoButton = upgradeAmmo.get_rect()
ammoButton.center = (WIDTH/2,460)

upgradeHull = font.render('Upgrade Hull', True, WHITE) 
hullButton = upgradeHull.get_rect()
hullButton.center = (WIDTH/2,500)

shipRect = selShip.get_rect()


running = True   #Game loop
while running:
    clock.tick(FPS)

    while menu:
        background_rect.center = (WIDTH/2,scroll)
        cashier = font.render('You have ' + str(cash) + " credits", True, WHITE) 
        ct = gameStart.get_rect()
        ct.center = (250,HEIGHT - 50)
        background1_rect.center = (WIDTH/2,scroll1)
        logo_rect.center = (WIDTH/2,HEIGHT/2)
        SCREEN.fill(BLACK)
        SCREEN.blit(background, background_rect)
        SCREEN.blit(background1, background1_rect)
        SCREEN.blit(logo, logo_rect)
        SCREEN.blit(gameStart, gameButton)
        SCREEN.blit(shipSel, shipButton)
        SCREEN.blit(cashier, ct)
        scroll += 3
        scroll1 += 3
        if scroll > 3072:
            scroll = -1024
        if scroll1 > 3072:
            scroll1 = -1024
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameButton.collidepoint(pygame.mouse.get_pos()):
                    killed = False
                    game = True
                    menu = False
                    ship = False
                    player.lives = lives
                if shipButton.collidepoint(pygame.mouse.get_pos()):
                    selShip = pygame.transform.rotate(selShip,270)
                    ship = True
                    menu = False
                    game = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        all_sprites.update()
        pygame.display.flip()


    while ship:
        SCREEN.fill(BLACK)
        if turretLevel == 2:
            selTur = c2
        if turretLevel == 3:
            selTur = c3
        turr = selTur.get_rect()
        cashier = font.render('You have ' + str(cash) + " credits", True, WHITE) 
        ct = gameStart.get_rect()
        ct.center = (250,HEIGHT - 50)
        background2_rect.center = (WIDTH/2,HEIGHT/2)
        SCREEN.blit(background2, background2_rect)
        pygame.draw.rect(SCREEN, WHITE,[WIDTH/2 - 200,10,400,130],5)
        if shipType == 'small':    
            turr.center = (shipRect.centerx + 15,shipRect.centery - 20)
        if shipType == 'medium':    
            turr.center = (shipRect.centerx + 50,shipRect.centery)
        if shipType == 'medium':    
            turr.center = (shipRect.centerx + 50,shipRect.centery)
        shipRect.left = (205)
        shipRect.top = (11)
        
        SCREEN.blit(selShip, shipRect)
        SCREEN.blit(back, backButton)
        SCREEN.blit(upgradeShip, ushipButton)
        SCREEN.blit(upgradeTurret, turretButton)
        SCREEN.blit(selTur,turr)
        SCREEN.blit(cashier, ct)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if backButton.collidepoint(pygame.mouse.get_pos()):
                    selShip = pygame.transform.rotate(selShip,270)
                    menu = True
                    game = False
                    ship = False
                if cash > 0 and ushipButton.collidepoint(pygame.mouse.get_pos()):
                    lives += 1
                    print("k1")
                    if shipType == 'small':
                        print("k2")
                        if mark == 1:
                            selShip = sship2
                            cash -= 100
                            mark += 1
                        elif mark == 2:
                            selShip = sship3
                            cash -= 250
                            mark += 1
                        elif mark == 3:
                            cash -= 500
                            selShip = mship1
                            shipType = 'medium'
                            mark = 1
                    if shipType == 'medium':
                        if mark == 1:
                            cash -= 900
                            selShip = mship2
                            mark += 1
                        elif mark == 2:
                            cash -= 1200
                            selShip = mship3
                            mark += 1
                        elif mark == 3:
                            cash -= 1500
                            selShip = bship1
                            shipType = 'big'
                            mark = 1
                    selShip = pygame.transform.rotate(selShip,90)
                if cash > 0 and turretButton.collidepoint(pygame.mouse.get_pos()):
                    cash -= turretLevel * 100
                    print("turet")
                    turretLevel += 1


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        all_sprites.update()
        pygame.display.flip()


    while game:
        if hyper == 150:
            for i in range(8):
                m = Mob() #instance
                all_sprites.add(m)
                mobs.add(m)
                m.image = pygame.transform.rotate(m.image,random.randint(1,360))
                
        hyper += 1
        background_rect.center = (WIDTH/2,scroll)
        background1_rect.center = (WIDTH/2,scroll1)
        Player().image = selShip
        SCREEN.fill(BLACK)
        SCREEN.blit(background, background_rect)
        SCREEN.blit(background1, background1_rect)
        if hyper > 120 and hyper < 160:
            pygame.mixer.Sound.play(alertS)
            SCREEN.blit(alert,alert_rect)
            SCREEN.blit(alert,alert1_rect)
            SCREEN.blit(alert,alert2_rect)
        #######HYPERSPEED#######
        if hyper < 10:
            scroll += 3
            scroll1 += 3
        if hyper < 30:
            scroll += 5
            scroll1 += 5
        if hyper < 60:
            scroll += 7
            scroll1 += 7
        if hyper < 90:
            scroll += 10
            scroll1 += 10
        if hyper < 150:
            scroll += 20
            scroll1 += 20
        else:
            scroll += 1
            scroll1 += 1
        if scroll > 3072:
            scroll = -1024
        if scroll1 > 3072:
            scroll1 = -1024
        #######HYPERSPEED#######
        all_sprites.draw(SCREEN)
        all_sprites.update()
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.lives -= 1
            pygame.mixer.Sound.play(lifeLos)
            if player.lives < 0:
                killed = True
                hyper = 0
                game = False
                menu = True
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
        """for i in hits:
            killed = True
            hyper = 0
            game = False
            menu = True"""
        enemyHits = pygame.sprite.groupcollide(mobs, bullets,True,True)#checks ALL collisions between all mob and all bullets
        for hit in enemyHits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            cash += m.speedy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(laser)
                    player.shoot()

        all_sprites.update()
        pygame.display.flip()


