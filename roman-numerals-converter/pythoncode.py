from flask import Flask 

app = Flask(__name__)

@app.route('/')
def roman_to_integer(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    previous_value = 0
    for char in roman[::-1]:
        current_value = roman_numerals[char]
        if current_value >= previous_value:
            result += current_value
        else:
            result -= current_value
        previous_value = current_value
    return result
# Örnek kullanım
roman_numeral = input("Enter a Roman number: ")
latin_number = roman_to_integer(roman_numeral)
print("Latin number:", latin_number)