#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import operator
import re
import nltk
from flask import Flask, render_template, request
from stopwords import stops, stops_fi
from collections import Counter
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get text that the person has entered
        try:
            r = request.form['sample']
        except:
            errors.append("Something went wrong").append(r)
            return render_template('finder.html', errors=errors)
        if r:
            # text processing
            sample = r
            sentences = nltk.sent_tokenize(sample)
            tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
            tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
            chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

            def extract_entity_names(t):
                entity_names = []
                if hasattr(t, 'label') and t.label:
                    if t.label() == 'NE':
                        entity_names.append(' '.join([child[0] for child in t]))
                    else:
                        for child in t:
                            entity_names.extend(extract_entity_names(child))
                return entity_names

            entity_names = []
            for tree in chunked_sentences:
                entity_names.extend(extract_entity_names(tree))
            # print(set(entity_names))

            # entity_names = [word for word in results if word not in stops_fi]
            results=set(entity_names)

    return render_template('finder.html', errors=errors, results=results)

if __name__ == '__main__':
    app.run()