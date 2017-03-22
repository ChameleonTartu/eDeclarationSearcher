#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import pprint
import json
from urllib import urlopen, unquote, quote
import sys
import time

app = Flask(__name__)

def create_query_url(search_phrase, page=1):
    if search_phrase == "":
      return 'https://public-api.nazk.gov.ua/v1/declaration/?page={0}'.format(page)
    return 'https://public-api.nazk.gov.ua/v1/declaration/?q={0}&page={1}'.format(search_phrase, page)

def search(search_phrase):

  search_phrase = quote(search_phrase.encode('utf-8'))
  dataset = []

  max_pages = 4
  page = 1
  total_items = 0
  while max_pages > page:
    url = create_query_url(search_phrase, page)
    print(url)
    response = urlopen(url).read()
    data = json.loads(response.decode('utf-8'))
    if 'error' in data:
      break
    total_items += len(data['items'])
    dataset.extend(data['items'])
    page += 1
    
  return dataset



@app.route('/', methods=['GET'])
def main_page():
  return render_template('eDeclaration.html')

@app.route('/search', methods=['GET'])
def search_page():
  search_query = request.args.get('search_query')
  print(search_query)
  return json.dumps({
            'status': 'OK',
            'items': search(search_query)
        }) 

if __name__  == "__main__":
  app.run()

