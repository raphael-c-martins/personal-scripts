# 🖼 Conversor de Imagens: AVIF para PNG

Este script permite converter imagens no formato **AVIF** para **PNG** de forma automática, utilizando as bibliotecas **Pillow** e **PyAV**.

## 🚀 Funcionalidades

✔️ Converte arquivos **.AVIF** para **.PNG** automaticamente

✔️ Processamento em lote de uma pasta inteira

✔️ Mantém a qualidade original da imagem

## 🛠 Requisitos

Antes de rodar o script, certifique-se de instalar as bibliotecas necessárias:

```bash
pip install pillow av

```

## 📌 Como Usar

1. Coloque os arquivos **.AVIF** na pasta de entrada
2. Defina os caminhos das pastas no código
3. Execute o script para converter as imagens

```bash
python converter_avif_para_png.py

```

## 📂 Estrutura do Projeto

```
📂 Conversor_AVIF_PNG
 ├── converter_avif_para_png.py  # Script principal
 ├── README.md                    # Documentação
 ├── ENTRADA (EXEMPLO)/           # Imagens AVIF originais
 ├── SAIDA (EXEMPLO)/             # Imagens PNG convertidas

```

## ⚠️ Observação

O script considera apenas o primeiro frame em arquivos AVIF animados (sem suporte para animações).

## 📜 Licença

Este projeto é de código aberto e pode ser usado livremente.