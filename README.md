# An�lise de Entidades em Not�cias do Mercado (1� Trimestre de 2015)

Este projeto realiza a extra��o e an�lise de entidades nomeadas (organiza��es) em not�cias da se��o/categoria "Mercado" publicadas no primeiro trimestre de 2015, utilizando o modelo de NER em portugu�s `monilouise/ner_pt_br` da HuggingFace.

## Objetivo
- Identificar e ranquear as organiza��es mais citadas nas not�cias da categoria "Mercado".
- Gerar visualiza��es (gr�fico de barras e nuvem de palavras) e um relat�rio detalhado da an�lise.

## Estrutura dos Dados
O arquivo de entrada deve estar em `data/articles.csv` e conter pelo menos as colunas:
- `date`: data da not�cia
- `category`: categoria/se��o da not�cia (ex: "Mercado")
- `text`: conte�do/texto da not�cia

## Instala��o
1. Clone o reposit�rio:
   ```bash
   git clone <url-do-repo>
   cd <nome-da-pasta>
   ```
2. Instale as depend�ncias:
   ```bash
   pip install -r requirements.txt
   ```

## Execu��o
Execute o script principal:
```bash
python analise_mercado2015.py
```

O script ir�:
- Ler e filtrar as not�cias da categoria "Mercado" do 1� trimestre de 2015
- Extrair entidades do tipo organiza��o usando o modelo `monilouise/ner_pt_br`
- Gerar um ranking das organiza��es mais citadas
- Salvar um gr�fico de barras (`ranking_organizacoes_mercado2015.png`)
- Salvar uma nuvem de palavras (`nuvem_palavras_organizacoes.png`)
- Gerar um relat�rio detalhado em `relatorio_mercado2015.md`
- Registrar eventuais erros de processamento em `errors_ner.log`

## Exemplo de Sa�da
```
Top 10 organiza��es mais citadas na categoria Mercado (1� tri 2015):
Empresa X: 42
Empresa Y: 37
...
```
Veja os arquivos de sa�da na raiz do projeto ap�s a execu��o.

## Observa��es
- O processamento pode ser demorado dependendo do tamanho do arquivo e do hardware.
- O modelo NER � carregado automaticamente da HuggingFace.
- Logs de erros de processamento ficam em `errors_ner.log`.

## Licen�a
Este projeto � apenas para fins educacionais e de demonstra��o. 