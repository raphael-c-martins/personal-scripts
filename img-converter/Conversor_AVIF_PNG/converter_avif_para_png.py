import os
import av
from PIL import Image
import io

def convert_avif_to_png(avif_path, png_path):
    try:
        # Abre o arquivo AVIF usando o pyav
        container = av.open(avif_path)
        for frame in container.decode(video=0):
            # Converte o frame para uma imagem PIL
            img = frame.to_image()
            
            # Salva a imagem como PNG
            img.save(png_path, format='PNG')
            print(f"Conversão bem-sucedida: {png_path}")
            break  # Considera apenas o primeiro frame (em caso de vídeos AVIF)
    except Exception as e:
        print(f"Erro ao converter {avif_path}: {e}")

def convert_folder_avif_to_png(input_folder, output_folder):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Processa todos os arquivos AVIF na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".avif"):
            avif_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)

            # Converte o arquivo AVIF para PNG
            convert_avif_to_png(avif_path, png_path)

# Caminhos das pastas 
input_folder = r"C:\caminho\para\pasta\com\avif" # Pasta com arquivos AVIF
output_folder = r"C:\caminho\para\pasta\com\png" # Pasta de saída para os arquivos convertidos PNG

# Converte todos os arquivos AVIF da pasta
convert_folder_avif_to_png(input_folder, output_folder)
