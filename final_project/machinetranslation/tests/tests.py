from translator import english_to_french
from translator import french_to_english



def main():
    english_text = "Hello, how are you?"	
    french_text = english_to_french(english_text)
    print("English Text:", english_text)
    print("French Translation:", french_text)
    
    
    french_text = "Bonjour, comment ça va?"
    english_text = french_to_english(french_text)
    print("French Text:", french_text)
    print("English Translation:", english_text)




    

if __name__ == "__main__":
    main()