# Desafio UFFMail STI

Desafio do processo seletivo da STI

Projeto de um serviço que gera e sugestiona opções de e-mail para alunos que ainda não possuem o mesmo. Baseado no nome completo do       aluno

## Funcionamento

Ao acessar o sistema com a matrícula, o sistema verifica se a mesma é valida e se válida verifica se o aluno possui um UFFMail

## Programação utilizada

O sistema foi feito usando Python 3.7 e compilado em arquivo executável (.exe) para Windows.

### Bibliotecas utilizadas e motivos

### Módulo Acesso
- [csv](https://docs.python.org/3/library/csv.html/): Biblioteca nativa do python com funcionalidades focadas na leitura e escrita de arquivos do tipo .csv e .xls com ou sem organização (headers)
- [random](https://docs.python.org/3/library/random.html/): Biblioteca nativa do python que tem como foco gerar números aleatórios.
- [os](https://docs.python.org/3/library/os.html/): Biblioteca para acessar e manipular arquivos presentes na máquina onde o programa está sendo processado, muito útil para criação de arquivos temporários de auxílio e até mesmo arquivos permanentes.

### Programa principal
- modulo_acesso.py: Módulo composto pela classe Leitor e funções que auxiliam na leitura, processamento e modificação do arquivo utilizado no desafio
- [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request/): Biblioteca nativa utilizada para acessar URLs e a função request para download de arquivos dada URL.


## Funções da classe Leitor
- busca_usuario(matricula)
  A função consiste em percorrer o documento e procurar no mesmo a linha que tem matrícula correspondente ao dado informado pelo usuário, caso exista, verifica se o usuário possui UFFMail, se não possuir, a função opcoes_email é chamada para dar as opções possíveis para o usuário. Após isso a função grava_email(matricula) é chamada para modificar o arquivo original, atualizando a listagem de alunos que possuem UFFMail
  
- opcoes_email(nome)
  A função recebe o nome do usuário (passada através da função busca_usuario) e monta algumas opções de e-mail para o mesmo, a opção escolhida é retornada.
  
- grava_email(matricula)
  Esta função recebe a matrícula do usuário que gerou um UFFMail, então cria um arquivo temporário para cópia do original. Após isso, o arquivo original é esvaziado e reescrito modificando o dado do aluno cuja matrícula for a mesma recebida. O arquivo temporário é deletado após esse processamento para ser novamente criado na próxima vez que o programa for utilizado.


## Funções do programa principal (main.py)

Para dar início ao processamento, o programa busca pelo arquivo 'alunos.csv', caso não encontre, acessa o repositório da STI e faz o download do arquivo. Todo o resto do processamento é feito pelo modulo_leitor.py.

## Como utilizar

A aplicação não possui interface gráfica, roda apenas como um terminal. Ao iniciar, o usuário é recebido com uma mensagem de boas vindas e é direcionado a informar a sua matrícula, recebe suas opções caso seja possível e seleciona a partir de uma numeração de 1 a 5. Recebe a mensagem de criação sucedida do e-mail novo e um último comando apenas para finalizar o programa.

## Desenvolvedor
Daniel Casadio
