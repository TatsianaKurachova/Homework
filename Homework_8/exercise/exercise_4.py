# Поставить в соответствие следующим английским символам русские буквы:
# h – х, 
# e – е, 
# l – л, 
# o – о, 
# w – в, 
# r – р, 
# d – д
# и преобразовать строку «hello world!» в русские символы

english: str = 'helowrd' 
russian: str = 'хеловрд'
symbols: dict = dict(zip(english, russian)) # zip is used to combine iterated objects. 

text_1: str = 'hello world!'
text_2: str = ''

def translit(text_1: str, symbols: dict) -> str:
    text_2: str = '' 
    for i in text_1:
        if i in symbols.keys(): 
            text_2 = text_2 + symbols.get(i) 
        else:
            text_2 += i
    return text_2

print(translit(text_1, symbols))