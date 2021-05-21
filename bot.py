#!/usr/bin/env python
import random
from datetime import datetime, timedelta

from check_mktcaps import do_check, do_check_crypto
from chuck_jokes import get_random_chuck_joke

from settings import TOKEN

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

last_check = datetime.now()
last_result = ""

last_check_crypto = datetime.now()
last_result_crypto = ""

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def top10(update, bot):
    # check top10 by market cap
    global  last_result, last_check
    now = datetime.now()
    if last_result == '' or (now - last_check) > timedelta(minutes=15):
        update.message.reply_text('Esperá que. Voy a ver qué dicen mis fuentes del INTERNET...')
        last_result = do_check()
        last_check = now

    update.message.reply_text("Here you go, *you're welcolme*\n```\n" + last_result + "```", parse_mode="Markdown")

def crypto(update, bot):
    # check top10 by market cap
    global  last_result_crypto, last_check_crypto
    now = datetime.now()
    if last_result_crypto == '' or (now - last_check_crypto) > timedelta(minutes=15):
        update.message.reply_text('Esperá que. Voy a ver qué dicen mis fuentes del INTERNET sobre el BITCOÑO...')
        last_result_crypto = do_check_crypto()
        last_check_crypto = now

    update.message.reply_text("Here you go, you're welcome:\n```\n" + last_result_crypto + "```", parse_mode="Markdown")


def answer_cacho(update, bot):
    update.message.reply_text("*RIGHT!*", parse_mode="Markdown")

def chuck_joke(update, bot):
    update.message.reply_text(get_random_chuck_joke())

POTRO_QUOTES = []
def potro(update, bot):
    global POTRO_QUOTES
    update.message.reply_text(random.choice(POTRO_QUOTES))

MATI_QUOTES = []
def mati(update, bot):
    global MATI_QUOTES
    update.message.reply_text(random.choice(MATI_QUOTES))

SHOULD_JAVIER_REPLY_ANSWERS = []
def should_javier_reply(update, bot):
    global SHOULD_JAVIER_REPLY_ANSWERS
    update.message.reply_text(random.choice(SHOULD_JAVIER_REPLY_ANSWERS))

def help(update, bot):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, bot):
    """Echo the user message."""
    print(update.effective_user)
    if not update.effective_user.is_bot and 'potro'.casefold() in update.message.text.casefold():
        if not update.message.text.startswith('/potro'):
            append_quote('potro', update.message.text)
    elif not update.effective_user.is_bot and 'mati'.casefold() in update.message.text.casefold():
        if not update.message.text.startswith('/mati'):
            append_quote('mati', update.message.text)
    print(f"Got message from {update.effective_user.username} --> [{update.message.text}]")


def error(update, bot, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("top10", top10))
    dp.add_handler(CommandHandler("crypto", crypto))
    dp.add_handler(CommandHandler("answer_caxo", answer_cacho))
    dp.add_handler(CommandHandler("chuck", chuck_joke))
    dp.add_handler(CommandHandler("potro", potro))
    dp.add_handler(CommandHandler("mati", mati))
    dp.add_handler(CommandHandler("should_javier_reply", should_javier_reply))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def append_quote(who, quote):
    global POTRO_QUOTES, MATI_QUOTES
    fname = None
    if who == 'potro':
        arr = POTRO_QUOTES
        fname = 'potro_quotes.txt'
    elif who == 'mati':
        arr = MATI_QUOTES
        fname = 'mati_quotes.txt'
    arr.append(quote)
    with open(fname, 'a') as f:
        f.write(quote + '\n')


def load_quote(fname):
    with open(fname) as f:
        return [x.strip() for x in f.readlines()]


def load_quotes():
    global POTRO_QUOTES, MATI_QUOTES, SHOULD_JAVIER_REPLY_ANSWERS
    POTRO_QUOTES = load_quote("data/potro_quotes.txt")
    MATI_QUOTES = load_quote("data/mati_quotes.txt")
    SHOULD_JAVIER_REPLY_ANSWERS = load_quote("data/should_javier_reply_answers.txt")

if __name__ == '__main__':
    load_quotes()
    main()
