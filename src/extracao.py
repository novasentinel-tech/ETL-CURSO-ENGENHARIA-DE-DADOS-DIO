import pandas as pd
from pathlib import Path


def extrair_csv(nome_arquivo: str) -> pd.DataFrame | None:
    """
    Lê o CSV de usuários e retorna um DataFrame
    """
    print("\n🔍 Extraindo dados do CSV...")
    
    caminho = Path("dados") / nome_arquivo
    
    if not caminho.exists():
        print(f"❌ Arquivo não encontrado: {caminho}")
        return None
    
    try:
        df = pd.read_csv(caminho)
        print(f"✅ CSV carregado! {len(df)} usuários prontos pra processar.")
        return df
    except Exception as erro:
        print(f"❌ Erro ao extrair CSV: {erro}")
        return None


def categorizar_usuarios(df: pd.DataFrame) -> dict:
    """
    Categoriza usuários por departamento e retorna um dict organizado
    """
    print("\n📂 Categorizando usuários por departamento...")
    
    categorizado = {}
    
    for _, usuario in df.iterrows():
        dept = usuario.get("department", "Unknown")
        
        if dept not in categorizado:
            categorizado[dept] = []
        
        categorizado[dept].append({
            "nome": usuario.get("name", ""),
            "email": usuario.get("email", ""),
            "cidade": usuario.get("city", ""),
            "empresa": usuario.get("company", ""),
            "telefone": usuario.get("phone", ""),
            "website": usuario.get("website", ""),
            "cargo": usuario.get("job_title", ""),
            "idade": usuario.get("age", 0),
            "departamento": dept
        })
    
    print(f"✅ Categorizado em {len(categorizado)} departamentos!")
    return categorizado


if __name__ == "__main__":
    df = extrair_csv("usuarios.csv")
    if df is not None:
        usuarios_categorizados = categorizar_usuarios(df)
        for dept, usuarios in usuarios_categorizados.items():
            print(f" - {dept}: {len(usuarios)} pessoas")