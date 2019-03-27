#!/usr/bin/env python2.7

import psycopg2


def queryForRun(queryChosen):
    if queryChosen == "articles":
		articles = """
      SELECT articles.title,
       Count(log.id) AS total
FROM   articles
       LEFT JOIN log
              ON log.path = ( '/article/'
                              || articles.slug )
GROUP  BY articles.title
ORDER  BY total DESC
LIMIT  3;
        """
                queryChosen = articles
    elif queryChosen == "author":
		author = """
SELECT authors.NAME,
       Count(log.id)
FROM   authors
       LEFT JOIN articles
              ON articles.author = authors.id
       LEFT JOIN log
              ON log.path = ( '/article/'
                              || articles.slug )
GROUP  BY authors.NAME
ORDER  BY count DESC;
        """
                queryChosen = author
    else:
		errors = """
 SELECT To_char(errors_by_day.DATE, 'Month DD, YYYY') AS DATE,
       To_char(( ( errors_by_day.count :: decimal
                 / requests_by_day.count :: decimal ) * 100 ), '9.99')
       || '%'                                        AS percentage
FROM   (SELECT DATE(TIME),
               Count(*)
        FROM   log
        GROUP  BY DATE(TIME)) AS requests_by_day,
       (SELECT DATE(TIME),
               Count(*)
        FROM   log
        WHERE  status != '200 OK'
        GROUP  BY DATE(TIME)) AS errors_by_day
WHERE  requests_by_day.DATE = errors_by_day.DATE
       AND ( ( errors_by_day.count :: decimal
             / requests_by_day.count :: decimal ) * 100 )
           > 1;
        """
                queryChosen = errors
    return queryChosen


def queryRequired(query):

    db = psycopg2.connect(database="news")
    cur = db.cursor()
    cur.execute(query)
    return cur.fetchall()
    db.close()


def runOutput():

    print "What are the most popular three articles of all time?\n"
    rows = queryRequired(queryForRun("articles"))
    for row in rows:
        print "%s - %d views" % (row[0], row[1])
    print "\n"

    print "Who are the most popular article authors of all time?\n"
    rows = queryRequired(queryForRun("author"))
    for row in rows:
        print "%s - %d views" % (row[0], row[1])
    print "\n"

    print "On which days did more than 1% of requests lead to errors?\n"
    rows = queryRequired(queryForRun("errors"))
    for row in rows:
        print "%s - %s errors" % (row[0], row[1])


runOutput()
