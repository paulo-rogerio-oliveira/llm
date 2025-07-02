# Análise de Entidades em Notícias do Mercado (1º Trimestre de 2015)

Repositório: [https://github.com/paulo-rogerio-oliveira/llm.git](https://github.com/paulo-rogerio-oliveira/llm.git)

Este projeto reúne duas aplicações principais para análise de textos jornalísticos da seção "Mercado":

- **Principal:** `app.py` ? Aplicação Streamlit para sumarização de textos usando LLMs (HuggingFace ou OpenAI)
- **Secundário:** `analise_mercado2015.py` ? Script para análise de entidades nomeadas (organizações) nas notícias do 1º trimestre de 2015

---

## 1. Aplicação Principal: `app.py` (Sumarizador com LLM)

Interface web interativa para:
- Inserir textos de artigos/notícias
- Gerar resumos automáticos usando modelos LLM (via HuggingFace ou OpenAI)

### Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o app:
   ```bash
   streamlit run app.py
   ```
3. Siga as instruções na interface para inserir o texto e o token HuggingFace (ou chave OpenAI, se aplicável).

---

## 2. Script Secundário: `analise_mercado2015.py` (Análise de Entidades)

Script para:
- Baixar a base de dados em https://www.kaggle.com/datasets/marlesson/news-of-the-site-folhauol
- Ler o arquivo `data/articles.csv`
- Filtrar notícias da seção "Mercado" do 1º trimestre de 2015
- Extrair entidades do tipo organização usando o modelo `monilouise/ner_pt_br`
- Gerar ranking, gráfico e relatório das organizações mais citadas

### Como executar

1. Instale as dependências (se ainda não instalou):
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script:
   ```bash
   python analise_mercado2015.py
   ```
3. Os resultados serão salvos como:
   - `ranking_organizacoes_mercado2015.png` (gráfico)
   - `relatorio_mercado2015.txt` (relatório)

---

## Estrutura dos Dados
O arquivo de entrada deve estar em `data/articles.csv` e conter pelo menos as colunas:
- `date`: data da notícia
- `section`: categoria/seção da notícia (ex: "Mercado")
- `content`: conteúdo/texto da notícia

---

## Observações
- O processamento pode ser demorado dependendo do tamanho do arquivo e do hardware.
- O modelo NER é carregado automaticamente da HuggingFace.
- O arquivo `data/articles.csv` está no `.gitignore` e não é versionado.

---

## Repositório
[https://github.com/paulo-rogerio-oliveira/llm.git](https://github.com/paulo-rogerio-oliveira/llm.git)

---

## Licença
Este projeto é apenas para fins educacionais e de demonstração. 