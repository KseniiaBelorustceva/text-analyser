#!/usr/bin/env python
# -*- coding: utf-8 -*-

stops = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
    'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
    'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having',
    'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
    'with', 'about', 'against', 'between', 'into', 'through', 'during',
    'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in',
    'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
    'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's',
    't', 'can', 'will', 'just', 'don', 'should', 'now', 'id', 'var',
    'function', 'js', 'd', 'script', '\'script', 'fjs', 'document', 'r',
    'b', 'g', 'e', '\'s', 'c', 'f', 'h', 'l', 'k'
]

stops_fi = [
    'me', 'minun', 'minä', 'me', 'meidän', 'meidän', 'itse', 'te',
    'Sinun', 'sinun', 'itse', 'itse', 'hän', 'häntä', 'hänen',
    'Itse', 'hän', 'häntä', 'hänen', 'itseään', 'se', 'sen', 'itse',
    'He', 'heitä', 'heidän', 'heidän', 'itse', 'mitä', 'mikä',
    'Kuka', 'kenelle', 'tämä', 'että', 'nämä', 'ne', 'am', 'on', 'ovat',
    'Oli', 'oli', 'on', 'ollut', 'on', 'on', 'on', 'oli', 'ottaa',
    'ei', 'ei', 'tekee', 'a', 'an', 'jäljempänä', 'ja', 'mutta', 'jos',
    'Tai', 'koska', 'kuten', 'asti', 'kun taas', 'on', 'at', 'ilmaisulla', 'varten',
    'Kanssa', 'noin', 'vastaan', 'välissä', 'tulee', 'läpi', 'aikana',
    'Ennen', 'jälkeen', 'yläpuolella', 'alla', 'on', 'alkaen', 'ylös', 'alas', 'in',
    'Out', 'päällä', 'pois päältä', 'yli', 'alla', 'uudelleen', 'edelleen', 'sitten',
    'Kerran', 'täällä', 'siellä', 'kun', 'missä', 'miksi', 'miten', 'kaikki', 'kaikki',
    'Molemmat', 'jokainen', 'muutaman', 'lisää', 'kaikkein', 'muut', 'jonkin verran', 'kuten', 'ei',
    'Eikä', 'ei', 'vain', 'oma', 'sama', 'niin', 'kuin', 'liian', 'erittäin', 's',
    'T', 'voi', 'se', 'vain', 'don', 'pitäisi', 'nyt', 'id', 'var',
    'Toiminto', 'js', 'd', 'käsikirjoitus', '\' käsikirjoitus ',' FJS ',' asiakirja ','r',
    'B', 'g', 'e', '\' s ',' c ',' f ',' h ',' l ',' k '
]
