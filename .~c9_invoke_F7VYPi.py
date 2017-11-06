im

class bTranslatorEN:
    def __init__(self):
        self.alph = {"a" : (1,0,
                            0,0,
                            0,0,),
                            
                     "b" : (1,0,
                            1,0,
                            0,0,),
                            
                     "c" : (1,1,
                            0,0,
                            0,0,),
                            
                     "d" : (1,1,
                            0,1,
                            0,0,),
                            
                     "e" : (1,0,
                            0,1,
                            0,0,),
                            
                     "f" : (1,1,
                            1,0,
                            0,0,),
                            
                     "g" : (1,1,
                            1,1,
                            0,0,),
                            
                     "h" : (1,0,
                            1,1,
                            0,0,),
                            
                     "i" : (0,1,
                            1,0,
                            0,0,),
                            
                     "j" : (0,1,
                            1,1,
                            0,0,),
                            
                     "k" : (1,0,
                            0,0,
                            1,0,),
                            
                     "l" : (1,0,
                            1,0,
                            1,0,),
                            
                     "m" : (1,1,
                            0,0,
                            1,0,),
                            
                     "n" : (1,1,
                            0,1,
                            1,0,),
                            
                     "o" : (1,0,
                            0,1,
                            1,0,),
                            
                     "p" : (1,1,
                            1,0,
                            1,0,),
                            
                     "q" : (1,1,
                            1,1,
                            1,0,),
                            
                     "r" : (1,0,
                            1,1,
                            1,0,),
                            
                     "s" : (0,1,
                            1,0,
                            1,0,),
                            
                     "t" : (0,1,
                            1,1,
                            1,0,),
                            
                     "u" : (1,0,
                            0,0,
                            1,1,),
                            
                     "v" : (1,0,
                            1,0,
                            1,1,),
                            
                     "w" : (0,1,
                            1,1,
                            0,1,),
                            
                     "x" : (1,1,
                            0,0,
                            1,1,),
                            
                     "y" : (1,1,
                            0,1,
                            1,1,),
                            
                     "z" : (1,0,
                            0,1,
                            1,1,),
                            
                    "UP" : (0,0,
                            0,0,
                            0,1,),
                            
                    "NUM" : (0,1,
                            0,1,
                            1,1,),
                            
                    "STR" : (0,0,
                            0,1,
                            0,1,),
                            
                     "." : (0,0,
                            1,1,
                            0,1,),
                            
                     "," : (0,0,
                            1,0,
                            0,0,),
                            
                     "?" : (0,0,
                            1,0,
                            0,1,),
                            
                     ";" : (0,0,
                            1,0,
                            1,0,),
                            
                     "!" : (0,0,
                            1,1,
                            1,0,),
                            
                    "\"" : (0,0,
                            1,0,
                            1,1,),
                            
                    "\"\"" : (0,0,
                              0,1,
                              1,1,),
                              
                    "(" : (0,0,
                           1,1,
                           1,1,),
                           
                    ")" : (0,0,
                           1,1,
                           1,1,),
                           
                    "-" : (0,0,
                           0,0,
                           1,1,),
                           
                    " " : (0,0,
                           0,0,
                           0,0,)
                    }
        self.num = dict(zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h"]))
        


    def Translation(self, en_str):
        def isnum(char):
            num = "1234567890"
            if char in num:
                return True
            else:
                return False
        
        strFlag = False
        self.res = []
        while en_str:
            char = en_str[0]
            
            if char.isupper():
                if strFlag:
                    self.res.append(self.alph["STR"])
                    strFlag = False
                self.res.append(self.alph["UP"])
                self.res.append(self.alph[char.lower()])
                en_str = en_str.replace(char, "", 1)
                
            elif isnum(char):
                self.res.append(self.alph["NUM"])
                while isnum(en_str[0]):
                    self.res.append(self.alph[self.num[int(char)]])
                    en_str = en_str.replace(char, "", 1)
                    char = en_str[0]
                strFlag = True
                
            else:
                if strFlag:
                    self.res.append(self.alph["STR"])
                    strFlag = False
                
                self.res.append(self.alph[char])
                en_str = en_str.replace(char, "", 1)
                
        return self.res
        
start = time()   
a = bTranslatorEN()
print(a.Translation("xxxxx"))
print("Program time {0}".format(start-time()))