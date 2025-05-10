nota1=int(input("Digite sua primeira nota: "))
nota2=int(input("Digite sua segunda nota: "))
media=float(nota1+nota2)/2
print(f"Sua média é {media}")
if media >=7:
    print(f"Você está acima da média, aprovado!")
else:
    print(f"Você está abaixo da média, reprovado!")