print('0 в качестве знака - выход из программы\n')

while True:
    s = input('Знак (+, -, *, /): ')
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input('a = '))
        b = float(input('b = '))
        match s:
            case '+':
                print('%.2f' % (a + b))
            case '-':
                print('%.2f' % (a - b))
            case '*':
                print('%.2f' % (a * b))
            case '/':
                if b != 0:
                    print('%.2f' % (a / b))
                else:
                    print('Деление на ноль!')
    else:
        print('Неверный знак операции!')
