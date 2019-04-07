from modulo_acesso import Leitor
import urllib.request as request
import os.path 
r = Leitor("alunos.csv")

if(not os.path.isfile("alunos.csv")):
    url = "https://raw.githubusercontent.com/sti-uff/trabalhe-conosco/master/datasets/alunos.csv"
    arquivo, headers = request.urlretrieve(url,filename="alunos.csv")
    r = Leitor(arquivo)

print("Bem vindo ao Sistema Acadêmico.\n")
matr = int(input("Por favor, digite sua matricula (0 finaliza o programa): "))
r.busca_usuario(matr)

print("Obrigado pela visita!")

input("Pressione a tecla ENTER para fechar o programa")



