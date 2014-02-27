#!/usr/bin/python

lst = ""

lines = open(".games", "r").readlines()

for line in lines:
    content = line.split("|")
    url = content[0].strip()
    name = content[1].strip()
    lst += '<li><a href="http://www.helixfossil.tv/games/%s">%s</a></li>' % (url, name)

print """
<!DOCTYPE html>
<html lang="en">
    <head>
    <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
    <title>HelixFossil.tv</title>
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
        <div class="container">
            <div class="row">
                <div class="well sidebar-nav">
                    <ul class="nav nav-list">
                        <li class="nav-header">Available Streams</li>
                        %s
                    </ul>
                </div>
            </div>
        </div>
    </body>
</html>
""" % lst
