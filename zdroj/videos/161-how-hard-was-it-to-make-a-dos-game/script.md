<!-- S01 -->
In 1993, a game called Doom
ran on a computer
with four megabytes of memory.

<!-- S02 -->
That's about the size
of a single photo on your phone.

<!-- S03 -->
There was no 3D accelerator.
The main processor
did all the rendering.

<!-- S04 -->
Today, a developer starts with an engine,
like Unity or Unreal,
that takes care of graphics, sound,
memory and the hardware.

<!-- S05 -->
On DOS, all of that
was the developer's problem.
And quite often, the player's too.

<!-- S06 -->
So how hard was it
to make a game for DOS?

<!-- S07 -->
Let's start with memory,
because memory was a mess.

<!-- S08 -->
The original IBM PC, from 1981,
could address one megabyte of memory.

<!-- S09 -->
But only the first
six hundred and forty kilobytes
were meant for programs.

<!-- S10 -->
The other three hundred and eighty-four
were reserved for video memory,
expansion cards and the BIOS.

<!-- S11 -->
For more than a decade,
DOS normally started programs
inside that space.
Anything beyond it took extra work.

<!-- S12 -->
That's where the famous line comes from.
640K ought to be enough for anybody.

<!-- S13 -->
It's usually credited to Bill Gates.
There's no record that he ever said it,
and he denies it.

<!-- S14 -->
By the early nineties,
a PC came with four megabytes,
or eight.

<!-- S15 -->
And a game could still stop
with the words
"not enough memory".

<!-- S16 -->
Having the memory
and being able to use it
were two different things.

<!-- S17 -->
One way around it was expanded memory,
or EMS.

<!-- S18 -->
A sixty-four kilobyte window
sat in the upper part
of that first megabyte.
Through it, a program could see
four pages of extra memory,
sixteen kilobytes each,

<!-- S19 -->
and swap them for others,
like turning the pages of a book
through a hole in a sheet of paper.

<!-- S20 -->
Another way was extended memory,
reached through a driver called HIMEM.

<!-- S21 -->
And this is where
the developer's problem
became the player's.

<!-- S22 -->
Drivers for the mouse, the CD drive
or the sound card
took a bite out of that precious memory,
unless you managed to load them high.

<!-- S23 -->
So players learned to edit two files,
CONFIG.SYS and AUTOEXEC.BAT.

<!-- S24 -->
One game wanted EMS.
Another wanted it switched off,
with a setting called NOEMS.
And a third needed every free kilobyte.

<!-- S25 -->
In 1993, MS-DOS 6 added
a menu at startup.

<!-- S26 -->
You picked the configuration
for the game you wanted to play,
and the computer started up for that game.

<!-- S27 -->
Some people ended up
with a separate entry
for almost every game they owned.

<!-- S28 -->
But by then,
the bigger games had found
a way around the limits of DOS.

<!-- S29 -->
Since the 386,
the processor itself could run
in 32-bit protected mode,
with room for up to four gigabytes.

<!-- S30 -->
We've looked at protected mode
in an earlier video.
DOS, though, couldn't use it.

<!-- S31 -->
So games brought their own helper,
a DOS extender.
The best known was DOS/4GW.

<!-- S32 -->
It came bundled with a popular compiler,
Watcom C.

<!-- S33 -->
When a game started,
DOS/4GW switched the processor
into protected mode,
giving the game access
to memory beyond the DOS limit.

<!-- S34 -->
DOS was still there underneath,
providing services like file access.
But the game now ran in protected mode,
not as a traditional DOS program.

<!-- S35 -->
If you played DOS games in the nineties,
you've seen its name
flash by on the screen.

<!-- S37 -->
Now, the picture.
In one of the most widely used VGA modes,
called Mode 13h,
the screen was three hundred and twenty
by two hundred pixels,
in two hundred and fifty-six colours.

<!-- S38 -->
Each pixel was one byte.
To colour a pixel,
you wrote a number into memory.
No graphics library. Just memory.

<!-- S39 -->
The whole screen took
sixty-four thousand bytes.

<!-- S40 -->
That's just under sixty-four kilobytes,
small enough to fit in one segment,
the block a 16-bit program
could address in one go.
For once, memory was on your side.

<!-- S41 -->
But if you draw straight
onto the visible screen,
the player sees half-finished pictures,
and the image flickers.

<!-- S42 -->
So games drew each frame
in a hidden buffer first,
then copied the finished image
into video memory.

<!-- S43 -->
In 1991, Michael Abrash,
a programmer and writer,
published a better way.
He called it Mode X.

<!-- S44 -->
It used a part of the VGA
that most programmers
had never touched.

<!-- S45 -->
It gave square pixels,
and room for several screens
in video memory.

<!-- S46 -->
The game drew on a screen
nobody could see,
and then simply switched to it.
But it was much harder to program.

<!-- S47 -->
Then there was sound.
And sound was a lottery.

<!-- S48 -->
The PC's own speaker
was built to beep.

<!-- S49 -->
Then came sound cards,
and other sound hardware.
No two of them
worked the same way.

<!-- S50 -->
AdLib, with a Yamaha chip
that synthesised music.
Sound Blaster, which could also play
recorded sound.

<!-- S51 -->
The Roland MT-32,
an expensive box with richer instruments.
The Gravis UltraSound.

<!-- S52 -->
Supporting all of them
meant writing different drivers.

<!-- S53 -->
And the game had to know
where the card was.
Its port, its interrupt,
and its DMA channel.

<!-- S54 -->
The usual answer, for a Sound Blaster,
was port 220, IRQ 7, DMA 1.
Usually.

<!-- S55 -->
Get one of them wrong,
and the game was silent.
Or it froze.

<!-- S56 -->
In 1991, a programmer called John Miles
released a library
that talked to many sound cards
through a single interface.

<!-- S57 -->
A game could write its sound code once,
and let the library deal with the card.

<!-- S58 -->
It was another layer
between the game and the hardware.
Keep that in mind.

<!-- S59 -->
And then there was speed.
Programmers counted
every step the processor took.

<!-- S63 -->
To find a pixel on the screen,
you multiply its row
by three hundred and twenty.

<!-- S63b -->
On older processors,
multiplying could be expensive.

<!-- S64 -->
But three hundred and twenty
is two hundred and fifty-six
plus sixty-four.
Both are powers of two.

<!-- S65 -->
So you can replace the multiplication
with two bit shifts and an addition.

<!-- S67 -->
Chris Sawyer went all the way down to the metal.
He wrote Transport Tycoon, in 1994,
almost entirely in assembly language,

<!-- S68 -->
the instructions
the processor itself understands,
one by one.

<!-- S69 -->
And sometimes,
even all of that wasn't enough.

<!-- S70 -->
In 1990, Wing Commander had a bug
that the team couldn't find,
with the deadline close.

<!-- S71 -->
When you quit the game,
the memory manager crashed
with an error message.

<!-- S72 -->
So a programmer, Ken Demarest,
opened the memory manager
in a hex editor
and changed the text of that message.

<!-- S73 -->
Now it said:
"Thank you for playing Wing Commander."

<!-- S74 -->
Then the team found the real bug,
and the joke never shipped.

<!-- S74b -->
Some players are still sure they saw it.
And later Origin games
really did say goodbye like that.

<!-- S75 -->
Which brings us back to Doom.

<!-- S76 -->
Doom used DOS/4GW,
and ran as a 32-bit program.

<!-- S77 -->
Floating-point hardware
wasn't guaranteed on every PC.

<!-- S78 -->
So Doom used fixed-point arithmetic.
Whole numbers,
with the lower sixteen bits
standing for the fraction.

<!-- S79 -->
And its world wasn't
really three-dimensional.

<!-- S80 -->
Every level is a flat floor plan,
with a height for each floor
and each ceiling.

<!-- S81 -->
One room can never sit above another.
And you can't properly look up or down.

<!-- S82 -->
Before a level could be played,
a tool cut the map
into a binary tree, a BSP.

<!-- S83 -->
The engine walks that tree
from front to back,
starting on the player's side,
and skips areas that can't be seen.

<!-- S84 -->
And Doom wasn't even written on DOS.

<!-- S85 -->
id Software built it
on NeXT workstations,
and compiled the result for DOS.

<!-- S86 -->
Doom wasn't a general 3D engine.
It was built for exactly
one kind of world.
That specialisation
helped it run on a 386.

<!-- S87 -->
And other studios wanted that world.

<!-- S88 -->
Raven Software licensed Doom's engine
for Heretic, in 1994,
and Hexen, in 1995.

<!-- S89 -->
Doom helped establish
a new way of making games.
Studios could license an existing engine,
instead of building it all from scratch.

<!-- S90 -->
A memory extender.
A sound library.
A licensed engine.

<!-- S91 -->
Each one took a problem
off the developer's hands.
And the layers kept growing,
into the engines
that developers start with today.

<!-- S92 -->
So was making games harder back then?
In many ways, yes.

<!-- S93 -->
But the difficulty didn't disappear.
It moved.

<!-- S94 -->
Today, developers fight
with gigabytes of assets
and millions of polygons,
instead of a few hundred kilobytes.

<!-- S95 -->
On DOS, even the player
had to know where their memory went.

<!-- S96 -->
So here's a question for you.
Do you remember building
a boot menu just to get one game running?
And was it a struggle,
or half the fun?
Let me know in the comments.
