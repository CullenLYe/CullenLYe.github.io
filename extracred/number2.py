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
.button {
border: 2px solid black;
background-color: white;
padding: 14px 28px;
font-size: 25px;
cursor: pointer;
display: inline-block;
color: black;
}
.button:hover {
background: gray;
color: white;
}
</style>
</head>
<body background="bground.jpeg">
<form method="get" action="number2.py">
<font size="6"><b><a style="text-decoration:none" class="button" href="http://homer.stuy.edu/~cye10/extracred/number.py?">Restart The Game</a></b></font>
<input type="hidden" name="winnumber" value=%s>
<input type="hidden" name="guess" value="lastguess">
<center>
<font size="5" style="font-family:helvetica"><b>TOO BLANK</b><br>
It is higher than HIGHERTHAN.<br>
It is lower than LOWERTHAN.<br>


<input type="hidden" name="lowguess" value="0">
<input type="hidden" name="highguess" value="1000">
<input type="hidden" name="numberguess" value=”1“>

<input type="number" name="anumber" min="1" max="999" autofocus><br>
<input type="submit" name="submitguess" value="Guess"><br>
You guessed NUMBERGUESS times so far.
</font>
</center>
</form>
</body>
</html>
''' % (str(form.getvalue('winnumber')))


    noinput1='''
<!DOCTYPE html>
<html>
<head>
<title>Number Game</title>
<script>
function noinput() {
alert("You didn't guess a number! Try again.");
}
</script>
</head>
<body onload="noinput()" background="bground.jpeg">
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
Type in a number from 1 to 999, inclusive!
Hmm, what number would be a good first guess?
</pre>
</font>
</center>
</form>
</body>
</html>
''' % (str(winningnumber))
    winningnumber=form.getvalue('winnumber')
    lowguess=form.getvalue('lowguess')
    highguess=form.getvalue('highguess')
    theguess=form.getvalue('anumber')
    numberguess=form.getvalue('numberguess')
    list=template.split('\n')
    gold=''
    gold2=''
    for x in list:
        if 'name="lowguess"' in x:
            gold=x
    for x in list:
        if 'name="highguess"' in x:
            gold2=x
    for x in list:
        if 'name="numberguess"' in x:
            gold3=x
    try:
        try:
            if int(theguess)<int(winningnumber):
                template=template.replace('BLANK', 'LOW')
                if int(theguess)>int(lowguess):
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % (str(theguess)))
                    lowguess=theguess
                    template=template.replace("HIGHERTHAN", lowguess)
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % (str(highguess)))
                    template=template.replace("LOWERTHAN", str(highguess))
                else:
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % (str(lowguess)))
                    template=template.replace("HIGHERTHAN", lowguess)
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % (str(highguess)))
                    template=template.replace("LOWERTHAN", str(highguess))
            if int(theguess)>int(winningnumber):
                template=template.replace('BLANK', 'HIGH')
                if int(theguess)<int(highguess):
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % (str(theguess)))
                    highguess=theguess
                    template=template.replace("LOWERTHAN", highguess)
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % (str(lowguess)))
                    template=template.replace("HIGHERTHAN", str(lowguess))
                else:
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % (str(highguess)))
                    template=template.replace("LOWERTHAN", highguess)
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % (str(lowguess)))
                    template=template.replace("HIGHERTHAN", str(lowguess))
            template=template.replace(gold3, '''
        <input type="hidden" name="numberguess" value="%s">
        ''' %(str(int(numberguess)+1)))
            if int(numberguess)+1<2:
                template=template.replace('NUMBERGUESS times', '1 time')
            else:
                template=template.replace('NUMBERGUESS', str(int(numberguess)+1))
            winningmessage='''
        <!DOCTYPE html>
        <html>
        <head>
        <title>You Win!</title>
        <style>
        .button {
        border: 2px solid black;
        background-color: white;
        padding: 14px 28px;
        font-size: 25px;
        cursor: pointer;
        display: inline-block;
        color: black;
        }
        .button:hover {
        background: gray;
        color: white;
        }
        </style>
        </head>
        <body background="bground.jpeg">
        <form method="get" action="number2.py">
        <center>
        <font size="6" style="font-family:fantasy"><b>You got it!</b><br>
        The correct number was <font color="indigo"><b>%s</b></font>.<br>
        You took <font color="red"><b>%s</b></font> guesses to get here.<br><br>
        <font size="6"><b><a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/extracred/number.py?">Restart The Game</a></b></font>
        </font>
        </center>
        </form>
        </body>
        ''' % (winningnumber, str(int(numberguess)+1))
            if int(numberguess)==0:
                winningmessage=winningmessage.replace('guesses', 'guess')
            if 'HIGHERTHAN' in template:
                print(winningmessage)
            else:
                print(template)
        except:
            if 0<int(winningnumber):
                template=template.replace('TOO BLANK', 'GUESS A NUMBER')
                if 0>int(lowguess):
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % ('0'))
                    lowguess=0
                    template=template.replace("HIGHERTHAN", lowguess)
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % (str(highguess)))
                    template=template.replace("LOWERTHAN", str(highguess))
                else:
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % (str(lowguess)))
                    template=template.replace("HIGHERTHAN", lowguess)
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % (str(highguess)))
                    template=template.replace("LOWERTHAN", str(highguess))
            if 0>int(winningnumber):
                template=template.replace('BLANK', 'HIGH')
                if 0<int(highguess):
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % ('0'))
                    highguess=0
                    template=template.replace("LOWERTHAN", highguess)
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % (str(lowguess)))
                    template=template.replace("HIGHERTHAN", str(lowguess))
                else:
                    template=template.replace(gold2, '''
        <input type="hidden" name="highguess" value="%s">
        ''' % (str(highguess)))
                    template=template.replace("LOWERTHAN", highguess)
                    template=template.replace(gold, '''
        <input type="hidden" name="lowguess" value="%s">
        ''' % (str(lowguess)))
                    template=template.replace("HIGHERTHAN", str(lowguess))
            template=template.replace(gold3, '''
        <input type="hidden" name="numberguess" value="%s">
        ''' %(str(int(numberguess))))
            if int(numberguess)<2:
                template=template.replace('NUMBERGUESS times', '1 time')
            else:
                template=template.replace('NUMBERGUESS', str(int(numberguess)))
            winningmessage='''
        <!DOCTYPE html>
        <html>
        <head>
        <title>You Win!</title>
        <style>
        .button {
        border: 2px solid black;
        background-color: white;
        padding: 14px 28px;
        font-size: 25px;
        cursor: pointer;
        display: inline-block;
        color: black;
        }
        .button:hover {
        background: gray;
        color: white;
        }
        </style>
        </head>
        <body background="bground.jpeg">
        <form method="get" action="number2.py">
        <center>
        <font size="6" style="font-family:fantasy"><b>You got it!</b><br>
        The correct number was <font color="indigo"><b>%s</b></font>.<br>
        You took <font color="red"><b>%s</b></font> guesses to get here.<br><br>
        <font size="6"><b><a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/extracred/number.py?">Restart The Game</a></b></font>
        </font>
        </center>
        </form>
        </body>
        ''' % (winningnumber, str(int(numberguess)+1))
            if int(numberguess)==0:
                winningmessage=winningmessage.replace('guesses', 'guess')
            if 'HIGHERTHAN' in template:
                print(winningmessage)
            else:
                if int(form.getvalue('numberguess'))>0:
                    print(template)
                else:
                    print(noinput1)
    except:
        print(noinput1)

main()
