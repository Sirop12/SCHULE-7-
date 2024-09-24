def crol():
    try:
        a=int(input("Ввод "))
        if a == 000:
            print("Выход")
        else:
            print(a, a*2 , a*3, a*4, a*5, sep="---")
            crol()
    except:
        print("Ошибка")
        crol()

if __name__ == '__main__':
 crol()












def fprint(*pr, sep="", end="\n", type="STD", ret=False):
    ''':param type: 
    ЦВЕТА: С0 - белый, C1 - Красный, C2 - Синий, C3 - Зеленый, C4 - Желтый, C5 - Фиолетовый, C6 - Бирюзовый, C7 - Черный. ФОРМАТ: T1 - Жирный, T2 - Подчеркнутый, T3 - Курсив, T4 - Зачеркнутый BANER - банер (Только английский)'''
    text = sep.join(pr) + end
    if type == "STD":
        if not ret:
            print("\033[0m" + text, end='')
        else:
            return "\033[0m" + text 
    else:
        collorText = ""
        reset = "\033[0m"
        F = type.split()
        for i in F:
            UnrightFormat = "\033[31m \033[1m    НЕПРАВИЛЬНЫЙ ФОРМАТ \033[0m"
            if len(i) == 2:
                if i[0] == "C":
                    if i[1] in list("01234567"):
                        Collor = int(i[1])
                        if Collor == 0:
                            collorText += '\033[29m'
                        elif Collor == 1:
                            collorText += '\033[31m'
                        elif Collor == 2:
                            collorText += '\033[34m'
                        elif Collor == 3:
                            collorText += '\033[32m'
                        elif Collor == 4:
                            collorText += '\033[33m'
                        elif Collor == 5:
                            collorText += '\033[35m'
                        elif Collor == 6:
                            collorText += '\033[36m'
                        elif Collor == 7:
                            collorText += '\033[8m'
                    else:
                        print(UnrightFormat + "Collor")
                elif i[0] == "T":
                    if i[1] in list("1234"):
                        Collor = int(i[1])
                        if Collor == 1:
                            collorText += '\033[1m'
                        elif Collor == 2:
                            collorText += '\033[4m'
                        elif Collor == 3:
                            collorText += '\033[3m'
                        elif Collor == 4:
                            collorText += '\033[9m'
                    else:
                        print(UnrightFormat + "Type")
                else:
                    print(UnrightFormat + "Argument len 2")
            elif i == "BANER":
                text = pyfiglet.figlet_format(text.upper())
            else:
                print(UnrightFormat + "Argument")
        if not ret:
            print(collorText + text + reset, end="")
        else:
            return collorText + text + reset
        

fprint("Smart attadenced system", type="C6 T1 BANER")
