from datetime import *
class consultas:
    def __init__(self,data,cliente,cpf,pagamento = False):

        self.data = data
        self.cliente = cliente
        self.cpf = cpf
        self.pagamento = pagamento

        fds = [5,6]

        d = datetime.strptime(data,"%d/%m/%Y").date()
        if d <= date.today() or d.weekday() in fds:
            raise ValueError('data de consulta menor que atual')
            print('Valor:',data)
        else:
            self.data = datetime.strptime(data,"%d/%m/%Y").date()

            

    def agendar_consulta(self):

        medico = int(input('''\n***** Médicos Disponíveis *****
1 - Antônio
2 - José
3 - Pedro
*******************************\n

Escolha seu médico:_'''))

        medicos = ['Antônio','José','Pedro']

        if medico == 1:
            self.medico = medicos[0]

        if medico == 2:
            self.medico = medicos[1]

        if medico == 3:
            self.medico = medicos[2]


        formato_data = self.data.strftime('%d/%m/%Y')


        print(f'\n***** CONSULTA AGENDADA *****\nData: {formato_data} \nCliente: {self.cliente}\nCPF:{self.cpf}\nMédico: {self.medico}\n')


    def pagar_consulta(self):

        valor = 0

        if self.pagamento == True:

            valor += 300

            print(f'\nR$: {valor},00 - Pagamento efetivado com sucesso!\n')


        else:

            print('\n Pagamento...\n')


    def cancelar_consulta(self):

        pass

        print(f'\nOlá, {self.cliente}, sua consulta foi cancelada!\n')

    def agendar_retorno(self):

        data_retorno = input('Data de retorno desejada(dd/mm/aaaa): ')

        data_retorno = datetime.strptime(data_retorno,"%d/%m/%Y").date()

        formato_data = data_retorno.strftime('%d/%m/%Y')

        data_consulta = self.data

        qtd_dias = abs((data_retorno - data_consulta)).days

        if qtd_dias < 30:

            print(f'\nRetorno agendado para o dia {formato_data}.')
            

        else:
            print(f'Retorno apenas com 30 dias após consulta. Por favor, agende uma nova consulta.')


    def relatorio_medico(self):

        print(f'\n****RELATÓRIO DE CONSULTAS POR MÉDICO****\n')

    def relatorio_faturamento(self):

        print(f'\n****RELATÓRIO DE FATURAMENTO DA CLÍNICA****\n')

        
def main():

    print('''************************ MENU ************************
1 - Agendar Consulta
2 - Pagar Consulta
3 - Cancelar Consulta
4 - Agendar Retorno
5 - Relatório de Consultas realizadas no mês por médico
6 - Relatório de Faturamento da Clínica por mês
*******************************************************
''')

    consulta1 = consultas('16/03/2023','Camila',123,True)
    
    while True:
        try:
            n = int(input('Digite sua escolha:_'))

            if n == 1:

                consulta1.agendar_consulta()
                
                break

            elif n == 2:

                consulta1.pagar_consulta()

                break

            elif n == 3:

                consulta1.cancelar_consulta()

                break

            elif n == 4:

                consulta1.agendar_retorno()

                break

            elif n == 5:

                consulta1.relatorio_medico()

                break

            elif n == 6:

                consulta1.relatorio_faturamento()

                break
                
            else:

                print('Opção inválida. Tente Novamente!\n')

        except:

            print('Opção invalida. Tente Novamente!\n')


if __name__=='__main__':
    main()
