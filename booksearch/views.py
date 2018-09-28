from django.shortcuts import render
from django.template import Context, Template
import os
import psycopg2

DATABASE_URL = os.environ[
        'postgres://bzhasqfkpvqslf:fc18438928bbe086372066469a856974e44f8aaddadc8edeb6aaca54f6f7142e@' +
        'ec2-54-217-235-159.eu-west-1.compute.amazonaws.com:5432/d40rmetu5fsrvu']

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
