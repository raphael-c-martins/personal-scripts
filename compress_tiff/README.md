# 📷 Compressão de Arquivos TIFF

Este projeto fornece um script Python para reduzir o tamanho de arquivos TIFF multi-frame, aplicando compressão LZW e redimensionamento opcional para otimização.

## 🚀 Funcionalidades

- Suporta arquivos TIFF de várias páginas.
- Aplica compressão "tiff_lzw" para reduzir o tamanho do arquivo sem perder qualidade.
- Redimensiona imagens automaticamente para um tamanho máximo configurável.

## 🛠 Requisitos

Antes de rodar o script, instale a biblioteca Pillow:

```
pip install pillow
```

## 📌 Uso

1. Defina o caminho do arquivo de entrada no script.
2. Execute o script para gerar um TIFF comprimido.

```
python compress_tiff.py
```

## 📂 Estrutura do Projeto

```
📂 compress-tiff
 ├── compress_tiff.py  # Script principal
 ├── README.md          # Documentação
```

## ✨ Personalização

- **Redimensionamento**: Modifique `max_width` para ajustar o tamanho máximo da largura das imagens.
- **Compressão**: Ajuste o método alterando `compression="tiff_lzw"` para outras opções suportadas.

## 📜 Licença

Este projeto é de código aberto e pode ser usado livremente.

---

💡 **Dica:** Caso seu arquivo TIFF tenha muitas páginas e algumas fiquem corrompidas, experimente dividi-lo em partes menores antes da compressão!