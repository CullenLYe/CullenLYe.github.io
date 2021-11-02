#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()

message='''
<!DOCTYPE html>
<html>
<head>
<title>About Page</title>
<style>
.button {
color: black;
border: 2px solid black;
background-color: white;
padding: 1px 28px;
font-size: 25px;
cursor: pointer;
display: inline-block;
}
.button:hover {
background: gray;
color: white;
}
</style>
</head>
<body background="index2.jpeg">
<a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistory2.html"><font size="6"><b>Go Home</b></font></a>
<font size="5">
<h1 style="font-family:helvetica"><center>About My Website</center></h1>
<p>Hello, my name is <u>Cullen Ye</u>! For my final project for Computer Science in 10th grade, I was told to make an interactive website, essentially about anything. I thought about it for a while and settled on the idea of
American History. While that may seem like a bizaare choice for most, I'm <i>extremely</i> fond about America, and because of my passion, I worked endlessly and tirelessly to finish this
website from scratch to showcase our country. <b>Endless nights of research and hard work has been put into this for weeks</b>, so I can safely say that <u>all the information presented here is 100% accurate</u>. Although this isn't perfect, I believe it turned out better than I
had envisioned. <u>Overall, it was a blast coding this.</u><br><br>
<center>Special thanks to <b>Mr. Brooks</b>, my 10th grade Computer Science teacher for teaching me HTML, Python, etc, and for getting me into coding. I'm <i>very</i> grateful.</center></p>
</font>
</body>
</html>
'''
print('Content-type: text/html\n')
def main():
    print(message)
main()
