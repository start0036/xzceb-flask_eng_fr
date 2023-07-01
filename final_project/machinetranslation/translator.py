from deep_translator import MyMemoryTranslator


def englishtofrench(english_text):
    """
    Translate English text to French.
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text


def frenchtoenglish(french_text):
    """
    Translate French text to English.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    english_text = translator.translate(french_text)
    return english_text
