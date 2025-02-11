from PIL import Image
import os

def compress_tiff(input_path, output_path, max_width=2000, compression="tiff_lzw"):
    try:
        with Image.open(input_path) as img:
            frames = []
            for i in range(img.n_frames):
                img.seek(i)
                frame = img.copy()
                width, height = frame.size
                if width > max_width:
                    ratio = max_width / width
                    new_size = (max_width, int(height * ratio))
                    frame = frame.resize(new_size, Image.LANCZOS)
                frames.append(frame)
            
            frames[0].save(output_path, save_all=True, append_images=frames[1:], format="TIFF", compression=compression)
            print(f"Arquivo salvo: {output_path}")
    except Exception as e:
        print(f"Erro ao processar {input_path}: {e}")

if __name__ == "__main__":
    input_file = r"C:\Users\X\Desktop\Exemplo"  # Substitua pelo caminho do seu arquivo
    output_file = r"arquivo_comprimido.tiff"
    compress_tiff(input_file, output_file)