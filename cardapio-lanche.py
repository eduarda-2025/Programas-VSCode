opcao=0
while opcao !=5:
    print("==Cardápio==")
    print("1-Hambúrguer")
    print("2-Pizza")
    print("3-Salada")
    print("4-Refrigerante")
    print("5-Sair")
    opcao=int(input("Escolha uma opção: "))
    if opcao==1:
        print("Você escolheu Hambúrguer")
    elif opcao==2:
        print("Você escolheu Pizza")
    elif opcao==3:
        print("Você escolheu Salada")
    elif opcao==4:
        print("Você escolheu Refrigerante")
    elif opcao==2:
        print("Saindo do Cardápio")
        break