import os
import sys
import google.generativeai as genai

# --- CONFIGURAÇÃO ---
# Se sua chave não estiver nas variáveis de ambiente, coloque ela abaixo dentro das aspas:
# Exemplo: API_KEY = "AIzaSyD..."
API_KEY = "Suachaveaqui"

# Códigos de Cores (ANSI) para dar o visual
COR_LOGO_1 = "\033[38;5;39m"  # Azul Ciano
COR_LOGO_2 = "\033[38;5;201m" # Rosa Magenta
COR_RESET = "\033[0m"
COR_USER = "\033[1;32m"       # Verde
COR_GEMINI = "\033[1;36m"     # Ciano claro

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_logo():
    # Logo estilizado simulando o oficial
    logo = f"""
    {COR_LOGO_1}  ____ _____ __  __ ___ _   _ ___ {COR_RESET}
    {COR_LOGO_1} / ___| ____|  \/  |_ _| \ | |_ _|{COR_RESET}
    {COR_LOGO_2}| |  _|  _| | |\/| || ||  \| || | {COR_RESET}
    {COR_LOGO_2}| |_| | |___| |  | || || |\  || | {COR_RESET}
    {COR_LOGO_2} \____|_____|_|  |_|___|_| \_|___|{COR_RESET}
    
    {COR_RESET}>>> Terminal Chat - Debian 32-bit Edition <<<
    """
    print(logo)

def main():
    limpar_tela()
    mostrar_logo()

    if not API_KEY:
        print(f"\n{COR_LOGO_2}[ERRO] Chave de API não encontrada!{COR_RESET}")
        print("Edite o arquivo e cole sua chave na linha 'API_KEY = ...' ou exporte a variável.")
        return

    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        chat = model.start_chat(history=[])
        
        print("Digite sua mensagem (ou 'sair' para fechar).\n")
        
        while True:
            prompt = input(f"{COR_USER}Você > {COR_RESET}")
            
            if prompt.lower() in ['sair', 'exit']:
                print("Até mais!")
                break
            
            if not prompt:
                continue
                
            print(f"{COR_GEMINI}Gemini pensando...{COR_RESET}", end="\r")
            
            try:
                response = chat.send_message(prompt)
                # Limpa a linha do "pensando" e mostra a resposta
                print(" " * 20, end="\r") 
                print(f"{COR_GEMINI}Gemini >{COR_RESET} {response.text}\n")
                print("-" * 40)
                
            except Exception as e:
                print(f"\n{COR_LOGO_2}Erro na conexão: {e}{COR_RESET}\n")

    except Exception as e:
         print(f"Erro fatal: {e}")

if __name__ == "__main__":
    main()
