import os
import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv


def decline_years(n):
    if n % 100 == 1:
        return 'год'
    if n % 10 == 1 and n % 100 != 11:
        return 'год'
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return 'года'
    else:
        return 'лет'


if __name__ == '__main__':
    load_dotenv()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    foundation_year = 1920
    now_year = datetime.datetime.now().year
    age = now_year - foundation_year
    suffix = decline_years(nowadays)
    excel_wines_df = pandas.read_excel(os.environ['DATA_FILE'])
    excel_wines_df = excel_wines_df.fillna(0)
    excel_wines = excel_wines_df.to_dict('records')

    wines_by_category = collections.defaultdict(list)
    for wine in excel_wines:
        wines_by_category[wine['Категория']].append(wine)

    rendered_page = template.render(
        year=f'{age} {suffix}',
        wines=wines_by_category
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
