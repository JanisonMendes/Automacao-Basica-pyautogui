import pyautogui
import time

pyautogui.PAUSE = 0.5 # tempo de espera entre cada comando  
# pyautogui.press() -> apertar 1 tecla 
# pyautogui.click() -> clicar com o mouse 
# pyautogui.write() -> escrever um texto
# pyautogui.hotkey("ctrl", "c") -> apertar 2 ou mais teclas ao mesmo tempo


# abriria o meu navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site 
pyautogui.write("https://github.com/JanisonMendes")
pyautogui.press("enter")

time.sleep(5) # esperar o site carregar
# preencher o formulário 
# enviar o formulário