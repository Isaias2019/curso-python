lista_pessoas = []

def exibir_pessoa(nome):
    for pessoa in lista_pessoas:
        if pessoa['nome'].lower() == nome.lower():
            return pessoa
    return None

while True:
    try:
        opcao = input("Digite 'adicionar' para adicionar uma pessoa, 'pesquisar' para buscar por nome ou 'sair' para encerrar: ")
        
        if opcao.lower() == 'sair':
            break
        
        if opcao.lower() == 'adicionar':
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            idade = int(input("Digite a idade: "))
            lista_pessoas.append({"nome": nome, "cpf": cpf, "idade": idade})
        
        elif opcao.lower() == 'pesquisar':
            nome_pesquisa = input("Digite o nome a ser pesquisado: ")
            resultado = exibir_pessoa(nome_pesquisa)
            if resultado:
                print(f"Pessoa encontrada: {resultado}")
            else:
                print("Nome não encontrado.")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos para idade.")
