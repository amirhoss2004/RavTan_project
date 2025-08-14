import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

from decouple import Config
from telegram import Update , KeyboardButton , ReplyKeyboardMarkup
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import MessageHandler   ,filters
token='8423524817:AAHyiy_9pau6s7x4IB-nBmKMCeHz-dDBygM'
  
# tk = Config('TOKEN')     
# print(tk)    

img="str"


async def start(update:Update , context: ContextTypes.DEFAULT_TYPE):
    
    keys=[[KeyboardButton('shcematizer'),KeyboardButton('draw')]
    ,[KeyboardButton('ask')]]
    key_mark_up=ReplyKeyboardMarkup(keys,resize_keyboard=True)


    await context.bot.send_message(
        chat_id=update._effective_chat.id
        ,text=f'welcom to shcematizer bot {update.effective_user.first_name}!!\n please choose an option'
        ,reply_markup=key_mark_up
        ,reply_to_message_id=update.effective_message.id)
    

async def sendphoto(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id
        ,photo=img
        ,caption="caption"
    )
    
        
    




def main():
    app=ApplicationBuilder().token(token=token).build()



    starthandler=CommandHandler('start',start)
    


     
    app.add_handler(starthandler)




    app.run_polling()

if __name__ == "__main__":
    main()