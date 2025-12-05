Esse é um código, em Python, que simula o Gemini CLI para terminais linux de arquitetura de 32 bits, aqueles que não conseguem rodar o Gemini CLI pois a versão do Node.js parou na 18.20.4 nessa arquitetura.
Para que funcione corretamente, baixe a biblioteca do google:

_sudo apt update
sudo apt install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install google-generativeai_
