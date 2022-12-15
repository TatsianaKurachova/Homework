import requests
 
def response():
    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = r.json()
    dict = ''
    for item in data['drinks']:
        dict += (f"Name: {item['strDrink']}, \n How_to_do: {item['strInstructions']}, \n Picture: {item['strDrinkThumb']}, \n")
    return dict
 
def record(x):
    with open('cocktails.txt', 'w+') as f:
        f.write(x)       
 
record(response())