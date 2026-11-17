<!-- S01 -->
In September 2026,
a single batch of Windows updates
broke four things at once.

<!-- S02 -->
Audio stopped working.
Remote Desktop stopped working.
Shared folders in virtual machines
stopped working.

<!-- S03 -->
And some computers stopped trusting
the company network
they belonged to,
so people couldn't log in at all.

<!-- S04 -->
One batch.
One Tuesday.

<!-- S05 -->
And if you're thinking
this is just another
bad Windows update...

<!-- S06 -->
it isn't.

<!-- S07 -->
Because this has been happening
again and again and again.

<!-- S08 -->
So what exactly is their QA doing?

<!-- S09 -->
How can a company this enormous
ship an operating system update
and not catch something obvious?

<!-- S10 -->
Let's start with the smallest one.

<!-- S11 -->
Microsoft shipped an update
that changed a few things
about the taskbar.
And shortly afterwards, it admitted
there was a problem
with mouse cursor settings.

<!-- S12 -->
For some people, a custom cursor
would revert to a large white arrow.
The kind of arrow that makes you check
whether you've accidentally booted
a computer from 1998.

<!-- S13 -->
Your carefully chosen cursor?
Gone.
And putting it back
apparently didn't work either.

<!-- S14 -->
Now, you might be thinking:
Every piece of software has bugs.
Absolutely.

<!-- S15 -->
But there is a difference between:
"We found a rare fault
under an unusual
hardware configuration."

<!-- S16 -->
And:
"After our update,
your mouse doesn't look like
the mouse you chose."

<!-- S17 -->
Because somebody has to install it.
Somebody has to log in.
Somebody has to move the mouse.
And apparently that wasn't enough.

<!-- S18 -->
Then there is the audio.
Install an update.
Reboot.
No sound.

<!-- S19 -->
Some USB audio devices simply stop,
and Windows reports
that the device cannot start.

<!-- S20 -->
And audio is not exactly
an exotic feature.
You would think one of the basic tests
for an operating system might be:

<!-- S21 -->
can the computer still make a sound?

<!-- S22 -->
Apparently that is more complicated
than it sounds.
Literally.

<!-- S23 -->
And at home, all this is annoying.
Your cursor looks silly.
Your speakers are quiet.
But you will survive.

<!-- S24 -->
But a server that stops trusting
the network it belongs to
means nobody can log in,
and somebody in the IT department
is having a very bad morning.

<!-- S25 -->
And this is where it stops being
a collection of funny stories.

<!-- S26 -->
Because we can look at
Microsoft's own update history.
Microsoft publishes it.
Every month they list
what their updates broke.

<!-- S27 -->
And if you line up
a single year of that list,
the same pattern
just keeps repeating.

<!-- S28 -->
January broke audio devices
and webcams.
February made the cursor spin
so the machine looked frozen.

<!-- S29 -->
March produced blue screens
and installations
stuck part of the way through.
April broke the face recognition
people use to log in.

<!-- S30 -->
May left File Explorer
not responding to the mouse.
And October broke connections
to your own computer.

<!-- S31 -->
Not the internet.
The address that means "this machine".

<!-- S32 -->
And two of them
are genuinely remarkable.

<!-- S33 -->
One update broke the button
that resets your PC.
Another broke the recovery screen,
where USB mice and keyboards
stopped responding.

<!-- S34 -->
Read that again.

<!-- S35 -->
Twice in three months,
an update broke the tool
you use to repair a broken computer.

<!-- S36 -->
And one more detail,
and it might be the important one.
That audio bug, the one where Windows
says the device cannot start?

<!-- S37 -->
It happened in January.
And then it happened again
twenty months later.

<!-- S38 -->
Same symptom.
Same kind of device.
Same message.

<!-- S39 -->
That is not a story
about writing bad code.
That is a story about testing.

<!-- S40 -->
And none of this is new.

<!-- S41 -->
There was an update in 2024
that stopped Linux from starting
on dual-boot machines.
The error message said, word for word:

<!-- S42 -->
"Something has gone
seriously wrong."

<!-- S43 -->
Which is, honestly, the most accurate
error message Windows has ever shown.

<!-- S44 -->
And in 2018 there was a version
that had to be pulled completely,
after people reported
that their files were gone.

<!-- S45 -->
So at this point
you might reasonably conclude:
Microsoft just isn't very good
at writing software.

<!-- S46 -->
And that would explain everything.
The bugs.
The regressions.
The updates that fix one thing
and break another.

<!-- S47 -->
But there is a problem
with that explanation.
Microsoft doesn't only make Windows.

<!-- S48 -->
They make Office.
Visual Studio.
Exchange.
Teams.
And a very large cloud.

<!-- S49 -->
And all of those have had
their own bugs, their own regressions
and their own spectacular outages.

<!-- S50 -->
And that matters.
Because the usual explanation for
Windows is that it carries
thirty years of old code.

<!-- S51 -->
A modern cloud service
doesn't carry thirty years
of anything.
It was built recently,
by people who knew
what they were building.

<!-- S52 -->
And it still breaks.

<!-- S53 -->
So the problem was never
simply old code.
The problem is complexity
at Microsoft's scale.

<!-- S54 -->
And Windows is the place
where that complexity
is easiest to see.

<!-- S55 -->
Because Windows isn't really
one operating system.
At the bottom is an architecture
that goes back to the early nineties.

<!-- S56 -->
Then decades of interfaces.
Then compatibility layers.
Then drivers.
Then services.

<!-- S57 -->
Then newer frameworks,
built on top of older frameworks.
Then a new look.
Then another new look.

<!-- S58 -->
It's less an operating system
and more an archaeological dig
that somehow still runs.

<!-- S59 -->
And Microsoft isn't allowed
to clear the site,
because businesses depend
on what's underneath.
There's a whole video about that one.

<!-- S60 -->
What matters here
is what it does to bugs.
Every layer has to keep working
with every layer below it.

<!-- S61 -->
So a change up here
can break something
nobody has looked at in years.

<!-- S62 -->
And there is one more clue
about how this goes,
and it isn't about bugs at all.

<!-- S63 -->
It's a pattern.
Microsoft removes something.
Users complain.
Microsoft takes years
to reconsider it.

<!-- S64 -->
And in the meantime,
somebody else builds a tool
to put it back.

<!-- S65 -->
And the really funny part
is that these aren't
obscure hobby projects.

<!-- S66 -->
There are entire applications
whose whole job is to make Windows
behave more like...

<!-- S67 -->
well...
Windows.

<!-- S68 -->
They bring back an older Start menu.
They restore the taskbar.
They change how Explorer behaves.

<!-- S69 -->
And some of them give you more control
over Windows than Windows does.

<!-- S70 -->
Microsoft has an enormous number
of engineers working on this system.
And then somebody outside the company
says: fine.
I'll put the old taskbar back myself.

<!-- S71 -->
And now something else has changed.
Microsoft is increasingly using AI
in how its software gets written.

<!-- S72 -->
Its own chief executive has said
that twenty to thirty per cent
of the code in their repositories
is now written by software.

<!-- S73 -->
And that should mean
more productivity.
More fixes.
Faster development.

<!-- S74 -->
But there is an obvious bottleneck.
Writing code can become faster.

<!-- S75 -->
Testing an enormous legacy system
does not necessarily become faster.

<!-- S76 -->
And if you can produce changes
faster than you can test
how they interact
with decades of existing code...

<!-- S77 -->
you may simply end up
producing regressions faster.

<!-- S78 -->
And it's worth being careful here.
That figure is Microsoft as a whole,
not Windows in particular.
And nobody has shown
that AI caused any of these bugs.

<!-- S79 -->
Maybe AI didn't make Microsoft
worse at testing.

<!-- S80 -->
Maybe it just made
the existing problem faster.

<!-- S80b -->
By the way, if you'd like to see
where the rest of this goes,
consider subscribing.

It really helps the channel.

<!-- S81 -->
So most of this video has argued
that Microsoft has
a real problem with quality.
And that argument holds.

<!-- S82 -->
So here's the part
that surprises people.
Why might the kernel
still be different?

<!-- S83 -->
Because almost everything
described so far
is not the kernel.

<!-- S84 -->
The cursor.
The taskbar.
The Start menu.
The settings.
The recovery screen.

<!-- S85 -->
All of that sits on top.

<!-- S86 -->
The kernel is the part underneath.
It decides which program
runs on which processor core.
It hands out memory.
It talks to the hardware.

<!-- S87 -->
And if that part went seriously wrong,
the symptom isn't
a silly-looking mouse.

<!-- S88 -->
The symptom is a machine
that stops, corrupts your data,
or quietly lets someone in.

<!-- S88b -->
And the kernel has something
the rest of Windows doesn't have.
Hard constraints.

<!-- S88c -->
A scheduler can't decide
to behave differently
because somebody redesigned
the Start menu.

<!-- S88d -->
Memory management can't be modernised
by moving a button.
And a driver doesn't get to assume
the hardware will behave nicely.

<!-- S88e -->
Above all, the kernel doesn't get
to hide a mistake behind
a slightly confusing settings page.

<!-- S88f -->
Which is one reason to suspect
it's a very different
engineering story
from the rest of Windows.

<!-- S89 -->
But suspecting isn't evidence.
So look at what this thing
has actually had to survive.

<!-- S90 -->
That architecture at the bottom is old.
Very old.
And it survived.

<!-- S91 -->
It became Windows 2000.
Then XP.
Then Vista.
Then 7, 8, 10 and 11.

<!-- S92 -->
Processors changed.
The number of cores exploded.
Memory sizes exploded.
Virtual machines went from exotic
to completely normal.

<!-- S93 -->
And the same family of code
ended up running servers
all over the world.

<!-- S94 -->
File servers.
Company logins.
Virtual machines.
Workloads nobody imagined
when it was designed.

<!-- S95 -->
If the part that decides
what runs when,
and hands out the memory,
were hopelessly broken...
that bill would be impossible to hide.

<!-- S96 -->
Now, an honest admission.
Nobody outside Microsoft can read
the source code of the modern kernel,
so nobody can call it beautiful.

<!-- S96b -->
Although somebody did look
at an older one.

<!-- S96c -->
Part of the Windows 2000 source
leaked in 2004,
and last year a researcher
went through it.

<!-- S96d -->
The findings were not flattering.
Bugs that sat in that code
for sixteen years
before anyone patched them.

<!-- S96e -->
But that is the grandparent
of today's kernel,
and only a fraction of it leaked.
It tells us about 2000,
not about now.

<!-- S97 -->
And surviving isn't the same
as being excellent.

<!-- S98 -->
So this isn't a claim
that the Windows kernel is brilliant.
Nobody knows that.

<!-- S99 -->
But we do have decades of evidence
that it is competent.

<!-- S100 -->
And that's a much stranger conclusion
than "Windows bad".

<!-- S101 -->
Because it means the answer
to "what is their QA doing"
probably isn't
"Microsoft can't write software".

<!-- S102 -->
It's that they've spent decades
building new things on old things,
without ever being allowed
to throw the old things away.

<!-- S103 -->
The result is enormous.
Powerful.
Compatible.
And occasionally ridiculous.

<!-- S104 -->
You install an update.
Your sound disappears.
Your cursor turns into Windows 98.

<!-- S105 -->
And underneath all of it,
something is quietly deciding
which program runs next.
Handing out memory.
Talking to the hardware.

<!-- S106 -->
Doing exactly what
it's supposed to do.

<!-- S107 -->
At least...
we think it is.

<!-- S108 -->
Because unlike the taskbar...
we can't actually see it.
