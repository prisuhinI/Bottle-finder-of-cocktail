from bottle import run, route, template, request, error
import requests, json


@route('/')
def home():
    if request.GET.go:
        name = request.GET.search.strip()
        url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
        res = requests.get(url)
        res = res.json()
        drinks = res['drinks'][0]
        return template('home', drinks=drinks)
    else:
        return template('search')


@error()
@error(404)
def error(error):
    return template('errorPage')


run(debug=True, reloader=True)