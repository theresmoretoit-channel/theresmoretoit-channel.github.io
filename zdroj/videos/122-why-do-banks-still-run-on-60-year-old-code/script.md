<!-- S01 -->
Nine hundred and ninety-nine pounds
and ninety-nine pence.
Add one penny.

<!-- S02 -->
The answer is zero.

<!-- S03 -->
No error message. No crash.
Just zero, written quietly into the account.

<!-- S04 -->
In COBOL, when the field for a result
is too small to hold it,
the extra digit can simply disappear.
Unless the program asks to be warned,
the calculation carries on.

<!-- S05 -->
It doesn't round, either.
Two pounds, thirty-four and a half pence,
stored to the penny,
becomes two thirty-four.

<!-- S06 -->
Write one extra word, ROUNDED,
and it becomes two thirty-five.

<!-- S07 -->
Neither of these is a bug.
They're rules.
And many of the world's banks
still run on rules like these.

<!-- S08 -->
COBOL is a programming language
from 1959.
Not every program written in it is that old.
But the language is,
and so are its habits.

<!-- S09 -->
So why haven't banks replaced it?
They have the money.
They have the engineers.

<!-- S10 -->
To find out, we'll look at three real cases.
A bank that tried to leave its old system,
one that managed it,
and a crisis where everyone blamed COBOL.

<!-- S11 -->
But first, that missing half penny.

<!-- S12 -->
Say you rewrite that banking program
in a modern language.
You'd probably fix those rules.
Overflow becomes an error.
Half a penny gets rounded up.

<!-- S13 -->
Cleaner. Safer.
And now, wherever half a penny turns up,
your program disagrees with the old one.

<!-- S14 -->
Modern languages can do exact decimal maths.
Java has a type built for it.
But even there,
the rounding rule is a choice.

<!-- S15 -->
One common setting rounds the half up:
two thirty-five.
Another rounds to the nearest even digit:
two thirty-four.
Both are correct. Only one matches.

<!-- S16 -->
And with ordinary floating point,
the kind most code uses by default,
it gets stranger.
Zero point one plus zero point two
isn't zero point three.

<!-- S17 -->
So replacing COBOL isn't translation.
It's finding every rule like this,
in millions of lines,
and keeping each one exactly as it was.

<!-- S18 -->
How did it end up there in the first place?

<!-- S19 -->
In May 1959,
the US Department of Defense
called a meeting at the Pentagon.
Computer makers, government agencies
and big companies came,
all with the same problem.

<!-- S20 -->
Every computer had its own language.
A payroll program written for one machine
was useless on another.

<!-- S21 -->
A committee designed a common language
for business.
Its biggest influence was FLOW-MATIC,
from Grace Hopper's team at Remington Rand.

<!-- S22 -->
And in December 1960,
essentially the same COBOL program
ran on two computers
from rival manufacturers.
That was the whole point.

<!-- S23 -->
It was designed so people could follow it.
ADD PAYMENT TO ACCOUNT-BALANCE.
You can probably guess what that does.

<!-- S24 -->
And it stored money the way people write it:
as decimal digits.
The decimal point
doesn't even have to be stored.
The field's description says where it goes:
the last two digits are pence.

<!-- S25 -->
In 1964, IBM launched the System/360.
Its design included instructions
for decimal arithmetic.

<!-- S26 -->
And IBM has designed its mainframes
to stay compatible ever since.
Many older programs can still run
on today's machines
without being rewritten.

<!-- S27 -->
So there was rarely a moment
that forced anyone to move.
Every year the code kept working,
and every year it collected more rules.
New products, new taxes, new regulations,
new exceptions.

<!-- S28 -->
Nobody has counted how much COBOL
is still running worldwide.
But IBM says forty-five
of the world's fifty biggest banks
still use its mainframes.

<!-- S29 -->
And some owners have counted.
In 2017, America's Social Security
Administration said its systems held
over sixty million lines of COBOL.

<!-- S30 -->
In 2025, US government auditors
listed the eleven federal systems
most in need of replacement.

<!-- S31 -->
They were between twenty-three
and sixty years old,
and cost about seven hundred and fifty
million dollars a year to run.

<!-- S32 -->
So the code is old, it's everywhere,
and it's full of rules nobody wrote down.
Surely the danger is in keeping it.

<!-- S33 -->
Let's see what happens
when a bank leaves.

<!-- S34 -->
In 2018, a British bank called TSB
had about five million customers,
and a problem.

<!-- S35 -->
Its systems were rented
from Lloyds Banking Group,
a competitor,
and the fees were set to rise sharply.

<!-- S36 -->
So TSB decided to move everything
onto a new platform,
built by its new owner,
the Spanish bank Sabadell.

<!-- S37 -->
One weekend in April.
On Sunday evening,
the new system was switched on.

<!-- S38 -->
On Monday, there were about
nine hundred thousand attempts to log in.
Only about one internet banking login
in ten succeeded.

<!-- S39 -->
Payments failed.
Some customers logged in
and saw other people's accounts.

<!-- S40 -->
The worst lasted about a week.
TSB didn't get back to business as usual
until December.

<!-- S41 -->
The fallout cost around
three hundred and thirty million pounds
in 2018 alone.
Regulators later added
nearly forty-nine million in fines.

<!-- S42 -->
And here's the strange part.
The customer data arrived intact.
Both official reports say so.

<!-- S43 -->
What failed was the new platform around it.
Two data centres, set up differently.
Performance tested on only one of them,
with the targets lowered
after the tests didn't pass.

<!-- S44 -->
And there was no going back.
Once the data had moved,
returning to the old system was,
in the regulator's words,
"essentially impossible".

<!-- S45 -->
TSB wasn't escaping a broken system.
It was leaving one that ran,
because of who owned it
and what it cost.
Leaving was the dangerous part.

<!-- S46 -->
So is leaving always a disaster?

<!-- S47 -->
In 2008, Australia's Commonwealth Bank
set out to replace core systems
that had served it
for more than forty-five years.

<!-- S48 -->
The plan: about five hundred and eighty
million Australian dollars,
and four years.

<!-- S49 -->
It took five.
Press reports later put the total
at roughly one point one billion,
as the project expanded.

<!-- S50 -->
But it didn't move everything
in one weekend.
Deposit accounts went first, in 2010.
Business accounts followed in 2011,
and loans in 2012.

<!-- S51 -->
Each step was something the bank
could watch, check and learn from
before it bet on the next one.

<!-- S52 -->
At the end, the bank says,
it became the first major Australian bank
with real-time banking,
around the clock.

<!-- S53 -->
So it can be done.
But look at what it took.
Five years, a much bigger bill,
and patience.

<!-- S54 -->
Modernisation isn't a purchase.
It's a project,
with risks of its own.

<!-- S55 -->
Now for the crisis
where everyone blamed COBOL.

<!-- S56 -->
March 2020.
As the pandemic shut down New Jersey,
new unemployment claims jumped
from under ten thousand in a week
to over a hundred and fifty-five thousand.

<!-- S57 -->
Sixteen times as many,
in seven days.
The unemployment office couldn't keep up.

<!-- S58 -->
In early April, the governor
asked for volunteers.
Not only health workers,
but people who knew COBOL.
The state's systems, he said,
were more than forty years old.

<!-- S59 -->
The story spread fast.
Ancient code had collapsed
under the pandemic.

<!-- S60 -->
But when the state auditor
looked into it later,
it found no evidence
that the delays had been caused
by the computer systems.

<!-- S61 -->
Separately, reporters who looked
at the error messages people were seeing
traced many of them to the website in front,
written in a much newer language, Java.
The old code behind it kept running.

<!-- S62 -->
So why did the state need COBOL programmers?
Because Congress was changing the rules.
New benefits, new amounts,
new people who qualified,
and every change had to go
into the code, fast.

<!-- S63 -->
The problem wasn't that the code was old.
It was that few people could change it,
and that the phone lines and the staff
were overwhelmed as well.

<!-- S64 -->
Three cases.
A bank that left a system that still ran,
and whose migration failed.
A bank that left carefully,
and succeeded.
And a crisis where the old code was blamed,
and nobody could show it was the cause.

<!-- S65 -->
That doesn't mean old systems never fail.
They do.
They get expensive,
the people who understand them retire,
and waiting has a cost of its own.

<!-- S66 -->
But age is easy to see,
and the real risks aren't.
Rules nobody wrote down.
Knowledge in a few people's heads.
And the moment you switch over.

<!-- S67 -->
That's why many banks don't replace
the old core in one go.
They wrap it.
The app on your phone is new,
but it may be talking to something
much older.

<!-- S68 -->
And they replace it piece by piece.
In 2004, the software writer Martin Fowler
named this after the strangler fig,
a rainforest plant that grows around a tree
until it can stand on its own.

<!-- S69 -->
The old system keeps working
while the new one grows around it,
one job at a time,
until nothing depends on the old one.

<!-- S70 -->
Which brings us back to that half penny.
Somewhere, a program may still drop it,
because someone decided it should,
decades ago.
Replacing that program means knowing that,
and everything like it.

<!-- S71 -->
The old system isn't necessarily
what fails.
Sometimes, it's what replaces it.

<!-- S72 -->
Because replacing the technology
isn't the same as removing the risk.
Sometimes it just moves the risk
into a single weekend in April.

<!-- S73 -->
So here's a question for you.
If a system has worked for forty years,
when is the right time to replace it?
And have you ever had to replace one yourself?
Let me know in the comments.
