import urllib
import hashlib
import requests
import json
import datetime
import random

class Query(object):
    URL_TEMPLATE = "http://suggestqueries.google.com/complete/search?client=chrome&hl={lang}&q={query}"
    def __init__(self, query, lang="en"):
        self.query = query
        self.lang = lang
        self.timestamp = datetime.datetime.now()
        self.rand = str(random.random())
        req = requests.get(self.url)
        self.response = req.json()

    @property
    def url(self):
        encoded = self.query.encode("utf-8")
        escaped = urllib.quote(encoded)
        return self.URL_TEMPLATE.format(
            query=escaped,
            lang=self.lang)

    @property
    def suggestions(self):
        query, sugg_texts, sugg_titles, _, meta = self.response
        zipped = zip(
            sugg_texts,\
            sugg_titles,\
            meta["google:suggesttype"],\
            meta["google:suggestrelevance"])
        dicts = [ {
            "text": z[0],
            "title": z[1],
            "type": z[2],
            "relevance": z[3]
        } for z in zipped ]
        return dicts

    @property
    def uid(self):
        _ = ":".join([
            self.query,
            self.lang,
            self.timestamp.ctime(),
            self.rand
        ]).encode("utf-8")
        return hashlib.md5(_).hexdigest()

    @property
    def meta(self):
        return {
            "query": self.query,
            "lang": self.lang,
            "timestamp": self.timestamp.ctime(),
            "uid": self.uid
        }
