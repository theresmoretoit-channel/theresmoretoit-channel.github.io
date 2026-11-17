# How Did ARM Take Over Computing?

<!-- S01 -->
In 1985, engineers in Britain
switched on a brand-new processor
for the very first time.

<!-- S02 -->
It worked.
Which was already a small miracle.

<!-- S03 -->
But then they noticed something strange.
The chip's power supply
wasn't connected.

<!-- S04 -->
And yet it was running.

<!-- S05 -->
It was getting by on tiny currents
leaking in through its input pins,
from the signals of the chips around it.

<!-- S06 -->
When they measured it properly,
the processor needed
about a tenth of a watt.

<!-- S07 -->
Nobody had aimed for that.
The engineers just wanted a chip
that was cheap to make.

<!-- S08 -->
That chip was the first ARM processor.

<!-- S09 -->
Forty years later, its descendants
are in almost every smartphone.
In Apple's computers.
In some of the largest data centres
in the world.

<!-- S10 -->
Hundreds of billions of chips.

<!-- S11 -->
So how did a processor
from a British home-computer company
take over computing?

<!-- S12 -->
The answer isn't simply
that it used very little power.
That part was almost an accident.

<!-- S12b -->
By the way, if you like videos
like this, consider subscribing.

It really helps the channel.

<!-- S13 -->
To understand what really happened,
we have to go back to 1983.

<!-- S14 -->
The company was Acorn Computers.
Its BBC Micro was in classrooms
all over Britain.

<!-- S15 -->
The BBC Micro ran on an older,
eight-bit chip, the 6502.
For its next machine,
Acorn needed something much faster.

<!-- S16 -->
So the team tested
the new processors on the market.
None of them did what Acorn wanted.

<!-- S17 -->
They were complicated,
and none of them really fit
what Acorn wanted to build.

<!-- S18 -->
Then two Acorn engineers,
Sophie Wilson and Steve Furber,
went to Arizona,
to a firm started by one of
the 6502's original designers.

<!-- S19 -->
They expected a big chip company.
Instead, they found a handful of people
working out of a suburban house.

<!-- S20 -->
And they came home
with a simple conclusion.
If they can design a processor...
so can we.

<!-- S22 -->
At the time, processors kept gaining
more and more elaborate instructions.

<!-- S23 -->
A single instruction could fetch
a number from memory,
do arithmetic with it,
and write the result back.

<!-- S24 -->
Convenient for the programmer.
But every instruction like that
makes the chip harder to build.

<!-- S25 -->
It needs more logic
just to work out what each one means.
More transistors.
More design time.

<!-- S26 -->
Researchers at Berkeley and Stanford
had asked a radical question.

<!-- S27 -->
What if a processor
only had simple instructions,
and the compiler did the rest?

<!-- S28 -->
They called it RISC.
Reduced Instruction Set Computer.

<!-- S29 -->
Sophie Wilson designed
ARM's instructions along those lines.

<!-- S30 -->
Arithmetic only works
on the chip's own registers,
small, fast slots inside the processor.
Memory gets its own instructions.

<!-- S31 -->
So adding a number from memory
becomes three steps.
Load it.
Add it.
Store it.

<!-- S32 -->
It's called a load-store architecture.

<!-- S33 -->
More steps for the program.
But each step is regular,
predictable,
and easy to decode.

<!-- S34 -->
And ARM had plenty of registers
to work with.
Sixteen, each thirty-two bits wide.
The 6502 had three small ones.

<!-- S35 -->
The result was the ARM1.

<!-- S36 -->
It had about
25,000 transistors.

<!-- S37 -->
Intel's 286, launched a few years earlier,
had about 134,000.

<!-- S38 -->
Fewer transistors meant a smaller chip.
A cheaper chip.

<!-- S39 -->
And, almost as a side effect,
a chip that barely used any power.

<!-- S40 -->
That's where the tenth of a watt
came from.
Acorn wanted a cheap plastic package,
which meant staying under one watt.
So they designed carefully...
and landed ten times below.

<!-- S41 -->
In 1987, a faster version of the ARM
went into Acorn's new computer,
the Archimedes.

<!-- S42 -->
It was one of the fastest
personal computers of its day.

<!-- S43 -->
And it barely mattered.

<!-- S44 -->
The world was buying IBM-compatible PCs
with Intel processors.
That's where the software was.
That's what businesses bought.

<!-- S45 -->
The Archimedes stayed
mostly in British schools.

<!-- S46 -->
And Acorn itself was struggling.
It had already needed rescuing
by Olivetti, back in 1985.

<!-- S48 -->
Then help came from Apple.
It was building a handheld computer
called the Newton.

<!-- S49 -->
It needed a processor
that was fast, cheap,
and could run on batteries.

<!-- S50 -->
The ARM fitted perfectly.
But Apple didn't want to depend
on a chip owned by
a rival computer maker.

<!-- S51 -->
So in 1990, the ARM team
was spun out of Acorn
into a company of its own.

<!-- S52 -->
Acorn, Apple
and the chip maker VLSI
owned it together.

<!-- S53 -->
Twelve engineers.
An old barn near Cambridge.

<!-- S54 -->
And a business model
that turned out to be the real secret.

<!-- S55 -->
Intel designed its processors,
made them in its own factories,
and sold them.

<!-- S56 -->
ARM would make nothing at all.
It would sell the design.

<!-- S57 -->
Any company could license it,
build the ARM core into its own chip,
and pay a small fee
on every chip it sold.

<!-- S58 -->
That mattered,
because a chip doesn't have to be
just a processor.
Around the ARM core
you can put a radio,
a graphics unit,
a camera processor.

<!-- S59 -->
One chip,
designed by whoever needs it,
with ARM at the centre.

<!-- S60 -->
ARM didn't have to beat Intel
in personal computers.
It could end up inside anything.

<!-- S61 -->
And in the 1990s,
anything increasingly meant
mobile phones.

<!-- S62 -->
A desktop computer can use
a hundred watts and a big fan.
A phone runs on a battery
in your pocket.

<!-- S63 -->
By the end of the decade,
ARM cores were inside
some of the best-selling phones,
from Nokia and others.

<!-- S64 -->
Then came the iPod.
Then the smartphone.

<!-- S65 -->
Billions of people suddenly carried
a computer that had to last
all day on a battery.

<!-- S66 -->
And the processor that was built
because it was cheap
turned out to be exactly
what that world needed.

<!-- S67 -->
So that's our answer, right?
ARM is simple,
simple means efficient,
and efficient wins.

<!-- S68 -->
Not quite.

<!-- S69 -->
Look inside a modern high-end ARM core.

<!-- S70 -->
Huge caches.
Several instructions running at once.
Branch prediction,
guessing which way the program will go
before it gets there.

<!-- S71 -->
Out-of-order execution,
running instructions
in whatever order is fastest.

<!-- S72 -->
Billions of transistors on the chip.
Nothing about it is simple.

<!-- S73 -->
So where did the simplicity go?

<!-- S74 -->
The trick is that a processor
is really two different things.

<!-- S75 -->
The instruction set is the language
the software speaks.
Which instructions exist,
and what they mean.

<!-- S76 -->
The microarchitecture is the machine
that actually carries them out.

<!-- S77 -->
The language can stay simple,
while the machine underneath
becomes enormously complicated.

<!-- S78 -->
And the same thing happened
on the other side.

<!-- S79 -->
Intel's x86 instructions
are famously complicated.

<!-- S80 -->
But since the mid-1990s,
Intel and AMD processors
break them down inside
into small, simple operations.

<!-- S81 -->
Then they run those on an engine
much like the one
inside a modern ARM core.

<!-- S82 -->
Underneath the labels,
the two have grown surprisingly alike.

<!-- S83 -->
ARM's cleaner instructions still help.
They're easier to decode,
which can save a little power.

<!-- S84 -->
But they're not a magic advantage
that x86 could never match.

<!-- S85 -->
So ARM didn't take over
because it was simple.
And it wasn't designed for low power.

<!-- S86 -->
It won because three things lined up.
An efficient design.
A business model
that let anyone build with it.
And a world that suddenly needed
billions of battery-powered computers.

<!-- S87 -->
And then, in 2020,
the story came back to Apple.

<!-- S88 -->
Apple had sold its stake in ARM
years earlier,
when it badly needed the money.

<!-- S89 -->
Now it put its own ARM-based chips
into the Mac.

<!-- S90 -->
The same kind of cores as the iPhone,
scaled up for a computer.
Fast cores, efficient cores,
graphics and much more,
in a single chip.

<!-- S91 -->
They were faster
than the Intel chips they replaced,
and the laptops ran far longer
on a charge.

<!-- S92 -->
ARM was no longer
just the phone processor.

<!-- S93 -->
And ARM didn't stop there.
It moved into data centres too,
where every watt costs money.
Amazon now designs
its own ARM server chips.

<!-- S95 -->
The first ARM chip had about
25,000 transistors.
Today's have billions.

<!-- S96 -->
Almost everything about
how they work inside has changed.

<!-- S98 -->
A small team wanted
a processor they could actually build.

<!-- S99 -->
They didn't build it for phones,
for Apple,
or to beat Intel.

<!-- S100 -->
And in the end,
the most important thing they made
wasn't the chip.

<!-- S101 -->
It was a simple foundation
that everyone else could build on.
