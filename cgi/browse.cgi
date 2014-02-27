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
    <title>HelixFossil.tv</title>
    </head>
    <body>
    %s
    </body>
</html>
""" % lst
