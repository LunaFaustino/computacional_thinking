import requests

url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

querystring = {"prefix":"spaghetti"}

headers = {
	"X-RapidAPI-Key": "ea262b61c3msh5f9d62d6beadb81p1efeb9jsne5e93e8bdc7a",
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

