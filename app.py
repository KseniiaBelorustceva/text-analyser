#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import operator
import re
import nltk
from flask import Flask, render_template, request, jsonify, json
import json
import logging
from stopwords import stops
from collections import Counter
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

#logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')

def extractKeywords(data):
    array = []
    logging.warning('NLTK processing starts:')
    logging.warning(data)
    for i, item in enumerate(data):
        sample = data[i]
        sentences = nltk.sent_tokenize(sample)
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

        def extract_entity_names(t):
            entity_names = []
            if hasattr(t, 'label') and t.label:
                if t.label() == 'NE':
                    entity_names.append(' '.join([child[0].lower() for child in t]))
                else:
                    for child in t:
                        entity_names.extend(extract_entity_names(child))
            return entity_names

        entity_names = []
        for tree in chunked_sentences:
            entity_names.extend(extract_entity_names(tree))
        for item in entity_names:
            if item not in stops:
                array.append(item)
    logging.warning('NLTK processing finished:')
    logging.warning(array)
    return array


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = []
    if request.method == "POST":
        try:
            jsonData = json.loads(request.data)
        except:
            return render_template('error.html', errors=errors)
        if jsonData:
            results=json.dumps(extractKeywords(jsonData), sort_keys=True)

    if request.method == "GET":
        params=[]
        try:
            params.append(request.args['sample'])
        except:
            return render_template('error.html', errors=errors)
        if params:
            results =json.dumps(extractKeywords(params), sort_keys=True)

    #return render_template('finder.html', errors=errors, results=results)
    return results

@app.route('/ui', methods=['GET','POST'])
def renderui():
    errors = []
    results = []

    if request.method == "POST":
        params = []
        try:
            params.append(request.form.get('sample'))
        except:
            logging.warning('errors:')
            logging.warning(errors)
            return render_template('error.html', errors=errors)
        if params:
                results = json.dumps(extractKeywords(params), sort_keys=True)

    if request.method == "GET":
        params=[]
        try:
            return render_template('finder.html', errors=errors, results=results)
            #params.append(request.args['sample'])
        except:
            return render_template('error.html', errors=errors)
        if params:
            results=json.dumps(extractKeywords(params), sort_keys=True)

    return render_template('finder.html', errors=errors, results=results, sample=params)

if __name__ == '__main__':
    app.run()