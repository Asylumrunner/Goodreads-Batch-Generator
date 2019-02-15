import csv
import requests

with open('books.txt', 'r') as book_file:
    with open('batch_books.csv', 'w', newline='') as csv_file:
        book_writer = csv.writer(csv_file, dialect='excel')
        book_writer.writerow(['Title', 'Author', 'ISBN'])
        for line in book_file:
            try:
                query_string = line.replace(' ', '+')
                response = requests.get("http://openlibrary.org/search.json?title=" + query_string)
                response_dict = response.json()
                title = response_dict['docs'][0]['title_suggest']
                author = response_dict['docs'][0]['author_name'][0]
                isbn = response_dict['docs'][0]['isbn'][0]
                book_writer.writerow([title, author, isbn])
            except Exception:
                print("Exception reached when attempting to query for " + line)
