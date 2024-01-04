import webbrowser
from urllib.parse import quote

def search_actress_images_on_google(actress_name):
    query = f"{actress_name} celebrity images"
    google_images_url = f"https://www.google.com/search?q={quote(query)}&tbm=isch"

    webbrowser.open(google_images_url)

    return f"Here is the Google Images page for {actress_name}"