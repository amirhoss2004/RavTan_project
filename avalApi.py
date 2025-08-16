# from langchain_openai import ChatOpenAI # pip install -U langchain_openai
# import base64
# import os



# base_url = "https://api.avalai.ir/v1"
# api_key = "AVALAI_API_KEY"

# model_name = "gpt-4o"


# llm = ChatOpenAI(
#     base_url=base_url,
#     model=model_name,
#     api_key=api_key,
# )

# start_key=None

# while start_key != None:
#     message_content=[]
#     user_choose=None
#     anatomy_type=None        
#     body_region=None
#     IMAGE_PATH = None
#     ai_type=None

#     def set_ai(value):
#         global ai_type
#         ai_type=value
#     def set_image(value):
#         global IMAGE_PATH
#         IMAGE_PATH=value
            
#     def set_anatomy_type(value):
#         global anatomy_type
#         anatomy_type = value
        
#     def set_body_region(value):
#         global body_region
#         body_region=value

    
#             # Open the image file and encode it as a base64 string
#     def encode_image(image_path):
#         with open(image_path, "rb") as image_file:
#             return base64.b64encode(image_file.read()).decode("utf-8")

#     base64_image = encode_image(IMAGE_PATH)
#     image_ext = os.path.splitext(IMAGE_PATH)[1][1:]



#     messages1 = [
#             {
#                 "role": "system",
#                 "content": f"you are a anatomist , user can give you a anatomical picture ofsome body region , at this case :{body_region} , and asks you the  {anatomy_type} that segmented with number , and you only only only tell the true and accurate complete name , remember, it should only the complete name , and the true and accurate one",
#             },
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": f"{user_choose}",
#                     },
#                     {
#                         "type": "image",
#                         "image": {
#                             "data": base64_image,  # base64 of the image
#                             "encoding": "base64"
#                         },
#                     },
#                 ],
#             },
#         ]

#     def choose_AI_type(ai_type):
#         if ai_type=="1":
#             ai_message = llm.invoke(messages1)
#             message_content.append(ai_message.content)
#         elif ai_type=="2":
#             pass 
#     print(message_content)
#___________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________
# from langchain_openai import ChatOpenAI
# import base64
# import os

# base_url = "https://api.avalai.ir/v1"
# api_key = "aa-qfaySfy9WkBPMXlGUuWCWFq9zdHxWDLm8wqHxtA5Qrc5u1V6"
# model_name = "gpt-4o"

# llm = ChatOpenAI(
#     base_url=base_url,
#     model=model_name,
#     api_key=api_key,
# )

# # avalApi.py
# ...
# # Global state variables
# user_choose = None
# anatomy_type = None        
# body_region = None
# IMAGE_BYTES = None  # Renamed for clarity
# IMAGE_FORMAT = None # New variable
# ai_type = None

# # Setters / Getters
# def set_ai(value):
#     global ai_type
#     ai_type = value


# # Setters / Getters
# def set_image(bytes_value, path_value):
#     global IMAGE_BYTES
#     global IMAGE_FORMAT
#     IMAGE_BYTES = bytes_value
#     # Extract the format from the file path
#     IMAGE_FORMAT = path_value.split('.')[-1]

# # Utility
# def encode_image(image_bytes, image_format):
#     # This function now creates the full data URI
#     base64_string = base64.b64encode(image_bytes).decode("utf-8")
#     return f"data:image/{image_format};base64,{base64_string}"

# # Setters / Getters
# def set_anatomy_type(value):
#     global anatomy_type
#     anatomy_type = value

# # Setters / Getters
# def set_body_region(value):
#     global body_region
#     body_region=value

# # Setters / Getters
# def set_user_choose(value):
#     global user_choose
#     user_choose=value




# # Main AI runner
# def run_ai():
#     # Check for requirment
#     if IMAGE_BYTES is None or anatomy_type is None or body_region is None or user_choose is None:
#         return "❌ Missing input for AI. Please restart the process by sending an image."

#     # image to url
#     base64_image = encode_image(IMAGE_BYTES, IMAGE_FORMAT)

#     if body_region == "don't know":
#         system_content = (
#             f"You are an anatomist. User gave you an anatomical picture asking for the "
#             f"{anatomy_type} segmented with number. The user does not know the body region. "
#             f"Only answer with the true and accurate complete name of the anatomical part."
#         )
#     else:
#         system_content = (
#             f"You are an anatomist. User gave you an anatomical picture of body region, at this case :{body_region} "
#             f"asking for the {anatomy_type} segmented with number. "
#             f"Only answer with the true and accurate complete name. Only answer with the true and accurate complete name."
#         )

#     messages1 = [
#         {
#             "role": "system",
#             "content": system_content,
#         },
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": f"{user_choose}"},
#                 {
#                     "type": "image",
#                     "image": {"data": base64_image, "encoding": "base64"},
#                 },
#             ],
#         },
#     ]
    
#     messages2 = [
#         {
#             "role": "system",
#             "content": f"You are an anatomist. User gave you an anatomical picture of body region, at this case :{body_region} "
#             f"asking for the {anatomy_type} segmented with number. "
#             f"answer the users question about that segment , be accurate ",
#         },
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": f"{user_choose}"},
#                 {
#                     "type": "image",
#                     "image": {"data": base64_image, "encoding": "base64"},
#                 },
#             ],
#         },
#         {

#             "role": "assitant",
#             "content": [
#                 {"type": "text", "text": f"{user_choose}"},
#                 {
#                     "type": "image",
#                     "image": {"data": base64_image, "encoding": "base64"},
#                 },
#             ],



#         }
#     ]
#     if ai_type == "1":
#         try:
#             ai_message = llm.invoke(messages1)
#             return ai_message.content
#         except Exception as e:
#             return f"❌ An error occurred while communicating with the AI: {e}"
#     elif ai_type == "2":
#         try:
#             ai_message = llm.invoke(messages2)
#             return ai_message.content
#         except Exception as e:
#             return f"❌ An error occurred while communicating with the AI: {e}"
#     else:
#         return "⚠️ No AI type selected. Please start the process again."
        #___________________________________________________________________________________________________________________________
# ________________________________________________________________________________________________________________________
from langchain_openai import ChatOpenAI
import base64
import os

base_url = "https://api.avalai.ir/v1"
api_key = "aa-qfaySfy9WkBPMXlGUuWCWFq9zdHxWDLm8wqHxtA5Qrc5u1V6"
model_name = "gpt-4o"

llm = ChatOpenAI(
    base_url=base_url,
    model=model_name,
    api_key=api_key,
)

# Global state variables
user_choose = None
anatomy_type = None        
body_region = None
IMAGE_BYTES = None
IMAGE_FORMAT = None
ai_type = None
chat_history = []

# Setters / Getters
def set_ai(value):
    global ai_type
    ai_type = value

def set_image(bytes_value, format_value):
    global IMAGE_BYTES
    global IMAGE_FORMAT
    IMAGE_BYTES = bytes_value
    IMAGE_FORMAT = format_value.lower()  # Ensure lowercase format

def set_anatomy_type(value):
    global anatomy_type
    anatomy_type = value

def set_body_region(value):
    global body_region
    body_region = value

def set_user_choose(value):
    global user_choose
    user_choose = value

# Utility
def encode_image(image_bytes, image_format):
    base64_string = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/{image_format};base64,{base64_string}"

def reset_user_choose():
    global user_choose
    user_choose = None
    
def reset_all_except_image():
    global user_choose, anatomy_type, chat_history
    user_choose = None
    anatomy_type = None
    chat_history = []

def append_to_chat_history(response):
    global chat_history
    chat_history.append({"role": "assistant", "content": response})

# Main AI runner
def run_ai():
    global chat_history
    # Check for requirements
    if IMAGE_BYTES is None or anatomy_type is None or body_region is None or user_choose is None:
        return "❌ Missing input for AI. Please restart the process by sending an image."

    base64_image = encode_image(IMAGE_BYTES, IMAGE_FORMAT)
    
    if ai_type == "1":
        if body_region == "don't know":
            system_content = (
                f"You are an anatomist. User gave you an anatomical picture asking for the "
                f"{anatomy_type} segmented with number. The user does not know the body region. "
                f"Only answer with the true and accurate complete name of the anatomical part."
            )
        else:
            system_content = (
                f"You are an anatomist. User gave you an anatomical picture of body region, at this case :{body_region} "
                f"asking for the {anatomy_type} segmented with number. "
                f"Only answer with the true and accurate complete name. Only answer with the true and accurate complete name."
            )

        messages = [
            {
                "role": "system",
                "content": system_content,
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"{user_choose}"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": base64_image,
                            "detail": "auto"
                        },
                    },
                ],
            },
        ]
        
        try:
            ai_message = llm.invoke(messages)
            return ai_message.content
        except Exception as e:
            return f"❌ An error occurred while communicating with the AI: {e}"
            
    elif ai_type == "2":
        messages = [
            {
                "role": "system",
                "content": "You are an anatomist providing detailed information about anatomical parts. Keep the conversation flowing based on the user's questions.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"The last identified part was about the body region: {body_region}, and the anatomy type: {anatomy_type}. The initial question was about part number: {user_choose}."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": base64_image,
                            "detail": "auto"
                        },
                    },
                ],
            },
        ]

        messages.extend(chat_history)
        messages.append({"role": "user", "content": user_choose})

        try:
            ai_message = llm.invoke(messages)
            return ai_message.content
        except Exception as e:
            return f"❌ An error occurred while communicating with the AI: {e}"
    else:
        return "⚠️ No AI type selected. Please start the process again."