import os
from PIL import Image

def convert_webp_to_png(webp_path, png_path):
    try:
        # Abre o arquivo WEBP usando o PIL
        with Image.open(webp_path) as img:
            # Converte e salva como PNG
            img.save(png_path, format='PNG')
            print(f"Conversão bem-sucedida: {png_path}")
    except Exception as e:
        print(f"Erro ao converter {webp_path}: {e}")

def convert_folder_webp_to_png(input_folder, output_folder):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Processa todos os arquivos WEBP na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            webp_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)

            # Converte o arquivo WEBP para PNG
            convert_webp_to_png(webp_path, png_path)

# Caminhos das pastas
input_folder = r"C:\caminho\para\pasta\com\webp" # Pasta com arquivos WEBP
output_folder = r"C:\caminho\para\pasta\com\png" # Pasta de saída para os arquivos convertidos PNG

# Converte todos os arquivos WEBP da pasta
convert_folder_webp_to_png(input_folder, output_folder)
