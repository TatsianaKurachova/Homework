import requests
 
def response():
    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = r.json()
    str = ''
    for item in data['drinks']:
        str += (f"Cocktail_Name: {item['strDrink']}, How_to_do: {item['strInstructions']}, Picture: {item['strDrinkThumb']} \n")
    return str
 
def record(x):
    with open('cocktails.txt', 'w+') as f:
        f.write(x)       
 
record(response())