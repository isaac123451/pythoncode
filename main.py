from classes import Sistema # importando a classe no arquivo principal
import os # importando uma função que permite interagir com o terminal

def main():
    sistema = Sistema() # instanciando a classe
    
    i = 0
    while True: # criando laço infinito
        print("1. Cadastrar cargo;") # opções
        print("2. Cadastrar funcionário;")
        print("3. Mostrar relatório;")
        print("4. Mostrar total de salário por cargo")
        print("5. Sair;")

        escolha = int(input("Escolha uma opção: "))       
        os.system('cls') # limpa o terminal
        
        if escolha == 1: # usei if e elif parar lidar com as escolhas
            cargo = input("Digite o cargo que você deseja cadastrar: ")
            salario = input("Agora, informe o salário do cargo cadastrado: ")
            sistema.cadastrar_cargo(cargo, salario)
            print(f"O cargo '{cargo}' foi criado com sucesso ")
            print(f"código do cargo: {i}")
            i += 1
        elif escolha == 2:
            nome = input("Digite o nome do funcionário: ")
            codigo = int(input("Digite o código para o funcionário: "))
            codigo_cargo = int(input("Digite o código do cargo: "))
            sistema.cadastrar_funcionario(codigo, nome, codigo_cargo) # argumentos da função

        elif escolha == 3:
            sistema.mostrar_relatorio()

        elif escolha == 4:
            codigo_cargo = int(input("Digite o código do cargo: "))
            sistema.mostrar_total_sal_cargo(codigo_cargo)

        elif escolha == 5:
            print("Você saiu do sistema.")
            break # quebra o laço caso a opção seja selecionada
        else:
            print("Opção inválida.")

main() # chamando a classe