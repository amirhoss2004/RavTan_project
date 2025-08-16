
# import telebot
# from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup , ReplyKeyboardMarkup, KeyboardButton
# import SAM
# import avalApi
# import os
# print("ready")

# #token is here
# token='8423524817:AAHyiy_9pau6s7x4IB-nBmKMCeHz-dDBygM'
# bot=telebot.TeleBot(token=token)

# #first menu button on this side
# menu_button=ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard=False,row_width=2)
# menu_button.add("Ask chatbot","anatomy picture schematizer","image generator")

# #firstinlinekeyboardbutton
# muscle = InlineKeyboardButton("muscle", callback_data="anatomy:muscle")
# bone = InlineKeyboardButton("bone", callback_data="anatomy:bone")
# artery = InlineKeyboardButton("artery", callback_data="anatomy:artery")
# vein = InlineKeyboardButton("vein", callback_data="anatomy:vein")
# inline_keyboard_step1 = InlineKeyboardMarkup(row_width=2)
# inline_keyboard_step1.add(muscle, bone, artery, vein)

# #secondinlinekeboaedbutton
# dont_know=InlineKeyboardButton("i dont know",callback_data="dont_know")
# inline_keyboard_step2=InlineKeyboardMarkup()
# inline_keyboard_step2.add(dont_know)

# #message variable
# loading_messages={}
# wellcome_messages={}
# waiting_for_photo={}

# #massege welcom handler
# @bot.message_handler(commands=['start'])
# def loading(message):
#     sent_msg=bot.send_message(message.chat.id ,f"""welcom to schematizer app 
#     please choose a button""" , reply_markup=menu_button )
#     wellcome_messages[message.chat.id] = sent_msg.message_id

# #menu button handler
# @bot.message_handler(func=lambda message:True)
# def menu_handler(message):
#     if message.text=="anatomy picture schematizer":
#         try:
#             bot.delete_message(message.chat.id , wellcome_messages[message.chat.id])
#         except Exception as e:
#             print(f"Failed to delete message: {e}")
        
#         avalApi.set_ai("1")
#         bot.send_message(message.chat.id,"please send your photo")
#         waiting_for_photo[message.chat.id]=True

#     elif message.text=="Ask chatbot":
#         avalApi.set_ai("2")
#     elif message.text=="image generator":
#         bot.send_message(message.chat.id ,"this ability is not functional right now")
#     else:
#         bot.send_message(message.chat.id , "please choose one of the buttons")

# #status reporter
# def send_status(chat_id, text):
#     bot.send_message(chat_id, text)

# #inline button handler
# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler(call):
#     if call.data.startswith("anatomy:"):
#         anatomy_value = call.data.split(":")[1]
#         avalApi.set_anatomy_type(anatomy_value)
        
#         sent_msg = bot.send_message(call.message.chat.id, "Which body region is shown in your picture? Please type it or press 'I don't know'.", reply_markup=inline_keyboard_step2)
#         bot.register_next_step_handler(sent_msg, handle_body_region_input)
    
#     elif call.data=="dont_know":
#         # Handle inline button "i don't know"
#         bot.send_message(call.message.chat.id, "Got it! Now, please type the number of the specific part you want to identify.")
#         avalApi.set_body_region("don't know")
#         bot.register_next_step_handler(call.message, handle_user_question_input)

# def handle_body_region_input(message):
#     body_region_value = message.text.lower()
#     avalApi.set_body_region(body_region_value)
    
#     bot.send_message(message.chat.id, "Got it! Now, please type the number of the specific part you want to identify.")
#     bot.register_next_step_handler(message, handle_user_question_input)

# def handle_user_question_input(message):
#     user_question = message.text
#     avalApi.set_user_choose(user_question)
    
#     bot.send_message(message.chat.id, f"Thanks! I'll ask the AI to identify number {user_question} for you.")
    
#     run_and_send_ai_response(message.chat.id)

# def run_and_send_ai_response(chat_id):
#     try:
#         ai_response = avalApi.run_ai()
#         if "❌" in ai_response: # Check if the response is an error message
#             bot.send_message(chat_id, ai_response)
#         else:
#             bot.send_message(chat_id, f"🔍 AI response: {ai_response}")
#     except Exception as e:
#         print(f"Error running AI: {e}")
#         bot.send_message(chat_id, "❌ Sorry, an error occurred while processing the request.")

# # main.py
# ...
# import tempfile

# @bot.message_handler(content_types=['photo'])
# def photo_handler(message):
#     if waiting_for_photo.get(message.chat.id):
#         ...
#         try:
#             file_id = message.photo[-1].file_id
#             file_info = bot.get_file(file_id)
#             downloaded_file_bytes = bot.download_file(file_info.file_path)

#             # Create a temporary file to save the image
#             with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_image:
#                 temp_image.write(downloaded_file_bytes)
#                 image_path = temp_image.name

#             final_image_buffer = SAM.process_and_segment_image(
#                 image_bytes=downloaded_file_bytes,
#                 chat_id=message.chat.id,
#                 status_callback=send_status
#             )

#             if final_image_buffer:
#                 bot.send_photo(message.chat.id, final_image_buffer, caption="""Here is your schematized image! 📷
#                 What would you like to ask AI about?""", reply_markup=inline_keyboard_step1)
                
#                 # Pass both the bytes and the file path (for the extension)
#                 avalApi.set_image(final_image_buffer.getvalue(), image_path)

#         except Exception as e:
#             print(f"Error in photo_handler: {e}")
#             bot.send_message(message.chat.id, "A critical error occurred while handling your photo.")
#         finally:
#             # Clean up the temporary file
#             if 'image_path' in locals() and os.path.exists(image_path):
#                 os.remove(image_path)

# #bot starter
# bot.polling()
# ____________________________________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________________________________
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import SAM
import avalApi
import os
import tempfile
import io

print("ready")

# Token is here
token = '8423524817:AAHyiy_9pau6s7x4IB-nBmKMCeHz-dDBygM'
bot = telebot.TeleBot(token=token)

# First menu button on this side
menu_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
menu_button.add("Ask chatbot", "anatomy picture schematizer", "image generator")

# First inline keyboard button
muscle = InlineKeyboardButton("muscle", callback_data="anatomy:muscle")
bone = InlineKeyboardButton("bone", callback_data="anatomy:bone")
artery = InlineKeyboardButton("artery", callback_data="anatomy:artery")
vein = InlineKeyboardButton("vein", callback_data="anatomy:vein")
inline_keyboard_step1 = InlineKeyboardMarkup(row_width=2)
inline_keyboard_step1.add(muscle, bone, artery, vein)

# Second inline keyboard button
dont_know = InlineKeyboardButton("i dont know", callback_data="dont_know")
inline_keyboard_step2 = InlineKeyboardMarkup()
inline_keyboard_step2.add(dont_know)

# New inline keyboard for post-response
ask_another_number_btn = InlineKeyboardButton("Ask another number", callback_data="ask_another_number")
ask_freely_btn = InlineKeyboardButton("Ask freely", callback_data="ask_freely")
inline_keyboard_post_response = InlineKeyboardMarkup()
inline_keyboard_post_response.add(ask_another_number_btn, ask_freely_btn)

# Message variable
loading_messages = {}
wellcome_messages = {}
waiting_for_photo = {}
waiting_for_free_question = {}

# Message welcome handler
@bot.message_handler(commands=['start'])
def loading(message):
    sent_msg = bot.send_message(message.chat.id, f"""welcom to schematizer app 
    please choose a button""", reply_markup=menu_button)
    wellcome_messages[message.chat.id] = sent_msg.message_id

# Menu button handler
@bot.message_handler(func=lambda message: True)
def menu_handler(message):
    if message.text == "anatomy picture schematizer":
        try:
            bot.delete_message(message.chat.id, wellcome_messages[message.chat.id])
        except Exception as e:
            print(f"Failed to delete message: {e}")
        
        # Set AI type and reset other variables
        avalApi.set_ai("1")
        avalApi.reset_all_except_image()
        bot.send_message(message.chat.id, "please send your photo")
        waiting_for_photo[message.chat.id] = True

    elif message.text == "Ask chatbot":
        avalApi.set_ai("2")
        bot.send_message(message.chat.id, "This ability is not functional right now.")
    elif message.text == "image generator":
        bot.send_message(message.chat.id, "This ability is not functional right now.")
    else:
        bot.send_message(message.chat.id, "please choose one of the buttons")

# Status reporter
def send_status(chat_id, text):
    bot.send_message(chat_id, text)

# Inline button handler
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("anatomy:"):
        anatomy_value = call.data.split(":")[1]
        avalApi.set_anatomy_type(anatomy_value)
        
        sent_msg = bot.send_message(call.message.chat.id, "Which body region is shown in your picture? Please type it or press 'I don't know'.", reply_markup=inline_keyboard_step2)
        bot.register_next_step_handler(sent_msg, handle_body_region_input)
    
    elif call.data == "dont_know":
        bot.send_message(call.message.chat.id, "Got it! Now, please type the number of the specific part you want to identify.")
        avalApi.set_body_region("don't know")
        bot.register_next_step_handler(call.message, handle_user_question_input)

    elif call.data == "ask_another_number":
        avalApi.set_ai("1") # Explicitly set AI type to 1 for this flow
        avalApi.reset_user_choose()
        bot.send_message(call.message.chat.id, "Please select the type of anatomy you'd like to identify.", reply_markup=inline_keyboard_step1)
        
    elif call.data == "ask_freely":
        avalApi.set_ai("2") # Set AI type to 2 for free-form questions
        bot.send_message(call.message.chat.id, "What would you like to ask about this part?")
        waiting_for_free_question[call.message.chat.id] = True
        bot.register_next_step_handler(call.message, handle_free_question)

def handle_body_region_input(message):
    body_region_value = message.text.lower()
    avalApi.set_body_region(body_region_value)
    
    bot.send_message(message.chat.id, "Got it! Now, please type the number of the specific part you want to identify.")
    bot.register_next_step_handler(message, handle_user_question_input)

def handle_user_question_input(message):
    user_question = message.text
    avalApi.set_user_choose(user_question)
    
    bot.send_message(message.chat.id, f"Thanks! I'll ask the AI to identify number {user_question} for you.")
    
    run_and_send_ai_response(message.chat.id, prompt_for_more=True)

def handle_free_question(message):
    user_question = message.text
    waiting_for_free_question.pop(message.chat.id, None)
    avalApi.set_user_choose(user_question)
    run_and_send_ai_response(message.chat.id, prompt_for_more=True)

def run_and_send_ai_response(chat_id, prompt_for_more=False):
    try:
        ai_response = avalApi.run_ai()
        if "❌" in ai_response:
            bot.send_message(chat_id, ai_response)
        else:
            bot.send_message(chat_id, f"🔍 AI response: {ai_response}")
            if prompt_for_more:
                avalApi.append_to_chat_history(ai_response)
                bot.send_message(chat_id, "What would you like to do next?", reply_markup=inline_keyboard_post_response)
    except Exception as e:
        print(f"Error running AI: {e}")
        bot.send_message(chat_id, "❌ Sorry, an error occurred while processing the request.")

@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    if waiting_for_photo.get(message.chat.id):
        bot.send_message(message.chat.id, "Image received ✅ Starting analysis...")
        waiting_for_photo.pop(message.chat.id, None)
        image_path = None

        try:
            file_id = message.photo[-1].file_id
            file_info = bot.get_file(file_id)
            downloaded_file_bytes = bot.download_file(file_info.file_path)

            # Create a temporary file to save the image
            with tempfile.NamedTemporaryFile(suffix=os.path.splitext(file_info.file_path)[1], delete=False) as temp_image:
                temp_image.write(downloaded_file_bytes)
                image_path = temp_image.name

            final_image_buffer = SAM.process_and_segment_image(
                image_bytes=downloaded_file_bytes,
                chat_id=message.chat.id,
                status_callback=send_status
            )
            
            if final_image_buffer:
                bot.send_photo(message.chat.id, io.BytesIO(final_image_buffer.getvalue()), caption="""Here is your schematized image! 📷
                What would you like to ask AI about?""", reply_markup=inline_keyboard_step1)
                
                # Pass both the bytes and the format for avalApi
                image_format = os.path.splitext(image_path)[1][1:]
                avalApi.set_image(final_image_buffer.getvalue(), image_format)

        except Exception as e:
            print(f"Error in photo_handler: {e}")
            bot.send_message(message.chat.id, "A critical error occurred while handling your photo.")
        finally:
            # Clean up the temporary file
            if image_path and os.path.exists(image_path):
                os.remove(image_path)

# Bot starter
bot.polling()