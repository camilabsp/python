import customtkinter 

customtkinter.set_appearance_mode('Light')
customtkinter.set_default_color_theme('dark-blue')
root = customtkinter.CTk()

class app():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.botao()
        root.mainloop()
    def tela(self):
        self.root.title('Otimizador de Investimentos')
        self.root.geometry('700x500')
        self.root.resizable(True,True) #responsividade
    
    def frames(self):
        self.frame1 = customtkinter.CTkFrame(self.root)
        self.frame1.place(relx = 0,rely = 0,relwidth = 1,relheight = 0.30)
        
    
    def botao(self):
        self.bt_add = customtkinter.CTkButton (self.frame1,text = 'Adicionar')
        self.bt_add.place(relx = 0.1, rely = 0.9)
        self.bt_apagar = customtkinter.CTkButton (self.frame1,text = 'Apagar')
        self.bt_apagar.place(relx = 0.5, rely = 0.9)




app()

