import pprint
import json
from urllib.request import urlopen, unquote, quote
import sys
import time


def create_query_url(search_phrase, page=1):
    return 'https://public-api.nazk.gov.ua/v1/declaration/?page={page}'.format(page=page)


def main():
    search_phrase = u"Петренко"
    print(quote(search_phrase))
    #url = "https://public-api.nazk.gov.ua/v1/declaration/?q={search_phrase}&page=1".format(search_phrase=search_phrase)

    page = 1
    total_items = 0
    while True:
        url = create_query_url(search_phrase, page)
        print(url)
        response = urlopen(url).read()
        data = json.loads(response.decode('utf-8'))
        #print(len(data['items']))
        total_items += len(data['items'])
        #pprint.pprint(data)
        if 'error' in data:
            break

        page += 1

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
