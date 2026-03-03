# 🚀 ETL-CURSO-ENGENHARIA-DE-DADOS-DIO

Uma pipeline **super massa** de ETL (Extract, Transform, Load) que usa **Gemini AI** pra gerar resumos criativos sobre usuários!

## O que é isso?

Basicamente você tem:
- **45 usuários** diferentes com info de verdade
- **Gemini AI** gera um resumo descontraído de cada um
- Salva tudo em **Markdown** bonito pra ler

Tipo assim:
```
Extração → Categorização → Transformação com IA → Carregamento em Markdown
```

## 📋 Estrutura do Projeto

```
ETL-CURSO-ENGENHARIA-DE-DADOS-DIO/
├── src/
│   ├── iniciador.py          # 🎬 COMEÇA TUDO AQUI!
│   ├── extracao.py           # Lê o CSV e categoriza usuários
│   ├── transformacao.py      # Usa Gemini pra gerar resumos
│   ├── carregamento.py       # Salva em Markdown
│   └── __pycache__/          # (ignorar abacaxi)
├── dados/
│   └── usuarios.csv          # 45 usuários pra processar
├── resumos_markdown/         # Saída com os .md gerados
├── requirements.txt          # Dependências Python
├── .env                      # Chaves de API (⚠️ não versione!)
├── .gitignore               # Arquivos ignorados no git
└── README.md                # Você tá lendo isso
```

## ⚙️ Como Configurar (Passo a Passo)

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/novasentinel-tech/ETL-CURSO-ENGENHARIA-DE-DADOS-DIO.git
cd ETL-CURSO-ENGENHARIA-DE-DADOS-DIO
```

### 2️⃣ Criar um Ambiente Virtual

**No Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**No macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Depois de ativar, seu terminal deve mostrar `(.venv)` no começo da linha.

### 3️⃣ Instalar as Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Configurar a Chave de API do Gemini

1. Vá para [Google AI Studio](https://aistudio.google.com/apikey)
2. Clique em **"Create API Key"**
3. Copie a chave gerada
4. Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui_sem_aspas
```

**⚠️ IMPORTANTE:**
- Nunca faça commit do `.env` (tá no `.gitignore`)
- Não compartilhe sua chave de forma pública
- Se vazar, desative a chave no Google AI Studio

### 5️⃣ Verificar Estrutura

Certifique-se que tem:

```bash
ls dados/usuarios.csv        # Deve existir
ls src/iniciador.py          # Deve existir
cat .env                      # Deve ter GEMINI_API_KEY
```

## 🎯 Usando a Pipeline

### Rodar Tudo de Uma Vez

```bash
cd src
python iniciador.py
```

Ele vai:
1. ✅ Extrair usuários do CSV
2. ✅ Categorizar por departamento
3. ✅ Processar com Gemini (pode levar uns minutos)
4. ✅ Gerar arquivos Markdown na pasta `resumos_markdown/`

### Verificar os Resultados

```bash
ls resumos_markdown/        # Ver todos os arquivos
cat resumos_markdown/Leanne_Graham.md   # Ver um resumo
```

## 🔍 Entendendo o Código

### `iniciador.py` - O Maestro

```python
# Ele chama os 3 em sequência:
df = extrair_csv("usuarios.csv")              # Extrai
categorizados = categorizar_usuarios(df)      # Categoriza
transformados = transformar_usuarios(categorizados)  # IA
carregar_em_markdown(transformados)           # Salva
```

### `extracao.py` - Lê e Organiza

```python
# Lê o CSV e retorna um DataFrame
df = extrair_csv("usuarios.csv")

# Separa por departamento
usuarios_categorizados = categorizar_usuarios(df)
```

### `transformacao.py` - Gemini Fazendo Magia

```python
# Manda cada usuário pro Gemini
# A IA gera um resumo descontraído
resumo = gerar_resumo_com_gemini(usuario)
```

### `carregamento.py` - Salva em Markdown

```python
# Pega os resumos e cria arquivos .md
carregar_em_markdown(usuarios_transformados)
```

## 📊 O Arquivo de Saída

Cada resumo fica assim:

```markdown
# Leanne Graham

## 📋 Informações Básicas
- **Email**: Sincere@april.biz
- **Cidade**: Gwenborough
- **Empresa**: Romaguera-Crona
- **Cargo**: Software Engineer
- **Idade**: 28 anos
- **Departamento**: Engineering

## 📞 Contato
- **Telefone**: (111) 555-0100
- **Website**: romaguera.info

## 🤖 Resumo Gerado por IA

[Resumo criativo gerado pelo Gemini aqui...]

---

*Gerado automaticamente pela pipeline ETL com Gemini AI*
```

## 🐛 Resolvendo Problemas

### Erro: "ModuleNotFoundError: No module named 'google'"

```bash
pip install google-generativeai
```

### Erro: "GEMINI_API_KEY not found"

- Verifica se criou o arquivo `.env`
- Verifica se tá escrito certinho a chave
- Tira espaços extras

### Erro: "Failed to connect to API"

- Verifica sua conexão de internet
- Tenta novamente (às vezes é problema temporário)
- Verifica se a chave ancora expira

### A Pipeline tá lenta?

É normal! Gemini tá processando cada usuário. Com 45 usuários leva uns 5-10 minutos dependendo da velocidade da internet.

## 🚀 Expandindo o Projeto

### Adicionar Mais Usuários

1. Edita `dados/usuarios.csv`
2. Adiciona linhas novas mantendo o formato
3. Roda `python iniciador.py` de novo

### Mudar o Prompt da IA

Edita a função `gerar_resumo_com_gemini()` em `transformacao.py`:

```python
prompt = f"""
Seu novo prompt aqui...
"""
```

### Usar GPT ao invés de Gemini

Seria fácil, mas pediu o Gemini então tá assim mesmo. Se quiser mudar, seria uma outra etapa.

## 📝 Variáveis de Ambiente

O arquivo `.env` pode ter essas variáveis:

```env
# OBRIGATÓRIO
GEMINI_API_KEY=sua_chave_aqui

# OPCIONAL (futuros)
LOG_LEVEL=INFO
OUTPUT_FORMAT=markdown
```

## 🤝 Contribuindo

Se quer melhorar:

1. Faz um fork
2. Cria uma branch (`git checkout -b feature/melhoria`)
3. Faz commit das mudanças
4. Manda um Pull Request

## 📜 Licença

Tá em `LICENSE`. Tipo MIT, pode usar à vontade.

## 🎓 Aprendizado

Esse projeto foi feito pra aprender:

- ✅ Pipeline de dados
- ✅ Integração com IA
- ✅ Python com Pandas
- ✅ Variáveis de ambiente
- ✅ Organização de código
- ✅ Git e GitHub
- ✅ Markdown

## 👨‍💻 Sobre

Feito com ☕ e criatividade por alunos do **DIO - Engenharia de Dados**.

---

**Got stuck?** Manda chamar a galera ou abre uma issue! 🚀

**Última atualização**: Março 2026

