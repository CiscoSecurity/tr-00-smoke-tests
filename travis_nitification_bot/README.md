# Travis notification bot

## Before deploy
* Please come to the Webex Teams page and register your bot account.
[Webex Teams Bot](https://developer.webex.com/docs/bots)
You must have bot API key for start using this bot.

* Create the bot chat room and find it's roomId, or use roomId of 
the existing room 
[Find room id](https://developer.webex.com/docs/api/v1/rooms/list-rooms)

* Add bot to your chat room

## How to deploy
* Go to the travis_notification_bot folder:

`cd travis_notofication_bot`
* Create a virtual environment named `venv`:

`python3 -m venv venv`

* Activate the virtual environment:
  - Linux/Mac: `source venv/bin/activate`
  - Windows: `venv\Scripts\activate.bat`
  
* Upgrade PIP (optional):

`pip install --upgrade pip`

* Install the libraries required for the application to function from
the `requirements.txt` file:

`pip install --upgrade --requirement requirements.txt`

* Deploy bot like lambda module:

`zappa deploy dev`

* Go to lambda on AWS UI and set the environment variables:

`ROOM_ID` - your room

`WEBEX_TEAMS_ACCESS_TOKEN` - bot API key

## How to connect bot to travis
Bot use travis webhooks. Just add such code in `.travis.yml`:

```
notifications:
  webhooks:
    urls:
      - https://euqsx55b02.execute-api.us-east-1.amazonaws.com/dev
    on_start:   always
```