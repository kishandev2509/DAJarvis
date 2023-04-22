from googletrans import Translator #pip install googletrans==3.1.0a0

def translate(query):
    translator = Translator()
    translated = translator.translate(query)
    return translated

if __name__ == "__main__":
    translated = translate("kaise ho")
    print(translated.text)