import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('Clique na opção desejada', buttons = ['Excel' , 'Explorer', 'Notepad'])


if opcao == "Excel":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('EXCEL.EXE')
    escolha_opcao.press('enter')    
elif opcao == "Explorer":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('explorer')
    escolha_opcao.press('enter')  
elif opcao == "Notepad":
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('notepad.exe')     
    escolha_opcao.press('enter')  
