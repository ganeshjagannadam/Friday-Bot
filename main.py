from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
from key import TOKEN


BOT_USERNAME: Final = '@GganeshJaggu_bot'

async def start_command(update: Update,contex : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello There I am here to share you the best resources to learn coding and crack interviews.If you want to know more about commands type /help')

async def help_command(update: Update,contex : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello There I am here to share you the best resources to learn coding and crack interviews')

async def custom_command(update: Update,contex : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello There I am here to share you the best resources to learn coding and crack interviews')

# Responses

def handle_responses(text: str)->str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello there! How can I Help?'
    if 'how are you' in processed:
        return 'I am Good'
    if 'roast me' in processed:
        return 'If you were any bigger moons will be oribiting you'
    
    return 'I do not understad what you are talking about'


async def handle_message(update: Update,contex: ContextTypes):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'')
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)

    print('Bot :',response)

    await update.message.reply_text(response)


async def error(update: Update,contex: ContextTypes):
    print(f'Update{update} caused error {contex.error}')


if __name__ == '__main__':
    print('Starting')
    app = Application.builder().token(TOKEN).build()

    #Commads
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Error Handler

    app.add_error_handler(error)

    print('Polling.....')
    app.run_polling(poll_interval=3)
