import random
import pygame , sys , math
from  datetime import  datetime

pygame.init()
screen = pygame.display.set_mode([1024,640])
pygame.display.set_caption("Projectile Simulation")
buttontext = pygame.font.SysFont("Calibri",20)
topictext = pygame.font.SysFont("Calibri",18)
maintext = pygame.font.SysFont("Calibri",19)
resulttext = pygame.font.SysFont("Cordia",35)
bigtext = pygame.font.SysFont("Calibri",50)
option = pygame.font.SysFont("Calibri",12)


#color RGB
white = (255,255,255)
black = (0,0,0)
colors = [(255,153,153),(255,204,153),(204,255,153),(153,204,255),(153,153,255),(204,153,255),(255,153,255),(255,153,204)]

#picture
bg = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\Artwork.png')
bg2 = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\Artwork2.png')
mach = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\ppp.png')
mach = pygame.transform.scale(mach, (80,80))
basket = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\basket.png')
basket = pygame.transform.scale(basket, (60,60))
noon = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\noon.png')
noon = pygame.transform.scale(noon,(300,300))
tan = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\tan.png')
tan = pygame.transform.scale(tan,(300,300))
malila = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\malila.png')
malila = pygame.transform.scale(malila,(300,300))
pim = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\pim.png')
pim = pygame.transform.scale(pim,(300,300))
yui = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\yui.png')
yui = pygame.transform.scale(yui,(300,300))
G11 = pygame.image.load('C:\\Users\\User\\Desktop\\งาน Fibo\\งานปี1_2\\sim ver6\\sim ver6\\g11ver2.png')
G11 = pygame.transform.scale(G11,(500,40))

def textlabel(text,x,y):
    label = maintext.render(text,True,black)
    screen.blit(label,(x,y))

def textlabel2(text,x,y):
    label = resulttext.render(text,True,(32,32,32))
    screen.blit(label,(x,y))

class rect():
    def __init__(self,w,h,pos):
        self.rect = pygame.Rect(pos,(w,h))
        self.rect_color = (255,229,204)
    def draw(self):
        pygame.draw.rect(screen, self.rect_color, self.rect)

class rect2():
    def __init__(self,w,h,pos):
        self.rect = pygame.Rect(pos,(w,h))
        self.rect_color = (255,204,229)
    def draw(self):
        pygame.draw.rect(screen, self.rect_color, self.rect,border_radius=15)

class textrect():
    def __init__(self,text,w,h,pos):
        self.textrect = pygame.Rect(pos,(w,h))
        self.textrect_color = (209,204,255)
        self.text_surf = topictext.render(text, True, black)
        self.text_rect = self.text_surf.get_rect(center=self.textrect.center)
    def draw(self):
        pygame.draw.rect(screen, self.textrect_color, self.textrect, border_radius=15)
        screen.blit(self.text_surf, self.text_rect)

class defaultbox():
    def __init__(self,text,w,h,pos):
        self.textrect = pygame.Rect(pos,(w,h))
        self.textrect_color = (255,229,204)
        self.text_surf = topictext.render(text, True, black)
        self.text_rect = self.text_surf.get_rect(center=self.textrect.center)
    def draw(self):
        pygame.draw.rect(screen, self.textrect_color, self.textrect,)
        screen.blit(self.text_surf, self.text_rect)

class button():
    def __init__(self,text,w,h,pos,elevation):
        #CORE ATTRIBUTES
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_posy = pos[1]
        #TOP RECT
        self.toprect = pygame.Rect(pos,(w,h))
        self.topcolor = white
        #BOTTOM RECT
        self.bottomrect = pygame.Rect(pos,(w,elevation))
        self.bottomcolor = (255,102,102)
        #TEXT
        self.text_surf = buttontext.render(text,True,black)
        self.text_rect = self.text_surf.get_rect(center = self.toprect.center)

    def draw(self):
        #ELEVATION LOGIC
        self.toprect.y = self.original_posy - self.dynamic_elevation
        self.text_rect.center = self.toprect.center

        self.bottomrect.midtop = self.toprect.midtop
        self.bottomrect.height = self.toprect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottomcolor,self.bottomrect,border_radius=15)
        pygame.draw.rect(screen,self.topcolor,self.toprect,border_radius=15)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.toprect.collidepoint(mouse_pos):
            self.topcolor = (255,153,153)
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    pass
                    # print('Click')
                    # self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.topcolor = white

COLOR_INACTIVE = (255,204,153)
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont("Calibri",18)
class InputBox():
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = topictext.render(text, True, black)
        self.active = False


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if len(self.text) < 6:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                # Re-render the text.
                    self.txt_surface = FONT.render(self.text, True, black)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+25, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


startbutton = button('START',90,40,(40,560),4)
resetbutton = button('RESET',90,40,(150,560),4)

distance = textrect('BASKET DISTANCE',150,30,(40,35))
spring_recoil = textrect('SPRING RECOIL',150,30,(40,145))
angletext = textrect('ANGLE',150,30,(40,305))
ballmass = textrect('SPRING CONSTANT',150,30,(40,415))
result = textrect('RESULT',150,30,(280,415))

default_angle = defaultbox('37',75,25,(147,350))
default_springcont = defaultbox('480',80,25,(100,460))
aboutbutton = button('about',80,20,(890,610),0.01)
backbutton = button('BACK',90,30,(30,30),0.5)
savebutton = button('save',80,20,(890,580),0.01)
okbutton = button('OK',80,30,(570,225),0.5)

clock = pygame.time.Clock()
input_distance = InputBox(100,80,82,25)
input_springrecoil = InputBox(100,190,82,25)
input_boxes = [input_distance, input_springrecoil]

floatdistance = 0.0
floatspringrecoil = 0.0
angle = 37 * (math.pi / 180)
k_spring = 480

g = 9.81
sy = 0.3
u_shooter = math.sqrt((( 0.5*k_spring * ((floatspringrecoil) ** 2)) - (2.3544 * (math.sin(angle)) * floatspringrecoil)) / 0.12)
u_ball = 1.8 * u_shooter
heightmax = ((u_ball ** 2) * ((math.sin(angle)) ** 2)) / 2 * g
time = (2 * u_ball * math.sin(angle)) / g
cal_distance = u_ball*math.cos(angle) * time

initialrect = rect(70,23,(470,468))
maxheightrect = rect(75,23,(805,468))
timerect = rect(75,23,(390,508))
distancerect = rect(75,23,(730,508))

distanceresults =  rect2(120,40,(800,70))



row = 1
col = 1

screen.blit(bg,(0,0))
pygame.draw.rect(screen, (255,255,255),(280,50,704,350),border_radius=12)
running = True
while running:


    # เพื่อให้จอไม่หระพิบเวลาขึ้นหน้า About
    if aboutbutton.pressed == False and backbutton.pressed == False:
        screen.blit(mach,(345,270))
        screen.blit(basket, (843, 211))

        #input
        pygame.draw.rect(screen, white, (40,50,200,80),border_radius=12)
        pygame.draw.rect(screen, white, (40,160,200,80),border_radius=12)
        #default
        pygame.draw.rect(screen, (204,229,255),(30,260,220,280),border_radius=12)
        pygame.draw.rect(screen,white, (40,320,200,80),border_radius=12)
        pygame.draw.rect(screen,white, (40,430,200,80),border_radius=12)
        #projectile
        pygame.draw.line(screen, (209, 204, 255), (340, 80), (340, 350), 3)
        pygame.draw.line(screen, (209, 204, 255), (340, 350), (950, 350), 3)
        pygame.draw.rect(screen, (209,204,255),(40,415,150,30),border_radius=12)
        #result
        pygame.draw.rect(screen,(255,255,255),(280,430,704,130),border_radius=12)

        startbutton.draw()
        resetbutton.draw()
        spring_recoil.draw()
        distance.draw()
        angletext.draw()
        ballmass.draw()
        result.draw()
        aboutbutton.draw()
        savebutton.draw()



        default_angle.draw()
        default_springcont.draw()

        initialrect.draw()
        maxheightrect.draw()
        timerect.draw()
        distancerect.draw()

        distanceresults.draw()

        #text input
        textlabel('S :',70,85)
        textlabel('m',195, 85)
        textlabel('X :',70,195)
        textlabel('m', 195,195)
        #text default
        textlabel('DEFAULT',106,275)
        textlabel('DEGREE :',70,355)
        textlabel('K :',70,465)
        textlabel('N/m',190,465)
        # text result
        textlabel('INITIAL  SPEED :',330,470)
        textlabel('m/s',555,470)
        textlabel('MAXIMUM HEIGHT :',640,470)
        textlabel('m',887,470)
        textlabel('TIME :',330,510)
        textlabel('s',480,510)
        textlabel('DISTANCE :', 640, 510)
        textlabel('m', 815, 510)
        # textlabel('BY G11 POWERPUFF GIRL', 640, 548)
        screen.blit(G11, (350, 580))

        range1 = option.render('min = 0.01 , max = 9.99', True, black)
        screen.blit(range1, (82, 115))
        range2 = option.render('min = 0.01 , max = 0.10', True, black)
        screen.blit(range2, (85, 225))

        for box in input_boxes:
            box.draw(screen)

    if startbutton.pressed == True:
        if floatdistance and floatspringrecoil == 0:
            print('please enter num')
            pass
        else:
            textlabel(str(format(u_ball,'.2f')), 488 , 470)
            textlabel(str(format(heightmax,'.2f')), 822, 470)
            textlabel(str(format(time, '.2f')), 410, 510)
            textlabel(str(format(cal_distance, '.2f')), 750, 510)
            if floatdistance - 0.07 <= cal_distance <= floatdistance + 0.07 :
                textlabel2('GOAL', 828, 78)
            else:
                textlabel2('FAIL', 837, 78)

    if savebutton.pressed == True:
        date = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        pygame.image.save(screen,f"data//{date}.png")
        savebutton.pressed = False

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        for box in input_boxes:
            box.handle_event(event)

    pygame.display.flip()

    floatdistance = 0.0
    floatspringrecoil = 0.0
    character = ['a','b','c','d','e','f','g','h','i'
                 'j','k','l','m','n','o','p','q','r',
                 's','t','u','v','w','x','y','z']
    for i in range(0,len(input_distance.text)):
        if input_distance.text[i] in character:
            pygame.draw.rect(screen, (255,102,102), (462, 170, 300, 100), border_radius=12)
            notice = resulttext.render('Enter numbers only', True, white)
            screen.blit(notice, (495,190))
            okbutton.draw()
        else:
            if input_distance.text[i] == '.':
                pass
            elif input_distance.text[i-1] == '.':
                floatdistance += float(input_distance.text[i])/10
            elif i == 3:
                floatdistance += float(input_distance.text[i])/100
            elif i == 4:
                floatdistance += float(input_distance.text[i])/1000
            else:
                floatdistance += float(input_distance.text[i])

    for i in range(0,len(input_springrecoil.text)):
        if input_springrecoil.text[i] in character:
            pygame.draw.rect(screen, (255, 102, 102), (462, 170, 300, 100), border_radius=12)
            notice = resulttext.render('Enter numbers only', True, white)
            screen.blit(notice, (495, 190))
            okbutton.draw()
        else:
            if input_springrecoil.text[i] == '.':
                pass
            elif input_springrecoil.text[i - 1] == '.':
                floatspringrecoil += float(input_springrecoil.text[i]) / 10
            elif i == 3:
                floatspringrecoil += float(input_springrecoil.text[i]) / 100
            elif i == 4:
                floatspringrecoil += float(input_springrecoil.text[i]) / 1000
            else:
                floatspringrecoil += float(input_springrecoil.text[i])

    u_shooter = math.sqrt(   ((0.5*k_spring* ((floatspringrecoil)**2)) - (2.3544 * (math.sin(angle)) * floatspringrecoil) )/ 0.12)
    u_ball = 1.8*u_shooter
    heightmax = ( (u_ball**2) * ( (math.sin(angle)) ** 2) ) / (2*g)
    time = (2 * u_ball * math.sin(angle)) / g
    cal_distance = u_ball*math.cos(angle) * time

    runtime = 0
    x = 0
    y = 0
    k = 480
    endtime = 0

    if startbutton.pressed == True:
        if u_ball == 0:
            pygame.draw.rect(screen, (255, 102, 102), (462, 170, 300, 100), border_radius=12)
            notice2 = resulttext.render('Please enter values', True, white)
            screen.blit(notice2, (495, 190))
            okbutton.draw()
        else:
            while runtime <= endtime:
                endtime = cal_distance / (u_ball * math.cos(angle))
                x = 428 + (u_ball * math.cos(angle) * runtime) * (500/floatdistance)
                y = 282 - (((u_ball * math.sin(angle)) * runtime) + (-4.9 * runtime ** 2)) * 255
                limity = 282 - 0.6 * 100  # y ที่มีหน่วยเป็น  cm
                runtime += 0.03 - ((floatspringrecoil/0.05)-1)*0.005
                if x <= 950 and y <= 282:
                    if y >= 81:
                        pygame.draw.circle(screen, random.choice(colors), (x, y), 5)

    if resetbutton.pressed == True or okbutton.pressed == True:
        startbutton.pressed = False
        resetbutton.pressed = False
        okbutton.pressed = False
        for box in input_boxes:
            box.text = ''
            box.txt_surface = FONT.render(box.text, True, black)
        pygame.draw.rect(screen, (255, 255, 255), (280, 50, 704, 350), border_radius=12)
        row += 1

    if aboutbutton.pressed == True :
        resetbutton.pressed = True
        pygame.draw.rect(screen, (204,229,255), (0, 0, 1024,640), border_radius=1)
        screen.blit(bg2, (0, 0))
        Member = bigtext.render('Our Members', True, black)
        screen.blit(Member, (360, 122))

        # textlabel('Our Members', 438, 122)
        textlabel('MALILA', 185, 200)
        textlabel('23', 200, 230)
        textlabel('TAN', 350, 200)
        textlabel('13', 355, 230)
        textlabel('NOON', 490, 200)
        textlabel('08', 500, 230)
        textlabel('YUI', 645, 200)
        textlabel('47', 650, 230)
        textlabel('PIM', 790, 200)
        textlabel('63', 795, 230)
        screen.blit(malila, (60, 225))
        screen.blit(tan, (210, 220))
        screen.blit(noon, (360, 220))
        screen.blit(yui, (510, 230))
        screen.blit(pim, (660, 220))
        backbutton.draw()

    if backbutton.pressed == True:
        screen.fill((255, 204, 229))
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (280, 50, 704, 350), border_radius=12)
        screen.blit(mach, (345, 270))
        screen.blit(basket, (843, 211))

        # input
        pygame.draw.rect(screen, white, (40, 50, 200, 80), border_radius=12)
        pygame.draw.rect(screen, white, (40, 160, 200, 80), border_radius=12)
        # default
        pygame.draw.rect(screen, (204, 229, 255), (30, 260, 220, 280), border_radius=12)
        pygame.draw.rect(screen, white, (40, 320, 200, 80), border_radius=12)
        pygame.draw.rect(screen, white, (40, 430, 200, 80), border_radius=12)
        # projectile
        pygame.draw.line(screen, (209, 204, 255), (340, 80), (340, 350), 3)
        pygame.draw.line(screen, (209, 204, 255), (340, 350), (950, 350), 3)
        pygame.draw.rect(screen, (209, 204, 255), (40, 415, 150, 30), border_radius=12)
        # result
        pygame.draw.rect(screen,(255,255,255),(280,430,704,130),border_radius=12)

        startbutton.draw()
        resetbutton.draw()
        spring_recoil.draw()
        distance.draw()
        angletext.draw()
        ballmass.draw()
        result.draw()
        aboutbutton.draw()

        default_angle.draw()
        default_springcont.draw()

        initialrect.draw()
        maxheightrect.draw()
        timerect.draw()
        distancerect.draw()

        distanceresults.draw()

        # text input
        textlabel('S :', 70, 85)
        textlabel('m', 195, 85)
        textlabel('X :', 70, 195)
        textlabel('m', 195, 195)
        # text default
        textlabel('DEFAULT', 106, 275)
        textlabel('DEGREE :', 70, 355)
        textlabel('K :', 70, 465)
        textlabel('N/m', 190, 465)
        # text result
        textlabel('INITIAL  SPEED :', 330, 470)
        textlabel('m/s', 555, 470)
        textlabel('MAXIMUM HEIGHT :', 640, 470)
        textlabel('m', 887, 470)
        textlabel('TIME :', 330, 510)
        textlabel('s', 480, 510)
        textlabel('DISTANCE :', 640, 510)
        textlabel('m', 815, 510)

        aboutbutton.pressed = False
        backbutton.pressed = False

    pygame.display.update()
    # print(pygame.mouse.get_pos())

pygame.quit()
sys.exit(0)

