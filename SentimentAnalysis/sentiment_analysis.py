import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL do serviço de análise de sentimentos
    myobj = {"raw_document":{"text" : text_to_analyse} }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Define os cabeçalhos necessários para a requisição da API
    response = requests.post(url,json = myobj, headers=header)

    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        # Se o código de status da resposta for 500, defina label e score como None
    elif response.status_code == 500:
        label = None
        score = None

    return {'label':label, 'score':score}
