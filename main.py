     
import requests
import typing
 
def response():
    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = r.json()
    for item in data['drinks']:
        arr = [item['strDrink'], item['strInstructions'], item['strDrinkThumb']]
        return str(arr)
 
def record(x):
    with open('cocktail.txt', 'w+') as f:
        f.write(x)
 
 
if __name__ == "__main__":
    print(record(response()))