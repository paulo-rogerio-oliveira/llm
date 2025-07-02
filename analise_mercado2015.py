# -*- coding: latin-1 -*-
import os
import sys
import logging
from datetime import datetime
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from collections import Counter
from wordcloud import WordCloud

# Configura��es gerais
CSV_PATH = Path('data/articles.csv')
REPORT_PATH = Path('relatorio_mercado2015.md')
FIG_PATH = Path('ranking_organizacoes_mercado2015.png')
WC_PATH = Path('nuvem_palavras_organizacoes.png')
ERROR_LOG = Path('errors_ner.log')
BATCH_SIZE = 16
BAR_COLOR = 'royalblue'  # voc� pode alterar
MIN_TOKEN_LENGTH = 3  # comprimento m�nimo para considerar um token como organiza��o
STOPWORDS = {'o', 'a', 'os', 'as', 'e', 'de', 'da', 'do'}  # palavras a ignorar

# Configura logger
logging.basicConfig(
    filename=ERROR_LOG,
    filemode='w',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 1. Carregamento dos dados
def carregar_dados(csv_path=CSV_PATH):
    if not csv_path.exists():
        print(f"Arquivo n�o encontrado: {csv_path}")
        sys.exit(1)
    print('Lendo os dados...')
    df = pd.read_csv(
        csv_path,
        usecols=['date', 'category', 'text'],
        parse_dates=['date'],
        encoding='latin1'
    )
    # padroniza nome das colunas para uso interno
    df.rename(columns={
        'date': 'date',
        'Category': 'category',
        'text': 'content'
    }, inplace=True)
    # padroniza categoria em lowercase para filtragem
    df['category_lc'] = df['category'].str.lower()
    return df

# 2. Filtragem por per�odo e categoria
def filtrar_mercado(df, inicio='2015-01-01', fim='2015-03-31'):
    inicio, fim = pd.Timestamp(inicio), pd.Timestamp(fim)
    df_mercado = df[
        (df['category_lc'] == 'mercado') &
        (df['date'] >= inicio) &
        (df['date'] <= fim)
    ].copy()
    print(f"Total de not�cias na categoria Mercado no 1� tri de 2015: {len(df_mercado)}")
    return df_mercado

# 3. Inicializa��o do NER (modelos carregados uma �nica vez)
print('Carregando modelo NER...')
tokenizer = AutoTokenizer.from_pretrained('monilouise/ner_pt_br')
model = AutoModelForTokenClassification.from_pretrained('monilouise/ner_pt_br')
ner_pipeline = pipeline(
    'ner',
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy='simple',
    device=0  # use GPU se dispon�vel
)

# 4. Extra��o de entidades em batches com filtros de tokens
def extrair_entidades(df_mercado, batch_size=BATCH_SIZE):
    print('Extraindo entidades...')
    org_counter = Counter()
    texts = df_mercado['content'].astype(str).tolist()
    for i in tqdm(range(0, len(texts), batch_size), desc='Batches NER'):
        batch = texts[i:i + batch_size]
        try:
            entities_batch = ner_pipeline(batch)
            flat = [ent for sub in entities_batch for ent in sub] if isinstance(entities_batch[0], list) else entities_batch
            for ent in flat:
                if ent['entity_group'] == 'ORG':
                    name = ent['word'].strip()
                    if name.startswith('##') or len(name) < MIN_TOKEN_LENGTH or name.lower() in STOPWORDS:
                        continue
                    org_counter[name] += 1
        except Exception as e:
            logging.error(f'Batch come�ando em {i}: {e}')
    return org_counter

# 5. Ranking das organiza��es mais citadas
def mostrar_ranking(org_counter, topn=10):
    top_orgs = org_counter.most_common(topn)
    print(f"\nTop {topn} organiza��es mais citadas na categoria Mercado (1� tri 2015):")
    for org, count in top_orgs:
        print(f"{org}: {count}")
    return top_orgs

# 6. Visualiza��o: gr�fico de barras e nuvem de palavras
def plotar_visualizacoes(org_counter, top_orgs, bar_path=FIG_PATH, wc_path=WC_PATH, color=BAR_COLOR):
    # Gr�fico de barras
    org_names, org_counts = zip(*top_orgs)
    plt.figure(figsize=(10, 6))
    plt.barh(org_names[::-1], org_counts[::-1], color=color)
    plt.xlabel('N�mero de cita��es')
    plt.title('Top 10 organiza��es mais citadas na categoria Mercado (1� tri 2015)')
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()
    print(f'Gr�fico de barras salvo em {bar_path}')
    
    # Nuvem de palavras (usa todas as organiza��es)
    print('Gerando nuvem de palavras...')
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate_from_frequencies(org_counter)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(wc_path)
    plt.close()
    print(f'Nuvem de palavras salva em {wc_path}')

# 7. Relat�rio resumido
def salvar_relatorio(top_orgs, report_path=REPORT_PATH):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Relat�rio: Organiza��es mais citadas na categoria Mercado (1� tri 2015)\n")
        f.write(f"_Gerado em: {now}_\n\n")
        f.write("## Metodologia\n")
        f.write("- Carregamento dos dados de data/articles.csv\n")
        f.write("- Filtragem das not�cias da categoria 'Mercado' publicadas entre 01/01/2015 e 31/03/2015\n")
        f.write("- Extra��o de entidades nomeadas usando o modelo 'monilouise/ner_pt_br' em batches e filtragem de tokens irrelevantes\n")
        f.write("- Contagem e ranking das organiza��es (ORG) mais citadas\n")
        f.write("- Gera��o de gr�fico de barras e nuvem de palavras\n\n")
        f.write("## Top 10 organiza��es:\n")
        for org, count in top_orgs:
            f.write(f"- {org}: {count}\n")
        f.write("\n## Observa��es:\n")
        f.write("- Limita��es: poss�veis erros de OCR, textos muito curtos ou entidades n�o reconhecidas.\n")
        f.write("- Logs de erro podem ser encontrados em errors_ner.log.\n")
        f.write("- Sugest�o: analisar outros per�odos ou tipos de entidades.\n")
    print(f'Relat�rio salvo em {report_path}')

if __name__ == '__main__':
    df = carregar_dados()
    df_mercado = filtrar_mercado(df)
    org_counter = extrair_entidades(df_mercado)
    top_orgs = mostrar_ranking(org_counter)
    plotar_visualizacoes(org_counter, top_orgs)
    salvar_relatorio(top_orgs)
