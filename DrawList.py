from PIL import Image, ImageDraw
from constant import alph
from BrailleTranslator import BrailleTranslator

class DrawList:
    def __init__(self,size_x=2480,size_y=3508):
        self.img = Image.new("RGB", (size_x, size_y), (255,255,255,0))
        self.draw = ImageDraw.Draw(self.img)
        self.translator = BrailleTranslator()


    def show(self):
        self.img.show()

    def drawBraille(self,text):
        brailleList = self.translator.translation(text)
        x=152
        y=152
        commonSize=23
        newLine = 0
        for char in brailleList:
            newLine+=1
            if char[0]==1: self.draw.ellipse((x,y,x+commonSize,y+commonSize),fill="black", outline="black")
            if char[1]==1: self.draw.ellipse((x+commonSize+1,y, x+commonSize+1+commonSize,y+commonSize),fill="black", outline="black")
            y+=commonSize+1
            if char[2]==1: self.draw.ellipse((x,y,x+commonSize,y+commonSize),fill="black", outline="black")
            if char[3]==1: self.draw.ellipse((x+commonSize+1,y, x+commonSize+1+commonSize,y+commonSize),fill="black", outline="black")
            y+=commonSize+1
            if char[4]==1: self.draw.ellipse((x,y,x+commonSize,y+commonSize),fill="black", outline="black")
            if char[5]==1: self.draw.ellipse((x+commonSize+1,y, x+commonSize+1+commonSize,y+commonSize),fill="black", outline="black")
            x+=3*commonSize
            y-=commonSize*2 + 2
            if newLine == 32:
                newLine = 0
                y+=commonSize*5
                x=152

    def saveFile(self):
        self.img = self.img.resize((310,430),Image.ANTIALIAS)
        self.img.save("""./picture.png""","PNG")

# a = DrawList()
# a.drawBraille("""Пусть я был смешон в Ваших глазах и в глазах Вашего брата, Николая Николаевича. Уходя, я в восторге говорю: "Да святится имя Твое". Восемь лет тому назад я увидел Вас в цирке в ложе, и тогда же в первую секунду я сказал себе: я ее люблю потому, что на свете нет ничего похожего на нее, нет ничего лучше, нет ни зверя, ни растения, ни звезды, ни человека прекраснее Вас и нежнее. В Вас как будто бы воплотилась вся красота земли...""")
# a.saveFile()
