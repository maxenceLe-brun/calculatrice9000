import pygame
import random
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 16)
screen = pygame.display.set_mode([300, 400])
running = True
l = [["2nd","deg","MOD","CE","AC"],["x!","nCr","Ran#","log","ln"],["√","x^y","x^-1","/","sin"],["7","8","9","*","cos"],["4","5","6","-","tan"],["1","2","3","+","π"],["+/-","0",".","e","="]]
screen.fill((190, 190, 190))
pygame.draw.rect(screen, (30,30,30), (0,0,300,40))
for a in range(5):
    for b in range(7):
        pygame.draw.rect(screen, (230,230,230),(3+60*a,48+50*b,52,42))
        pygame.draw.rect(screen,(100,100,100),(5+60*a,50+50*b,52,42))
        pygame.draw.rect(screen,(215,215,215),(5+60*a,50+50*b,50,40))
        text_surface = my_font.render(l[b][a], False, (0, 0, 0))
        screen.blit(text_surface, (25-(len(l[b][a])-1)*4+a*60,54+b*50))
pygame.display.flip()
result = ""
last = False
order = 0
R = []
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event,pygame.event.get())
        print(result)
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pressed(),last)
            xy = pygame.mouse.get_pos()
            print(xy,result)
            for a in range(5):
                for b in range(7):
                    print(5+60*a <= xy[0] <= 55+60*a,50+50*b <= xy[1] <= 90+50*b)
                    if 5 + 60 * a <= xy[0] <= 55 + 60 * a and 50 + 50 * b <= xy[1] <= 90 + 50 * b:
                        result += l[b][a]
                        
                        pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
                        text = my_font.render(result,False,(200,200,200))
                        screen.blit(text,(280-9*len(result),18))
                        
        if len(result)>0:
            if result[-1] == "=" and len(result) > 1:
                if "√" in result:
                    root = []
                    for a in range(len(result)):
                        if result[a] == "√":
                            root.append(a)
                        elif len(root)==1 and result[a] not in ["0","1","2","3","4","5","6","7","8","9","."]:
                            root.append(a)
                    if len(root) == 2:
                        print(result[:root[0]] + result[root[0]+1:root[1]] + "**(1/2)" + result[root[1]:])
                        result = result[:root[0]] + result[root[0]+1:root[1]] + "**(1/2)" + result[root[1]:]
                    elif len(root):
                        print(result[:root[0]] + result[root[0]+1:-1] + "**(1/2)" + result[-1])
                        result = result[:root[0]] + result[root[0]+1:-1] + "**(1/2)" + result[-1]
                if "ln" in result:
                    root = []
                    for a in range(1,len(result)):
                        if result[a-1]+result[a] == "ln":
                            root.append(a)
                        elif len(root) == 1 and result[a] not in ["0","1","2","3","4","5","6","7","8","9","."]:
                            root.append(a)
                    if len(root)>0:
                        result = result[:root[0]-1] + "1/2.718**" +result[root[0]+1:]
                #if "sin" in result:
                    #root = []
                    #for a in range(len(result)):
                        #if result[a-2] + result[a-1] + result[a] == "sin":
                            #root.append(a)
                        #elif len(root) == 1 and result[a] not in ["0","1","2","3","4","5","6","7","8","9","."]:
                            #root.append(a)
                    #if len(root) == 2:
                        #reset = 0
                        #for b in range(int(result[root[0]+1:root[1]])):
                            #div = [2*c+1 for c in range(1,b+1)]
                            #for d in range(len(div)):
                                #
                            #reset += (-1)**b * (int(result[root[0]+1:root[1]])**(2*b + 1) / [2*c+1 for c in range(1,b+1)])
                        
                result = result[:-1]
                if order:
                    result += ")"
                test = str(eval(result))
                result = test
                pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
                text= my_font.render(test,False,(200,200,200))
                screen.blit(text,(280-9*len(test),18))
            elif result[-1] == "C":
                result = ""
                pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
            elif result[-1] == "E":
                result = result[:-2]
                tab = 0
                for a in range(len(result)):
                    print(a,result)
                    if result[-(a+1)] not in ["0","1","2","3","4","5","6","7","8","9","."]:
                        result = result[:-a]
                        tab += 1
                        pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
                        text= my_font.render(result,False,(200,200,200))
                        screen.blit(text,(280-9*len(result),18))
                        break
                    if tab == len(result):
                        result == ""
            elif result[-1] == "y":
                result = result[:-3] + "**"
                pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
                text= my_font.render(result,False,(200,200,200))
                screen.blit(text,(280-9*len(result),18))
            elif result[-1] == "!":
                result = result[:-2]
                tab = 0
                for a in range(len(result)):
                    if result[a] not in ["0","1","2","3","4","5","6","7","8","9"]:
                        tab = a
                call = int(result[tab+1:])
                reset = 1
                for a in range(1,call+1):
                    reset *= a
                result = result[:tab+1] + str(reset)
                pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
                text= my_font.render(result,False,(200,200,200))
                screen.blit(text,(280-9*len(result),18))
            elif result[-1] == "π":
                result = result[:-1]
                result += "3.14"
            elif result[-1] == "e":
                result = result[:-1] + "*10**"
            elif len(result)>=3:
                if result[-3:] == "+/-":
                    result = result[:-3]
                    if result[0] == "-":
                        result = "+" + result[1:]
                    elif result[0] == "+":
                        result = "-" + result[1:]                    
                    else: 
                        result = "-" + result
                elif result[-3:] == "2nd":
                    result = result[:-3]
                    pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
                    text= my_font.render(result,False,(200,200,200))
                    screen.blit(text,(280-9*len(result),18))
                elif result[-3:] == "^-1":
                    result = result[:-4] + "**" + result[-2:]
                elif result[-3:] == "MOD":
                    result = result[:-3] +"%"
                elif result[-3:] == "an#":
                    result = result[:-4] +str(random.randrange(100,1000))
                    pygame.draw.rect(screen,(30,30,30),(0,0,300,40))
                    text= my_font.render(result,False,(200,200,200))
                    screen.blit(text,(280-9*len(result),18))
                    
                    
    pygame.display.flip()
pygame.quit()
