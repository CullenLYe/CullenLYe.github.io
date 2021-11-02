#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()

greetings='''
<!DOCTYPE html>
<html>
<head>
<title> Greetings! </title>
<style>
.button {
color: black;
border: 2px solid black;
background-color: beige;
padding: 7px 20px;
font-size: 25px;
cursor: pointer;
display: inline-block;
}
.button:hover{
background: gray;
color: beige;
}
</style>
</head>
<body background="index.jpeg">
<form method="get" action="continue.py"><br/>
<h1><center><font size="7" style="font-family:helvetica" color=#154360>Welcome to my website buddy!</font></center><br/></h1>
<font size="5"><h3>This website is meant to show the history of the
<u><font color="red">United</font> <font color="blue">States</font>
<font color="red">of</font> <font color="blue">America</font></u>
in a comprehensible and educational way.<br/>
Since you're in age grade,</h3></font><br/>
<center><a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistory2.html"><font size="7"><b>Continue</b></font></a></center>
</form>
</body>
</html>
'''

error='''
<!DOCTYPE html>
<html>
<head>
<style>
.goback {
color: midnightblue;
border: 2px solid black;
background-color: skyblue;
padding: 14px 28px;
font-size: 25px;
cursor: pointer;
display: inline-block;
}
.goback:hover{
background: midnightblue;
color: lightblue;
}
</style>
<title>Go Back</title>
</head>
<body style="background-color:lightblue;">
<br><br>
<font size="8"><center><a class="goback" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistory.html">
Go back and fill in the name box.</a></center></font></body></html>
'''

print('Content-type: text/html\n')
def main():
    form=cgi.FieldStorage()
    test=form.getvalue('buddy')
    try:
        new1=greetings.replace('buddy', test)
        a=form.getvalue('age')
        if a!="none":
            new2=new1.replace('age', a)
            if a=='9th':
                print(new2.replace('grade,',"grade, you will likely be taking US History in two years, so my website may be very useful for you to start studying now!"))
            if a=='10th':
                print(new2.replace('grade,',"grade, you are probably taking US History next year, so my website may be very useful for you to get a headstart now!"))
            if a=='11th':
                print(new2.replace('grade,',"grade, you're probably taking US History right now. If you ever feel your grades dropping, or if you just need extra review, drop by my website!"))
            if a=='12th':
                print(new2.replace('grade,',"grade, you probably finished the US History course. Either way, if you are ever bored or just have a passion for American History, feel free to drop by this website!"))
        else:
            print(new1.replace("Since you're in age grade,", "Even though you're not in high school, this website may still be fun for you if you are ever bored or just have a passion for American History!"))
    except:
        print(error)
main()
