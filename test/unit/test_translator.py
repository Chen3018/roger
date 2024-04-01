from src.translator import translate_content


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