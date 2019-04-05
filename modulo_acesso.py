import csv as csv
import random
import os

class Leitor:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def list_names(self):
        with open(self.arquivo) as f:
            reader = csv.DictReader(f)
            # fieldnames ['nome', 'matricula', 'telefone', 'email', 'uffmail', 'status']
            for row in reader:
                print(row['nome'])
        f.close()
    def busca_usuario(self, matricula):
        if(matricula != 0):
            found = False
            print(str(matricula))
            with open(self.arquivo) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if (row['matricula'] == str(matricula)):
                        found = True
                        nome = row['nome'].split()
                        if(row['uffmail'] == ''):
                            print("\nOlá " + nome[0] + ", por favor escolha uma das opções abaixo para seu UFFMail:")
                            email = self.opcoes_mail(nome)
                            self.grava_email(email, matricula)
                            print ("\nA criação do seu email ("+email+") será feita nos próximos minutos\nUm SMS foi enviado para " + row['telefone']+ " com a sua senha de acesso")
                        else:
                            print ("\nOlá " + nome[0] + ", você já tem e-mail, então prossiga para o sistema.")
                if (found == False):
                    print("Matrícula não encontrada")
                    mtrc = input("Por favor, digite uma matrícula válida (0 finaliza o programa): ")
                    return self.busca_usuario(mtrc)
            f.close()
        else:
            exit(1)
    def opcoes_mail(self, nome):
        nome = [i.lower() for i in nome]
        opt=[]
        tamanho = len(nome)
        sufix = '@id.uff.br'
        opt.append(nome[0]+'_'+nome[random.randint(1,tamanho-1)] + sufix)
        opt.append(nome[0]+nome[tamanho-2][0]+nome[tamanho-1][0] + sufix)
        opt.append(nome[0]+nome[random.randint(1,tamanho-1)]+sufix)
        opt.append(nome[0][0]+nome[random.randint(1,tamanho-1)]+sufix)
        opt.append(nome[0][0]+nome[tamanho-2]+nome[tamanho-1]+sufix)

        for i in range(5):
            print(str(i+1) +' - ' +opt[i])
        print("")
        resp = int(input())
        if (0< resp < 6):
            return opt[resp-1]

    def grava_email(self, uffmail, matricula):
        infile = open(self.arquivo, 'r')
        i = csv.reader(infile)
        # campos = i.fieldnames
        outfile = open('temporario.csv', 'a', newline ='\n')
        f = csv.writer(outfile)
        for row in i:
            if (str(matricula) == row[1]):
                linha = [ row[0], row[1], row[2],row[3], uffmail,row[5] ]
                f.writerow(linha)
            else:
                f.writerow(row)
        
        infile.close()
        outfile.close()  

        infile = open("temporario.csv", 'r')
        i = csv.reader(infile)
        outfile = open(self.arquivo, 'w+', newline ='\n')
        outfile.truncate()
        outfile.close
        outfile = open(self.arquivo, 'a', newline ='\n')
        f = csv.writer(outfile)
        outfile.truncate()
        for row in i:
            f.writerow(row)  
        
        infile.close()
        outfile.close()       