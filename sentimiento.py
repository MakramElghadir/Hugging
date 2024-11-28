import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I love cats",
    # hacer una interfaz de consola bonica, es decir mostrar la respuesta en lenguaje
    #natural, por ejemplo, el sentimiento es mayormente positivo o el sentimiento es mayormente
    #negativo

})

print(output)