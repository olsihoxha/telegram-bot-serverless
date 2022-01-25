# Simple Telegram Bot with Serverless Framework

You need telegram account from which you have to get the telegram token and set it to the `serverless.yml` file.

# Installing 

```
# Install the Serverless Framework
$ npm install serverless -g

# Install the necessary plugins
$ npm install

# Create and active a Python 3.7 venv
$ python3.7 -m venv venv && souce venv/bin/activate

# Get a bot from Telegram
$ /newbot

# Put the token received into a file called serverless.env.yml, like this
$ cat serverless.env.yml
TELEGRAM_TOKEN: <your_token>

# Deploy it!
$ serverless deploy

# With the URL returned in the output, configure the Webhook
$ curl -X POST https://<your_url>.amazonaws.com/dev/set_webhook
```
