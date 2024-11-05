import requests

from bs4 import BeautifulSoup


URL = "https://www.audible.com/search?keywords=book&node=18573211011"

response = requests.get(URL)
website_html = response.text


soup = BeautifulSoup(website_html, "html.parser")

books_title = [title.getText() for title in soup.find_all('h3', class_="bc-heading bc-color-link bc-pub-break-word bc-size-medium")]
books = books_title[::-1]

subtitle = [sub.getText() for sub in soup.find_all('li', class_="bc-list-item subtitle")]
subtitles = subtitle[::-1]

authors = [auth.getText() for auth in soup.find_all('li', class_="bc-list-item authorLabel")]
all_authors = authors[::-1]




with open('books.csv', mode='w') as file:
    for book in books_title:
        for subtitlee in subtitle:
            for author in authors:
                file.write(f'Title: {book}\nSubtitle:{subtitlee}\nAuthor:{author}\n')



