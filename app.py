from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Google Books API Key (replace this with your own key if needed)
API_KEY = 'AIzaSyCyVgnY4TAUURkXoi9ba4JqhTSpucLFFcc'

# Fetch top recommended books of the week
@app.route('/')
def index():
    url = f'https://www.googleapis.com/books/v1/volumes?q=subject:fiction&orderBy=relevance&maxResults=10&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Extract book details
    books = []
    if 'items' in data:
        books = [{
            'title': item['volumeInfo'].get('title', 'No Title'),
            'author': item['volumeInfo'].get('authors', ['Unknown'])[0],
            'description': item['volumeInfo'].get('description', 'No description available'),
            'thumbnail': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''),
            'link': item['volumeInfo'].get('infoLink', '#')
        } for item in data['items']]

    return render_template('index.html', books=books)

# Search for a specific book
@app.route('/search', methods=['GET', 'POST'])
def search():
    books = []
    if request.method == 'POST':
        query = request.form.get('query')
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10&key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Extract book details
        if 'items' in data:
            books = [{
                'title': item['volumeInfo'].get('title', 'No Title'),
                'author': item['volumeInfo'].get('authors', ['Unknown'])[0],
                'description': item['volumeInfo'].get('description', 'No description available'),
                'thumbnail': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''),
                'link': item['volumeInfo'].get('infoLink', '#')
            } for item in data['items']]
    
    return render_template('search.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
