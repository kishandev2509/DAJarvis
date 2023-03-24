from googletrans import Translator

def translate(query):
    translator = Translator()
    translated = translator.translate(query)
    return translated

if __name__ == "__main__":
    translated = translate("kaise ho")
    print(translated)