
from translator import englishtofrench
from translator import frenchtoenglish



def main():
    english_text = "Hello, how are you?"	
    french_text = englishtofrench(english_text)
    print("English Text:", english_text)
    print("French Translation:", french_text)
    
    
    french_text = "Bonjour, comment ça va?"
    english_text = frenchtoenglish(french_text)
    print("French Text:", french_text)
    print("English Translation:", english_text)




    

if __name__ == "__main__":
    main()