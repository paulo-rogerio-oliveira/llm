# Análise de Entidades em Notícias do Mercado (1º Trimestre de 2015)

Este projeto realiza a extração e análise de entidades nomeadas (organizações) em notícias da seção/categoria "Mercado" publicadas no primeiro trimestre de 2015, utilizando o modelo de NER em português `monilouise/ner_pt_br` da HuggingFace.

## Objetivo
- Identificar e ranquear as organizações mais citadas nas notícias da categoria "Mercado".
- Gerar visualizações (gráfico de barras e nuvem de palavras) e um relatório detalhado da análise.

## Estrutura dos Dados
O arquivo de entrada deve estar em `data/articles.csv` e conter pelo menos as colunas:
- `date`: data da notícia
- `category`: categoria/seção da notícia (ex: "Mercado")
- `text`: conteúdo/texto da notícia

## Instalação
1. Clone o repositório:
   ```bash
   git clone <url-do-repo>
   cd <nome-da-pasta>
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução
Execute o script principal:
```bash
python analise_mercado2015.py
```

O script irá:
- Ler e filtrar as notícias da categoria "Mercado" do 1º trimestre de 2015
- Extrair entidades do tipo organização usando o modelo `monilouise/ner_pt_br`
- Gerar um ranking das organizações mais citadas
- Salvar um gráfico de barras (`ranking_organizacoes_mercado2015.png`)
- Salvar uma nuvem de palavras (`nuvem_palavras_organizacoes.png`)
- Gerar um relatório detalhado em `relatorio_mercado2015.md`
- Registrar eventuais erros de processamento em `errors_ner.log`

## Exemplo de Saída
```
Top 10 organizações mais citadas na categoria Mercado (1º tri 2015):
Empresa X: 42
Empresa Y: 37
...
```
Veja os arquivos de saída na raiz do projeto após a execução.

## Observações
- O processamento pode ser demorado dependendo do tamanho do arquivo e do hardware.
- O modelo NER é carregado automaticamente da HuggingFace.
- Logs de erros de processamento ficam em `errors_ner.log`.

## Licença
Este projeto é apenas para fins educacionais e de demonstração. 