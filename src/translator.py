from vertexai.preview.language_models import ChatModel, InputOutputTextPair

def get_translation(post: str) -> str:
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    context_text = "You are a translator. If given a sentence not in English, translate it to English. If the sentence is already in English, return the same sentence."

    parameters = {
        "temperature": 0.7,
        "max_output_tokens": 256,
    }

    chat_translate = chat_model.start_chat(context=context_text)
    response = chat_translate.send_message(post, **parameters)
    return response.text

def get_language(post: str) -> str:
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    context_lang = "You are a translator. Your job is to classify the language of a piece of text."

    parameters = {
        "temperature": 0.7,
        "max_output_tokens": 256,
    }

    chat_lang = chat_model.start_chat(context=context_lang)
    response = chat_lang.send_message(post, **parameters)
    return response.text

def translate_content(content: str) -> tuple[bool, str]:
    isEnglish = get_language(content) == "English"
    return (isEnglish, get_translation(content))