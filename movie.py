import requests
from bs4 import BeautifulSoup

# ...
def get_recipe(recipe_name):
    search_url = f"https://tasty.co/search?q={recipe_name}&sort=popular"
    response = requests.get(search_url)

    webbrowser.open(google_images_url)

    return f"Here is the Google Images page for {actress_name}"

    return recipe_info