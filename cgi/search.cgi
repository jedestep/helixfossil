#!/usr/bin/python

import cgi

form = cgi.FieldStorage()
lines = open(".games").readlines()
streams = []
names = []
for line in lines:
    streams.append(line.split("|")[0].strip())
    names.append(line.split("|")[1].strip().lower())

content = ""

if "query" not in form:
    content = """
        Please enter a search term.
        """
else:
    query = form["query"].value
    if query.lower() in names:
        i = names.index(query.lower())
        link = '<li><a href="http://www.helixfossil.tv/games/%s">%s</a></li>' % (streams[i], names[i])
        content= """
            <div class="container">
                <div class="row">
                    <div class="well sidebar-nav">
                        <ul class="nav nav-list">
                            <li class="nav-header">Search results</li>
                            %s
                        </ul>
                    </div>
                </div>
            </div>
            """ % link
    else:
        content= """
            <div class="container">
                <div class="row">
                    <div class="well sidebar-nav">
                        <ul class="nav nav-list">
                            <li class="nav-header">Search results</li>
                            <li>Stream not found. Wanna <a href="#">vote</a> for it?</li>
                        </ul>
                    </div>
                </div>
            </div>
            """
                        

header = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script src="http://cdn.jquerytools.org/1.2.7/full/jquery.tools.min.js"></script>
        <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <script src="../bootstrap/js/bootstrap.min.js"></script>
        <style type="text/css">
            body {
                padding-top: 60px;
                padding-bottom: 40px;
            }
        </style>
    </head>
    <body>
        <div id="title" class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container-fluid">
                    <a class="brand" href="http://www.helixfossil.tv">HelixFossil.tv</a>
                    <div class="nav-collapse collapse">
                        <ul class="nav">
                            <li><a href="http://www.helixfossil.tv/cgi/browse.cgi">Browse streams</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
"""

footer = """
    </body>
</html>
"""

print "Content-Type: text/html\n\n"
print ""
print header + content + footer
