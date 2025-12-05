## 📖 Sobre o Projeto
Este projeto nasceu da necessidade de rodar o Google Gemini em um notebook antigo (**Debian 12, arquitetura 32-bit**).

A ferramenta oficial do Google (`@google/gemini-cli`) exige versões recentes do Node.js (v20+) que não suportam mais arquiteturas 32-bit. Este projeto resolve isso utilizando **Python**, que continua oferecendo suporte robusto para hardware mais antigo e sistemas leves.

Funcionalidades:
- Interface via terminal limpa e colorida.
- Compatível com ambientes virtuais (venv) do Debian 12.
- Script de diagnóstico (`teste.py`) para verificar modelos disponíveis.
- Leve e rápido.

## 🚀 Pré-requisitos
- Python 3 instalado.
- Acesso à internet.
- Uma API Key do Google AI Studio.

Para que funcione corretamente, baixe a biblioteca python 3:
_sudo apt update
sudo apt install python3-pip python3-venv_

**Solução leve para rodar o Google Gemini no Terminal Linux (compatível com 32-bit/i386 e 64-bit).**

Esse é um código, em Python, que simula o Gemini CLI, através de API's, para terminais linux de arquitetura de 32 bits, aqueles que não conseguem rodar o Gemini CLI pois a versão do Node.js parou na 18.20.4 nessa arquitetura.

## UTILIZAÇÃO:

Obtenha sua chave da API no Google AI Studio: https://aistudio.google.com/api-keys

**1. Crie um diretório para o projeto:**
_mkdir gemini_ 

**2. Adicione os arquivos _main.py_ e _teste.py_ ao diretório**

**3. Use seu editor para escrever a sua API_KEY nos 2 arquivos**

**4. Crie e ative o ambiente viertual dentro do diretório do projeto:**
_python3 -m venv venv
source venv/bin/activate_

**5. Baixe a biblioteca do Google:**
_pip install google-generativeai_

**6. Play:**
_python main.py_

Obs:
Sempre que quiser usar, entre na pasta, ative o ambiente e de play:
_cd gemini
source venv/bin/activate
python main.py_


## ATENÇÂO!
Caso apareça o erro 404 (erro de modelo), significa que o modelo atual do código não é compativel com a sua conta do google.
verifique os modelos compativeis utilizando o código _teste.py_ disponivel no diretório.

