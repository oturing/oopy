import Tkinter
from time import strftime

relogio = Tkinter.Label()

relogio.pack()
relogio['text'] = strftime('%H:%M:%S')
relogio['font'] = 'Helvetica 120 bold'

def tictac():
    agora = strftime('%H:%M:%S')
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(100, tictac)

tictac()
relogio.mainloop()
