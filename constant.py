#тот же constant.py, только с цифрами
#к некоторым символам приделан юникод
#дальше их делать мне было впадлу
#тема доделает
#coding: utf-8
alph = {"1":  (1, 0,
               0, 0,
               0, 0,),

        "2":  (1, 0,
               1, 0,
               0, 0,),

        "3":  (1, 1,
               0, 0,
               0, 0,),

        "4":  (1, 1,
               0, 1,
               0, 0,),

        "5": (1, 0,
              0, 1,
              0, 0,),

        "6": (1, 1,
              1, 0,
              0, 0,),

        "7": (1, 1,
              1, 1,
              0, 0,),

        "8": (1, 0,
              1, 1,
              0, 0,),

        "9": (0, 1,
              1, 0,
              0, 0,),

        "0": (0, 1,
              1, 1,
              0, 0,),

        "a": (1, 0,
              0, 0,
              0, 0,),

        "b": (1, 0,
              1, 0,
              0, 0,),

        "c": (1, 1,
              0, 0,
              0, 0,),

        "d": (1, 1,
              0, 1,
              0, 0,),

        "e": (1, 0,
              0, 1,
              0, 0,),

        "f": (1, 1,
              1, 0,
              0, 0,),

        "g": (1, 1,
              1, 1,
              0, 0,),

        "h": (1, 0,
              1, 1,
              0, 0,),

        "i": (0, 1,
              1, 0,
              0, 0,),

        "j": (0, 1,
              1, 1,
              0, 0,),

        "k": (1, 0,
              0, 0,
              1, 0,),

        "l": (1, 0,
              1, 0,
              1, 0,),

        "m": (1, 1,
              0, 0,
              1, 0,),

        "n": (1, 1,
              0, 1,
              1, 0,),

        "o": (1, 0,
              0, 1,
              1, 0,),

        "p": (1, 1,
              1, 0,
              1, 0,),

        "q": (1, 1,
              1, 1,
              1, 0,),

        "r": (1, 0,
              1, 1,
              1, 0,),

        "s": (0, 1,
              1, 0,
              1, 0,),

        "t": (0, 1,
              1, 1,
              1, 0,),

        "u": (1, 0,
              0, 0,
              1, 1,),

        "v": (1, 0,
              1, 0,
              1, 1,),

        "w": (0, 1,
              1, 1,
              0, 1,),

        "x": (1, 1,
              0, 0,
              1, 1,),

        "y": (1, 1,
              0, 1,
              1, 1,),

        "z": (1, 0,
              0, 1,
              1, 1,),

        "UP": (0, 0,
               0, 0,
               0, 1,),

        "NUM": (0, 1,
                0, 1,
                1, 1,),

        "STR": (0, 0,
                0, 1,
                0, 1,),

        ".": (0, 0,
              1, 1,
              0, 1,),

        ",": (0, 0,
              1, 0,
              0, 0,),

        "?": (0, 0,
              1, 0,
              0, 1,),

        ";": (0, 0,
              1, 0,
              1, 0,),

        ":": (0, 0,
              1, 1,
              0, 0,),

        "*": (0, 0,
              0, 1,
              1, 0,),

        "!": (0, 0,
              1, 1,
              1, 0,),

        """/""": (0, 0,
               1, 0,
               1, 1,),

        """\\""": (0, 0,
                 0, 1,
                 1, 1,),

        "(": (0, 0,
              1, 1,
              1, 1,),

        ")": (0, 0,
              1, 1,
              1, 1,),

        "-": (0, 0,
              0, 0,
              1, 1,),

        " ": (0, 0,
              0, 0,
              0, 0,),

        "а": (1, 0,
              0, 0,
              0, 0,),

        "б": (1, 0,
              1, 0,
              0, 0,),

        "в": (1, 1,
              1, 0,
              0, 0,),

        "г": (1, 1,
              1, 1,
              0, 0,),

        "д": (1, 1,
              0, 1,
              0, 0,),

        "е": (1, 0,
              0, 1,
              0, 0,),

        "ё": (1, 0,
              0, 0,
              0, 1,),

        "ж": (0, 1,
              1, 1,
              0, 0,),

        "з": (1, 0,
              0, 1,
              1, 1,),

        "и": (0, 1,
              1, 0,
              0, 0,),

        "_": (0,0,
              0,0,
              0,0,),

        "#": (0,0,
              0,0,
              0,0,),

        "й": (1, 1,
              1, 0,
              1, 1,),

        "к": (1, 0,
              0, 0,
              1, 0,),

        "л": (1, 0,
              1, 0,
              1, 0,),

        "м": (1, 1,
              0, 0,
              1, 0,),

        "н": (1, 1,
              0, 1,
              1, 0,),

        "о": (1, 0,
              0, 1,
              1, 0,),

        "п": (1, 1,
              1, 0,
              1, 0,),

        "р": (1, 0,
              1, 1,
              1, 0,),

        "с": (0, 1,
              1, 0,
              1, 0,),

        "т": (0, 1,
              1, 1,
              1, 0,),

        "у": (1, 0,
              0, 0,
              1, 1,),

        "ф": (1, 1,
              1, 0,
              0, 0,),

        "х": (1, 0,
              1, 1,
              0, 0,),

        "ц": (1, 1,
              0, 0,
              0, 0,),

        "ч": (1, 1,
              1, 1,
              1, 0,),

        "ш": (1, 0,
              0, 1,
              0, 1,),

        "щ": (1, 1,
              0, 0,
              1, 1,),

        "ъ": (1, 0,
              1, 1,
              1, 1,),

        "ы": (0, 1,
              1, 0,
              1, 1,),

        "ь": (0, 1,
              1, 1,
              1, 1,),

        "э": (0, 1,
              1, 0,
              0, 1,),

        "ю": (1, 0,
              1, 1,
              0, 1,),

        "я": (1, 1,
              1, 0,
              0, 1,),

        }
