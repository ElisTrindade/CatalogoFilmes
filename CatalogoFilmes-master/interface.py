import os
from bd import BD
# Classe para interface do usuário do programa

class Interface:
    # Construtor
    def __init__(self):
        self.banco = BD("catalogoRoupas.db")

    def logotipo(self):
        print("============================")
        print("=====Catalogo de Roupas=====")
        print("============================")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Função que permite o usuário escolher uma opção
    # opcoes = []
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)

        # Tenta converter para números
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Verifica se a opção selecionada é uma das opções válidas
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuário
        return opcaoSelecionada

    # Mostra menu principal do sistema
    def mostraMenuPrincipal(self):
        print("1 - Cadastrar Roupas")
        print("2 - Lista de Roupas")
        print("0 - Sair")
        print()

    def mostraCadastroRoupas(self):
        self.logotipo()

        print("Insira os dados da Peça:")
        print("(campos com * são obrigatórios)")
        print()

        titulo = self.solicitaValor('Digite o título*: ', 'texto', False)
        genero = self.solicitaValor('Digite o gênero*: ', 'texto', False)
        valor = self.solicitaValor('Digite o valor*: ', 'texto', True)

        # Armazena os valores no banco de dados!
        valores = {
            "titulo": titulo,
            "genero": genero,
            "valor": valor,
            
        }

        self.banco.inserir('Roupas', valores)

    def mostrarListaRoupas(self):
        self.logotipo()
        print("Veja abaixo a lista de Roupas cadastradas.")
        print()

        Roupas = self.banco.buscaDados('Roupas')

        for Roupa in Roupas:
            id, titulo, genero, valor = Roupa
            print(f"Roupa {id} - {titulo} | {genero}")

        print()

        input("Aperte Enter para continuar...")

    # Solicita um valor do usuário e valida ele.
    # return valorDigitado
    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se está vazio
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
            return valor
        
        # Verifica se está no formato correto
        if tipo == 'numero':
            try:
                valor = float(valor)
            except ValueError:
                print("Valor Inválido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
            
        return valor