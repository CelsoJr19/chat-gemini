Esse é um código, em Python, que simula o Gemini CLI para terminais linux de arquitetura de 32 bits, aqueles que não conseguem rodar o Gemini CLI pois a versão do Node.js parou na 18.20.4 nessa arquitetura.

UTILIZAÇÃO:

Para que funcione corretamente, baixe a biblioteca do google:

_sudo apt update
sudo apt install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install google-generativeai_


ATENÇÂO!
Caso apareça o erro 404 (erro de modelo), significa que o modelo atual do código não é compativel com a sua conta do google.
verifique os modelos compativeis utilizando o código _teste.py_ disponivel no diretório.
