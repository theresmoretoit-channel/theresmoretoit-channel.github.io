<!-- S01 -->
On the nineteenth of July, 2024,
a security company called CrowdStrike
sent out a routine update.

<!-- S02 -->
Not a new program.
Just a small configuration file.

<!-- S03 -->
Within hours, eight and a half million
Windows computers had stopped
on a blue screen.

<!-- S04 -->
Airlines grounded flights.
Hospitals cancelled operations.
A news channel went off the air.

<!-- S05 -->
And the mistake behind it
was an ordinary one.
The program expected twenty pieces of data.
The update gave it twenty-one.

<!-- S06 -->
Your games and apps make mistakes
like that all the time.
When they do, the game closes,
and you start it again.

<!-- S07 -->
Same kind of bug.
One closes a window.
The other stops
eight and a half million machines.

<!-- S08 -->
The difference isn't the mistake.
It's where the code was running.

<!-- S09 -->
So why can't one program
take over your computer...
and why could this one?

<!-- S10 -->
It hasn't always been like this.

<!-- S11 -->
On a PC running DOS in the 1980s,
nothing in the processor stopped a program.
It could write into any part of memory,
and talk straight to the hardware.

<!-- S12 -->
One program writing
somewhere it shouldn't
could overwrite the operating system,
and the whole machine froze.

<!-- S13 -->
The fix was to stop trusting programs,
and to make the processor
do the distrusting.

<!-- S14 -->
In 1982, Intel's 80286 processor
introduced protected mode,
with four levels of privilege.

<!-- S15 -->
They're usually drawn
as four rings, one inside another.

<!-- S16 -->
Ring zero is in the centre.
Ring three is on the outside.

<!-- S17 -->
And the numbering runs backwards.
The lower the number,
the more the code is allowed to do.

<!-- S18 -->
Ring zero belongs to the kernel,
the core of the operating system.
It hands out memory,
decides which program runs next,
and talks to the hardware.

<!-- S19 -->
Ring three is where your browser,
your games and your text editor run.
This is called user mode.

<!-- S19b -->
Windows, macOS and Linux
all divide the work this way.
The kernel in ring zero,
your apps in ring three.

<!-- S19c -->
Phones and Apple's newer Macs
use ARM chips instead.
There, the levels are called exception levels.
Different name, same split:
one for the kernel, one for your apps.

<!-- S20 -->
The processor always knows
which ring it's running in.
And it checks.

<!-- S21 -->
Some instructions only work in ring zero.
Switching off interrupts, for example,
or changing how memory is mapped.

<!-- S22 -->
When a program in ring three tries one,
the processor refuses.
It raises an exception
and hands control to the kernel,
which usually ends the program.

<!-- S23 -->
Memory gets the same treatment.
Every page of memory is marked
as either user or supervisor.

<!-- S24 -->
A program in ring three
that touches a supervisor page
doesn't get the data.
It gets stopped.

<!-- S25 -->
Your browser and your game
both run in ring three.
What keeps them apart
is that each one gets its own map of memory.
The other program's memory
simply isn't on it.

<!-- S26 -->
So when a game crashes,
the damage stays inside the game.
The kernel cleans up.
Everything else carries on.

<!-- S27 -->
Now look at CrowdStrike again.
Its driver ran in ring zero,
right next to the kernel.

<!-- S28 -->
Nothing above ring zero
can catch a mistake like that.

<!-- S29 -->
So Windows did the only safe thing left.
It stopped the whole machine, on purpose,
rather than carry on with memory
it could no longer trust.

<!-- S30 -->
That's what the blue screen is.

<!-- S31 -->
And because the driver started
every time Windows did,
every restart brought the crash back.

<!-- S32 -->
But this raises a question.
If your browser can't touch the hardware,
how does it ever save a file,
or send anything over the network?

<!-- S33 -->
It asks.

<!-- S34 -->
The program puts its request
into the processor's registers.
Which file. Where the data should go.
How much of it.

<!-- S35 -->
Then it runs one special instruction.
On a modern PC, it's called SYSCALL.

<!-- S36 -->
In that instant, the processor switches
from ring three to ring zero...

<!-- S37 -->
but it doesn't jump
wherever the program wants.
It jumps to one entry point
the kernel chose in advance.

<!-- S38 -->
The kernel checks the request,
does the work,
and drops back to ring three.
The program never touched the disk itself.

<!-- S39 -->
This is a system call,
and it happens constantly.

<!-- S40 -->
We counted them on a laptop.
A program that does nothing at all
still makes thirty.

<!-- S41 -->
Firefox, starting up
and loading one Wikipedia page,
made about six hundred and seventy thousand
in twenty seconds...
even with our counting slowing it down.

<!-- S42 -->
Every one of them
is a trip through the wall and back.

<!-- S43 -->
Which leaves something odd.
Four rings,
and we've only needed two.

<!-- S44 -->
What happened to rings one and two?

<!-- S45 -->
The idea of rings is older than the PC.
Multics, an operating system
from the late 1960s,
had eight of them.

<!-- S46 -->
The idea was layers of trust.
The core of the system in the middle,
less trusted services around it,
and programs on the outside.

<!-- S46b -->
Intel drew the same picture.
Rings one and two were meant
for the layers in between,
like drivers and system services.
Trusted more than your apps,
less than the kernel.

<!-- S47 -->
Two things got in the way.

<!-- S48 -->
First, systems like Unix and Windows NT
were designed to run
on many kinds of processor.

<!-- S49 -->
And the one split
every processor offered
was two levels.
One for the kernel,
one for everything else.

<!-- S50 -->
Second, the x86 processor itself.
When it maps memory,
each page knows only two states.
User, or supervisor.

<!-- S51 -->
Rings one and two count as supervisor.
So a driver in ring one
could still touch the kernel's memory.
The extra ring wouldn't protect much.

<!-- S51b -->
A few systems used them anyway.
OS/2 let some programs step into ring two,
just to talk to the hardware directly.

<!-- S51c -->
And before processors had help
for running virtual machines,
Xen and VirtualBox moved the guest's kernel
into ring one,
so the system underneath
could keep ring zero to itself.

<!-- S52 -->
In 2023, Intel proposed
removing rings one and two altogether.

<!-- S53 -->
In December 2024, it dropped the plan.
They're still in your processor.
Almost nothing uses them.

<!-- S54 -->
So far, this sounds reassuring.
The rules are in the hardware,
and the hardware checks every access.

<!-- S55 -->
In 2017, three teams of researchers,
working separately,
found a way through that wall.

<!-- S56 -->
They called it Meltdown.
And to follow it,
you need one trick
that modern processors play.

<!-- S57 -->
A processor doesn't wait
for one instruction to finish
before starting the next.
It runs ahead,
on instructions it will probably need.

<!-- S58 -->
If it guessed wrong,
it throws the results away,
as if nothing had happened.

<!-- S59 -->
Here's the flaw.
On affected Intel chips,
a program in ring three could ask
for a byte of kernel memory...

<!-- S60 -->
and the processor would fetch it
and pass it on to the next instructions
before it had finished checking
whether that was allowed.

<!-- S61 -->
The check did fail.
The result was thrown away.

<!-- S62 -->
But those next instructions
had already used the secret byte
to pull one piece
of the program's own memory
into the processor's cache.

<!-- S63 -->
And the cache doesn't forget,
just because the result was cancelled.

<!-- S64 -->
So the program times
how fast each piece of its memory answers.
The one that comes back fast
gives away the secret byte.

<!-- S65 -->
One byte at a time,
an ordinary program could read
the kernel's memory,
and whatever secrets were sitting in it.
Passwords and encryption keys included.

<!-- S66 -->
Meltdown affected Intel processors
going back to 1995.

<!-- S67 -->
It was made public
on the third of January, 2018.

<!-- S68 -->
The fix couldn't change the silicon.
So operating systems changed the map.

<!-- S69 -->
While your program runs,
the kernel's memory is now taken off
its map almost entirely.
There's nothing there to fetch.

<!-- S70 -->
But remember those system calls.
Every trip through the wall
now has to swap the map as well.

<!-- S71 -->
Red Hat measured the patches for Meltdown
and a related flaw, Spectre.
Under one percent on some work...
up to nineteen on busy databases.

<!-- S72 -->
The rule was right all along.
The processor just checked it too late.

<!-- S73 -->
Which brings us back to CrowdStrike,
and a harder question.

<!-- S74 -->
Why was a security program
in ring zero in the first place?

<!-- S75 -->
Because from there, it sees everything.
It starts before other software does.
And malware with administrator rights
has a harder time switching it off.

<!-- S76 -->
Microsoft's own list
ends with a warning.
They come at the cost of resilience.

<!-- S77 -->
After the outage,
Microsoft started building a way
for antivirus software
to run outside the kernel.

<!-- S78 -->
By autumn 2026,
it's still in test versions of Windows.
And the kernel hasn't been closed
to security companies.

<!-- S79 -->
Your games face the same dilemma.

<!-- S80 -->
Cheats that run in the kernel
are invisible to an anti-cheat
that runs in ring three.

<!-- S81 -->
So the anti-cheat moved in too.
Riot's Vanguard, used by Valorant,
puts a driver into ring zero.
On most PCs, it loads as Windows starts...
even if you never open the game.

<!-- S82 -->
That doesn't make it faulty.
But it sits in the same place
the CrowdStrike driver did,
where one mistake stops the whole machine.

<!-- S83 -->
So why can't one program
take over your computer?

<!-- S84 -->
Because the processor keeps
almost every program out of the centre,
and checks them every time they knock.

<!-- S85 -->
But the processor can't decide
who gets let in.
People decide that...
every time they install a driver.

<!-- S86 -->
So here's a question for the comments.
Who should decide which programs
get into ring zero:
you, Microsoft,
or the companies that make them?
