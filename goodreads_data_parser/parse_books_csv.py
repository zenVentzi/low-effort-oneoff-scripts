
import csv

str = ''

with open('data/goodreads_library_export.csv', 'r', encoding="utf8") as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    for index, row in enumerate(csv_reader):
        book_id = row['Book Id']
        title = row['Title']
        author = row['Author']
        url = f'https://www.goodreads.com/book/show/{book_id}'
        isbn = row['ISBN']
        isbn13 = row['ISBN13']
        isbn_text = f'ISBN{isbn}, ISBN13{isbn13}'
        str += f'{index + 1}. **{title}** - *{author}*   [(link)]({url}), {isbn_text} \n\n'


print(str)

with open("output/books.txt", "w", encoding="utf8") as text_file:
    print(str, file=text_file)
