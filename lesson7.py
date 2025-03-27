import mysql.connector
from mysql.connector import Error  # Import the Error clas
from telegram import Update
from telegram.ext import *

bot_token = "7836336644:AAFVBATVsgkq3urGfDCTAtekWSZjD_0nLmg"

# connect to a database mysql
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="16133",
        database="telegram_bot"
    )
    cursor = conn.cursor()

    # Granting privileges
    cursor.execute("GRANT ALL PRIVILEGES ON telegram_bot.* TO 'root'@'localhost'")
    cursor.execute("FLUSH PRIVILEGES")
except Error  as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)  # Exit the script if the database connection fails



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

async def chat_memory(update:Update,context:CallbackContext)->None:
    user_id=update.message.chat_id
    user_message=update.message.text.lower()
    
    if not user_message.startswith("/history"):
        cursor.execute("INSERT INTO messages(user_id,message) VALUES(%s,%s)",(user_id,user_message))
        conn.commit()

    

async def history_command(update: Update, context: CallbackContext) -> None:
    user_id = update.message.chat_id

    # Retrieve last 5 messages from this user
    cursor.execute("SELECT message FROM messages WHERE user_id = %s ORDER BY id DESC LIMIT 10", (user_id,))
    history = cursor.fetchall()

    history_text = "\n".join([msg[0] for msg in history]) if history else "No messages found."

    await update.message.reply_text(f"Your recent messages:\n{history_text}")




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