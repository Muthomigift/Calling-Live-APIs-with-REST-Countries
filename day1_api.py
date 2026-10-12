import requests

url = "https://countriesnow.space/api/v0.1/countries"
body = {"country": "Kenya"}

response = requests.post(url + "/capital", json=body)
print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()["data"]

    name = data["name"]
    capital = data["capital"]
    population = requests.post(url + "/population", json=body).json()["data"]["populationCounts"][-1]["value"]
    currency = requests.post(url + "/currency", json=body).json()["data"]["currency"]

    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)