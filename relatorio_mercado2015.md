# Relatório: Organizações mais citadas na categoria Mercado (1º tri 2015)
_Gerado em: 2025-07-02 16:13_

## Metodologia
- Carregamento dos dados de data/articles.csv
- Filtragem das notícias da categoria 'Mercado' publicadas entre 01/01/2015 e 31/03/2015
- Extração de entidades nomeadas usando o modelo 'monilouise/ner_pt_br' em batches e filtragem de tokens irrelevantes
- Contagem e ranking das organizações (ORG) mais citadas
- Geração de gráfico de barras e nuvem de palavras

## Top 10 organizações:
- Folha: 466
- Brasil: 115
- Sete: 90
- Brad: 83
- Google: 67
- Moody ': 63
- S &: 53
- Volks: 49
- Investimentos: 48
- Vale: 46

## Observações:
- Limitações: possíveis erros de OCR, textos muito curtos ou entidades não reconhecidas.
- Logs de erro podem ser encontrados em errors_ner.log.
- Sugestão: analisar outros períodos ou tipos de entidades.
