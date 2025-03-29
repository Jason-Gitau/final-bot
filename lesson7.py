import mysql.connector
from mysql.connector import Error  # Import the Error clas
from telegram import Update
from telegram.ext import *

bot_token = "7836336644:AAFVBATVsgkq3urGfDCTAtekWSZjD_0nLmg"





async def start(Update:Update, context: CallbackContext) ->None:
    await Update.message.reply_text("I am a telegram bot built with python")

# /help command
async def help_command(update :Update, context:CallbackContext) -> None:
    await update.message.reply_text(
        "Here are the commands you can use:\n"
        "/start: to start the bot\n"
        "/help: to get list of commands\n"
        "/info: to get information about the bot\n"
        "/service: see what i can do!\n"
        "/history: see the chat history"
    )

# /info command
async def info_command(update:Update,context:CallbackContext)-> None:
    await update.message.reply_text("I am a Telegram automation bot built using Python by Jason Mbugua! 🚀")

# /service command
async def service_command(update:Update,context:CallbackContext)->None:
    await update.message.reply_text("I can send messages, automate tasks, and more! 🤖")


    




def main():
    application=Application.builder().token(bot_token).build()

    # add command handler
    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("help",help_command))
    application.add_handler(CommandHandler("info",info_command))
    application.add_handler(CommandHandler("service",service_command))
    application.add_handler(CommandHandler("history",history_command))

    # Message handler (for normal texts)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_memory))

    

    # start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
