import os
from PIL import Image

# Caminho do diretório onde estão os arquivos
caminho_diretorio = r'C:\Users\Raphael\Desktop\Estudos\# Scripts\Conversor de formato de imagem\Conversor_PNG_TIF\pasta_com_imagens'
# caminho_diretorio = r'C:\Users\SeuUsuario\Caminho\Para\Imagens'

# Lista todos os arquivos no diretório
arquivos = os.listdir(caminho_diretorio)

# Extensões de arquivos que serão convertidos
extensoes = ('.png', '.jpg', '.jpeg')

# Itera pelos arquivos e converte os arquivos para .tif
for nome_arquivo in arquivos:
    if nome_arquivo.lower().endswith(extensoes):
        # Caminho completo do arquivo
        caminho_arquivo = os.path.join(caminho_diretorio, nome_arquivo)

        # Abre a imagem com base na extensão
        with Image.open(caminho_arquivo) as img:
            # Define o novo nome do arquivo com a extensão .tif
            nome_arquivo_tif = os.path.splitext(nome_arquivo)[0] + '.tif'
            caminho_novo_arquivo = os.path.join(caminho_diretorio, nome_arquivo_tif)
            
            # Converte e salva como .tif
            img.save(caminho_novo_arquivo, format='TIFF')

        # Remove o arquivo original
        os.remove(caminho_arquivo)

        print(f"Arquivo convertido e removido: {nome_arquivo} -> {nome_arquivo_tif}")

print("Conversão e remoção de arquivos concluídas!")
