import vertexai
from src.translator import translate_content
from mock import patch
from typing import Callable

def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("guhjbnh ghjbnhukyhj hu")
    assert is_english == True
    assert translated_content == "guhjbnh ghjbnhukyhj hu"

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_unexpected_language(mocker):
    mocker.return_value.text = "I don't understand your request"
    content = "Aquí está su primer ejemplo."
    assert translate_content(content) == (True, content)
    assert translate_content("??????????") == (True, "??????????")
    mocker.return_value.text = ""
    assert translate_content(content) == (True, content)
    mocker.return_value.text = {}
    assert translate_content(content) == (True, content)

