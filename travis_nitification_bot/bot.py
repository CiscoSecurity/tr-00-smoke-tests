import json
import os

from flask import Flask, request
from webexteamssdk import WebexTeamsAPI

MESSAGE_TEMPLATE = 'BUILD: {build_url}\nREPOSITORY: {repo}\n' \
                   'STARTED_AT: {start_time}\nFINISHED_AT: {finish_time}\n' \
                   'STATUS: {status}'

app = Flask(__name__)

api = WebexTeamsAPI()


@app.route('/', methods=['GET'])
def get_status():
    return 'OK'


@app.route('/', methods=['POST'])
def travis_webhook():
    data = data_mapping(json.loads(request.form['payload']))
    api.messages.create(os.environ.get('ROOM_ID'), text=data)
    return 'OK'


def data_mapping(data):
    if data:
        return MESSAGE_TEMPLATE.format(
            build_url=data.get('build_url'),
            repo=data.get('compare_url'),
            start_time=data.get('started_at'),
            finish_time=data.get('finished_at'),
            status=data.get('state')
        )


@app.before_request
def before():
    app.logger.error(request.form)


if __name__ == '__main__':
    app.run()
