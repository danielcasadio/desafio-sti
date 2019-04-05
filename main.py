from modulo_leitor import Leitor
import urllib.request as request
import os.path 

url = "https://raw.githubusercontent.com/sti-uff/trabalhe-conosco/master/datasets/alunos.csv"
arquivo, headers = request.urlretrieve(url,filename="alunos.csv")

if(not os.path.isfile(arquivo)):
    r = Leitor("alunos.csv")

print("Bem vindo ao Sistema Acadêmico.\n")
matr = int(input("Por favor, digite sua matricula (0 finaliza o programa): "))
r.busca_usuario(matr)

print("Obrigado pela visita!")

input("Pressione qualquer tecla para fechar o programa")



