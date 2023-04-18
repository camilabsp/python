from tkinter import *
from tkinter import ttk
from datetime import *
import sqlite3

root = Tk()

class funcoes():
    def limpar_tela(self):
        self.data_entry.delete(0,END)
        self.codigo_entry.delete(0,END)
        self.qtd_entry.delete(0,END)
        self.valor_unit_entry.delete(0,END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('invest')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def cria_bd(self):
        self.conecta_bd()
        ##criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS invest(
                data TEXT PRIMARY KEY,
                codigo TEXT NOT NULL,
                qtd TEXT,
                valor_unit TEXT,
                c_v TEXT,
                valor_operacao REAL,
                tx_corret REAL,
                tx_imposto REAL,
                valor_final REAL
                
            );
        """)

        self.conn.commit();print('banco de dados criado')
        self.desconecta_bd

    def add_dados(self):
        self.data = self.data_entry.get()    
        self.codigo = self.codigo_entry.get().upper()
        self.qtd = int(self.qtd_entry.get())
        self.valor_unit = float(self.valor_unit_entry.get())

        self.c_v = 'c' #criar evento e botao comprar/vender'''
        self.valor_operacao = self.qtd * self.valor_unit
        self.tx_corret = 5.00
        self.tx_imposto = round((0.0003 * self.valor_operacao),2)

        if self.c_v == 'C':
            self.valor_final = round((self.valor_operacao + self.tx_corret + self.tx_imposto),2)
        else:
            self.valor_final = round((self.valor_operacao - self.tx_corret - self.tx_imposto),2)
        

        self.conecta_bd()

        self.cursor.execute("""INSERT INTO invest(data,codigo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_imposto,valor_final)
            VALUES (?,?,?,?,?,?,?,?,?)""",(self.data,self.codigo,self.qtd,self.valor_unit,self.c_v,self.valor_operacao,self.tx_corret,self.tx_imposto,self.valor_final)) 

        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()

    def select_lista(self):
        self.lista.delete(*self.lista.get_children())
        self.conecta_bd()
        l = self.cursor.execute(""" SELECT data,codigo,qtd,valor_unit,c_v,valor_operacao,tx_corret,tx_imposto,valor_final
            FROM invest """)
        for i in l:
            self.lista.insert("",END,values=i)

        self.desconecta_bd()

class app(funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        self.cria_bd()
        self.select_lista()
        root.mainloop()
        
    def tela(self):
        self.root.title('Otimizador de Investimentos')
        self.root.configure(background='white')
        self.root.geometry('600x500')
        self.root.resizable(True,True) #responsividade
        
    def frames(self):
        
        self.frame1 = Frame(self.root,bd=9,bg='lightgray')
        self.frame1.place(relx=0.0,rely=0.0,relwidth=1,relheight=0.35)
        self.frame2 = Frame(self.root,bd=9,bg='white')
        self.frame2.place(relx=0.0,rely=0.36,relwidth=1,relheight=0.75)
        
    def widgets_frame1(self):
        
        #botão_limpar
        self.bt_limpar = Button(self.frame1,text = 'Limpar', bg='#67B3FF',bd = '0.05',command=self.limpar_tela)
        self.bt_limpar.place(relx=0.8,rely=0.1,relwidth=0.1,relheight=0.15)
        #botão_buscar
        self.bt_comprar = Button(self.frame1,text = 'Comprar',bg='#67B3FF',bd = '0.05')
        self.bt_comprar.place(relx=0.8,rely=0.4,relwidth=0.1,relheight=0.15)
        #botão_adicionar
        self.bt_adicionar = Button(self.frame1,text = 'Adicionar',bg='#67B3FF',bd = '0.05',command=self.add_dados)
        self.bt_adicionar.place(relx=0.8,rely=0.7,relwidth=0.1,relheight=0.15)
        #Label e entrada da data
        self.lb_data = Label(self.frame1,text = 'Data',bg = 'white')
        self.lb_data.place(relx=0.08,rely=0.001)
        self.data_entry = Entry(self.frame1)
        self.data_entry.place(relx=0.05,rely=0.15,relwidth=0.12)
        #Label e entrada do codigo
        self.lb_codigo = Label(self.frame1,text = 'Código',bg = 'white')
        self.lb_codigo.place(relx=0.22,rely=0.001)
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.2,rely=0.15,relwidth=0.12)
        #Label e entrada da quantidade
        self.lb_qtd = Label(self.frame1,text = 'Qtd.',bg = 'white')
        self.lb_qtd.place(relx=0.39,rely=0.001)
        self.qtd_entry = Entry(self.frame1)
        self.qtd_entry.place(relx=0.35,rely=0.15,relwidth=0.12)
        #Label e entrada do valor unitario
        self.lb_valor_unit = Label(self.frame1,text = 'Valor unit.',bg = 'white')
        self.lb_valor_unit.place(relx=0.51,rely=0.001)
        self.valor_unit_entry = Entry(self.frame1)
        self.valor_unit_entry.place(relx=0.5,rely=0.15,relwidth=0.12)
        #radiobutton
        self.radio_valor = IntVar()
        self.compra = ttk.Radiobutton(self.frame1,text = 'Comprar', value = 1, variable = self.radio_valor)
        self.compra.place(relx = 0.65, rely = 0.005)
        self.venda = ttk.Radiobutton(self.frame1,text = 'Vender', value = 2, variable = self.radio_valor)
        self.venda.place(relx = 0.65, rely = 0.15)

        
        
    def widgets_frame2(self):
        
        #tabela
        self.lista = ttk.Treeview(self.frame2,height = 10,column = ('col1','col2','col3','col4','col5','col6','col7','col9','col10'))

        self.lista.heading('#0',text='')
        self.lista.heading('#1',text='Data')
        self.lista.heading('#2',text='Código')
        self.lista.heading('#3',text='Qtd.')
        self.lista.heading('#4',text='Valor Unit.')
        self.lista.heading('#5',text='C/V')
        self.lista.heading('#6',text='Valor Op.')
        self.lista.heading('#7',text='tx.Corret.')
        self.lista.heading('#8',text='tx.Imposto')
        self.lista.heading('#9',text='Valor Final')

        self.lista.column('#0',width=0)
        self.lista.column('#1',width=70)
        self.lista.column('#2',width=70)
        self.lista.column('#3',width=50)
        self.lista.column('#4',width=70)
        self.lista.column('#5',width=40)
        self.lista.column('#6',width=60)
        self.lista.column('#7',width=60)
        self.lista.column('#8',width=70)
        self.lista.column('#9',width=90)
       
      
        
        self.lista.place(relx=0,rely=0,relwidth=1,relheight=0.85)
        
        #barra de rolagem
        #self.scrol_tab = scrollbar(self.frame2,orient='vertical')
        #self.lista.configure(yscroll=self.scrol_tab.set)
        #self.scroollista.pack()

app()
