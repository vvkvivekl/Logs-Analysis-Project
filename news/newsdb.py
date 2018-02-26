#!/usr/bin/env python3

import os
import sys
import psycopg2
DBNAME = "news"


def connect(database_name):
    """Connect to the database.  Returns a database connection."""
    try:
        db = psycopg2.connect(dbname=database_name)
        return db

    except psycopg2.Error as e:
        # THEN you could print an error
        # and perhaps exit the program
        print ("Unable to connect to database")
        sys.exit(1)


def popular_articles():
    conn = connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(
        "select articles.title, count(log.ip) as views from log "
        "join articles on log.path = CONCAT('/article/',articles.slug) "
        "group by articles.title order by views desc limit 3;"
        )
    results = cursor.fetchall()
    conn.close()
    clear()
    print "\n\nThe most popular three articles of all time's are:-"
    i = 1
    for result in results:
        print "\n", i, ") \"", result[0], "\" -- ", result[1], " views"
        i += 1


def popular_articles_author():
    conn = connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(
        "select authors.name, count(log.ip) as views from log, "
        "authors, articles where articles.author = authors.id and "
        "CONCAT('/article/',articles.slug) = log.path "
        "group by authors.name order by views desc;"
        )
    results = cursor.fetchall()
    conn.close()
    clear()
    print "\n\nThe most popular article authors of all time's are:-"
    i = 1
    for result in results:
        print "\n", i, ") \"", result[0], "\" -- ", result[1], " views"
        i += 1


def log_error():
    conn = connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(
        "select to_char(date, 'FMMonth FMDD, YYYY'), "
        "err/total as ratio"
        "from (select time::date as date,"
        "count(*) as total,"
        "sum((status != '200 OK')::int)::float as err"
        "from log group by date) as errors"
        "where err/total > 0.01;"
        )
    results = cursor.fetchall()
    conn.close()
    clear()
    print "\n\nOn this day(s) more than 1%' of requests lead to errors:-"
    i = 1
    for result in results:
        print "\n", i, ") \"", result[0], "\" -- ", result[1], "%"
        i += 1


a = 0


def questions():
    print "\n\nGive numric value to select query"
    print "1) Most popular three articles of all time"
    print "2) Most popular article authors of all time"
    print "3) On which days did more than 1%' of requests lead to errors?"
    print "9) To exit"
    a = input("Which query you want to run: ")
    clear()
    print "\n\n\nLoading..."
    display(a)


def display(type):
    if (type == 1):
        popular_articles()
        print "\nAwosome, try for more"
        questions()
    elif (type == 2):
        popular_articles_author()
        print "\nAwosome, more!!"
        questions()
    elif (type == 3):
        log_error()
        print "\nAwosome, more!!"
        questions()
    elif (type == 9):
        clear()
        sys.exit()
    else:
        questions()


def clear():
    os.system('clear')


clear()
display(a)
