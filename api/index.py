# index.py
from urllib import parse
from http.server import BaseHTTPRequestHandler
from capital_finder import country_to_capital_handler, capital_to_country_handler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # Choose the appropriate handler based on the presence of 'country' or 'capital'
        if 'country' in dic:
            response = country_to_capital_handler({'query': dic})
        elif 'capital' in dic:
            response = capital_to_country_handler({'query': dic})
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
