nota1 = int(input("digite a primeiro nota: "))
nota2 = int(input("digite a segundo nota: "))

soma = nota1 + nota2
media = soma / 2

if media >= 7:
    print("parabéns, você está aprovado! :)")

if media == 10:
    print("Parabéns, você é o aluno destaque!")

if media < 7:
    print("que pena, você está reprovado! :")
