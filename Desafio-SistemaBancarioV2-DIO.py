# Função para saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques, limite_emprestimo, saldo_emprestimo):
    if saldo - valor >= -limite and numero_saques < limite_saques:
        saldo -= valor
        extrato += f"\nSaque de R${valor:.2f}"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        return saldo, extrato, numero_saques, limite_emprestimo, saldo_emprestimo

    else:
        print("Saque não autorizado!")
        if saldo<valor:
            print("Saldo insuficiente!")
            if valor <= limite_emprestimo:
                opcao_emprestimo = input("Deseja fazer um empréstimo? (S - Sim) (N - Não): ")
                while opcao_emprestimo.upper() not in ["S", "N"]:
                    print("Opção Inválida!")
                    opcao_emprestimo = input("Deseja fazer um empréstimo? (S - Sim) (N - Não): ")
                if opcao_emprestimo.upper() == "S":
                    saldo, extrato, limite_emprestimo, saldo_emprestimo = emprestimo(saldo, extrato, limite_emprestimo, saldo_emprestimo)
                    return saldo, extrato, numero_saques, limite_emprestimo, saldo_emprestimo
                else:
                    return saldo, extrato, numero_saques, limite_emprestimo, saldo_emprestimo
            else:
                print("Limite para empréstimo excedido!")
                return saldo, extrato, numero_saques, limite_emprestimo, saldo_emprestimo
        elif numero_saques>limite_saques:
            print("Limite de Saques atingido!")
            return saldo, extrato, numero_saques, limite_emprestimo, saldo_emprestimo

        else:
            return saldo, extrato, numero_saques, limite_emprestimo, saldo_emprestimo

# Função Empréstimo
def emprestimo(saldo, extrato, limite_emprestimo, saldo_emprestimo):
    if limite_emprestimo > saldo_emprestimo:
        valor = float(input("Digite o valor do empréstimo: "))
        
        # Verificar se o valor do empréstimo é válido
        if valor <= 0:
            print("Valor inválido para o empréstimo.")
            return saldo, extrato, limite_emprestimo, saldo_emprestimo
        
        # Verificar se o valor do empréstimo excede o limite disponível
        if valor + saldo_emprestimo > limite_emprestimo:
            print("Limite de empréstimo excedido!")
            if saldo_emprestimo == 0:
                return saldo, extrato, limite_emprestimo, saldo_emprestimo
            opcao_saldo = input(f"Saldo do Empréstimo: R$ {saldo_emprestimo}! Deseja pagar o Saldo? S - Sim | N - Nao: ")
            
            # Solicitar ao usuário se deseja usar o saldo para pagar o empréstimo excedido
            while opcao_saldo.upper() not in ["S", "N"]:
                print("Opção Inválida!")
                opcao_saldo = input(f"Saldo do Empréstimo: R$ {saldo_emprestimo}! Deseja pagar o Saldo? S - Sim | N - Nao: ")
                
            if opcao_saldo.upper() == "S":
                valor_pagamento_emprestimo = float(input(f"Saldo do Empréstimo: R$ {saldo_emprestimo}! Digite o valor a pagar: "))
                
                # Verificar se o saldo é suficiente para pagar o empréstimo excedido
                if saldo >= valor_pagamento_emprestimo:
                    saldo_emprestimo -= valor_pagamento_emprestimo
                    saldo -= valor_pagamento_emprestimo
                    extrato += f"\nPagamento de Empréstimo R${valor_pagamento_emprestimo:.2f}"
                    print("Pagamento de Empréstimo realizado com sucesso!")
                else:
                    print("Saldo em conta insuficiente para pagar o empréstimo!")
                    return saldo, extrato, limite_emprestimo, saldo_emprestimo
            elif opcao_saldo.upper() == "N":
                return saldo, extrato, limite_emprestimo, saldo_emprestimo
        else:
            saldo += valor
            limite_emprestimo -= valor
            saldo_emprestimo += valor
            extrato += f"\nEmpréstimo de R${valor:.2f}"
            print("Empréstimo realizado com sucesso!")
            return saldo, extrato, limite_emprestimo, saldo_emprestimo
    else:
        print("Limite de empréstimo atingido!")
        opcao_emprestimo = input("Deseja pagar o Saldo do Empréstimo? S - Sim | N - Não: ")
        
        # Solicitar ao usuário se deseja pagar o saldo do empréstimo
        while opcao_emprestimo.upper() not in ["S", "N"]:
            print("Opção Inválida!")
            opcao_emprestimo = input("Deseja pagar o Saldo do Empréstimo? S - Sim | N - Não: ")
            
        if opcao_emprestimo.upper() == "S":
            saldo_real = saldo - saldo_emprestimo
            
            # Verificar se há saldo suficiente para pagar o empréstimo
            if saldo_real >= 0:
                print(f"\nSaldo Real em conta: R${saldo_real:.2f}.\nSaldo Total: R${saldo:.2f}")
                valor = float(input("Digite o valor a pagar: "))
                
                # Verificar se o valor do pagamento é válido
                while valor > saldo_real or valor < 0:
                    print("Digite um valor válido!")
                    valor = float(input("Digite o valor a pagar: "))
                    
                saldo -= valor
                saldo_emprestimo -= valor
                extrato += f"\nPagamento de Empréstimo R${valor:.2f}"
                print("Pagamento de Empréstimo realizado com sucesso!")
            else:
                print("\nNão possui saldo suficiente para pagar o empréstimo!")
        
        return saldo, extrato, limite_emprestimo, saldo_emprestimo

def pagar_emprestimo(saldo, extrato, limite_emprestimo, saldo_emprestimo):
    print("\n=== Pagamento de Empréstimo ===")
    print(f"Saldo em Conta: {saldo:.2f}")
    print(f"Saldo do Empréstimo: R${saldo_emprestimo:.2f}")
    
    # Verificar se há saldo de empréstimo a ser pago
    if saldo_emprestimo == 0:
        print("Não há saldo de empréstimo a ser pago.")
        return saldo, extrato, limite_emprestimo, saldo_emprestimo
    
    print("\nOpções:")
    print("1. Pagar o saldo do empréstimo com saldo da conta.")
    print("2. Voltar ao menu anterior.")
    
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == "1":
        valor_pagamento = float(input("Digite o valor a ser pago: "))
        
        # Verificar se o valor de pagamento é válido
        if valor_pagamento <= 0:
            print("Valor inválido para o pagamento do empréstimo.")
            return saldo, extrato, limite_emprestimo, saldo_emprestimo
        
        # Verificar se há saldo suficiente para pagar o empréstimo
        if saldo >= valor_pagamento:
            saldo -= valor_pagamento
            saldo_emprestimo -= valor_pagamento
            extrato += f"\nPagamento de Empréstimo R${valor_pagamento:.2f}"
            print("Pagamento de Empréstimo realizado com sucesso!")
        else:
            print("Saldo em conta insuficiente para pagar o empréstimo.")
    elif escolha == "2":
        print("Retornando ao menu anterior...")
    else:
        print("Opção inválida!")

    return saldo, extrato, limite_emprestimo, saldo_emprestimo

# Função para depósito
def deposito(saldo, valor, extrato,/):
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito de R${valor:.2f}"
            print("Depósito realizado com sucesso!")
            return saldo, extrato
        else:
            print("Depósitos precisam ser maiores que R$0.00")
            return saldo, extrato

# Função para extrato
def extrato_conta(saldo, *, extrato, saldo_emprestimo):
    print("\nSaldo:", saldo)
    print("Saldo Empréstimo:", saldo_emprestimo)
    print("\nExtrato:", extrato)

# Classe para representar um Cliente do banco
class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

# Classe para representar uma Conta Corrente
class ContaCorrente:
    num_conta = 1  # Número da conta inicia em 1

    def __init__(self, usuario):
        self.agencia = "0001"
        self.num_conta = ContaCorrente.num_conta
        ContaCorrente.num_conta += 1
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.limite = 1
        self.numero_saques = 0
        self.limite_saques = 3
        self.limite_emprestimo = 5000
        self.saldo_emprestimo = 0
# Função para criar um novo usuário
def criar_usuario(lista_usuarios):
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF do cliente: ")
    endereco = input("Digite o endereço do cliente (logradouro, número - bairro - cidade/UF): ")
    cpf_numeros = ''.join(filter(str.isdigit, cpf))  # Remover caracteres não numéricos do CPF
    if cpf_numeros not in [user.cpf for user in lista_usuarios]:
        novo_usuario = Cliente(nome, data_nascimento, cpf_numeros, endereco)
        lista_usuarios.append(novo_usuario)
        print("Usuário criado com sucesso!")
    else:
        print("CPF já cadastrado!")

# Função para criar uma nova conta corrente vinculada a um usuário existente
def criar_conta_corrente(lista_usuarios, lista_contas):
    if lista_usuarios:
        print("Selecione o usuário para criar a conta:")
        for i, usuario in enumerate(lista_usuarios):
            print(f"{i + 1}. {usuario.nome}")
        
        # Solicitação da escolha do usuário com tratamento de exceções
        escolha = input("Digite o número correspondente ao usuário: ")
        if escolha is not None and escolha.isdigit():
            escolha= int(escolha)
            if 1 <= escolha <= len(lista_usuarios):
                novo_usuario = lista_usuarios[escolha - 1]
                nova_conta = ContaCorrente(novo_usuario)
                lista_contas.append(nova_conta)
                print("Conta corrente criada com sucesso!")
            else:
                print("Escolha inválida!")
            
        else:
            print("Inválido!")
    else:
        print("Não há usuários cadastrados.")
# Função para listar todas as contas correntes
def listar_contas(lista_contas):
    print("\nLista de contas correntes:")
    if lista_contas:
        for conta in lista_contas:
            print(f"Agência: {conta.agencia} - Conta: {conta.num_conta} - Titular: {conta.usuario.nome}")
    else:
        print("Não há contas cadastradas.")

# Função para retirar uma conta corrente da lista
def retirar_conta(lista_contas):
    if lista_contas:
        num_conta = int(input("Digite o número da conta corrente a ser retirada: "))
        for conta in lista_contas:
            if conta.num_conta == num_conta:
                lista_contas.remove(conta)
                print("Conta corrente retirada com sucesso!")
                return
        print("Conta não encontrada.")
    else:
        print("Não há contas cadastradas.")
# Função para o menu de operações bancárias
def menu_operacoes(saldo, extrato, limite, numero_saques, limite_saques, limite_emprestimo, saldo_emprestimo):
    while True:
        print("\n=== Menu de Operações Bancárias ===")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Extrato")
        print("4. Pagar Empréstimo")
        print("5. Voltar ao Menu Principal")
        escolha = input("Digite o número da opção desejada: ")
        if escolha == "1":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, numero_saques, limite_emprestimo, saldo_emprestimo = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques, limite_emprestimo=limite_emprestimo, saldo_emprestimo=saldo_emprestimo)
        elif escolha == "2":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif escolha == "3":
            extrato_conta(saldo, extrato=extrato, saldo_emprestimo=saldo_emprestimo)
        elif escolha == "4":
            saldo, extrato, limite_emprestimo, saldo_emprestimo = pagar_emprestimo(saldo, extrato, limite_emprestimo, saldo_emprestimo)
        elif escolha == "5":
            print("Retornando ao Menu Principal...")
            break
        else:
            print("Opção inválida!")
            
# Função para o menu principal
def menu_principal():
    usuarios = []
    contas_correntes = []
    while True:
        print("\n=== Menu Principal ===")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Listar Contas Correntes")
        print("4. Retirar Conta Corrente")
        print("5. Operações Bancárias")
        print("6. Sair")
        escolha = input("Digite o número da opção desejada: ")
        if escolha == "1":
            criar_usuario(usuarios)
        elif escolha == "2":
            criar_conta_corrente(usuarios, contas_correntes)
        elif escolha == "3":
            listar_contas(contas_correntes)
        elif escolha == "4":
            retirar_conta(contas_correntes)
        elif escolha == "5":
            if contas_correntes:
                num_conta = int(input("Digite o número da conta corrente: "))
                for conta in contas_correntes:
                    if conta.num_conta == num_conta:
                        menu_operacoes(saldo=conta.saldo, extrato=conta.extrato, limite=conta.limite, numero_saques=conta.numero_saques, limite_saques=conta.limite_saques, limite_emprestimo=conta.limite_emprestimo, saldo_emprestimo=conta.saldo_emprestimo)
                        break
                else:
                    print("Conta não encontrada.")
            else:
                print("Não há contas cadastradas.")
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Chamada do menu principal
if __name__ == "__main__":
    menu_principal()
