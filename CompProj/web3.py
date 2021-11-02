#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()

print('Content-type: text/html\n')
def main():
    form=cgi.FieldStorage()
    template='''
<!DOCTYPE html>
<html><head>
<title>US History Review</title>
<style>
.bottom {
position: fixed;
right: 0;
bottom: 0;
height: 30;
width: 100%;
color: black;
text-align: center;
}
#topbutton {
display: none;
position: fixed;
bottom: 30px;
right: 30px;
z-index: 99;
border: none;
outline: black;
background-color: burlywood;
color: black;
cursor: pointer;
padding: 15px;
border-radius: 10px;
font-size: 25px;
}
#topbutton:hover {
background-color: tan;
}
.button {
color: black;
border: 2px solid black;
background-color: wheat;
padding: 2px 28px;
font-size: 25px;
cursor: pointer;
display: inline-block;
}
.button:hover {
background: gray;
color: wheat;
}
</style></head><body style="background-color:tan;">
<button onclick="topFunction()" id="topbutton" title="Return to the top">Return To Top</button>
<a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistory2.html"><font size="6"><b>Go Home</b></font></a><br>
<a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistoryTimeline.html"><font size="6"><b>Back To Timeline</b></font></a>
<div style="background-color:wheat">
<font size="5">
meat
</font>
<br><br>
</div>
<br><br><br>
<div class="bottom">
<button type="button" onclick="alert('Wikipedia, HISTORY, etc.')">The Main Sources I Used</button>
</div>
<script>
window.onscroll = function() {scroll()};
function scroll() {
if (document.body.scrollTop>100 || document.documentElement.scrollTop > 100) {
document.getElementById("topbutton").style.display="block";
} else {
document.getElementById("topbutton").style.display="none";
}}
function topFunction() {
document.body.scrollTop = 0;
document.documentElement.scrollTop = 0;
}
</script>
</body></html>
'''
    error='''
<!DOCTYPE html>
<html><head>
<title>Go Back</title>
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
</head><body style="background-color:tan;">
<center>
<font size="5"><h1>You didn't fill in any checkboxes.</h1>
<a class="button" style="text-decoration:none" href="http://homer.stuy.edu/~cye10/CompProj/USHistoryTimeline.html"><font size="6">Go back.</font></a></font>
</center>
</body></html>
'''
    americanrevolution='''
<center><h1>American Revolution</h1>
<img src="americanrevolution.jpeg" alt="americanrevolution" height="400" width="687"><br>
<font size="4"><i>George Washington crossing the Delaware</i></font></center>
<p>
The American Revolution was an armed revolution in which the North American British colonies, the Americans, fought for independence from Great Britain.<br>
The war, which lasted from 1765 to 1783, resulted in an American victory, creating the United States of America.<br><br>
The Americans revolted primarily because of "taxation without representation".<br>
In other words, heavy taxes were imposed upon the colonies without their consent, leading to widespread outrage.<br>
Protests were met with stricter laws set by the English Parliament, eventually reaching a boiling point at Lexington and Concord, the firefight that started the Revolutionary War.<br>
After a grueling struggle, the Americans defeated the British against all odds and proceeded to build a new nation.<br>
To prevent future corruption, the Constitution and Bill of Rights were created.<br>
The rest is history...
</p>
meat
'''
    louisianapurchase='''
<center><h1>Louisiana Purchase</h1>
<img src="louisianapurchase.jpeg" alt="louisianapurchase" height="400" width="566"><br>
<font size="4"><i>A map displaying the amount of land America received</i></font></center>
<p>
The Louisiana Purchase was an agreement between the United States and France in 1803.<br>
Thomas Jefferson, the President at the time, bought the Louisiana territory from Napoleon for 15 million dollars, 300 million in today's currency.<br>
The land we obtained is illustrated in the map shown above, essentially doubling the size of America at the time.<br>
This purchase of land was essential to the growth of our nation and allowed us to pursue manifest destiny.<br>
Furthermore, it allowed us to gain control of the Mississippi River, giving us a crucial port for trading.
</p>
meat
'''
    warof1812='''
<center><h1>War of 1812</h1>
<img src="warof1812.jpeg" alt="warof1812" height="400" width="566"><br>
<font size="4"><i>General Andrew Jackson at the Battle of New Orleans</i></font></center>
<p>
The War of 1812 was essentially a rematch against the British in 1812, which we also won.<br><br>
Some people see the war as a side conflict between Britain and France in the Napoleonic Wars.<br>
Britain had imposed a naval blockade to stop neutral trade to France, including from America.<br>
Despite complaints that this act was against international law, the British persisted.<br>
The Little Belt affair made situations worse, in which an American warship defeated a British warship, seemingly in self-defense.<br>
In response, Britain supplied Native Americans along America's western frontier, who attacked American settlers, halting expansion.<br>
As a result, James Madison, the President at the time, declared war against the British.<br>
The British tried many times to invade the United States homefront, but to no avail.<br>
One notable event was when Americans defended Fort McHenry in Maryland.<br>
It was here when Francis Scott Key was awestruck by the American flag still standing after a grueling defense.<br>
He proceeded to write the poem, "The Star-Spangled Banner", which would later become the United States national anthem. 
</p>
meat
'''
    mexicanamericanwar='''
<center><h1>Mexican-American War</h1>
<img src="mexicanamericanwar.jpeg" alt="mexicanamericanwar" height="400" width="612"><br>
<font size="4"><i>Battle of Palo Alto, the first major battle of the war</i></font></center>
<p>
The Mexican-American War was the first United States conflict mainly fought in a foreign country.<br>
The war was between Mexico and America from 1846 to 1848.<br>
The war began when Texas gained its independence from Mexico, so the United States considered annexing it.<br>
When U.S. President James K. Polk's offer to buy Texas, Oregon, California, etc was denied, he moved troops into Mexican territory to instigate a fight.<br>
Mexican soldiers attacked the U.S. soldiers, but the Americans were able to achieve victory.<br>
The United States officially declares war against Mexico and advance into their country.<br>
After a hard-fought war, the Americans win, and the Treaty of Guadalupe Hidalgo officially end the conflict.<br>
As part of the treaty, the United States received a lot of land, including Texas and California.
</p>
meat
'''
    civilwar='''
<center><h1>Civil War</h1>
<img src="civilwar.jpeg" alt="civilwar" height="400" width="713"><br>
<font size="4"><i>Battle of Franklin, an incredible disaster for the Confederacy</i></font></center>
<p>
Before the American Civil War (Civil War), which continued from 1861 to 1865, controversy over the morality and acceptability of slavery was widespread.<br>
The North, later called the Union, opposed slavery, while the South, later called the Confederacy, supported it.<br>
Furthermore, the Confederate States upheld the belief in states' rights to uphold slavery and secede if desired.<br>
Tensions increased after territorial disputes, such as Bleeding Kansas, which finally reached a boiling point after Abraham Lincoln was elected.<br>
The South feared Lincoln would stop slavery and promote the North, leading to their secession from the United States.<br>
The Civil War that followed seemed to be evenly matched, with outstanding leaders from both sides.<br>
For example, the Confederacy had Robert E. Lee, "Stonewall" Jackson, and Nathan Bedford Borrest.<br>
On the other hand, the Union had Ulysses S. Grant, William SHerman, and Philip Sheridan.<br>
After a long war with many unexpected turns, the Civil War <i>effectively</i> ends when General Robert E. Lee (Confederacy) surrenders to Genereal Ulysses S. Grant (Union) in 1865.<br>
After the war, Reconstruction took place, which was the repairment of the broken South. 
</p>
meat
'''
    spanishamericanwar='''
<center><h1>Spanish-American War</h1>
<img src="spanishamericanwar.jpeg" alt="spanishamericanwar" height="400" width="524"><br>
<font size="4"><i>American soldiers at the Battle of Las Guasimas</i></font></center>
<p>
The Spanish-American War was a conflict between Spain and the United States in 1898.<br>
Before the war, Spain had been brutally oppressing Cubans who were fighting for independence.<br>
This authoritarianism was broadcasted to American citizens, who sympathized with the Cubans.<br>
The war began when the USS Maine, an American ship, mysteriously blew up, killing hundreds.<br>
This was immediately pinned on the Spanish in newspapers, leading to The U.S. Congress declaring war on Spain.<br>
The war that ensued was very one-sided. Simply put, the Americans very easily defeated the Spanish, ending the war in less than a year.<br>
It was in this war that Theodore Roosevelt became well-known.<br>
He was the second-in-command of the Rough Riders, the only U.S. regiment to have seen action in the war.
</p>
meat
'''
    ww1='''
<center><h1>World War 1</h1>
<img src="ww1.jpeg" alt="ww1" height="400" width="685"><br>
<font size="4"><i>Soldiers wearing gas masks and equipped with machine guns</i></font></center>
<p>
World War 1, dubbed "The Great War" at the time, was a worldwide conflict between multiple countries from 1914 to 1918.<br><br>
Before the war started, there were already tensions between the Austrians and Serbians.<br>
When a Serbian nationalist assassinated Archduke Franz Ferdinand of Austria, all hell broke loose.<br>
Nations quickly began constructing alliances. When this was done, there were two distinct sides of the war.
The Allies mainly consisted of Britain, France, Russia, and Serbia.<br>
The Central Powers consisted of Germany, Ottoman Empire, and Austria-Hungary.<br>
Originally thought to be a short war, soldiers quickly realized with the introduction of new technology, trench warfare, and chemical weapons, this war would be an uphill struggle.<br>
As the Central Powers were stampeding through neighboring countries, America had been trading with the Allies as a neutral nation.<br>
After the Germans sunk the Lusitania, an apparent passenger ship, United States citizens became outraged.<br>
In 1917, America intercepted the Zimmermann Telegram, a letter sent from Germany to Mexico.<br>
The letter attempted to persuade Mexico to join the Central Powers and attack the United States.<br>
The United States quickly joined the Allies. The Allies eventually won, and the Treaty of Versailles officially ended the war.
</p>
meat
'''
    ww2='''
<center><h1>World War 2</h1>
<img src="ww2.jpeg" alt="ww2" height="400" width="515"><br>
<font size="4"><i>American soldiers capture the Japanese island of Iwo Jima</i></font></center>
<p>
World War 2 was a worldwide conflict between multiple countries from 1939 to 1945.<br><br>
After World War 1, Germany was humiliated and economically damaged by the Treaty of Versailles.<br>
Full of spite and hatred, Adolf Hitler, a German nationalist, quickly captivated the hearts of Germans with promises of glory.<br>
He led the German army, the Nazis, on a rampage through its neighbors, aided by Italy and Japan.<br>
These three countries mainly formed the Axis. Britain and China originally formed the Allies.<br>
Along with their acquisition of land, or Lebensraum, the Nazis committed a genocide against Jews, called the Holocaust.<br>
The Axis were winning when Hitler went against a truce and foolishly decided to backstab the Soviet Union.<br>
Because of this act of betrayal, the Soviet Union joined the Allies.<br>
Furthermore, Japan chose to bomb America, who was neutral at the time, in 1941.<br>
Japan launched an attack on Pearl Harbor, Hawaii to weaken the American navy.<br>
Because of this, the United States joined the Allies.<br>
With help from the United States and the Soviet Union, the Allies pushed the Axis back.<br>
In 1945, the United States unleashed the world's first two atomic bombs on Japan, effectively ending the war.<br>
After the war, Germany was divided and Japan was instilled with democratic values by America.
</p>
meat
'''
    coldwar='''
<center><h1>Cold War</h1>
<img src="coldwar.jpeg" alt="coldwar" height="400" width="931"><br>
<font size="4"><i>Capitalist propaganda targeting communism</i></font></center>
<p>
The Cold War was not an actual war, but rather, a period of increased tensions between the United States and the Soviet Union from 1947 to 1991.<br>
Tensions were high because of a difference in ideologies and the attainment of nuclear weapons by both countries.<br>
The United States supported capitalism, while the Soviet Union supported communism.<br>
As a result, the United States tried to stop the spread of communism, a policy called "containment".<br>
This involved interfering with foreign affairs, which led to proxy wars between America and the Soviet Union.<br>
Furthermore, both nations competed to attain better technology in a show of power.<br>
This led to events such as the Space Race, in which both countries tried to accomplish more than each other in space exploration.<br>
Meanwhile, as all this was occuring, the Red Scare plagued America.<br>
The Red Scare was a period of widespread fear of the rise of communism in our country.<br>
Another notable conflict was the Cuban Missile Crisis, in which the Soviet Union stored missiles in nearby Cuba.<br>
This frightened the American public, almost leading to the start of an actual war.<br>
The Cold War effectively ended when Mikhail Gorbachev, former leader of the Soviet Union, tore down the Berlin Wall.<br>
The Berlin Wall was a physical symbol of the conflict, so when Gorbachev took it down and established reforms, tensions dramatically lessened.
</p>
meat
'''
    koreanwar='''
<center><h1>Korean War</h1>
<img src="koreanwar.jpeg" alt="koreanwar" height="400" width="500"><br>
<font size="4"><i>An American soldier comforts a soldier whose friend was killed in South Korea</i></font></center>
<p>
The Korean War was a war between North Korea and South Korea, similar to the upcoming Vietnam War.<br>
This conflict lasted from 1950 to 1953, with the Soviet Union and China backing the North and the United Nations backing the South.<br>
The war started when North Korean soldiers crossed the 38th Parallel, the line dividing the Korean peninsula, and invaded South Korea.<br>
They eventually captured Seoul, the South Korean capital, prompting the United Nations to respond.<br>
America intervened and pushed the North Koreans back to the 38th Parallel.<br>
However, the famous General Douglas MacArthur insisted on liberating North Korea from its communists.<br>
This led to an American offensive, pushing North Korean forces farther.<br>
Eventually, China essentially demanded for the United States to stop, much to MacArthur's disapproval.<br>
After negotiations, both sides agreed to an armistice and to draw a new boundary close to the original 38th Parallel.<br>
The Korean region remains divided to this day.
</p>
meat
'''
    vietnamwar='''
<center><h1>Vietnam War</h1>
<img src="vietnamwar.jpeg" alt="vietnamwar" height="400" width="709"><br>
<p>
<font size="4"><i>An American Sergeant overlooking his fallen companion</i></font></center>
The Vietnam War was mainly a war between North Vietnam, supported by the Soviet Union and China, and South Vietnam, supported by the United States.<br>
This conflict lasted from 1955 to 1975, and was similar to the previous Korean War.<br>
Before the war, North and South Vietnam were separated by the Geneva Accords.<br>
The North was led by Ho Chi Minh, a communist leader, while the South was led by Ngo Dinh Diem, a dictator backed by the United States.<br>
Diem's popularity diminished due to his favoritism of Catholics, persecution of Buddhists, and corruption.<br>
After his death in a coup, the United States got more involved in the conflict between the two Vietnams.<br>
The United States began cracking down on the Vietcong, North Vietnamese guerilla fighters who were attacking South Vietnam.<br>
The Vietcong proved to be a challenge due to their nation's support and their guerilla tactics.<br>
However, back in America, the public <i>heavily</i> protested U.S. involvement in Vietnam.<br>
This, on top of the Tet Offensive, which was a series of assaults against South Vietnam, persuaded America to withdraw.<br>
In a process called Vietnamization, the United States slowly withdrew its troops from the conflict.<br>
Once we left, North Vietnam conquered Saigon, the South Vietnamese capital, renaming the unified Vietnam the Socialist Republic of Vietnam.<br>
The Sovialist Republic of Vietnam remains unified and under hardline communist rule to this day.
</p>
meat
'''
    nineeleven='''
<center><h1>September 11 Attacks</h1>
<img src="nineeleven.jpeg" alt="nineeleven" height="400" width="552"><br>
<font size="4"><i>A second plane approaches the North Tower</i></font></center>
<p>
On September 11, 2011, al-Qaeda launched a giant terrorist attack against the United States.<br>
Four passenger planes were hijacked and headed for major governmental centers.<br>
Two of the pasenger planes crashed into the Twin Towers in Manhattan, New York.<br>
This resulted in the deaths of thousands of civilians.<br>
Another airplane crashed into the side of the Pentagon.<br>
The final airplane was headed for the White House, but ended up crashing in Pennsylvania because the passengers fought back.<br>
These attacks devastated the American public and left them feeling vulnerable.<br>
People were scared that something like this could happen again.<br>
As a result of the September 11 Attacks, nations banded together to aid the United States in our following War on Terror.
</p>
meat
'''
    waronterror='''
<center><h1>War On Terror</h1>
<img src="waronterror.jpeg" alt="waronterror" height="400" width="547"><br>
<font size="4"><i>Americans invade Afghanistan</i></font></center>
<p>
The War on Terror is a series of international military campaigns initiated by the United States.<br>
After the September 11 Attacks, many nations united to aid America in its pursuit to end terrorism and to ensure a similar event doesn't happen again.<br>
Most of these campaigns took place in the Middle East, against Arab nations and terrorist groups.<br>
During the War on Terror, Osama bin Laden, leader of al-Queda and orchestrator of the September 11 Attacks, was shot and killed by U.S. Navy SEALs.<br>
In 2013, the War on Terror began to end, the Islamic State of Iraq and Syria (ISIS), a terrorist group, sprung up, leading to new campaigns to end it.<br>
Because of this, the War on Terror is still ongoing.
</p>
meat
'''
    if form.getvalue('americanrevolution')=='yes':
        template=template.replace('meat', americanrevolution)
    if form.getvalue('louisianapurchase')=='yes':
        template=template.replace('meat', louisianapurchase)
    if form.getvalue('warof1812')=='yes':
        template=template.replace('meat', warof1812)
    if form.getvalue('mexicanamericanwar')=='yes':
        template=template.replace('meat', mexicanamericanwar)
    if form.getvalue('civilwar')=='yes':
        template=template.replace('meat', civilwar)
    if form.getvalue('spanishamericanwar')=='yes':
        template=template.replace('meat', spanishamericanwar)
    if form.getvalue('ww1')=='yes':
        template=template.replace('meat', ww1)
    if form.getvalue('ww2')=='yes':
        template=template.replace('meat', ww2)
    if form.getvalue('coldwar')=='yes':
        template=template.replace('meat', coldwar)
    if form.getvalue('koreanwar')=='yes':
        template=template.replace('meat', koreanwar)
    if form.getvalue('vietnamwar')=='yes':
        template=template.replace('meat', vietnamwar)
    if form.getvalue('911')=='yes':
        template=template.replace('meat', nineeleven)
    if form.getvalue('waronterror')=='yes':
        template=template.replace('meat', waronterror)
    if form.getvalue('americanrevolution')!='yes' and form.getvalue('louisianapurchase')!='yes' and form.getvalue('warof1812')!='yes' and form.getvalue('waronterror')!='yes' and form.getvalue('mexicanamericanwar')!='yes' and form.getvalue('civilwar')!='yes' and form.getvalue('spanishamericanwar')!='yes' and form.getvalue('ww1')!='yes' and form.getvalue('ww2')!='yes' and form.getvalue('coldwar')!='yes' and form.getvalue('koreanwar')!='yes' and form.getvalue('vietnamwar')!='yes' and form.getvalue('911')!='yes':
          print(error)
    else:
        print(template.replace('meat',''))
main()
