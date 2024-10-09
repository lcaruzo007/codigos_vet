import os
import barcode
import random
from barcode.writer import ImageWriter
from PIL import Image

# Função para gerar o código de barras e salvar como imagem
def gerar_codigo_barras(produto):
    EAN = barcode.get_barcode_class('ean13')  # Escolher o padrão de código de barras
    codigo_random = ''.join([str(random.randint(0, 9)) for _ in range(9)])  # Gerar 9 dígitos aleatórios
    codigo_completo = "789" + codigo_random  # Prefixo brasileiro + dígitos aleatórios
    ean = EAN(codigo_completo, writer=ImageWriter())
    nome_arquivo = f"{produto}_{codigo_completo}.png"
    caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)
    ean.save(caminho_arquivo)
    print(f"Arquivo salvo em: {caminho_arquivo}")  # Debugging statement
    return caminho_arquivo

# Função para listar produtos e gerar código de barras
def gerar_codigos_barras_produtos(produtos):
    for produto in produtos:
        print(f"Gerando código de barras para o produto: {produto}")
        nome_arquivo = gerar_codigo_barras(produto)
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
        "Cateter 14G (laranja)",
        "Cateter 16G (preto)",
        "Solução Fisiológica 1000ml",
        "Cateter 18G (verde)",
        "Agulha Spinal 25G",
        "Scalp 19G",
        "Scalp 21G",
        "Scalp 23G",
        "Seringa de 60mL",
        "Pacote gaze",
        "Solução Fisiológica 500mL",

        # Adicione mais produtos conforme necessário
    ]

    print("Lista de produtos:")
    for produto in produtos:
        print(f"Produto: {produto}")

    opcao = input("Deseja gerar os códigos de barras? (s/n): ").lower()
    if opcao == 's':
        gerar_codigos_barras_produtos(produtos)
    else:
        print("Opção de geração não selecionada.")

if __name__ == "__main__":
    main()
