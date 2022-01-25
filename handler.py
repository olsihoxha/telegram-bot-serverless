import json
from turtle import update
import telegram
import os

from configs.constants import configure_telegram, logger, OK_RESPONSE, ERROR_RESPONSE




def webhook(event, context):
    bot = configure_telegram()
    logger.info()

    logger.info('Event: {}'.format(event))

    if event.get('httpMethod') == 'POST' and event.get('body'): 
        logger.info('Message received')
        update = telegram.Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat.id
        text = update.message.text

        if text == '/start':
            # YOU CAN USE SOME EXTERNAL API TO PROCESS THE MESSAGE OR MAKE YOUR OWN BOT TO REPLY
            text = """Hello there! I am a bot, built with Python and the Serverless Framework. """
        
        bot.sendMessage(chat_id=chat_id, text=text)
        logger.info('Message sent')

        return OK_RESPONSE
    return ERROR_RESPONSE


def set_webhook(event, context):
   
    logger.info('Event: {}'.format(event))
    bot = configure_telegram()
    url = 'https://{}/{}/'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage'),
    )
    webhook = bot.set_webhook(url)

    if webhook:
        return OK_RESPONSE

    return ERROR_RESPONSE



