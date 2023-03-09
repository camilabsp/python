class musica:
    def __init__(self,titulo,artista,volume=0,status=True):
        
        self.titulo = titulo
        self.artista = artista
        self.status = status
        self.volume = volume

    def play_pause(self):

        if self.status == True:
            print(f'Reproduzindo agora...\nMúsica: {self.titulo}\nArtista: {self.artista}')

        elif self.status == False:
            print(f'Pausado...')


    def aumentar_volume(self):

        self.volume += 1

        print(f'Volume ++: {self.volume}')

    def diminuir_volume(self):

        self.volume -= 1

        print(f'Volume --: {self.volume}')


def main():

    musica1 = musica('sera','legiao urbana',5)

    musica1.play_pause()
    musica1.aumentar_volume()
    musica1.diminuir_volume()

        

if __name__=='__main__':
    main()
    
