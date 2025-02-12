# Conversor de PNG/JPG/JPEG para TIF

## 📌 Descrição

Este script converte automaticamente imagens nos formatos **PNG, JPG e JPEG** para **TIF**. Além disso, após a conversão, os arquivos originais são removidos do diretório.

## 🚀 Funcionalidades

- Converte arquivos **PNG, JPG e JPEG** para o formato **TIF**.
- Processa todos os arquivos dentro de um diretório especificado.
- Remove automaticamente os arquivos originais após a conversão.


## 📂 Estrutura de Pastas

O script percorre um diretório especificado onde estão localizados os arquivos a serem convertidos. Após a conversão, os arquivos **TIF** serão salvos na mesma pasta dos arquivos originais.

```
📂 Conversor_AVIF_PNG
 ├── converter_png-jpg-jpeg_para_tif.py  # Script principal
 ├── README.md                           # Documentação
📁 pasta_com_imagens
├── 🖼 imagem1.png                       # Imagem de exemplo
├── 🖼 imagem2.jpg                       # Imagem de exemplo
├── 🖼 imagem3.jpeg                      # Imagem de exemplo
└── 🔄 (Após a conversão)
    ├── 🖼 imagem1.tif                   # Imagem de exemplo convertida
    ├── 🖼 imagem2.tif                   # Imagem de exemplo convertida
    ├── 🖼 imagem3.tif                   # Imagem de exemplo convertida

```

## ⚠️ **Observação Importante**

Para que o script funcione corretamente, é essencial que toda a pasta do projeto seja aberta no seu interpretador de código (como VSCode, PyCharm, ou outro de sua preferência). Ou seja, ao invés de abrir o script diretamente, abra a pasta Conversor_AVIF_PNG no seu ambiente de desenvolvimento. Depois, execute o script converter_avif_para_png.py a partir do interpretador de código para garantir que os caminhos e configurações do projeto sejam corretamente reconhecidos.

### 🚨 Observação extra

A conversão substitui os arquivos originais ao excluí-los após a conversão. Certifique-se de ter um backup caso precise manter os arquivos originais.

## 📦 Dependências

- Python 3
- Biblioteca **Pillow** 

```bash
pip install pillow av

```

## 🛠 Como Usar

1. Configure o caminho da pasta onde estão os arquivos a serem convertidos.
2. Execute o script e aguarde a conversão ser concluída.

## 📜 Licença

Este projeto é de código aberto e pode ser usado livremente.