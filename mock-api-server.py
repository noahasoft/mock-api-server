import os

from flask import Flask
import toml


app = Flask(__name__)

CONFIG_DIR = '/etc/mock-api-server'


def get_body(response):
    if 'body' in response:
        return response['body']
    elif 'body_filename' in response:
        filename = os.path.join(CONFIG_DIR, response['body_filename'])
        with open(filename) as f:
            return f.read()
    else:
        return ''


def add_endpoint(name, request, response):

    def handler():
        resp = get_body(response)
        status = response.get('status_code', 200)
        headers = response.get('headers', {})
        return (resp, status, headers)

    app.add_url_rule(
        rule=request['path'],
        endpoint=name,
        view_func=handler,
        methods=(request['method'], ),
    )


config = toml.load(os.path.join(CONFIG_DIR, 'config.toml'))
for endpoint in config['endpoint']:
    add_endpoint(endpoint['name'], endpoint['request'], endpoint['response'])
