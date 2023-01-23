"""

Made by : Maxence Le Brun
IDE used : Spyder
module recquired: pygame | random


"""


import pygame
import random
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 16)
screen = pygame.display.set_mode([300, 400])
running = True
l = [["2nd", "deg", "MOD", "CE", "AC"],
     ["x!", "nCr", "Ran#", "log", "ln"],
     ["√", "x^y", "x^-1", "/", "sin"],
     ["7", "8", "9", "*", "cos"],
     ["4", "5", "6", "-", "tan"],
     ["1", "2", "3", "+", "π"],
     ["+/-", "0", ".", "e", "="]]
screen.fill((190, 190, 190))
pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
for a in range(5):
    for b in range(7):
        if a == 4 and b == 6:
            pygame.draw.rect(screen, (255, 218, 0), (3 + 60 * a, 48 + 50 * b, 52, 42))
            pygame.draw.rect(screen, (230, 88, 20), (5 + 60 * a, 50 + 50 * b, 52, 42))
            pygame.draw.rect(screen, (255, 128, 0), (5 + 60 * a, 50 + 50 * b, 50, 40))
            text_surface = my_font.render(l[b][a], False, (0, 0, 0))
            screen.blit(text_surface, (25 - (len(l[b][a]) - 1) * 4 + a * 60, 54 + b * 50))
        else:
            pygame.draw.rect(screen, (230, 230, 230), (3 + 60 * a, 48 + 50 * b, 52, 42))
            pygame.draw.rect(screen, (100, 100, 100), (5 + 60 * a, 50 + 50 * b, 52, 42))
            pygame.draw.rect(screen, (215, 215, 215), (5 + 60 * a, 50 + 50 * b, 50, 40))
            text_surface = my_font.render(l[b][a], False, (0, 0, 0))
            screen.blit(text_surface, (25 - (len(l[b][a]) - 1) * 4 + a * 60, 54 + b * 50))
pygame.display.flip()
result = ""
R = []
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            xy = pygame.mouse.get_pos()
            for a in range(5):
                for b in range(7):
                    if 5 + 60 * a <= xy[0] <= 55 + 60 * a and 50 + 50 * b <= xy[1] <= 90 + 50 * b:
                        result += l[b][a]
                        pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
                        text = my_font.render(result,False,(200,200,200))
                        screen.blit(text,(280-9*len(result),18))
                        
        if len(result)>0:
            
            #The first IF must be the result request
            if result[-1] == "=" and len(result) > 1:
                
                #Checking part, if root square/log/ln/sin/cos is in the equation to calculate them
                if "√" in result:
                    root = []
                    for a in range(len(result)):
                        if result[a] == "√":
                            root.append(a)
                        elif len(root) == 1 and result[a] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                            root.append(a)
                    if len(root) == 2:
                        result = result[:root[0]] + result[root[0]+1:root[1]] + "**(1/2)" + result[root[1]:]
                    elif len(root):
                        result = result[:root[0]] + result[root[0]+1:-1] + "**(1/2)" + result[-1]
                
                if "log" in result:
                    root = []
                    for a in range(len(result)):
                        if result[a-2]+result[a-1]+result[a] == "log":
                            root.append(a)
                        elif len(root)==1 and result[a] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                            root.append(a)
                    if len(root) == 2:
                        result = result[:root[0] - 2] + "((1/2.718**" + result[root[0] + 1:root[1]] + ")/(1/2.718**10))" + result[root[1]:]
                
                if "ln" in result:
                    root = []
                    for a in range(1, len(result)):
                        if result[a - 1] + result[a] == "ln":
                            root.append(a)
                        elif len(root) == 1 and result[a] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                            root.append(a)
                    if len(root) > 0:
                        result = result[:root[0]-1] + "1/2.718**" + result[root[0] + 1:]
                
                if "sin" in result:
                    root = []
                    for a in range(len(result)):
                        if result[a - 2] + result[a - 1] + result[a] == "sin":
                            root.append(a)
                        elif len(root) == 1 and result[a] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" , "."]:
                            root.append(a)
                    if len(root) == 2:
                        reset = 0
                        for b in range(40):
                            div = 1
                            for c in range(2 * b + 1):
                                div *= c+1
                            reset += ((-1) ** (b % 2)) * ( ( float(result[root[0]+1:root[1]]) ** (2 * b + 1) ) / div)
                        result = result[:root[0] - 2] + str(reset) + result[root[1]:]
                        
                if "cos" in result:
                    root = []
                    for a in range(len(result)):
                        if result[a - 2] + result[a - 1] + result[a] == "cos":
                            root.append(a)
                        elif len(root) == 1 and result[a] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                            root.append(a)
                    if len(root) == 2:
                        reset = 0
                        for b in range(40):
                            div = 1
                            for c in range(2*b):
                                div *= c+1
                            reset += ( ( (-1) ** b) / div ) * ( float(result[root[0] + 1:root[1]]) ** ( 2 * b ) )
                        result = result[:root[0] - 2] + str(reset) + result[root[1]:]
                
                #extract the calcul requested, without the "=" and will eval the string. 
                result = result[:-1]
                test = str(eval(result))
                result = test
                pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
                text = my_font.render(test, False, (200, 200, 200))
                screen.blit(text, (280 - 9 * len(test), 18))
            
            #The All Clear and Cancel Entry
            elif result[-1] == "C":
                result = ""
                pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
            
            elif result[-1] == "E":
                result = result[:-2]
                tab = 0
                for a in range(len(result)):
                    if result[-(a + 1)] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                        result = result[:-a]
                        tab += 1
                        pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
                        text= my_font.render(result, False, (200, 200, 200))
                        screen.blit(text, (280 - 9 * len(result), 18))
                        break
                    if tab == len(result):
                        result == ""
            
            #the x^y request
            elif result[-1] == "y":
                result = result[:-3] + "**"
                pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
                text= my_font.render(result, False, (200, 200, 200))
                screen.blit(text, (280 - 9 * len(result), 18))
            
            #factorial, quite good!
            elif result[-1] == "!":
                result = result[:-2]
                tab = 0
                for a in range(len(result)):
                    if result[a] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                        tab = a
                call = int(result[tab + 1:])
                reset = 1
                for a in range(1, call + 1):
                    reset *= a
                result = result[:tab + 1] + str(reset)
                pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
                text= my_font.render(result, False, (200, 200, 200))
                screen.blit(text, (280 - 9 * len(result), 18))
            
            #pi? what is that? oh... 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893809525720106548586327886593615338182796823030195203530185296899577362259941389124972177528347913151557485724245415069595082953311686172785588907509838175463746493931925506040092770167113900984882401285836160356370766010471018194295559619894676783744944825537977472684710404753464620804668425906949129331367702898915210475216205696602405803815019351125338243003558764024749647326391419927260426992279
            elif result[-1] == "π":
                result = result[:-1]
                result += "3.14159265"
            
            
            elif result[-1] == "e":
                result = result[:-1] + "*10**"
            
            elif len(result) >= 3:
                
                #+/- means that you can reverse your final result with a single click
                if result[-3:] == "+/-":
                    result = result[:-3]
                    if result[0] == "-":
                        result = "+" + result[1:]
                    elif result[0] == "+":
                        result = "-" + result[1:]                    
                    else: 
                        result = "-" + result
                
                #useless button
                elif result[-3:] == "2nd":
                    result = result[:-3]
                    pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
                    text= my_font.render(result, False, (200, 200, 200))
                    screen.blit(text, (280 - 9 * len(result), 18))
                
                #the pow -1 is simple
                elif result[-3:] == "^-1":
                    result = result[:-4] + "**" + result[-2:]
                
                #nothing to explain
                elif result[-3:] == "MOD":
                    result = result[:-3] +"%"
                
                #the random part of the calculator
                elif result[-3:] == "an#":
                    result = result[:-4] +str(random.randrange(100, 1000))
                    pygame.draw.rect(screen, (30, 30, 30), (0, 0, 300, 40))
                    text= my_font.render(result, False, (200, 200, 200))
                    screen.blit(text, (280 - 9 * len(result), 18))
                    
                    
    pygame.display.flip()
pygame.quit()
