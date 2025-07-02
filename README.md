# An�lise de Entidades em Not�cias do Mercado (1� Trimestre de 2015)

Reposit�rio: [https://github.com/paulo-rogerio-oliveira/llm.git](https://github.com/paulo-rogerio-oliveira/llm.git)

Este projeto re�ne duas aplica��es principais para an�lise de textos jornal�sticos da se��o "Mercado":

- **Principal:** `app.py` ? Aplica��o Streamlit para sumariza��o de textos usando LLMs (HuggingFace ou OpenAI)
- **Secund�rio:** `analise_mercado2015.py` ? Script para an�lise de entidades nomeadas (organiza��es) nas not�cias do 1� trimestre de 2015

---

## 1. Aplica��o Principal: `app.py` (Sumarizador com LLM)

Interface web interativa para:
- Inserir textos de artigos/not�cias
- Gerar resumos autom�ticos usando modelos LLM (via HuggingFace ou OpenAI)

### Como executar

1. Instale as depend�ncias:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o app:
   ```bash
   streamlit run app.py
   ```
3. Siga as instru��es na interface para inserir o texto e o token HuggingFace (ou chave OpenAI, se aplic�vel).

---

## 2. Script Secund�rio: `analise_mercado2015.py` (An�lise de Entidades)

Script para:
- Baixar a base de dados em https://www.kaggle.com/datasets/marlesson/news-of-the-site-folhauol
- Ler o arquivo `data/articles.csv`
- Filtrar not�cias da se��o "Mercado" do 1� trimestre de 2015
- Extrair entidades do tipo organiza��o usando o modelo `monilouise/ner_pt_br`
- Gerar ranking, gr�fico e relat�rio das organiza��es mais citadas

### Como executar

1. Instale as depend�ncias (se ainda n�o instalou):
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script:
   ```bash
   python analise_mercado2015.py
   ```
3. Os resultados ser�o salvos como:
   - `ranking_organizacoes_mercado2015.png` (gr�fico)
   - `relatorio_mercado2015.txt` (relat�rio)

---

## Estrutura dos Dados
O arquivo de entrada deve estar em `data/articles.csv` e conter pelo menos as colunas:
- `date`: data da not�cia
- `section`: categoria/se��o da not�cia (ex: "Mercado")
- `content`: conte�do/texto da not�cia

---

## Observa��es
- O processamento pode ser demorado dependendo do tamanho do arquivo e do hardware.
- O modelo NER � carregado automaticamente da HuggingFace.
- O arquivo `data/articles.csv` est� no `.gitignore` e n�o � versionado.

---

## Reposit�rio
[https://github.com/paulo-rogerio-oliveira/llm.git](https://github.com/paulo-rogerio-oliveira/llm.git)

---

## Licen�a
Este projeto � apenas para fins educacionais e de demonstra��o. 