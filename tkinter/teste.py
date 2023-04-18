import customtkinter 

customtkinter.set_appearance_mode('Light')
customtkinter.set_default_color_theme('dark-blue')
root = customtkinter.CTk()

class app():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        root.mainloop()
    def tela(self):
        self.root.title('Otimizador de Investimentos')
        self.root.geometry('700x500')
        self.root.resizable(True,True) #responsividade
    
    def frames(self):
        self.frame1 = customtkinter.CTkFrame(self.root)
        self.frame1.place(relx = 0,rely = 0,relwidth = 1,relheight = 0.20)
        

    
    def widgets_frame1(self):
        self.bt_add = customtkinter.CTkButton (self.frame1,text = 'Adicionar', width = 70)
        self.bt_add.place(relx = 0.8, rely = 0.2)
        self.bt_apagar = customtkinter.CTkButton (self.frame1,text = 'Apagar', width = 70)
        self.bt_apagar.place(relx = 0.8, rely = 0.6)

        
        self.compra = customtkinter.CTkRadioButton(self.frame1,text = 'Comprar')
        self.compra.place(relx = 0.65, rely = 0.2)
        self.venda = customtkinter.CTkRadioButton(self.frame1,text = 'Vender')
        self.venda.place(relx = 0.65, rely = 0.6)
        

    def widgets_frame2(self):
        pass
        


app()

