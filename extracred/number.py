#!/usr/bin/python3
import cgi
import cgitb
import random
cgitb.enable()

print('Content-type: text/html\n')
def main():
    form=cgi.FieldStorage()
    winningnumber=random.randint(0, 1000)
    template='''
<!DOCTYPE html>
<html>
<head>
<title>Number Game</title>
<style>
.pic {
position: fixed;
right: 0;
}
</style>
</head>
<body background="bground.jpeg">
<form method="get" action="number2.py">
<input type="hidden" name="winnumber" value="%s">
<input type="hidden" name="lowguess" value="0">
<input type="hidden" name="highguess" value="1000">
<input type="hidden" name="numberguess" value="0">
<center>
<font size="5" style="font-family:helvetica"><b>I'm thinking of a number...</b><br>
<input type="number" name="anumber" min="1" max="999" autofocus><br>
<input type="submit" name="submitguess" value="Guess">
</font>
<font size="5">
<pre>
Type in a number from 1 to 999, inclusive, in the box above!
<i>Hmm, what number would be a good first guess?</i>
</pre>
</font>
</center>
<img class="pic" src="index.png" height="200" width="400">
</form>
</body>
</html>
''' % (str(winningnumber))
    noinput=template.replace('<body', '''
<body onload="alert('You didn't guess a number! Try again.')"
''')
    try:
        print(template)
    except:
        print(noinput)
main()
