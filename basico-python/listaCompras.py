lista_compras = []

def exibir_lista():
    print("\nLista de Compras:")
    total = 0
    for item in lista_compras:
        print(f"{item['descricao']} - R$ {item['valor']:.2f}")
        total += item['valor']
    print(f"Total: R$ {total:.2f}\n")

while True:
    descricao = input("Digite a descrição do item (ou 'sair' para encerrar): ")
    if descricao.lower() == 'sair':
        break
    
    try:
        valor = float(input("Digite o valor do item: "))
        lista_compras.append({"descricao": descricao, "valor": valor})
        exibir_lista()
    except ValueError:
        print("Por favor, digite um valor válido.")
