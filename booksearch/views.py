from django.shortcuts import render
from django.template import Context, Template
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def top(request):
    return render(request, 'welcome/Frontpage.html', {})


def index(request):

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    d = {}
    d["top3books"] = []
    cur.execute("SELECT * FROM Raamatud")
    for i in range(3):
        book = cur.fetchone()
        d["top3books"][i] = book[1]
    cur.close()
    conn.close()
    t = Template("Top 3 raamatut:\n{{top3books.0}}\n{{top3books.1}}"
                 "\n{{top3books.2}}")
    return t.render(Context(d))
