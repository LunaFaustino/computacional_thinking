import requests

def translate_text_libretranslate(text, target_language="pt"):
    url = "https://libretranslate.de/translate"
    params = {
        "q": text,
        "source":"en",
        "target": target_language,
        "format": "text"
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        translated_text = response.json()["translatedtext"]
        return translated_text
    else:
        return f"Erro na tradução: {response.status_code}"

def get_piada():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        piada = response.json()["value"]
        return piada
    else:
        return f"Erro na piada: {response.status_code}"

piada_ingles = get_piada()
piada_port = translate_text_libretranslate(piada_ingles)

print("Piada em inglês:", piada_ingles)
print("Piada em potuguês:", piada_port)