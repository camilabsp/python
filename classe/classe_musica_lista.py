class musica:
    def __init__(self,playlist,volume=0,status = True):
    
        self.playlist = playlist
        self.volume = volume
        self.status = status


    def play_pause(self):

        if self.status == True:

            print(f'REPRODUZINDO...')

        else:

            print(f'ÁUDIO PAUSADO...')


    def exibir_playlist(self):

        for i in range(len(self.playlist)):
            m = self.playlist[i]
            print(f'{i+1} {m}')

                
    def aumentar_volume(self):

        self.volume += 1

        print(f'Aumentando o volume ++: {self.volume}')


    def diminuir_volume(self):

        self.volume -= 1

        print(f'Diminuindo o volume --: {self.volume}')


    def adicionar_musica(self):

        k = str(input('Qual música deseja adicionar na playlist? '))

        self.playlist.append(k)

        for i in range(len(self.playlist)):
            m = self.playlist[i]
            print(f'{i+1} {m}')


    def excluir_musica(self):

        n = str(input('Qual música deseja excluir da playlist? '))

        self.playlist.remove(n)
        

        for i in range (len(self.playlist)):
            m = self.playlist[i]
            print(f'{i+1} {m}')
        

def main():

    musicas = musica(['November Rain','Patience','Snuff','Nothing Else Matter'],5,True)

    musicas.play_pause()
    musicas.exibir_playlist()
    musicas.aumentar_volume()
    musicas.diminuir_volume()
    musicas.adicionar_musica()
    musicas.excluir_musica()
   


if __name__=='__main__':
    main()
    
