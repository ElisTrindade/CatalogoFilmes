# Importa a classe Interface
from interface import Interface
from bd import BD

# Classe principal do programa
interface = Interface()
banco = BD("catalogoFilmes.db")

opcao = ""
while opcao != 0:
    interface.logotipo()
    interface.mostraMenuPrincipal()
    opcao = interface.selecionaOpcao([1, 2, 0])
    interface.limpaTela()

    # Tela de cadastro de filmes
    if opcao == 1:
        interface.mostraCadastroFilmes()

    # Tela de lista de filmes
    if opcao == 2:
        pass