#!/usr/bin/python3
import cgi
import cgitb
import random
cgitb.enable()

response='''
<!DOCTYPE html>
<html>
<head>
<title>Your Results</title>
<style>
.button {
color: black;
border: 2px solid black;
background-color: white;
padding: 3px 28px;
font-size: 25px;
cursor: pointer;
display: inline-block;
}
.button:hover{
background: gray;
color: white;
}
</style>
</head>
<body background="index2.jpeg">
<form method="get" action="findresults.py"><br>
<a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistory2.html"><font size="6"><b>Go Home</b></font></a>
<center>
<hr width="100%" size="2">
<font size="10" color=#1E6591><b>presidentname</b></font><br>
<img src="picture" alt="President" width="400" height="480"><br>
<p><font size="6">explanation</font></p>
<font size="7" color="red"><a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistoryQuiz.html">Unhappy with your result? Take it again!</a></font>
<br><br><br></center>
</form>
</body>
</html>
'''

print('Content-type: text/html\n')
def main():
    form=cgi.FieldStorage()
    a=form.getvalue('characteristic')
    b=form.getvalue('flaw')
    c=form.getvalue('party')
    d=form.getvalue('leader')
    e=form.getvalue('killchoice')
    f=form.getvalue('shirtchoice')
    g=form.getvalue('drink')
    h=form.getvalue('army')
    i=form.getvalue('bully')
    washington=0
    jefferson=0
    jackson=0
    lincoln=0
    grant=0
    fdr=0
    jfk=0
    nixon=0
    reagan=0
    obama=0
    trump=0
    q1=False
    q2=False
    q3=False
    q4=False
    q5=False
    q6=False
    q7=False
    q8=False
    q9=False
#Question1(GoodQuality)
    if 3==3:
        if a=='brave':
            jackson+=1
            trump+=1
            nixon+=1
            q1=True
        if a=='kind':
            washington+=1
            obama+=1
            q1=True
        if a=='resilient':
            lincoln+=1
            grant+=1
            reagan+=1
            q1=True
        if a=='charming':
            fdr+=1
            jfk+=1
            q1=True
        if a=='talented':
            jefferson+=1
            lincoln+=1
            q1=True
#Question2(BadQuality)
        if b=='stubborn':
            washington+=1
            lincoln+=1
            reagan+=1
            q2=True
        if b=='unstable':
            jackson+=1
            trump+=1
            q2=True
        if b=='ignorant':
            jefferson+=1
            obama+=1
            q2=True
        if b=='weakwilled':
            grant+=1
            fdr+=1
            q2=True
        if b=='manipulative':
            jfk+=1
            nixon+=1
            q2=True
#Question3(Party)
        if c=='democrat':
            jackson+=1
            fdr+=1
            jfk+=1
            obama+=1
            q3=True
        if c=='republican':
            lincoln+=1
            grant+=1
            nixon+=1
            reagan+=1
            trump+=1
            q3=True
        if c=='other':
            washington+=1
            jefferson+=1
            q3=True
        if c=='none':
            q3=True
#Question4(ResponseToAttack)
        if d=='r1':
            jackson+=1
            trump+=1
            q4=True
        if d=='r2':
            washington+=1
            jefferson+=1
            grant+=1
            nixon+=1
            reagan+=1
            q4=True
        if d=='r3':
            lincoln+=1
            fdr+=1
            jfk+=1
            obama+=1
            q4=True
        if d=='r4':
            q4=True
#Question5(KillSomeone)
        if e=='yes':
            jefferson+=1
            jackson+=1
            grant+=1
            nixon+=1
            q5=True
        if e=='no':
            washington+=1
            lincoln+=1
            fdr+=1
            jfk+=1
            reagan+=1
            obama+=1
            trump+=1
            q5=True
#Question6(Shirt)
        if f=='yes':
            washington+=1
            jackson+=1
            nixon+=1
            reagan+=1
            trump+=1
            q6=True
        if f=='middle':
            jefferson+=1
            grant+=1
            fdr+=1
            q6=True
        if f=='no':
            lincoln+=1
            jfk+=1
            obama+=1
            q6=True
#Question7(Drink)
        if g=='water':
            jefferson+=1
            nixon+=1
            obama+=1
            q7=True
        if g=='soda':
            jfk+=1
            trump+=1
            q7=True
        if g=='juice':
            jackson+=1
            lincoln+=1
            q7=True
        if g=='wine':
            washington+=1
            grant+=1
            fdr+=1
            nixon+=1
            q7=True
#Question8(Army)
        if h=='yes':
            washington+=1
            jackson+=1
            grant+=1
            q8=True
        if h=='maybe':
            jefferson+=1
            lincoln+=1
            fdr+=1
            nixon+=1
            reagan+=1
            q8=True
        if h=='no':
            jfk+=1
            trump+=1
            q8=True
#Question9(Bully)
        if i=='console':
            lincoln+=1
            fdr+=1
            reagan+=1
            q9=True
        if i=='snitch':
            jefferson+=1
            jfk+=1
            obama+=1
            q9=True
        if i=='verbal':
            washington+=1
            grant+=1
            nixon+=1
            q9=True
        if i=='fight':
            jackson+=1
            trump+=1
            q9=True
        if i=='nothing':
            q9=True
        results=[[washington, 'George Washington'],[jefferson,'Thomas Jefferson'],[jackson,'Andrew Jackson'],
                 [lincoln,'Abraham Lincoln'],[grant,'Ulysses S. Grant'],[fdr,'Franklin D. Roosevelt'],[jfk,'John F. Kennedy'],
                 [nixon,'Richard Nixon'],[reagan,'Ronald Reagan'],[obama,'Barack Obama'],[trump,'Donald J. Trump']]
        if q1 and q2 and q3 and q4 and q5 and q6 and q7 and q8 and q9:
            maxnumber=0
            for i in range(11):
                if results[i][0]>maxnumber:
                    maxnumber=results[i][0]
            possiblewinners=[]
            for i in range(11):
                if results[i][0]==maxnumber:
                    possiblewinners.append(results[i][1])
            winner=random.choice(possiblewinners)
            response2=response.replace('picture', winner+'.jpeg')
            response3=response2.replace('presidentname', winner)
            if winner=="George Washington":
                cullen='''
You are a natural leader, unswayed by peer pressure and other forms of negativity.<br>Your honor and character are shown through your ability to
push through obstacles and maintain your humility while doing so.<br>You're like a shepherd, always looking out for the little guy and protecting
your loved ones, no matter the difficulty.<br>You tend to choose the path others wouldn't take: the path that leads to success.<br>Although your pride
may blind you sometimes, you ultimately maintain your humility.
'''
            if winner=="Thomas Jefferson":
                cullen='''
Ambitious in life, you're always looking to learn new things.<br>You try to diversify your fields of expertise, and as such, you are very talented.<br>
Leading is also another talent of yours. You always want to lift people up and help them push their boundaries, like you have.<br>
Although your ambition may lead you to make foolish choices sometimes, you have learned to pick yourself up after every mishap.<br>
Despite this, people still tend to look up to you.
'''
            if winner=="Andrew Jackson":
                cullen='''
Simply put, you're a person of action. When troubles come your way, you confront them directly and overcome them.<br>If others are facing
difficulties of their own, you do not hesitate to beat their obstacles <i>for</i> them.<br>When you are asked to complete a task, you
get the job done efficiently.<br>Although some may see you as hardheaded or emotionless, most see you as a tough protector who stands
up for the little guys.
'''
            if winner=="Abraham Lincoln":
                cullen='''
You're an extremely kind individual, although you may be too humble to admit this.<br>Although potentially introverted at times, you still
have a warm soul.It's a shame not everybody knows about it.<br>Whenever you're given a chance to help, you do not hesitate to do so.<br>However,
your compassion and love for others may be seen by others as a weakness.<br>As such, you may be pushed around by people, but you never let it
get to you.<br>Many continue to see you as a silent protector, and others may see you as a gentle giant.
'''
            if winner=="Ulysses S. Grant":
                cullen='''
One perfect word to describe you is 'honorable'.<br>Your honor and nobility is shown through everything you do.<br>Your internal moral compass is
incredibly strong, and as such, you can easily distinguish between right and wrong.<br>You always try to right the wrongs in the world.
However, sometimes you tend to prioritize the problems around you more than your own health.<br>Despite this, your strong work ethic
and your never-give-up attitude allows you to overcome any obstacle.
'''
            if winner=="Franklin D. Roosevelt":
                cullen='''
You are an exemplar of a good friend.<br>You are always there for others, consoling them through the toughest of times.<br>Your words truly
comfort those who hear them, lightening up any situation.<br>Most people deem you trustworthy, and are willing to share their secrets and
problems with you.<br>They know you legitimately care about their concerns.<br>Although your ego/self esteem may be delicate at times,
you will always have people who will be there for you, in repayment for what you have done for them.
'''
            if winner=="John F. Kennedy":
                cullen='''
You're every friend group's party animal.<br>You know how to have fun, and your charming and witty attitude makes every environment
entertaining.<br>Your charm is loved by all, and you tend to like being in the center of attention.<br>Many of those around you strive to be
just like you.<br>As a result of your exuberance, you sometimes act irresponsibly, neglecting important people or things in your
life.<br>However, you always manage to pull through and fix your errors.
'''
            if winner=="Richard Nixon":
                cullen='''
You're a very complex person, and as a result, many find you interesting.<br>People go out of their way to talk to you, and many
find that you're a very likeable person.<br>Your unique qualities stand out and complement the personalities of others.<br>However,
you may find yourself manipulating others subconciously.<br>Despite this, you typically suppress such behavior and continue
to be the best person you can be.
'''
            if winner=="Ronald Reagan":
                cullen='''
You are a person who never gives up.<br>Your determination to accomplish what needs to be done is unparalleled, and you tend to
go out of your way to do simple things.<br>Those around you admire your steadfastness, and you purposefully use yourself as a
good role model for them.<br>Because of your constant resolve, you may encounter a lot of criticism from others.<br>Fortunately,
you don't let it get in the way of your path to success.
'''
            if winner=="Barack Obama":
                cullen='''
You are someone who is always reliable and approachable.<br>Whenever people need help with something, they come
to you first, and you don't hesitate in offering your aid.<br>You are the complete opposite of intimidating, and your friendliness
is very evident to all who meet you.<br>However, just because you try to help everyone doesn't mean you can.<br>Nevertheless, you've learned to
acknowledge your faults and continue moving on.
'''
            if winner=="Donald J. Trump":
                cullen='''
You are someone who is extremely bold. Never afraid to voice your opinion, your bravery is displayed to others on a daily basis.<br>You
always try to speak up for those who can't speak for themselves, and you're naturally commanding.<br>Your pursuits for concrete
solutions to every problem is very admirable.<br>Although some may call you rash, you always brush it off, knowing your 'rashness' is
simply being confused for fervor.
'''
            print(response3.replace('explanation', cullen))
#######################################
        else:
            print('''
<!DOCTYPE html>
<html>
<head><title>Go Back</title>
<style>
.button {
color: black;
border: 2px solid black;
background-color: skyblue;
padding: 5px 28px;
font-size: 25px;
cursor: pointer;
display: inline-block;
}
.button:hover{
background: gray;
}
</style>
</head>
<body style="background-color:powderblue;">
<font size="5" style="font-family:helvetica"><center><h1>You didn't answer all the questions.</h1><br>
<a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistoryQuiz.html">Go back</a></font>
</center></body></html>
''')
#Washington, Jefferson, Jackson, Lincoln, Grant,
#FDR, JFK, Nixon, Reagan, Obama, Trump

main()
