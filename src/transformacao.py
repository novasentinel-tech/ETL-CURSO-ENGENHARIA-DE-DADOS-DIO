import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configurar Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ Ey! Falta a chave GEMINI_API_KEY no .env")

genai.configure(api_key=GEMINI_API_KEY)


def gerar_resumo_com_gemini(usuario: dict) -> dict:
    """
    Usa Gemini pra gerar um resumo massa do usuário
    """
    nome = usuario.get("nome", "Desconhecido")
    cargo = usuario.get("cargo", "Indefinido")
    empresa = usuario.get("empresa", "Desconhecida")
    cidade = usuario.get("cidade", "Desconhecida")
    departamento = usuario.get("departamento", "Indefinido")
    idade = usuario.get("idade", "N/A")
    
    prompt = f"""
Crie um resumo CRIATIVO, INTERESSANTE e bem DESCONTRAÍDO (como se fosse escrito por um adolescente de 16 anos) sobre este profissional:

Nome: {nome}
Cargo: {cargo}
Empresa: {empresa}
Cidade: {cidade}
Departamento: {departamento}
Idade: {idade}

Destaque:
1. Um resumo da vida profissional dele com jeito descontraído
2. Skills que provavelmente tem
3. Um fato interessante/curiosidade fictícia mas realista
4. Uma dica de carreira descontraída

Responda em PORTUGUÊS e seja CRIATIVO! Isso vai virar um resumo em Markdown.
"""
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        
        time.sleep(1)
        
        return {
            "sucesso": True,
            "resumo": response.text,
            "usuario": nome
        }
    except Exception as e:
        print(f"❌ Erro ao gerar com Gemini para {nome}: {e}")
        return {
            "sucesso": False,
            "resumo": f"Erro ao processar {nome}",
            "usuario": nome
        }


def transformar_usuarios(usuarios_categorizados: dict) -> dict:
    """
    Transforma usuários usando IA Generativa
    Retorna um dict com os resumos gerados
    """
    print("\n🤖 Transformando dados com IA (Gemini)...")
    
    usuarios_transformados = {}
    total_usuarios = sum(len(usuarios) for usuarios in usuarios_categorizados.values())
    processados = 0
    
    for departamento, lista_usuarios in usuarios_categorizados.items():
        usuarios_transformados[departamento] = []
        
        for usuario in lista_usuarios:
            print(f"  ⚙️  Processando {usuario.get('nome', 'Desconhecido')}... ({processados + 1}/{total_usuarios})")
            
            resumo_dict = gerar_resumo_com_gemini(usuario)
            
            usuarios_transformados[departamento].append({
                "usuario_original": usuario,
                "resumo_ia": resumo_dict["resumo"],
                "processado": resumo_dict["sucesso"]
            })
            
            processados += 1
    
    print(f"✅ Transformação concluída! {processados} usuários processados.")
    return usuarios_transformados


if __name__ == "__main__":
    from extracao import extrair_csv, categorizar_usuarios
    
    df = extrair_csv("usuarios.csv")
    if df is not None:
        categorizados = categorizar_usuarios(df)
        transformados = transformar_usuarios(categorizados)

