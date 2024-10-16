import os
from datetime import datetime

# Definindo algumas cores para o terminal
CYAN = '\033[96m'
RESET = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'

# Lista para armazenar funcionários e a lixeira
funcionarios = []
lixeira = []

# Dicionário para mapeamento de estados e seus primeiros dígitos de CPF
ESTADOS_CPF = {
    'SP': '1',
    'RJ': '2',
    'MG': '3',
    'RS': '4',
    # Adicione mais estados conforme necessário
}

# Função para solicitar e verificar a senha
def senhas():
    senha_correta = '123456'  # Defina a senha correta aqui
    while True:
        senha = input(f'{CYAN}Digite a senha: {RESET}')
        if senha == senha_correta:
            print(f'{GREEN}Senha correta!{RESET}')
            break
        else:
            print(f'{RED}Senha incorreta. Tente novamente.{RESET}')

# Função para mostrar o menu
def menu():
    print(f'{CYAN}==== MENU ===={RESET}')
    print(f'{YELLOW}1. Cadastrar Funcionário')
    print(f'2. Listar Funcionários')
    print(f'3. Remover Funcionário')
    print(f'4. Editar Funcionário')
    print(f'5. Exibir Lixeira')
    print(f'6. Sair{RESET}')
    print('='*20)

# Função para verificar a validade do CPF com base no estado
def verificar_cpf(cpf, estado):
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Verifica se o primeiro dígito do CPF corresponde ao estado
    primeiro_digito = cpf[0]
    if primeiro_digito != ESTADOS_CPF.get(estado, '0'):
        return False

    return True

# Função para cadastrar funcionários
def cadastro():
    nome = input(f'{CYAN}Nome: {RESET}')
    endereco = input(f'{CYAN}Endereço: {RESET}')
    numero = int(input(f'{CYAN}Número: {RESET}'))
    bairro = input(f'{CYAN}Bairro: {RESET}')
    cidade = input(f'{CYAN}Cidade: {RESET}')
    estado = input(f'{CYAN}Estado: {RESET}')
    cep = int(input(f'{CYAN}CEP: {RESET}'))
    
    # Solicitar CPF
    cpf = input(f'{CYAN}CPF (apenas números): {RESET}')
    if not verificar_cpf(cpf, estado):
        print(f'{RED}CPF inválido para o estado informado.{RESET}')
        return

    data_nascimento = input(f'{CYAN}Digite sua data de nascimento (XX/XX/XXXX): {RESET}')
    dia = int(data_nascimento[:2])
    mes = int(data_nascimento[3:5])
    ano = int(data_nascimento[6:])
    
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade >= 18:
        print(f'{GREEN}Você já pode acessar nosso sistema de cadastro de funcionários{RESET}')
    else:
        print(f'{RED}Você é menor de idade, não pode acessar nosso sistema de cadastro de funcionários{RESET}')
        return

    dependentes = input(f'{CYAN}Dependentes responda com (SIM/NAO): {RESET}').strip().upper()
    if dependentes == 'SIM':
        quantidade_dependentes = int(input(f'{CYAN}Quantidade de dependentes: {RESET}'))
    else:
        quantidade_dependentes = 0
    cargo = input(f'{CYAN}Cargo: {RESET}')
    salario = float(input(f'{CYAN}Salário: {RESET}'))

    funcionario = {
        'Nome': nome,
        'Endereço': endereco,
        'Número': numero,
        'Bairro': bairro,
        'Cidade': cidade,
        'Estado': estado,
        'CEP': cep,
        'CPF': cpf,
        'Idade': idade,
        'Data de nascimento': data_nascimento,
        'Dependentes': quantidade_dependentes,
        'Cargo': cargo,
        'Salário': salario
    }
    funcionarios.append(funcionario)
    print(f'{GREEN}Funcionário {nome} cadastrado com sucesso!{RESET}')

# Função para listar funcionários
def listar():
    if funcionarios:
        print('='*40)
        print(f'{BLUE}LISTA DE FUNCIONÁRIOS CADASTRADOS:{RESET}')
        for indice, funcionario in enumerate(funcionarios, start=1):
            print(f'{indice}.\n{YELLOW}Nome: {funcionario["Nome"]}\nEndereço: {funcionario["Endereço"]}\nNúmero: {funcionario["Número"]}\nBairro: {funcionario["Bairro"]}\nCidade: {funcionario["Cidade"]}\nEstado: {funcionario["Estado"]}\nCEP: {funcionario["CEP"]}\nCPF: {funcionario["CPF"]}\nIdade: {funcionario["Idade"]}\nData de nascimento: {funcionario["Data de nascimento"]}\nDependentes: {funcionario["Dependentes"]}\nCargo: {funcionario["Cargo"]}\nSalário: {funcionario["Salário"]}{RESET}')
            print('='*40)
    else:
        print(f'{RED}Nenhum funcionário cadastrado{RESET}')
        print('='*40)

# Função para remover funcionários
def remover():
    if funcionarios:
        print(f'{CYAN}Funcionários disponíveis para remoção:{RESET}')
        for indice, funcionario in enumerate(funcionarios, start=1):
            print(f'{indice}. {funcionario["Nome"]}')
       
        escolha_funcionario = input(f'{CYAN}Qual funcionário deseja remover (número): {RESET}')
       
        if escolha_funcionario.isdigit():
            escolha_funcionario = int(escolha_funcionario)
            if 1 <= escolha_funcionario <= len(funcionarios):
                funcionario_removido = funcionarios.pop(escolha_funcionario - 1)
                lixeira.append(funcionario_removido)
                print(f'{GREEN}Funcionário {funcionario_removido["Nome"]} removido com sucesso.{RESET}')
            else:
                print(f'{RED}Escolha inválida. Número fora do intervalo.{RESET}')
        else:
            print(f'{RED}Escolha inválida. Por favor, insira um número válido.{RESET}')
    else:
        print(f'{RED}Nenhum funcionário cadastrado para remover.{RESET}')

# Função para editar funcionários
def editar():
    if funcionarios:
        print(f'{CYAN}Funcionários disponíveis para edição:{RESET}')
        for indice, funcionario in enumerate(funcionarios, start=1):
            print(f'{indice}. Nome: {funcionario["Nome"]}, Endereço: {funcionario["Endereço"]}, Número: {funcionario["Número"]}, Bairro: {funcionario["Bairro"]}, Cidade: {funcionario["Cidade"]}, Estado: {funcionario["Estado"]}, CEP: {funcionario["CEP"]}, CPF: {funcionario["CPF"]}, Idade: {funcionario["Idade"]}, Data de nascimento: {funcionario["Data de nascimento"]}, Dependentes: {funcionario["Dependentes"]}, Cargo: {funcionario["Cargo"]}, Salário: {funcionario["Salário"]}.')
       
        escolha_funcionario = input(f'{CYAN}Qual funcionário deseja editar (número): {RESET}')
       
        if escolha_funcionario.isdigit():
            escolha_funcionario = int(escolha_funcionario)
            if 1 <= escolha_funcionario <= len(funcionarios):
                funcionario = funcionarios[escolha_funcionario - 1]
               
                print(f'{CYAN}Editando funcionário: {funcionario["Nome"]}{RESET}')
                print(f'{YELLOW}1. Nome\n2. Endereço\n3. Número\n4. Bairro\n5. Cidade\n6. Estado\n7. CEP\n8. Idade\n9. Data de nascimento\n10. Dependentes\n11. Cargo\n12. Salário{RESET}')
                escolha_campo = input(f'{CYAN}Qual campo deseja editar (número): {RESET}')
               
                if escolha_campo == '1':
                    novo_nome = input(f'{CYAN}Novo nome: {RESET}')
                    funcionario['Nome'] = novo_nome
                elif escolha_campo == '2':
                    novo_numero = input(f'{CYAN}Novo número: {RESET}')
                    funcionario['Número'] = novo_numero
                elif escolha_campo == '3':
                    novo_bairro = input(f'{CYAN}Novo bairro: {RESET}')
                    funcionario['Bairro'] = novo_bairro
                elif escolha_campo == '4':
                    nova_cidade = input(f'{CYAN}Nova cidade: {RESET}')
                    funcionario['Cidade'] = nova_cidade
                elif escolha_campo == '5':
                    novo_estado = input(f'{CYAN}Novo estado: {RESET}')
                    funcionario['Estado'] = novo_estado
                elif escolha_campo == '6':
                    novo_cep = input(f'{CYAN}Novo CEP: {RESET}')
                    funcionario['CEP'] = novo_cep
                elif escolha_campo == '7':
                    nova_idade = int(input(f'{CYAN}Nova idade: {RESET}'))
                    funcionario['Idade'] = nova_idade
                elif escolha_campo == '8':
                    nova_data_nascimento = input(f'{CYAN}Nova data de nascimento (XX/XX/XXXX): {RESET}')
                    funcionario['Data de nascimento'] = nova_data_nascimento
                elif escolha_campo == '9':
                    novo_dependentes = input(f'{CYAN}Novo número de dependentes: {RESET}')
                    funcionario['Dependentes'] = novo_dependentes
                elif escolha_campo == '10':
                    novo_cargo = input(f'{CYAN}Novo cargo: {RESET}')
                    funcionario['Cargo'] = novo_cargo
                elif escolha_campo == '11':
                    novo_salario = float(input(f'{CYAN}Novo salário: {RESET}'))
                    funcionario['Salário'] = novo_salario
                else:
                    print(f'{RED}Escolha inválida. Por favor, insira um número válido.{RESET}')
            else:
                print(f'{RED}Escolha inválida. Número fora do intervalo.{RESET}')
    else:
        print(f'{RED}Nenhum funcionário cadastrado para editar.{RESET}')

# Parte que vai exibir a lixeira
def lixeira_funcionarios():
    if lixeira:
        print('='*40)
        print(f'{BLUE}LIXEIRA DE FUNCIONÁRIOS REMOVIDOS:{RESET}')
        for indice, funcionario in enumerate(lixeira, start=1):
            print(f'{indice}.\n{YELLOW}Nome: {funcionario["Nome"]}\nEndereço: {funcionario["Endereço"]}\nNúmero: {funcionario["Número"]}\nBairro: {funcionario["Bairro"]}\nCidade: {funcionario["Cidade"]}\nEstado: {funcionario["Estado"]}\nCEP: {funcionario["CEP"]}\nCPF: {funcionario["CPF"]}\nIdade: {funcionario["Idade"]}\nData de nascimento: {funcionario["Data de nascimento"]}\nDependentes: {funcionario["Dependentes"]}\nCargo: {funcionario["Cargo"]}\nSalário: {funcionario["Salário"]}{RESET}')
            print('='*40)
    else:
        print(f'{RED}Nenhum funcionário removido.{RESET}')

# Aqui é onde o programa começa, exibindo o menu e chamando as funções correspondentes
if __name__ == "__main__":
    senhas()
    while True:
        os.system('cls')
        menu()
        escolha = input(f'{CYAN}Escolha uma opção: {RESET}')

        if escolha == '1':
            cadastro()
        elif escolha == '2':
            listar()
        elif escolha == '3':
            remover()
        elif escolha == '4':
            editar()
        elif escolha == '5':
            lixeira_funcionarios()
        elif escolha == '6':
            print(f'{GREEN}Saindo do sistema...{RESET}')
            break
        else:
            print(f'{RED}Opção inválida!{RESET}')
