import compleat
from compleat.output import to_db, to_csv, to_json
import argparse
import itertools
import time
import sys

parser = argparse.ArgumentParser(
    description="Retreive autocomplete suggetions, and output results as CSV [default] or JSON, or store in a database.")

parser.add_argument("--queries",
    "-q",
    nargs="+",
    required=True,
    help="Queries to execute. Space-delimited. If --template is provided, query is first substituted into the template.")

parser.add_argument("--template",
    "-t",
    default="{}",
    help="String describing the shape of the query. {}s will be replaced by the values supplied to --queries. Default: '{}'")

parser.add_argument("--languages",
    "-l",
    nargs="+",
    default=["en"],
    help="Languages (as two-letter codes) to search with. Default: 'en'")

parser.add_argument("--db",
    help="SQLAlchemy connection string to database. If supplied, outputs results to this database, instead of JSON or CSV. Requires `dataset` package.")

parser.add_argument("--json",
    action="store_true",
    help="Output as JSON.")

parser.add_argument("--silent",
    "-s",
    action="store_true",
    help="Don't print query progress to STDERR.")

parser.add_argument("--wait",
    type=float,
    default=0,
    help="Seconds to wait between queries. Default: 0.")

args = parser.parse_args()

def log_query(query_string, lang):
    if args.silent: return
    sys.stderr.write("{lang}: {query}\n".format(
        lang=lang,
        query=query_string))
    
def exec_query(query_string, lang):
    time.sleep(args.wait)
    log_query(query_string, lang)
    q = compleat.suggest(query_string, lang)
    return q

def main():
    templated = map(args.template.format, args.queries)
    combos = itertools.product(templated, args.languages)
    queries = [ exec_query(*c) for c in combos ]
    if args.db: to_db(queries, args.db)
    elif args.json: to_json(queries)
    else: to_csv(queries)

if __name__ == "__main__":
    main()
