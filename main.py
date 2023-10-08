from Lab01.start import lab1_start
from Lab02.start import lab2_start, lab2_start_with_lcom
from Lab03.start import lab3_start


if __name__ == '__main__':
    while True:
        print("Selecione o Lab para executar:")
        print("Digite 1 para Lab01")
        print("Digite 2 para Lab02")
        print("Digite 22 para Lab02 com Lcom")
        print("Digite 3 para Lab03")
        print("Digite S para Sair")
        x = str(input('Opção: '))
        if x == '1':
            lab1_start()
        elif x == '2':
            lab2_start()
        elif x == '22':
            lab2_start_with_lcom()
        elif x == '3':
            lab3_start()
        elif x.lower() == 's':
            print('Até mais')
            break
        else:
            print('Opção não existe!')
            print('Tente novamente')
