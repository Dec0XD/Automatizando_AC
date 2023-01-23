import pyautogui
from time import sleep
import keyboard


#Passos para automatizar o jogo Adventure Captalist

#Abrir a Steam
pyautogui.click(813,1061)
sleep(2)
#Abrir a aba do jogo
pyautogui.click(116,367)
#Abrir o jogo - time(10)
pyautogui.click(394,430)
sleep(5)
#Selecionar Resolução do jogo e abrir - time (10)
pyautogui.click(1049,726)
sleep(10)
pyautogui.click(1015,823)
#Clicar em max buy
def max_buy():
    for i in range(1,5):
        pyautogui.click(1815,50)

#LOOP de incio de game
def inicio():
    for i in range(0,10):
        pyautogui.click(730,250)
        pyautogui.click(730,400)
        pyautogui.click(730,550)
        pyautogui.click(730,700)
        pyautogui.click(730,850)

        pyautogui.click(1450,250)
        pyautogui.click(1450,400)
        pyautogui.click(1450,550)
        pyautogui.click(1450,700)
        pyautogui.click(1450,850)

#LOOP de compras 
def compras():
    for i in range(0,10):
        #Comprar lojas
        pyautogui.click(704,309)
        pyautogui.click(704,461)
        pyautogui.click(704,620)
        pyautogui.click(704,777)
        pyautogui.click(704,951)
        
        pyautogui.click(1400,309)
        pyautogui.click(1400,461)
        pyautogui.click(1400,620)
        pyautogui.click(1400,777)
        pyautogui.click(1400,951)
        #Comprar upgrades
        pyautogui.click(1495,58)


#Comprando os upgrades pela 1 vez
def ups():
    pyautogui.click(151,524)
    pyautogui.click(1338,642)
    for i in range(0,2):
        for i in range(0,11):
            pyautogui.click(806,680)
        pyautogui.click(955,274)
        pyautogui.click(1338,642)
        for i in range(0,11): 
            pyautogui.click(806,680)
        pyautogui.click(1794,102)

#Comprando o quickup
""" def quick_up():
    for i in range(0,1):
        pyautogui.click(151,524)
        pyautogui.click(1338,642)
        pyautogui.click(955,274)
        pyautogui.click(1338,642)
        pyautogui.click(1800,100)
 """

#Comprando os managers
def menagers():
    pyautogui.click(149,627)
    
    for i in range(0,21):
        pyautogui.click(821,688)
    pyautogui.click(1089,273)
    
    for i in range(0,13):
        pyautogui.click(821,688)
    pyautogui.click(1800,100)
        
#LOOP full gameplay
for i in range(0,1):
    max_buy()
    inicio()
    menagers()
    compras()
    ups()
while True:
    compras()
    
    
