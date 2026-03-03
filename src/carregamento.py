from pathlib import Path


def carregar_em_markdown(usuarios_transformados: dict, pasta_destino: str = "resumos_markdown") -> bool:
    """
    Salva os resumos em arquivos Markdown
    Cada usuário vira um arquivo .md na pasta de destino
    """
    print(f"\n📝 Carregando dados em Markdown ({pasta_destino})...")
    
    caminho_saida = Path(pasta_destino)
    caminho_saida.mkdir(exist_ok=True)
    
    total_arquivos = 0
    
    try:
        for departamento, usuarios in usuarios_transformados.items():
            for usuario_data in usuarios:
                usuario = usuario_data["usuario_original"]
                nome = usuario.get("nome", "Desconhecido").replace(" ", "_")
                resumo = usuario_data["resumo_ia"]
                
                # Criar conteúdo do markdown
                conteudo_md = f"""# {usuario.get("nome")}

## 📋 Informações Básicas
- **Email**: {usuario.get("email")}
- **Cidade**: {usuario.get("cidade")}
- **Empresa**: {usuario.get("empresa")}
- **Cargo**: {usuario.get("cargo")}
- **Idade**: {usuario.get("idade")} anos
- **Departamento**: {departamento}

## 📞 Contato
- **Telefone**: {usuario.get("telefone")}
- **Website**: {usuario.get("website")}

## 🤖 Resumo Gerado por IA

{resumo}

---

*Gerado automaticamente pela pipeline ETL com Gemini AI*
"""
                
                # Salvar arquivo
                arquivo_saida = caminho_saida / f"{nome}.md"
                
                with open(arquivo_saida, "w", encoding="utf-8") as f:
                    f.write(conteudo_md)
                
                total_arquivos += 1
                print(f"  ✅ {arquivo_saida.name}")
        
        print(f"\n✨ Sucesso! {total_arquivos} arquivos Markdown salvos em {pasta_destino}/")
        return True
        
    except Exception as erro:
        print(f"❌ Erro ao salvar arquivos: {erro}")
        return False


if __name__ == "__main__":
    from extracao import extrair_csv, categorizar_usuarios
    from transformacao import transformar_usuarios
    
    df = extrair_csv("usuarios.csv")
    if df is not None:
        categorizados = categorizar_usuarios(df)
        transformados = transformar_usuarios(categorizados)
        carregar_em_markdown(transformados)