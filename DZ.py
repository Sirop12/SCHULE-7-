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
