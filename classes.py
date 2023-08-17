class Sistema:
    def __init__(self): # iniciar a classe criando valores padrões
        self.cargos = []
        self.funcionarios = []

    def cadastrar_cargo(self, cargo, salario): # cadastro de um cargo
        self.cargos.append((cargo, salario))

    def cadastrar_funcionario(self, codigo, nome, codigo_cargo): # função para cadastrar o usuário
        if codigo in [funcionario[0] for funcionario in self.funcionarios]: # essa condicional impede a criação de código existente
            print("Código de funcionário já existe.")
            return

        if codigo_cargo < 0 or codigo_cargo >= len(self.cargos): # checa um cargo não criado
            print("Código de cargo inválido.")
            return

        self.funcionarios.append((codigo, nome, codigo_cargo)) # armazenando em lista



    def mostrar_relatorio(self): # relatório de um funcionário
        for funcionario in self.funcionarios:
            codigo, nome, codigo_cargo = funcionario # desempacotamento
            cargo, salario = self.cargos[codigo_cargo]
            print(f"Código: {codigo}, Nome: {nome}, Cargo: {cargo}, Salário: {salario}")


    def mostrar_total_sal_cargo(self, codigo_cargo): # esta função irá mostrar o total de salario por cargo
            if codigo_cargo < 0 or codigo_cargo >= len(self.cargos): # caso o codigo do cargo seja inválido
                print("Código de cargo inválido.") # irá apresentar isso
                return

            total_salario = 0
            for funcionario in self.funcionarios:
                _, _, cargo = funcionario  
                if codigo_cargo == cargo: # caso o codigo do cargo exista ele irá apresentar os valores
                    _, salario = self.cargos[codigo_cargo] 
                    total_salario += float(salario)
            
            print("Total de salário para o cargo", codigo_cargo, ":", total_salario)