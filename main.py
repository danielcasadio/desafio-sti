from modulo_leitor import Leitor

r = Leitor('alunos.csv')

print("Bem vindo ao Sistema Acadêmico.\n")
matr = int(input("Por favor, digite sua matricula (0 finaliza o programa): "))
r.busca_usuario(matr)

print("Obrigado pela visita!")



