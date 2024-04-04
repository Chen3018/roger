
from src.translator import translate_content, get_language, get_translation
from mock import patch
from typing import Callable

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_chinese(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "Chinese"
    mock_get_translation.return_value = "This is a Chinese message"
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_llm_normal_response(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "French"
    mock_get_translation.return_value = "This is a French message"
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"

    mock_get_language.return_value = "English"
    mock_get_translation.return_value = "This is an English message"
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_llm_gibberish_response(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "English"
    mock_get_translation.return_value = "guhjbnh ghjbnhukyhj hu"
    is_english, translated_content = translate_content("guhjbnh ghjbnhukyhj hu")
    assert is_english == True
    assert translated_content == "guhjbnh ghjbnhukyhj hu"

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_unexpected_language(mock_get_translation, mock_get_language):
    mock_get_language.return_value = "English"
    mock_get_translation.return_value = "Aquí está su primer ejemplo."
    content = "Aquí está su primer ejemplo."
    assert translate_content(content) == (True, content)

    mock_get_language.return_value = "English"
    mock_get_translation.return_value = "??????????"
    assert translate_content("??????????") == (True, "??????????")