""" 
Aluno: Juliano F. da Mata
Curso: Ciência de Dados e IA
Modulo: 04
Disciplina: Linguagem de Programação
Professor: Valdinei J. Saugo
Data: 07/09/2024
"""
""" Estudo de Caso
Elabore um programa em linguagem Python para cálculo de notas de alunos considerando um período letivo de 4 bimestres e média para aprovação sendo 7,0 pontos. Seu programa deverá pedir para o usuário informar o nome de um aluno e qual seu código matrícula e as notas do 1º ao 4º bimestre.

Ao final da inserção dos dados o programa deve apresentar as seguintes informações:

a) nome e matrícula do aluno

b) nota de cada bimestre

c) média final

d) status do aluno:

- aprovado se a média for maior ou igual a 7,0

- em recuperação se a média for menor que 7,0  e maior que 3,0

- reprovado se a média for menor que 3,0"""

while True:  # Loop principal para permitir que o usuário reinicie ou saia do programa
    # Solicitar e validar o nome do aluno
    while True:
        nome = input("Informe o nome do aluno (somente letras e espaços): ")
        if nome.replace(" ", "").isalpha():  # Verifica se todos os caracteres são letras ou espaços
            nome = nome.upper()  # Converter o nome para maiúsculas
            break  # Sai do loop se o nome for válido
        else:
            print("Nome inválido. Por favor, insira um nome contendo apenas letras e espaços. Tente novamente!")

    # Solicitar o código de matrícula do aluno
    matricula = input("Informe o código de matrícula do aluno: ")

    # Solicitar e validar as notas dos 4 bimestres
    notas = []  # Lista para armazenar as notas
    for i in range(1, 5):  # Loop para cada bimestre (1º ao 4º)
        while True:  # Loop para garantir que a nota inserida seja válida
            try:
                nota = float(input(f"Informe a nota do {i}º bimestre (0 a 10): "))  # Solicita a nota e tenta convertê-la para um número decimal
                if 0 <= nota <= 10:  # Verifica se a nota está no intervalo válido (0 a 10)
                    notas.append(nota)  # Adiciona a nota à lista de notas
                    break  # Sai do loop se a nota for válida
                else:
                    print("Nota inválida. A nota deve estar entre 0 e 10.")  # Exibe uma mensagem se a nota estiver fora do intervalo permitido
            except ValueError:  # Captura o erro se a entrada não puder ser convertida para um número (por exemplo, se o usuário digitar letras)
                print("Entrada inválida. Por favor, insira um número.")  # Exibe uma mensagem pedindo ao usuário para tentar novamente

    # Calcular a média final das notas
    media_final = sum(notas) / 4  # Soma todas as notas e divide por 4 para calcular a média

    # Determinar o status do aluno com base na média final
    if media_final >= 7.0:
        status = "Aprovado, Parabéns!!"  # O aluno é aprovado se a média for maior ou igual a 7.0
    elif 3.0 < media_final < 7.0:
        status = "Em Recuperação, vc pode fazer melhor!"  # O aluno está em recuperação se a média for maior que 3.0 e menor que 7.0
    else:
        status = "Reprovado, vc precisa estudar mais!"  # O aluno é reprovado se a média for menor ou igual a 3.0

    # Exibir as informações solicitadas
    print("\n--- Resultado ---")
    print(f"Nome do aluno: {nome}")  # Exibe o nome do aluno
    print(f"Matrícula: {matricula}")  # Exibe o código de matrícula do aluno
    for i, nota in enumerate(notas, 1):  # Loop para exibir cada nota com o número do bimestre correspondente
        print(f"Nota do {i}º bimestre: {nota:.2f}")  # Exibe a nota formatada com duas casas decimais
    print(f"Média final: {media_final:.2f}")  # Exibe a média final formatada com duas casas decimais
    print(f"Status do aluno: {status}")  # Exibe o status do aluno (Aprovado, Em Recuperação ou Reprovado)

    # Perguntar ao usuário se deseja sair ou reiniciar
    while True:
        sair = input("\nDeseja sair do programa? Digite 's' para sair ou 'n' para reiniciar: ").lower()
        if sair == 's':
            print("Encerrando o programa.")
            exit()  # Sai do programa
        elif sair == 'n':
            print("Reiniciando o programa.\n")
            break  # Volta ao início do loop principal para reiniciar o processo
        else:
            print("Entrada inválida. Por favor, digite 's' para sair ou 'n' para reiniciar.")
            # Exibe uma mensagem se a entrada não for 's' ou 'n' e pede ao usuário para tentar novamente
