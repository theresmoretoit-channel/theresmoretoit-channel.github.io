<!-- S01 -->
948.
That's how many separate ways an AI found
to take over a Linux computer from the inside.

<!-- S02 -->
No stolen password. No remote break-in.
Each one starts with an ordinary user
who has no special rights,
and ends with root,
the account that can do anything.

<!-- S03 -->
OpenAI published the result in November 2026.
The whole run cost
$1.2 million in API credits.

<!-- S05 -->
These are OpenAI's own numbers,
published the day before
it launched the model that produced them,
and nobody outside has confirmed the full count.
But hundreds of reports and patches
have already gone out.

<!-- S06 -->
Here's why this matters beyond Linux.
The Linux source code is public.
Anyone can read it.
For decades, that was the argument
for why it's safe.

<!-- S07 -->
So if a machine can read public code
and turn it into working exploits at this scale,
should software keep its code secret after all?

<!-- S08 -->
Let's look at software that already does.
In April 2026, Microsoft fixed
164 security flaws
on its monthly patch day.
In October, it fixed
1,413.

<!-- S09 -->
In that single month, it fixed more
than in any whole year before it.
Over 1,000 of those fixes were in Windows,
and Microsoft had warned
that its own AI tools would drive the surge.

<!-- S10 -->
You can't compare the two numbers directly.
Companies count differently,
and Microsoft was searching its own private code.

<!-- S11 -->
But it does show one thing.
Keeping the code private
had not kept the bugs out.

<!-- S12 -->
So what actually protects you?
To answer that,
we need to see how this machine works,
because every step of it throws something away.

<!-- S13 -->
The Linux kernel has
more than 40 million lines of code.
First, scout agents went through it
and picked out the parts
an ordinary user can actually reach.

<!-- S14 -->
That left about 7%.
It's the part they judged worth attacking,
not a random sample,
so you can't multiply the result by 14.

<!-- S15 -->
Next, analyst agents went through that code
and listed everything suspicious.
2,308 candidates,
in 12 hours.

<!-- S16 -->
But a suspicion proves nothing.
So other agents wrote test programs
and ran them on isolated virtual machines.
1,724 bugs
turned out to be real.

<!-- S17 -->
Then came the expensive part:
building working exploits,
with the standard protections
of a normal desktop system switched on.
1,169
reached root.

<!-- S18 -->
Group those by the underlying flaw,
and you get the 948.

<!-- S19 -->
There's one detail in the report
that's hard to forget.
In an early run,
the agents reported 200 successes.
Then humans checked how they had got there.

<!-- S20 -->
Twenty of them had reached root
through a different unknown bug,
not the one they had been told to use.
Sent to open one door,
they found another that nobody knew about.

<!-- S21 -->
In a sample of its exploits,
OpenAI identified ten exploitation techniques
that outside experts hadn't seen before.

<!-- S22 -->
In July, an earlier model
found 166 of these flaws.
Three months of fixes later,
the newer model found 948.
The bugs hadn't run out.
The later run found far more.

<!-- S23 -->
Now, there's an important limit.
None of this breaks into your computer
over the internet.
The attacker already has to be on the machine,
as an ordinary user.

<!-- S24 -->
That's less comforting than it sounds,
because real attacks often come in two steps.
First you get in,
through a browser flaw or a malicious download.
Then you need root.
This is the second step.

<!-- S25 -->
OpenAI's advice is blunt.
On a system without the latest patches,
treat any ordinary account as root,
at least against a well-funded attacker.

<!-- S26 -->
So where does that leave
the old argument for open code?
In the late nineties,
Eric Raymond gave it a slogan:
"Given enough eyeballs, all bugs are shallow."

<!-- S27 -->
He called it Linus's Law.
It's a lovely idea, with one assumption inside it:
that somebody is actually looking.

<!-- S28 -->
In 2014, a bug called Heartbleed
turned up in OpenSSL,
the code that protected a huge share of the web.
About half a million secure servers
were thought to be exposed.

<!-- S29 -->
The bug had sat in public code for two years.
The project was getting
about $2,000 a year in donations,
and had one full-time developer.

<!-- S30 -->
Anyone could read it.
Hardly anyone did.

<!-- S31 -->
That was always the real weakness of open source.
Not too many eyes on the code. Too few.

<!-- S32 -->
And that's the part AI changes.
A machine can keep scanning,
and investigate far more candidates
than a human researcher could handle alone.
The old promise is finally being kept,
for everybody, attackers included.

<!-- S33 -->
So public code really does get examined now.
Does hiding it help?

<!-- S34 -->
A closed program still has to run,
so its machine code sits
on every computer that uses it.
Tools like Ghidra turn that back
into something like source code.

<!-- S35 -->
And there's a classic trick.
Compare a program
before and after a security update.
Whatever changed shows you where the hole was.

<!-- S35b -->
That tells attackers where to aim,
well before every system
has installed the update.

<!-- S36 -->
Anthropic tried this on the Windows kernel,
with 21 flaws
Microsoft had recently patched,
and no source code.
The AI's first crash came in 31 minutes.
It had 18 within six hours.

<!-- S37 -->
Eight became working exploits
capable of taking full control of the machine,
at roughly $2,000 each.

<!-- S38 -->
But these weren't unknown bugs.
The patches already pointed
to where the problems were.
Finding a new flaw from scratch is harder.

<!-- S39 -->
So secrecy still costs an attacker something.
It's a speed bump, not a wall.
How high is the bump?
There's no public number.

<!-- S40 -->
What about the other side?
What does being open actually buy you?
The answer is in a small detail
of OpenAI's report.

<!-- S41 -->
During the ten days of that scan and analysis,
over 100 of these Linux flaws
were fixed, or about to be,
by other people.
About 300 more
were already being discussed in public.

<!-- S42 -->
Other people were finding the same bugs
at the same time.

<!-- S43 -->
Linus Torvalds had described this back in May.
He said AI reports
had made the kernel's security mailing list
"almost entirely unmanageable",
because different people kept finding
the same things with the same tools.

<!-- S44 -->
And his advice was this:
"If you found a bug using AI tools,
the chances are somebody else found it too."

<!-- S45 -->
The kernel's rules now say it outright.
A bug found with AI must be treated as public,
because these bugs surface
across several researchers,
often on the same day.

<!-- S46 -->
Think about what that does
to the idea of a secret bug.
If it was cheap for you to find,
it was cheap for everyone.

<!-- S47 -->
With open source,
anyone can inspect the report,
verify the fix, and challenge the result.
With closed software,
you mostly have to trust the vendor.

<!-- S49 -->
But openness has a bill,
and it isn't the one you'd expect.
It's tempting to say
a small project can't afford the scanning.
AI companies are already
offering maintainers free access.

<!-- S50 -->
What's short is people.
The kernel used to log
about 500 security issues per release.
This year it passed 1,500.
Many are minor,
but somebody still has to go through them.

<!-- S51 -->
In January, the curl project
ended its paid bug bounty,
to stop rewarding a flood of junk reports.

<!-- S52 -->
Even good reports only move the work along.
AI-generated patches still need human review.
Some early fixes added unnecessary code
or missed other versions of the same bug.

<!-- S53 -->
You can buy more scanning.
You can't buy more people
who understand a piece of code that well.
Here, a company with a paid security team
really does have an edge.

<!-- S54 -->
And then comes the last problem.
Fixed is not the same as installed.

<!-- S55 -->
In March 2017,
Microsoft patched a flaw in Windows.
Closed source, one vendor, one update system.
Two months later,
WannaCry went through that same hole,
into some 200,000 computers
in about 150 countries.

<!-- S56 -->
That patch had two months to spread,
and it wasn't enough.
An attacker may no longer leave you two months.
In the same Anthropic study,
the AI took a public fix
for Firefox's JavaScript engine,
and had a working exploit in under an hour.

<!-- S57 -->
The fixed version of Firefox
was still 18 days away.

<!-- S58 -->
This is the danger of publishing a fix.
The information can reach attackers
before the update reaches you.

<!-- S59 -->
A Linux fix has a long way to travel,
from the kernel to a stable release,
to your distribution, to your device.
A phone may wait months, or forever.

<!-- S60 -->
And closed software doesn't escape this.
We just saw it: the Windows patch was enough.
Every update is now also a map.

<!-- S60b -->
So keep everything up to date,
your computer, your phone, even your router,
and install updates as soon as they arrive.
As AI gets better at turning fixes into attacks,
every day you wait will matter more.

<!-- S61 -->
So, is open source still safer?
Honestly, nobody knows.
As far as is publicly known,
no one has run the same test on both sides,
under the same rules.

<!-- S62 -->
What we can say is more modest.
Hiding code buys less than it used to.
Showing it lets anyone check the work,
and hands a bigger pile of that work
to the people who maintain it.

<!-- S64 -->
Even if AI never finds every bug,
it has already changed the economics of finding them.

<!-- S65 -->
What matters now is how long a hole stays open
between the moment somebody finds it
and the moment it's closed on your machine.

<!-- S66 -->
So here's a question for you.
If any bug can be found by anyone,
would you rather trust code you can read,
or a company that's paid to fix it?
Let me know in the comments.
