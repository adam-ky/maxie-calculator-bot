import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from calculator import Calculator

DEL = '\u232B'
MULT = '\u00D7'
DIV = '\u00F7'

c = Calculator()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update, context):
    keyboard = [
        ['7', '8', '9', DIV, DEL],
        ['4', '5', '6', MULT, 'C'],
        ['1', '2', '3', '-', '('],
        ['0', '.', '=', '+', ')']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text(
        'Start typing or use the keyboard below!', reply_markup=reply_markup)


def handle_input(update, context):
    result = ""
    user_input = update.message.text

    if user_input == '=':
        result = c.evaluate()
    elif user_input == 'C':
        c.clear_input()
    elif user_input == DEL:
        c.backspace_input()
    elif user_input == MULT:
        c.add_input('*')
    elif user_input == DIV:
        c.add_input('/')
    else:
        c.add_input(user_input)

    if not result:
        result = "Your current expression:\n\t" + c.get_input()

    logger.info("Maxie displayed: %s", result)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=result)


def main():
    updater = Updater(
        # TOKEN to be replaced with Telegram bot token
        token='TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(
        Filters.text & (~Filters.command), handle_input))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
