import pyautogui as abrirSap
import time 

abrirSap.alert("Olá, pressione OK e aguarde")
abrirSap.PAUSE = 0.5

abrirSap.hotkey('winleft', 'r')
abrirSap.write('saplogon.exe')
abrirSap.press('enter')
time.sleep(1)
abrirSap.press('down')
abrirSap.press('down')
abrirSap.press('down')
abrirSap.press('down')
abrirSap.press('down')
abrirSap.press('down')
abrirSap.press('enter')
time.sleep(8)               
abrirSap.press('esc')
abrirSap.press('enter')
time.sleep(1)
abrirSap.write('iw38')
abrirSap.press('enter')
abrirSap.hotkey('shift','f5')
time.sleep(1)
abrirSap.write('SIM_MI_PD')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.hotkey('delete')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.press('enter')
abrirSap.hotkey('tab')
abrirSap.hotkey('tab')
abrirSap.press('enter')
time.sleep(1)
abrirSap.alert("Seu SAP foi aberto, insira as ordens e prossiga com a execução")


