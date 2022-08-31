import os
import webbrowser
import time

while(0==0):
    #b = webbrowser.get('firefox')
       
    #urL='https://www.google.com'
    #chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    #webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
    #webbrowser.get('chrome').open_new_tab(urL)
    
    webbrowser.open_new("https://www.youtube.com/watch?v=EBC5F_JaEMs&t=1s")
    webbrowser.open_new("https://www.youtube.com/watch?v=9c2vhVl24Wk&t=3s")
    webbrowser.open_new("https://www.youtube.com/watch?v=TS7bK9_wv3g&t=1s")
    webbrowser.open_new("https://www.youtube.com/watch?v=6HLIOeGSdUY&t=1s")
    webbrowser.open_new("https://www.youtube.com/watch?v=oUmEsN6muCc&t=113s")
    webbrowser.open_new("https://www.youtube.com/watch?v=hdxiH4Co4qc&t=66s")

    time.sleep(200)

    #os.system('killall -KILL tu_navegador') || os.system('taskkill /IM tu_navegador /F')
    #ojo "tu_nevegador" tiene que ser el nombre del proceso que quieres cerrar. En windows puedes ver el mismo en el Administrador de tareas, y en linux con herramientas como htop.
    #recuerda que esto cerrara todos los procesos con ese nombre, por lo que si estas ocupando una ventana aun que no forme parte de las que abriste en el codigo, esta sera cerrada
    #windows te permite seleccionar con que navegador quieres abrir el programa la primera vez que lo ejecutas, si eliges uno diferente a firefox recuerda cambiar el nombre
    #os.system('killall -KILL firefox')
    os.system('taskkill /IM Firefox /F')
    