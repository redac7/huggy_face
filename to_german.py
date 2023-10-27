import sys
from transformers import pipeline

en_de_translator = pipeline("translation_en_to_de")

# ask user for text to translate
user_input = input("Enter text to translate to German: ")
# get text to translate

# if no argument is given, use default text
if user_input == "":
    user_input = "You forgot to pass in a text to translate you silly goose!"
# translate text
translation = en_de_translator(user_input)
# print translation
print(translation)