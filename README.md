# compleat

Fetch autocomplete suggestions from Google Search. Use responsibly. Not affiliated with Google.

## Usage

`compleat` can be used as either a Python library or command-line tool.

### Library

```python
>>> import compleat
>>> q = compleat.suggest("is allen iverson ")
>>> q.meta
{
    'lang': 'en',
    'query': 'is allen iverson ',
    'uid': '2c83d58b7350a9f55066cf4f49d16fd9',
    'timestamp': 'Fri Jan 31 00:13:00 2014'
}
>>> len(q.suggestions)
20
>>> q.suggestions[0:5]

[{'relevance': 800,
  'text': u'is allen iverson broke',
  'title': u'',
  'type': u'QUERY'},
 {'relevance': 601,
  'text': u'is allen iverson really broke',
  'title': u'',
  'type': u'QUERY'},
 {'relevance': 600,
  'text': u'is allen iverson still broke',
  'title': u'',
  'type': u'QUERY'},
 {'relevance': 566,
  'text': u'is allen iverson still in the nba',
  'title': u'',
  'type': u'QUERY'},
 {'relevance': 565,
  'text': u'is allen iverson back in the nba',
  'title': u'',
  'type': u'QUERY'}]
```

Note: `compleat.suggest()` also accepts an optional `lang` parameter, which is "en" (English) by default.

```python
>>> import compleat
>>> [ s["text"] for s in compleat.suggest("bon", lang="en").suggestions[:5] ]
['bones', 'bonnie and clyde', 'bonobos', 'bon appetit', 'bonefish grill']
>>> [ s["text"] for s in compleat.suggest("bon", lang="fr").suggestions[:5] ]
['bon coin', 'bonobo', 'bon prix', 'bon patron', 'bonnet']
>>> [ s["text"] for s in compleat.suggest("bon", lang="es").suggestions[:5] ]
['bonoloto', 'bonus', 'bon jovi', 'bones', 'bonsai']
```

### Command-line tool

Run `compleat -h` from the command line for full set of options. Examples:

`compleat -q "where is "`

`compleat -q "where is " --json`

`compleat -q "where is " --db sqlite:///whereis.sqlite`

`compleat -q "who is " "why is " "where is "`

`compleat --template "is {} " -q "allen iverson" "marie curie" "meryl streep"`

