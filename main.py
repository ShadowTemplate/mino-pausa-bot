import json
import logging as log
import mino_pausa_bot
import secrets
import telegram
import webapp2

from telegram import Update


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(mino_pausa_bot.get_status())


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        url = self.request.get('url')
        if url:
            mino_pausa_bot = telegram.Bot(token=secrets.mino_pausa_bot_token)
            if mino_pausa_bot.setWebhook(url):
                self.response.write("Webhook set to: " + url)
        self.response.write("Error while setting webhook.")


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        update_body = self.request.body
        log.info(update_body)
        mino_pausa_bot.handle_update(Update.de_json(json.loads(update_body)))
        self.response.write("Message processed.")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler)
], debug=True)
