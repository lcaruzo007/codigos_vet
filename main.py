import os
import barcode
from barcode.writer import ImageWriter
from PIL import Image

# Função para gerar o código de barras e salvar como imagem
def gerar_codigo_barras(produto, codigo):
    EAN = barcode.get_barcode_class('ean13')  # Escolher o padrão de código de barras
    ean = EAN(codigo, writer=ImageWriter())
    nome_arquivo = f"{produto}_{codigo}.png"
    caminho_arquivo = os.path.join(os.path.dirname(__file__), nome_arquivo)
    ean.save(caminho_arquivo)
    print(f"Arquivo salvo em: {caminho_arquivo}")  # Debugging statement
    return caminho_arquivo

# Função para listar produtos e gerar código de barras
def gerar_codigos_barras_produtos(produtos):
    for produto, codigo in produtos:
        print(f"Gerando código de barras para o produto: {produto} com código: {codigo}")
        nome_arquivo = gerar_codigo_barras(produto, codigo)
        print(f"Código de barras salvo como: {nome_arquivo}")
        exibir_imagem(nome_arquivo)

# Função para exibir a imagem do código de barras
def exibir_imagem(caminho_imagem):
    if os.path.exists(caminho_imagem):
        img = Image.open(caminho_imagem)
        img.show()
    else:
        print(f"Erro: O arquivo {caminho_imagem} não foi encontrado.")  # Debugging statement

# Função principal
def main():
    produtos = [
        ("Produto A", "123456789012"),
        ("Produto B", "987654321098"),
        ("Produto C", "123123123123"),
    ]

    print("Lista de produtos:")
    for produto, codigo in produtos:
        print(f"Produto: {produto}, Código: {codigo}")

    opcao = input("Deseja imprimir os códigos de barras? (s/n): ").lower()
    if opcao == 's':
        gerar_codigos_barras_produtos(produtos)
    else:
        print("Opção de impressão não selecionada.")

if __name__ == "__main__":
    main()