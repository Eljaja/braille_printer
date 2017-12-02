from PIL import Image, ImageDraw
from constant import alph
from BrailleTranslator import BrailleTranslator

class DrawList:
    def __init__(self,size_x=2480,size_y=3508):
        self.img = Image.new("RGB", (size_x, size_y), (255,255,255,0))
        self.draw = ImageDraw.Draw(self.img)
        self.translator = BrailleTranslator()


    def drawCircle(self,x,y,rad, point):
        if point:
            self.draw.ellipse((x-rad,y-rad,x+rad,y+rad),fill="black",outline="black")
        else:
            pass

    def drawBraille(self,text):
        brailleList = self.translator.translation(text)
        x=159
        y=159
        newLine = 0
        for char in brailleList:
            if char == "\n":
                continue
            self.drawCircle(x, y, 7, char[0]); self.drawCircle(x+28 ,y, 7, char[1])
            self.drawCircle(x, y+28, 7, char[2]); self.drawCircle(x+28, y+28, 7, char[3])
            self.drawCircle(x, y+28+28, 7, char[4]); self.drawCircle(x+28, y+28+28, 7, char[5])
            x+=70
            newLine+=1
            if newLine == 32:
                newLine = 0
                x=159
                y+=110

    def saveFile(self):
        self.img = self.img.resize((310,430),Image.ANTIALIAS)
        self.img.save("""./picture.png""","PNG")
# a = DrawList()
# a.drawBraille("hsafjslafhsila nhyniosuyhfa iousy ifuyas iufyiasugfuasgfukagsifgasufguasgfuagsfuygasufguasygfuasygfuaygi")
# a.show()
