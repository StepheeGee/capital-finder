import requests
from urllib import parse
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        try:
            if 'country' in dic:
                response = requests.get(f'https://restcountries.com/v3.1/name/{dic["country"]}?fields=name,capital')
                response.raise_for_status()  # Raise HTTPError for bad responses
                country_list = response.json()
                country_obj = country_list[0]
                capital = country_obj['capital'][0]
                message = f'The capital of {country_obj["name"]["common"]} is {capital}'
            elif 'capital' in dic:
                response = requests.get(f'https://restcountries.com/v3.1/capital/{dic["capital"]}?fields=name,capital')
                response.raise_for_status()
                capital_list = response.json()
                capital_obj = capital_list[0]
                country = capital_obj['name']['common']
                message = f'{dic["capital"]} is the capital of {country}'
            else:
                message = 'Invalid query parameters'
                response = {
                    'statusCode': 400,
                    'body': 'Invalid query parameters'
                }
        except requests.exceptions.RequestException as e:
            message = 'Error making API request'
            response = {
                'statusCode': 500,
                'body': f'Internal Server Error: {str(e)}'
            }
        
        self.send_response(response['statusCode'])
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return
