def to_db(queries, db_str):
    import dataset
    db = dataset.connect(db_str)
    query_table = db.get_table("queries")
    suggestion_table = db.get_table("suggestions")
    for q in queries:
        query_table.insert(q.meta)
        suggestion_table.insert_many([
            dict(s.items() + {
                "query_uid": q.uid
            }.items()) for s in q.suggestions
        ])

def to_csv(queries):
    import unicodecsv, sys
    fieldnames = queries[0].meta.keys() + \
        queries[0].suggestions[0].keys()
    writer = unicodecsv.DictWriter(sys.stdout, fieldnames)
    writer.writeheader()
    for q in queries:
        for s in q.suggestions:
            row_dict = dict(q.meta.items() + s.items())
            writer.writerow(row_dict)

def to_json(queries):
    import json
    def convert(query):
        sugg_tuple = ("suggestions", query.suggestions)
        return dict(query.meta.items() + [ sugg_tuple ])
    obj = map(convert, queries)
    json.dump(obj, sys.stdout)
