<!-- S01 -->
You open a terminal.
Someone walks past.
They see a black screen
covered in mysterious text.
And suddenly...

<!-- S02 -->
"Oh my god! You're hacking!"

<!-- S03 -->
Well...
Maybe.
Or maybe you are just trying to find out
why the server is down.

<!-- S04 -->
Today we are going to look at why
terminals and hacking have become
almost the same thing in popular culture.
And, more importantly...
what hacking actually looks like.

<!-- S05 -->
For most people, a computer has buttons.
You click something.
Something happens.
Then there is the terminal.
No buttons.
No friendly messages.
Just this.
And that is terrifying.

<!-- S06 -->
A graphical interface might say:
delete user.
A terminal says this instead.

<!-- S07 -->
To an experienced Linux user,
that is perfectly ordinary.
To everyone else, it looks like
you are about to launch a missile.

<!-- S08 -->
There is actually a historical reason
for the way it looks.
Early computers had no graphical interface.
People talked to them through text terminals.

<!-- S09 -->
And those terminals had dark screens
with green or amber phosphor text.
That was not an attempt to look cool.
It was simply how the technology worked.

<!-- S10 -->
But then film and television
noticed something useful.
A black screen full of
rapidly changing text looks technical.
And, more importantly...
it looks complicated.

<!-- S11 -->
You do not need to understand
what the characters mean.
You just see this.
And your brain decides:
this person is doing something illegal.

<!-- S12 -->
Hollywood has developed a remarkably
consistent language for hacking.
The hacker sits in a dark room.
There are six monitors.

<!-- S13 -->
The room is lit entirely by the monitors.
Nobody has turned the lights on.
The hacker starts typing
at roughly nine hundred words a minute.

<!-- S14 -->
Text flies across the screen.
A progress bar appears.
Ninety-seven per cent.
Ninety-eight.
Ninety-nine.
And finally, one hundred.
The hacker leans back.
And says...

<!-- S15 -->
"I'm in."

<!-- S16 -->
That is not how most
computer security incidents work.
Let us imagine the real conversation.
"I am going to hack this server."
And the server answers:
permission denied.

<!-- S17 -->
"Oh."
Tries again.
Permission denied.
Checks the password.

<!-- S18 -->
Reads the documentation.
Searches the error message.
Eventually discovers that the administrator
turned off password logins six months ago.

<!-- S19 -->
"Right."

<!-- S20 -->
Computers are remarkably good at making you
spend twenty minutes discovering that you
forgot one character in a configuration file.

<!-- S21 -->
On one side of the screen:
system administrator.
On the other:
hacker.
The same tools can appear on both.
That is because the terminal
is not a hacking tool.
It is an interface.

<!-- S22 -->
You can use it to run a server,
read logs, copy files, install software,
or work out what broke at three in the morning.

<!-- S23 -->
Or, depending on what you are doing
and whether you have permission,
you can use it for security testing.
Or for an attack.

<!-- S24 -->
The tool does not tell you
which one you are doing.
A screwdriver can repair a computer.
It can also destroy one.
The screwdriver is not the criminal.

<!-- S25 -->
So what actually is a hacker?
The word has a much older history
than modern cybercrime.

<!-- S26 -->
Originally, a hacker was someone
who liked to explore systems
and could find unexpected solutions.

<!-- S27 -->
Over time, the word became attached
to computer security.
And today, when someone says
"he is a hacker", they might mean

<!-- S28 -->
a security researcher,
a penetration tester,
a genuine attacker,
or simply someone who knows
an alarming amount about Linux.
Usually the context helps.

<!-- S29 -->
Now let us look at our picture again.
The caption says:
you hacked it.
And look at her screens.

<!-- S29b -->
On one of them, something like nmap.
On the other, something that looks
even more suspicious.
Slash etc slash passwd.

<!-- S30 -->
To someone who does not know Linux,
she is clearly breaking into the Pentagon.
To a system administrator, she is checking
the network and reading a list of accounts.

<!-- S31 -->
And that is where the joke comes from.
The woman may not be hacking anything at all.
She might just be doing her job.

<!-- S32 -->
So what is nmap actually doing?
It is a tool for network discovery
and security auditing.

<!-- S33 -->
In very simple terms,
you point it at a machine and ask:
what is this computer
exposing to the network?

<!-- S34 -->
It might tell you that certain ports are open.
And ports correspond to network services.
That is not automatically an attack.

<!-- S35 -->
It is more like looking at a building
and asking which doors are open.
If it is your building,
that is normal administration.

<!-- S36 -->
If it is someone else's,
and you are deliberately
looking for a way in...

<!-- S37 -->
well, that is a different story.

<!-- S38 -->
And what about that path?
Someone might think:
she is reading the password file.
It does contain information about accounts.

<!-- S39 -->
But on a modern Linux system,
the actual password hashes are stored somewhere else.
They are in slash etc slash shadow,
which is much more restricted.

<!-- S40 -->
So seeing that file is not the same thing
as discovering everyone's passwords.
Hollywood, of course,
would make this much more dramatic.

<!-- S41 -->
A Linux administrator would say:
it is literally a list of users.

<!-- S42 -->
Another classic scene cracks a password
in approximately fourteen seconds.
Real cracking is duller.
You have a hash, you have a wordlist,
and you let the computer try candidates.

<!-- S43 -->
Maybe it finds one in a minute.
Maybe in a week.
Maybe never.
And while it works, the attacker
is not sitting there typing.
They might be eating a sandwich.

<!-- S44 -->
Which brings me to my favourite
Hollywood tradition.
Apparently computers do not accept commands
unless you type them extremely fast.

<!-- S45 -->
Real programmers and administrators
do not type constantly.
They think.
They read.
They stare at an error.

<!-- S46 -->
Then they discover that someone
solved it eleven years ago.
And then they copy the solution.

<!-- S47 -->
That is computer science.

<!-- S48 -->
Sometimes the most dangerous thing
you can type is not
a mysterious hacking command.
It is something perfectly legitimate.

<!-- S49 -->
The famous example is this one.

<!-- S50 -->
Which is a wonderful story,
except that a modern system refuses.
It answers that operating recursively
on slash is dangerous,
unless you add a flag saying you meant it.

<!-- S51 -->
The commands that really destroy things
are duller.
A delete in the wrong directory.
A disk written over the wrong disk.

<!-- S52 -->
The terminal does not warn you about those,
because as far as it can tell,
nothing is wrong.
It can only ask: are you absolutely sure?

<!-- S53 -->
And if you answer yes...
it may believe you.

<!-- S54 -->
And here is the biggest problem
with the Hollywood stereotype.
A real attack might not look
like hacking at all.

<!-- S55 -->
It might involve a stolen password.
Phishing.
An unpatched server.
A leaked API key.
A password reused from somewhere else.

<!-- S56 -->
The attacker might not even need
a terminal.
They might simply log in
to a web interface.
Username.
Password.
And now they are inside.

<!-- S57 -->
No green text.
No Matrix-style graphics.
No dramatic music.

<!-- S58 -->
Which is arguably much scarier.

<!-- S59 -->
People imagine a hacker as a hoodie,
a dark room and a glowing keyboard.
None of that has anything to do with hacking.

<!-- S60 -->
The person next to you on the train,
with a completely ordinary laptop,
might know considerably more
about computer security.

<!-- S61 -->
And the person sitting
in front of six servers
might simply be trying to work out
why the database will not start.

<!-- S62 -->
So let us return to our original picture.
The man points at the woman.
You hacked it.
Was she hacking?

<!-- S63 -->
Maybe.
Maybe not.

<!-- S64 -->
She has a terminal.
She has nmap.
She has a list of accounts.
But none of those things prove
that she has hacked anything.
She could be the administrator,
or running a security audit.

<!-- S65 -->
Or she could actually be hacking.
We do not know.
And that is the joke.

<!-- S66 -->
The real difference between
ordinary administration and hacking
is not the colour of your terminal.
It is not how many monitors you have.

<!-- S67 -->
It is not how fast you type.
And it is certainly not
whether you are wearing a hoodie.
It is what you are doing,
and whether you have permission to do it.

<!-- S68 -->
So next time you see someone
staring at a black screen
full of mysterious text,
do not assume they are hacking.

<!-- S69 -->
They might just be fixing the server.

<!-- S70 -->
Although...
if they are typing at nine hundred words
a minute while shouting
"I'm in"...

<!-- S71 -->
you might want to ask
what they are doing.

