#!/usr/bin/python

lst = ""

lines = open(".games", "r").readlines()

for line in lines:
    content = line.split("|")
    url = content[0].strip()
    name = content[1].strip()
    lst += '<a href="http://www.helixfossil.tv/games/%s">%s</a><br/>' % (url, name)

print """
<!DOCTYPE html>
<html lang="en">
    <head>
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
    <title>HelixFossil.tv</title>
    </head>
    <body>
    %s
    </body>
</html>
""" % lst
