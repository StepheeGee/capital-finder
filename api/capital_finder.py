# capital_finder.py
import requests

def capital_finder(request):
    query_params = request.get('query', {})

    if 'country' in query_params:
        country = query_params['country']
        capital = get_capital_by_country(country)
        if capital:
            return {
                'statusCode': 200,
                'body': f'The capital of {country} is {capital}'
            }
        else:
            return {
                'statusCode': 404,
                'body': f'Capital not found for {country}'
            }
    elif 'capital' in query_params:
        capital = query_params['capital']
        country = get_country_by_capital(capital)
        if country:
            return {
                'statusCode': 200,
                'body': f'{capital} is the capital of {country}'
            }
        else:
            return {
                'statusCode': 404,
                'body': f'Country not found for {capital}'
            }
    else:
        return {
            'statusCode': 400,
            'body': 'Invalid query parameters'
        }

def get_capital_by_country(country):
    url = f'https://restcountries.com/v3.1/name/{country}?fields=name,capital'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data:
        capital = data[0]['capital'][0]
        return capital
    else:
        return None

def get_country_by_capital(capital):
    url = f'https://restcountries.com/v3.1/capital/{capital}?fields=name,capital'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data:
        country = data[0]['name']['common']
        return country
    else:
        return None
