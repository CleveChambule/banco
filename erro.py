"""
from conta import ContaCorrente

def metodo1():
    print("inicio do sistema")
    try:
        metodo2()
    except AttributeError:
        print("erro")
    print("fm do metodo2")

def metodo2():
    print("inicio do metodo2")
    cc = ContaCorrente("Cleive", "123")

    for i in range(1, 15):
        cc.deposita(i + 1000)
        print(cc.saldo)
        if i == 5:
            cc = None
    print('fim do metodo2')


if __name__ == '__main__':
    print('inicio do main')
    try:
        metodo1()
    except AttributeError:
        print("erro")
    print('fim do main')
"""
"""
cond = True
while cond:
    try:
        n = int(input("Digite um numero: "))
        z = int(input("Digite o divisor: "))
        s = n / z
        print("Resultado: {}".format(s))
        cond = False
    except ZeroDivisionError:
        print('\nERRO!! Um nunmero nao e divisel por 0 \nTente novamente!')
print("SUCESSO!")
"""

def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")
wek = int(input("Digite "))

week(6)