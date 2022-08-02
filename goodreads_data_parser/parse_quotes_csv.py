import csv

str = ''

with open('data/goodreads_quotes_export.csv', 'r', encoding="utf8") as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    for row in csv_reader:
        quote = row['Quote']
        quote = quote.replace('<br/>', ' ')
        author = row['Author']
        str += f'**{quote}** - *{author}* \n\n'


print(str)

with open("output/quotes.txt", "w") as text_file:
    print(str, file=text_file)