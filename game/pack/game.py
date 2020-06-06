import pygame
pygame.init()

mode = pygame.display.set_mode((500,500))
pygame.display.set_caption("wondering kid")

Right = [pygame.image.load('r1.png'),pygame.image.load('r2.png'),pygame.image.load('r3.png'),pygame.image.load('r4.png'),pygame.image.load('r5.png'),pygame.image.load('r6.png'),
         pygame.image.load('r7.png'),pygame.image.load('r8.png'),pygame.image.load('r9.png')]
Left = [pygame.image.load('l1.png'),pygame.image.load('l2.png'),pygame.image.load('l3.png'),pygame.image.load('l4.png'),pygame.image.load('l5.png'),pygame.image.load('l6.png'),
        pygame.image.load('l7.png'),pygame.image.load('l8.png'),pygame.image.load('l9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
music= pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width =width
        self.height =height
        self.vel=5
        self.jump= False
        self.left=False
        self.right=False
        self.walk=0
        self.count=10
    def draw(self,mode):
        if self.walk +1 >=27:
            self.walk = 0
        if self.left:
            mode.blit(Left[self.walk//3],(self.x,self.y))
            self.walk +=1
        elif self.right:
            mode.blit(Right[self.walk//3],(self.x,self.y))
            self.walk += 1
        else:
            mode.blit(char ,(self.x,self.y))
def redrawGameWindow():
    mode.blit(bg,(0,0))
    p.draw(mode)
    pygame.display.update()


p = player(200,330,64,64)
run = True  #initiate running

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed() #dict to use key
    if keys[pygame.K_LEFT] and p.x>p.vel:
        p.x -= p.vel
        p.left = True
        p.right = False
    elif keys[pygame.K_RIGHT] and p.x<500 -p.vel - p.width:
        p.x += p.vel
        p.left = False
        p.right = True
    else:
        p.right = False
        p.left = False
        p.walk = 0
        
    if not p.jump:
        if keys[pygame.K_SPACE]:
            p.jump = True
            p.right = False
            p.left = False
            p.walk = 0      
    else:
        if p.count >= -10:
            n = 1
            if p.count <0:
                n=-1
            p.y -= (p.count **2)*0.5*n
            p.count -= 1
        else:
            p.count = 10
            p.jump = False
    redrawGameWindow()
    
   
pygame.quit()
