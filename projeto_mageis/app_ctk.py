import customtkinter 
from tkinter import ttk #treeview(tabela)

customtkinter.set_appearance_mode('Light')
customtkinter.set_default_color_theme('dark-blue')
root = customtkinter.CTk()

class app():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        root.mainloop()
    def tela(self):
        self.root.title('Otimizador de Investimentos')
        self.root.geometry('700x500')
        self.root.resizable(True,True) #responsividade
        self.root.maxsize(width=750,height=500)
        self.root.minsize(width=500, height=400)
    
    def frames(self):
        #frames
        self.frame1 = customtkinter.CTkFrame(self.root)
        self.frame1.place(relx = 0,rely = 0,relwidth = 1,relheight = 0.18)
        self.frame2 = customtkinter.CTkFrame(self.root)
        self.frame2.place(relx = 0,rely =0.18, relwidth = 1, relheight = 0.85)
    
    def widgets_frame1(self):
        #labels
        self.data = customtkinter.CTkLabel(self.frame1,text='Data')
        self.data.place(relx = 0.1, rely = 0.1)
        self.codigo = customtkinter.CTkLabel(self.frame1,text='Código')
        self.codigo.place(relx = 0.23, rely = 0.1)
        self.qtd = customtkinter.CTkLabel(self.frame1,text='Qtd.')
        self.qtd.place(relx = 0.38, rely = 0.1)
        self.valor_unit = customtkinter.CTkLabel(self.frame1,text='Valor unit. (R$)')
        self.valor_unit.place(relx = 0.48, rely = 0.1)
        #entrys
        self.data_entry = customtkinter.CTkEntry(self.frame1, width=80)
        self.data_entry.place(relx = 0.06, rely = 0.4)
        self.codigo_entry = customtkinter.CTkEntry(self.frame1, width=80)
        self.codigo_entry.place(relx = 0.2, rely = 0.4)
        self.qtd_entry = customtkinter.CTkEntry(self.frame1, width=70)
        self.qtd_entry.place(relx = 0.35, rely = 0.4)
        self.valor_unit_entry = customtkinter.CTkEntry(self.frame1, width=80)
        self.valor_unit_entry.place(relx = 0.48, rely = 0.4)
        #botão 
        self.bt_add = customtkinter.CTkButton (self.frame1,text = 'Adicionar', width = 70)
        self.bt_add.place(relx = 0.8, rely = 0.2)
        self.bt_apagar = customtkinter.CTkButton (self.frame1,text = 'Apagar', width = 70)
        self.bt_apagar.place(relx = 0.8, rely = 0.6)
        #radiobutton
        self.compra = customtkinter.CTkRadioButton(self.frame1,text = 'Comprar')
        self.compra.place(relx = 0.65, rely = 0.2)
        self.venda = customtkinter.CTkRadioButton(self.frame1,text = 'Vender')
        self.venda.place(relx = 0.65, rely = 0.6)
        

    def widgets_frame2(self):
        #cria tabela
        self.tabela = ttk.Treeview(self.frame2,height=3,column=('col1','col2','col3','col4','col5','col6','col7','col8'))
        #cabeçado das colunas
        self.tabela.heading('#0',text='Data')
        self.tabela.heading('#1',text='Código')
        self.tabela.heading('#2',text='Qtd.')
        self.tabela.heading('#3',text='Valor unit.')
        self.tabela.heading('#4',text='C/V')
        self.tabela.heading('#5',text='Valor op.')
        self.tabela.heading('#6',text='Taxa corret.')
        self.tabela.heading('#7',text='Taxa imposto')
        self.tabela.heading('#8',text='Valor final')
        #tamanho das colunas em relação a lista
        self.tabela.column('#0',width= 70)
        self.tabela.column('#1',width=70)
        self.tabela.column('#2',width= 50)
        self.tabela.column('#3',width=80)
        self.tabela.column('#4',width= 65)
        self.tabela.column('#5',width=90)
        self.tabela.column('#6',width= 90)
        self.tabela.column('#7',width=90)
        self.tabela.column('#8',width= 80)
        #posicao da tabela
        self.tabela.place(relx = 0.01,rely = 0.01, relwidth=0.98, relheight=0.93)

        #scrol
        #self.scrol = customtkinter.CTkScrollbar(self.frame2,orientation='vertical')
        #self.tabela.configure(yscroll=self.scrol.set)
        #self.scrol.place(relx = 0.98, rely = 0.04)

app()

