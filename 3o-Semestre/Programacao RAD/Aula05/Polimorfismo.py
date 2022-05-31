class ArquivoAudio:

    def __init__(self, arquivo):
        
        self.arquivo = arquivo

        if(not arquivo.endswith(self.ext)): #verifica se o objeto instanciado termina com a extensão determinada pela classe filha
            raise Exception("Fomrato InválidO!!")

class ArquivoMp3(ArquivoAudio):

    ext = "mp3"
    def tocar(self):
        print(f"Tocando {self.arquivo} como MP3")

class ArquivoWAV(ArquivoAudio):
    
    ext = "wav"
    def tocar(self):
        print(f"Tocando {self.arquivo} como WAV")

class ArquivoOGG(ArquivoAudio):

    ext = "ogg"
    def tocar(self):
        print(f"Tocando {self.arquivo} como OGG")

ogg = ArquivoOGG("musicaOGG.ogg")
mp3 = ArquivoMp3("musicaMP3.mp3")
wav = ArquivoWAV("musicaWAV.wav")

ogg.tocar()
mp3.tocar()
wav.tocar()