<!-- S01 -->
You click a button.
Nothing happens.
You click it again.
Still nothing.

<!-- S02 -->
You move the mouse.
Nothing.
For a few seconds,
your computer looks completely dead.

<!-- S03 -->
And then everything happens at once.
The window moves.
The menu opens.
Every click you made arrives,
all together.

<!-- S04 -->
Here is the strange part.
Your computer knew you clicked.
It knew within microseconds.

<!-- S05 -->
That is not a guess.
Right now, with you
doing nothing in particular,
your machine is dealing with thousands
of hardware events every second.

<!-- S06 -->
A key going down.
A packet arriving.
A timer firing.
A disk finishing a job.

<!-- S07 -->
Each one of those is an interrupt,
and computers have worked this way
since the 1950s,
for exactly this purpose:

<!-- S08 -->
so that a processor could react
to the world outside itself.

<!-- S09 -->
So the hardware reported your click.
The processor noticed.
And you still sat there for five seconds
staring at a dead screen.

<!-- S10 -->
Shouldn't the user come first?

<!-- S11 -->
There is an answer,
and it is not
that your computer is too slow.

<!-- S12 -->
It is that being noticed
and being served
are two completely different things.

<!-- S13 -->
Let's start with the noticing.
Imagine a computer without interrupts.

<!-- S14 -->
The processor would have to ask,
over and over:
Did the keyboard receive anything?
Did the disk finish?

<!-- S15 -->
Did a packet arrive?
Did the mouse move?
And then ask again.
And again.

<!-- S16 -->
Almost every answer would be no,
and the asking itself
would eat the machine alive.

<!-- S17 -->
So devices got a way to raise a hand.
The mouse moves,
the hardware raises an interrupt,

<!-- S18 -->
and the processor drops
whatever it was doing,
jumps into a small piece of code
called a handler,

<!-- S19 -->
and the operating system finds out
that something happened.

<!-- S20 -->
It is a brilliant idea.
And it leads to a very reasonable
assumption.

<!-- S21 -->
If the processor can be pulled away
from anything, instantly,
then surely my click
gets dealt with instantly too.

<!-- S22 -->
Except the handler is not allowed
to do anything much.

<!-- S23 -->
While the processor is inside it,
everything else is waiting.
Including the next interrupt.
And the next one is already coming.

<!-- S24 -->
So the rule is the opposite
of what you would expect.
The handler does as little
as it possibly can.

<!-- S25 -->
It notes what happened.
It tells the device
that the message arrived.
It drops the event into a queue.
And then it gets out.

<!-- S26 -->
Kernel engineers even split the work
into two named halves:
the part that must happen now,
and the part that can happen later.

<!-- S27 -->
Everything interesting,
everything you would ever see,
is in the second half.

<!-- S28 -->
Which gives us the first answer.
An interrupt gets
the computer's attention.

<!-- S29 -->
It does not get your program
onto a processor.

<!-- S30 -->
Fine, you might say. Then fix that.
Make input the most important thing
in the building.

<!-- S31 -->
Mouse? Highest priority.
Keyboard? Highest priority.
The window in front of you?
Highest priority.

<!-- S32 -->
Everything else can wait its turn.
It sounds obviously right.

<!-- S33 -->
And the best argument against it
happened on Mars.

<!-- S34 -->
In 1997, the Pathfinder lander
touched down and started working.
Then, days later,
it began resetting itself.

<!-- S35 -->
Not a cosmic ray.
Not a broken part.
A scheduling problem.

<!-- S36 -->
There was a high priority task
that moved data
around the spacecraft,
and it needed a shared piece of memory.

<!-- S37 -->
A low priority task
collecting weather data
had got there first
and was holding it.

<!-- S38 -->
Which would have been fine
for a moment.
But a medium priority task
then took the processor,

<!-- S39 -->
and the low priority one
never got a chance to finish.
So it never let go.

<!-- S40 -->
The most important task
on the spacecraft
was now stuck behind
the least important one.

<!-- S41 -->
It has a name.
Priority inversion.

<!-- S42 -->
A watchdog timer noticed
that the important task
had not run for far too long,
assumed disaster,

<!-- S43 -->
and reset the entire spacecraft.
Then it happened again.
And again.

<!-- S44 -->
Engineers on Earth worked out why,
and sent a fix up to Mars.

<!-- S45 -->
And the lesson costs nothing
to carry home.
High priority does not mean
you get served.

<!-- S46 -->
It only means you get asked first.
If the thing you need
is held by somebody slower,
your importance buys you nothing.

<!-- S47 -->
And priority has a second limit.
It decides who goes first.
It does not create
a single extra cycle.

<!-- S48 -->
Suppose every core on your machine
is at one hundred percent.
You might think that means frozen.
It usually doesn't.

<!-- S49 -->
The scheduler hands out slices of time
so quickly
that you cannot feel the joins.

<!-- S50 -->
That is why you can compile something
enormous
and still scroll a web page
while it runs.

<!-- S51 -->
What changes under load
is not really speed.
The computer is not slow.

<!-- S52 -->
It is late.

<!-- S53 -->
You click, and the answer comes
half a second later.
Then a second.
Then five.

<!-- S54 -->
And people are extraordinarily good
at noticing that.
Half a second feels like a machine
that is thinking.

<!-- S55 -->
Five feels like a machine
that has died.

<!-- S56 -->
And there is a version of this
that surprises people most.
Sometimes the processor
is not the problem at all.

<!-- S57 -->
Open too many things at once
and physical memory fills up.
The operating system starts shuffling
pages of memory out to storage.

<!-- S58 -->
Do enough of that
and the machine spends its time
moving memory around
instead of doing your work.

<!-- S59 -->
It has a name too.
Thrashing.

<!-- S60 -->
And this is the confusing one,
because the processor
might not look busy at all.

<!-- S61 -->
It is not working.
It is waiting.

<!-- S62 -->
You can hand a waiting task
the highest priority on the system
and it will wait
at exactly the same speed.

<!-- S63 -->
And then there is
the most human version of this.
The event arrived.
The kernel has it.

<!-- S64 -->
It is sitting in a queue
with your program's name on it.
And your program
is not picking it up.

<!-- S65 -->
Maybe it is doing a long calculation
on the same thread
that is supposed to be watching
its own window.

<!-- S66 -->
So the mouse works.
The keyboard works.
Other programs work.

<!-- S67 -->
And that one window turns pale
and says it is not responding.

<!-- S68 -->
Which is not a diagnosis.
Windows puts that label on a window
after about five seconds
of nobody collecting its messages.

<!-- S69 -->
The system is perfectly alive.
The application simply
has not come to the door.

<!-- S70 -->
The computer receiving your click
and the application answering it
are not the same event.

<!-- S70b -->
By the way, if you'd like to see
where the next question takes us,
consider subscribing.

It really helps the channel.

<!-- S71 -->
There is one more link,
and it is the one
we never think about.
Nothing so far has actually put
anything on your screen.

<!-- S72 -->
The application changes its state.
Something has to build the next frame.
The graphics card has to draw it.
The display has to show it.

<!-- S73 -->
On an ordinary screen
a new picture appears
about every sixteen milliseconds.

<!-- S73b -->
So there is a difference between
the computer dealing with your click
and you seeing that it did.

<!-- S74 -->
And underneath all of it
sits the part
that no amount of engineering fixes.
The operating system knows
that your mouse moved.
It has no idea why.

<!-- S75 -->
You might be aiming at something
in a game.
Or editing a document.
Or you might have knocked the desk.

<!-- S76 -->
To the hardware,
those are the same event.
A system can rank kinds of work.
It cannot guess what you meant.

<!-- S77 -->
So it compromises.
Fast enough for you,
most of the time,
without starving everything else.

<!-- S78 -->
Which brings us back
to that dead screen.
Your click was never one event.

<!-- S79 -->
The hardware has to report it.
The kernel has to store it.
The queue has to reach your program.

<!-- S80 -->
Your program has to run.
The interface has to change.
Something has to draw the new picture,
and the screen has to show it to you.

<!-- S81 -->
Every one of those steps
is small and fast.

<!-- S82 -->
Delay any single one of them
and you don't experience
a slow window.

<!-- S83 -->
You experience a dead computer.

<!-- S84 -->
And the strangest thing
about the whole business
is how rarely it happens.

<!-- S85 -->
We expect a machine
running billions of operations
a second
to answer a twitch of the hand.

<!-- S86 -->
And almost always, it does.

<!-- S87 -->
So the next time you click
and nothing happens,
give it a moment.

<!-- S88 -->
It heard you.

<!-- S89 -->
It just had a queue,
and you were in it.
