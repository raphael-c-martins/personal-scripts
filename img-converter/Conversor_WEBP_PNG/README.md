# Conversor de Imagens: WEBP para PNG

Este script permite converter imagens do formato **WEBP** para **PNG** de forma automática. Ele pode processar arquivos individuais ou converter todos os arquivos WEBP dentro de uma pasta específica.


## 📌 Funcionalidades

- Converte imagens **WEBP** para **PNG**
- Suporte para conversão em **lote** dentro de uma pasta
- Mantém a qualidade original da imagem

## 📂 Estrutura do Projeto

```
📂 Conversor_WEBP_PNG
 ├── converter_webp_para_png.py  # Script principal
 ├── README.md                    # Documentação
 ├── ENTRADA (EXEMPLO)/           # Imagens WEBP originais
 ├── SAIDA (EXEMPLO)/             # Imagens PNG convertidas
```

## 🚀 Requisitos

Antes de executar o script, certifique-se de ter o **Python** instalado junto com as bibliotecas necessárias:

```
pip install pillow
```

## 🔧 Como Usar

### 1️⃣ Converter um arquivo WEBP específico

No script, defina os caminhos para os arquivos de entrada e saída:

```
webp_path = "caminho/para/imagem.webp"
png_path = "caminho/para/imagem.png"
convert_webp_to_png(webp_path, png_path)
```

### 2️⃣ Converter todos os arquivos WEBP de uma pasta

No script, altere os caminhos das pastas de entrada e saída:

```
input_folder = r"C:\caminho\para\pasta\com\webp"
output_folder = r"C:\caminho\para\pasta\com\png"
convert_folder_webp_to_png(input_folder, output_folder)
```

Execute o script e ele converterá automaticamente todas as imagens WEBP para PNG.

## ⚠️ **Observação Importante**

Para que o script funcione corretamente, **é essencial que toda a pasta do projeto seja aberta no seu interpretador de código** (como VSCode, PyCharm, ou outro de sua preferência). Ou seja, ao invés de abrir o script diretamente, abra a pasta **Conversor_AVIF_PNG** no seu ambiente de desenvolvimento. Depois, execute o script `converter_avif_para_png.py` a partir do interpretador de código para garantir que os caminhos e configurações do projeto sejam corretamente reconhecidos.

### 🚨 Observação extra

Caso os arquivos WEBP possuam transparência, essa característica será mantida na conversão para PNG.

---

## 📜 Licença

Este projeto é de código aberto e pode ser usado livremente.