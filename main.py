from Lab03.start import lab3_start


if __name__ == '__main__':
    while True:
        print("Selecione o Lab para executar:")
        print("Digite 3 para Lab03")
        print("Digite S para Sair")
        x = str(input('Opção: '))
        if x == '3':
            lab3_start()
        elif x.lower() == 's':
            print('Até mais')
            break
        else:
            print('Opção não existe!')
            print('Tente novamente')
