# Mino Pausa Bot

A Telegram bot to receive tragic poems by the Italian poet Mino Pausa. This bot 
checks in real time all the messages exchanged in a group waiting for sad 
words to be triggered. It is designed to be deployed on 
[Google App Engine](https://cloud.google.com/appengine/).

Feel free to use the bot in your groups by adding [@MinoPausaBot](
https://telegram.me/minopausabot).

---
## Information

**Status**: `Actively maintained`

**Type**: `Personal project`

**Development year(s)**: `2016+`

**Authors**: [ShadowTemplate](https://github.com/ShadowTemplate)

---
## Getting Started

The bot can be already added to your group. However, you can customize it 
and redeploy it anywhere. Please create a *secrets.py* file and set this 
value:

```
mino_pausa_bot_token = "your_telegram_bot_token"
```

### Prerequisites

Clone the repository and install the required Python dependencies:

```
$ git clone https://github.com/ShadowTemplate/Mino-Pausa-Bot.git
$ cd Mino-Pausa-Bot/
$ pip install --user -r requirements.txt
```

### Deployment

This repository includes the required Google App Engine libraries. The project 
is thus ready to be deployed.


---
## Building tools

* [Python 2.7](https://www.python.org/downloads/release/python-270/) - 
Programming language
* [Google App Engine](https://cloud.google.com/appengine/) - Web framework
* [python-telegram-bot](https://python-telegram-bot.org/) - Telegram API 
wrapper 

---
## Contributing

Any contribution is welcome. Feel free to open issues or submit pull requests.

---
## License

This project is licensed under the GNU GPLv3 license.
Please refer to the [LICENSE.md](LICENSE.md) file for details.

---
*This README.md complies with [this project template](
https://github.com/ShadowTemplate/project-template). Feel free to adopt it
and reuse it.*
