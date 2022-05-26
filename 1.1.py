def letter(ch):
    symbols = "ёЁуУеЕыЫаАоОэЭяЯиИюЮ"
    symbols += ",./!?""<>:;-"
    for i in range(1, len(symbols), 1):
        if symbols[i] == ch:
            return False
    return True


def translate(text):
    translate_text = ""
    for i in range(1, len(text), 1):
        if letter(text[i]):
            translate_text += text[i]
    return translate_text


text = str(input())
translate(text)
print(translate(text))
