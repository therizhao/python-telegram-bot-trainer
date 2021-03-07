#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import threading

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

player1 = ''
player2 = ''

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('''Hello! Welcome to the scissors paper stone game! You are player 1. 

What command do you want to choose? 
/scissors /paper /stone''')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def evaluate(update: Update):
    global player1
    global player2

    # If both players have input
    if player1 != '' and player2 != '':
        # evaluate result
        # both use same thing -> draw

        # Command to matrix index
        cmds = {
            'paper': 0,
            'scissors': 1,
            'stone': 2
        }
        # 1st index (i.e. row index): Player 2
        # 2nd index (i.e. col index): Player 1
        matrix = [
             # P      ,  Sc   , St
            [ 'draw', 'p1', 'p2'], # P
            [ 'p2', 'draw', 'p1'],  # Sc
            [ 'p1', 'p2', 'draw' ] # St
        ]

        # Translate string command to integer
        player1Int = cmds[player1]
        player2Int = cmds[player2]

        result = matrix[player2Int][player1Int] # p1 | p2 | draw
        pretty_output = {
            "p1": "Player 1 wins. 🎉",
            "p2": "Player 2 wins. 🎉",
            "draw": "Draw"
        }
        update.message.reply_text(pretty_output[result])
        update.message.reply_text('''Do you want to play again?
If yes, click /start''')
        
        # clear input
        player1 = ''
        player2 = ''

def handle_cmd(update: Update, cmd: str) -> None:
    global player1
    global player2
    # If it's player1
    if player1 == '':
        player1 = cmd
        update.message.reply_text("Ok! Player1 chose " + cmd + ".")
        update.message.reply_text('''Hello Player2. What command do you want to choose?
/scissors /paper /stone''')
    else:
        # If it's player 2
        player2 = cmd
        update.message.reply_text("Ok! Player2 chose " + cmd + ".")
        update.message.reply_text("Evaluating result...")
    
    evaluate(update)


def scissors(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /scissors is issued."""
    handle_cmd(update, "scissors")

def stone(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /stone is issued."""
    handle_cmd(update, "stone")

def paper(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /paper is issued."""
    handle_cmd(update, "paper")


def send_100_times(update: Update, message):
    for i in range(100):
        update.message.reply_text(message)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    x = threading.Thread(target=send_100_times, args=(update, update.message.text))
    x.start()

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1641071131:AAFmHdiogXRMrlq104PeP40mB78Av-rP63U")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher


    '''

    mcdonalds
    cashier

    1. give a set of instructions to cashier
    2. if someone say mcchicken -> go make mcchicken -> give mcchicken -> collect $2

    cashier (brain))
    '''
    # on different commands - answer in Telegram
    '''
    /start

    '''
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Scissors paper game
    # use scissors /scissors
    dispatcher.add_handler(CommandHandler("scissors", scissors))
    # use paper /paper
    dispatcher.add_handler(CommandHandler("paper", paper))
    
    dispatcher.add_handler(CommandHandler("stone", stone))


    # on noncommand i.e message - echo the message on Telegram


    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()