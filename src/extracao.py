import requests
import pandas as pd
import jsonfrom 
from pathlib import Path

def extrair_dados(url_api, salvar_json=False):
    print("Iniciando extração amigo...")

    try:
        resposta = requests.get(url_api, timeout=10)

        if resposta.status_code == 200:
            print("API respondeu 200 vezes, então foi bem sucedido")

            dados = resposta.json()

            df = pd.DataFrame(dados)

            print(f"Foram extraidos {len(df)} registros")

            if salvar_json:
                pasta = Path("dados")
                pasta.mkdir(exist_ok=True)

                with open(pasta / "resposta_exemplo.json", "w", encoding="utf-8") as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)
                    
                print()
