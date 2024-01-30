# index.py
import requests
from urllib import parse
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # Choose the appropriate handler based on the presence of 'country' or 'capital'
        if 'country' in dic:
            response = requests.get(f'https://restcountries.com/v3.1/name/{dic["country"]}?fields=name,capital')
        elif 'capital' in dic:
            response = requests.get(f'https://restcountries.com/v3.1/capital/{dic["capital"]}?fields=name,capital')
        else:
            response = {
                'statusCode': 400,
                'body': 'Invalid query parameters'
            }

        self.send_response(response['statusCode'])
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response['body'].encode('utf-8'))
        return


