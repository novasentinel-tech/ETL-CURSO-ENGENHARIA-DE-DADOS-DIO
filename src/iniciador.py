"""
🚀 INICIADOR DA PIPELINE ETL
Ey! Este é o arquivo que começa TUDO.
Ele chama extracao -> transformacao -> carregamento
Uma coisa de cada vez, certinho!
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Adicionar o diretório src ao path pra importar os módulos
sys.path.insert(0, str(Path(__file__).parent))

from extracao import extrair_csv, categorizar_usuarios
from transformacao import transformar_usuarios
from carregamento import carregar_em_markdown


def main():
    """
    Função principal que executa toda a pipeline
    Tipo um maestro coordenando uma orquestra, saca?
    """
    
    print("\n" + "=" * 60)
    print("🎬 INICIANDO PIPELINE ETL COM GEMINI AI")
    print("=" * 60)
    
    # ============================================================
    # ETAPA 1: EXTRAÇÃO
    # ============================================================
    print("\n" + "🔷" * 30)
    print("ETAPA 1: EXTRAÇÃO")
    print("🔷" * 30)
    
    df_usuarios = extrair_csv("usuarios.csv")
    
    if df_usuarios is None:
        print("\n❌ Falha na extração. Abortando pipeline.")
        return False
    
    # ============================================================
    # ETAPA 1.5: CATEGORIZAÇÃO
    # ============================================================
    print("\n" + "🔷" * 30)
    print("ETAPA 1.5: CATEGORIZAÇÃO POR DEPARTAMENTO")
    print("🔷" * 30)
    
    usuarios_categorizados = categorizar_usuarios(df_usuarios)
    
    if not usuarios_categorizados:
        print("\n❌ Falha na categorização. Abortando pipeline.")
        return False
    
    # ============================================================
    # ETAPA 2: TRANSFORMAÇÃO COM IA
    # ============================================================
    print("\n" + "🔷" * 30)
    print("ETAPA 2: TRANSFORMAÇÃO (COM GEMINI AI)")
    print("🔷" * 30)
    
    usuarios_transformados = transformar_usuarios(usuarios_categorizados)
    
    if not usuarios_transformados:
        print("\n❌ Falha na transformação. Abortando pipeline.")
        return False
    
    # ============================================================
    # ETAPA 3: CARREGAMENTO
    # ============================================================
    print("\n" + "🔷" * 30)
    print("ETAPA 3: CARREGAMENTO EM MARKDOWN")
    print("🔷" * 30)
    
    sucesso = carregar_em_markdown(usuarios_transformados)
    
    if not sucesso:
        print("\n❌ Falha no carregamento. Pipeline abortada.")
        return False
    
    # ============================================================
    # FIM
    # ============================================================
    print("\n" + "=" * 60)
    print("✨ PIPELINE EXECUTADA COM SUCESSO! ✨")
    print("=" * 60)
    print("\nTodos os resumos foram salvos em resumos_markdown/")
    print("Abra qualquer arquivo .md pra ver a mágica acontecer! 🎉\n")
    
    return True


if __name__ == "__main__":
    try:
        # Validar se a chave de API está configurada
        if not os.getenv("GEMINI_API_KEY"):
            print("❌ ERRO: Falta a variável GEMINI_API_KEY")
            print("Adicione ela no arquivo .env")
            sys.exit(1)
        
        sucesso = main()
        
        if not sucesso:
            sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline interrompida pelo usuário!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro não esperado: {e}")
        sys.exit(1)
