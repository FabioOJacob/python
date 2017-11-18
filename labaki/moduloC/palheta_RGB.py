from tkinter import *
class Palheta:
    def __init__(self, raiz):

        raiz.title('Palheta')
        self.canvas = Canvas(raiz, width = 300, height = 300)
        self.canvas.pack()
        self.frame = Frame(raiz)
        self.frame.pack()
        self.frame2 = Frame(raiz)
        self.frame2.pack()

        self.canvas.create_oval(45, 45, 255, 255, fill = 'white', tag = 'bola')
        r = IntVar()
        g = IntVar()
        b = IntVar()
        Label(self.frame, text = 'Vermelho: ').pack(side = LEFT)
        self.vermelho = Entry(self.frame, width = 4, text = r)
        self.vermelho.focus_force()
        self.vermelho.pack(side = LEFT)
        Label(self.frame, text = 'Verde: ').pack(side = LEFT)
        self.verde = Entry(self.frame, width = 4, text = g)
        self.verde.pack(side = LEFT)
        Label(self.frame, text = 'Azul: ').pack(side = LEFT)
        self.azul = Entry(self.frame, width = 4, text = b)
        self.azul.pack(side = LEFT)
        r.set(0)
        g.set(0)
        b.set(0)

        Button(self.frame2, text = 'Mostrar', command = self.misturar).pack(side = LEFT)
        self.rgb = Label(self.frame2, text = '', width = 15, font = ('Verdana', '10', 'bold'))
        self.rgb.pack()

        
    def misturar(self):
        verm = self.vermelho.get().lower()
        verd = self.verde.get().lower()
        azul = self.azul.get().lower()
        if verm not in 'abcdefghijklmonpqrstuvwyxz':
            if verd not in 'abcdefghijklmonpqrstuvwyxz':
                if azul not in 'abcdefghijklmonpqrstuvwyxz':
                    if 0 <= int(self.vermelho.get()) <= 255 and 0 <= int(self.verde.get()) <= 255 and 0 <= int(self.azul.get()) <= 255:
                        cor = '#%02x%02x%02x' %(int(self.vermelho.get()), int(self.verde.get()), int(self.azul.get()))
                        self.canvas.delete('bola')
                        self.canvas.create_oval(45, 45, 255, 255, fill = cor, tag = 'bola')
                        self.rgb['text'] = cor
                        self.vermelho.focus_force()
                    else:
                        self.rgb['text'] = 'Valor Inválido'
                else:
                    self.rgb['text'] = 'Somente números'
            else:
                self.rgb['text'] = 'Somente números'
        else:
            self.rgb['text'] = 'Somente números'

inst = Tk()
Palheta(inst)
inst.mainloop()
