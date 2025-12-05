import google.generativeai as genai

# COLOQUE SUA CHAVE DENTRO DAS ASPAS ABAIXO
API_KEY = "SUA_CHAVE_AQUI"

try:
    genai.configure(api_key=API_KEY)
    print("--- Verificando Versão da Biblioteca ---")
    print(f"Versão: {genai.__version__}")
    
    print("\n--- Listando Modelos Disponíveis ---")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")

except Exception as e:
    print(f"Erro: {e}")
