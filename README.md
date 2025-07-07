# Sentiment Analysis com BERT

Este projeto é uma aplicação web simples para análise de sentimentos utilizando o modelo BERT, integrando uma API externa da IBM para processamento de linguagem natural.

## Funcionalidades

- Interface web para entrada de texto e exibição do resultado da análise de sentimento.
- Backend em Flask que recebe o texto, consulta a API de análise de sentimentos e retorna o resultado.
- Testes automatizados para garantir o correto funcionamento da análise.

## Estrutura do Projeto

```
Sentiment-Analysis/
├── SentimentAnalysis/
│   └── sentiment_analysis.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_sentiment_analysis.py
├── README.md
```

## Como Executar

1. **Instale as dependências:**
   - Python 3.x
   - Flask
   - requests

   Você pode instalar as dependências com:
   ```sh
   pip install flask requests
   ```

2. **Inicie o servidor Flask:**
   ```sh
   python server.py
   ```

3. **Acesse a aplicação:**
   Abra o navegador e acesse [http://localhost:5000](http://localhost:5000).

4. **Utilize a interface:**
   - Digite um texto no campo indicado e clique em "Run Sentiment Analysis".
   - O resultado será exibido na tela.

## Testes

Para rodar os testes automatizados:
```sh
python test_sentiment_analysis.py
```

## Observações

- A análise de sentimento é feita via API externa da IBM, portanto é necessário acesso à internet.
- O resultado exibido indica se o texto é positivo, negativo ou neutro, junto com um score de confiança.
