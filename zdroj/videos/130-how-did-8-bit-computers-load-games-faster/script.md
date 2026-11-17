<!-- S01 -->
This is a ZX Spectrum loading a program.

<!-- S02 -->
And this is the same program,
on the same computer,
from the same kind of cassette.

<!-- S03 -->
It finishes in half the time.
Nothing in the hardware changed.
No faster tape, no faster recorder.

<!-- S04 -->
The only thing that changed
was the way the computer listened.

<!-- S05 -->
So how did 8-bit computers
learn to load games faster?
And if it was that easy,
why didn't they do it from the start?

<!-- S06 -->
In an earlier video,
we saw how the Spectrum stores bits
as pulses on the tape.

<!-- S07 -->
A short pair of pulses means zero.
A pair twice as long means one.

<!-- S08 -->
That gives about fourteen hundred bits
every second.
A game that fills the 48K memory
takes around five minutes.

<!-- S09 -->
Now make every pulse half as long.

<!-- S10 -->
The computer still tells short from long.
But twice as many bits
pass the tape head every second.

<!-- S11 -->
That's the whole trick behind a turbo loader.
And it isn't just a thought experiment.

<!-- S12 -->
In 1984, the game Skool Daze
loaded its data at twice
the Spectrum's normal speed.

<!-- S13 -->
So why didn't the Spectrum
load that fast by itself?

<!-- S14 -->
The built-in loader is stored in the ROM,
the memory chip the computer starts from.
It doesn't measure a pulse in seconds.

<!-- S15 -->
It counts.
After each edge of the signal,
it waits a moment,
then counts how long until the next one.

<!-- S16 -->
One single number in the ROM
decides where zero ends
and one begins.

<!-- S17 -->
And that number leaves a lot of room.
A zero can stretch
by more than forty per cent
and still be read as a zero.

<!-- S18 -->
That margin is what lets a worn tape
on a cheap recorder
still load.

<!-- S19 -->
And the computer wasn't the limit.
The Spectrum checks the tape signal
about sixty thousand times a second.

<!-- S20 -->
The cassette was the limit.
Shorter pulses mean higher tones.
At double speed, a zero
moves from two kilohertz to four.

<!-- S21 -->
And high tones are exactly what
a cheap recorder,
or a slightly misaligned head,
loses first.

<!-- S22 -->
A Spectrum magazine in 1986 reckoned
most people could manage
at least twice the normal speed.
How much further
depended on the recorder.

<!-- S23 -->
But turbo had a stranger problem.

<!-- S24 -->
If the computer only knows
the slow format,
how does it load the program
that teaches it the fast one?

<!-- S25 -->
The answer is at the start of the tape.
The first part is recorded
in the ordinary, slow format.

<!-- S26 -->
It's short,
and the ROM loads it like any other program.

<!-- S27 -->
Then that little program takes over.
In the simplest case,
it's a copy of the ROM's own loading routine,
with a few numbers changed.

<!-- S28 -->
In Skool Daze,
the changes sit in three places.
A shorter wait, a new starting count,
a new dividing line.

<!-- S29 -->
So the ROM loads the program
that does the ROM's job, only faster.

<!-- S30 -->
It's a bit like downloading
a faster downloader.
The slow step gets you the tool.
The tool does the rest.

<!-- S31 -->
Commercial games used the same idea.
One well-known example was Speedlock,
first used by Ocean in 1984.

<!-- S32 -->
One of its authors said he wrote it
because he was fed up
with how long the standard loader took.

<!-- S33 -->
But here's the surprise.
Speedlock was only about one and a half
times as fast.

<!-- S34 -->
The first day
of Daley Thompson's Decathlon
took three minutes twenty seconds,
where the same data at normal speed
would take four minutes forty-seven.

<!-- S35 -->
Later versions were only about
a fifth faster than the ROM.
Because speed wasn't the only job.

<!-- S36 -->
From 1983, copying programs
could read a game's header
and copy the whole game onto another tape.

<!-- S37 -->
A custom format
gave those programs nothing to read.

<!-- S38 -->
Early Speedlock even chopped its lead-in tone
into short bursts,
so the ROM's own loader
wouldn't recognise it at all.

<!-- S39 -->
And you could hear it.
A Speedlock tape loaded with clicks,
and jerking stripes around the screen.

<!-- S40 -->
It didn't stop anyone copying
a tape from one deck to another.
But it did give publishers
a reason to write their own loaders.

<!-- S41 -->
On the Commodore 64,
the reason to switch was much bigger.

<!-- S42 -->
Its built-in routine
recorded everything twice,
as a safety copy.
A forty-kilobyte game took
about twelve and a half minutes.

<!-- S43 -->
And here, the recorder
did almost nothing clever.
It just turned the sound
into clean on and off pulses.

<!-- S44 -->
The computer timed every pulse itself,
in software.

<!-- S45 -->
So a faster loader
was just a different program.

<!-- S46 -->
In 1985, Compute! magazine
tested one called TurboTape.

<!-- S47 -->
Once it had found the program on the tape,
it loaded twelve kilobytes
in twenty-eight seconds.

<!-- S48 -->
Commodore's own floppy disk drive
needed thirty-four seconds.

<!-- S49 -->
A cassette,
beating a floppy disk.

<!-- S50 -->
And because the computer was doing
all the listening itself,
it could do other things in between.

<!-- S51 -->
Loaders such as Freeload
gave reading the tape priority.
Whatever processor time was left
went to music, smooth scrolling,
even small games.

<!-- S52 -->
With Mastertronic's Invade-a-Load,
you played a Space Invaders clone
while the real game loaded.

<!-- S53 -->
The Atari 8-bit computers
were a different story.

<!-- S54 -->
Here, the recorder did the listening.
Inside it were two filters,
one for each tone,
and a circuit that handed the computer
finished ones and zeros.

<!-- S55 -->
The standard was six hundred bits a second,
and the filters limited
how much faster it could go.

<!-- S56 -->
Clever software could nudge that up
a little, at best to about twelve hundred.
But to go much faster,
you had to open the recorder.

<!-- S57 -->
And in Czechoslovakia, people did.

<!-- S58 -->
A floppy drive there
cost two to three times
as much as the computer itself.
So most Atari owners there stayed with tape.

<!-- S59 -->
In 1987, a Prague student
from the local Atari club
designed Turbo 2000.

<!-- S60 -->
It added one new path for the signal.
A wire inside the recorder took the sound
straight from its amplifier,
before the filters,
through one small chip,
and onto the line to the computer.

<!-- S61 -->
A switch, flipped by the computer,
chose between the old path and the new.

<!-- S62 -->
The computer now timed the pulses itself.
Around two thousand three hundred bits
a second.
Almost four times as fast.

<!-- S63 -->
Turbo wasn't one universal format.

<!-- S64 -->
Sometimes you changed the program.
Sometimes, you had to change the machine.

<!-- S65 -->
And faster wasn't free.

<!-- S66 -->
Compute! warned that a TurboTape recording
would sometimes refuse to load
on a different recorder,
with its head aligned slightly differently.

<!-- S67 -->
The standard save, it said,
was much slower,
but extremely reliable.

<!-- S68 -->
Recording everything twice
wasn't Commodore being lazy.
It was the price of loading reliably.

<!-- S69 -->
But a different loader
could also do something unexpected.
It could read a tape
that the built-in one refused.

<!-- S70 -->
On the Sharp MZ-800,
a computer that found its way
to Czechoslovakia in the late 1980s,
owners knew a program called Turbo Copy.

<!-- S71 -->
A game would fail to load,
with a checksum error.
Owners found Turbo Copy
could often load it anyway.

<!-- S72 -->
Then you saved it at normal speed
onto a fresh cassette,
and the computer
loaded it normally again.
It felt like repairing a broken game.

<!-- S73 -->
So how could one loader read
what the other couldn't?

<!-- S74 -->
The Sharp's ROM recorded every block twice,
at about twelve hundred bits a second.

<!-- S75 -->
And it never measured a pulse.
After each pulse began,
it waited a fixed moment,
and looked once.

<!-- S76 -->
Still high?

<!-- S76b -->
That's a one.

<!-- S76c -->
Already low?

<!-- S76d -->
That's a zero.

<!-- S77 -->
A stopwatch, set in advance.

<!-- S78 -->
On an old tape, or a different recorder,
the pulses came back a little rounder.
Then that single look
could see the wrong level.

<!-- S79 -->
One wrong bit spoils the checksum.
If both copies fail,
the load fails.

<!-- S80 -->
Turbo Copy listened differently.
It timed every pulse
with the computer's timer chip.

<!-- S81 -->
And before each block,
it listened to the lead-in tone,
and set its dividing line
from the pulses it was actually hearing.

<!-- S82 -->
Its stopwatch was set
to the tape in front of it.

<!-- S83 -->
And the repair wasn't a copy of the sound.
Turbo Copy kept the bytes,
and wrote a brand new,
cleanly timed signal.

<!-- S84 -->
The data hadn't been lost.
The usual way of reading it
just wasn't good enough.

<!-- S84b -->
Turbo Copy could also save the game with turbo,
at two or three times the normal speed,
with its own small loader in front.

<!-- S85 -->
And that's what all of these
have in common.

<!-- S86 -->
The cassette stayed the same.
What changed was the way it was read.

<!-- S87 -->
Today, we expect games to load instantly.
In the 1980s, loading was part of the game.
You listened to the tape.
You watched the stripes.
You waited.

<!-- S88 -->
And sometimes, a different loader
made the same cassette behave
like a completely different machine.

<!-- S89 -->
The computer didn't need a faster tape.
It needed a better way to listen.

<!-- S90 -->
So here's a question for you.
Did you use turbo loaders back then?
How do you remember them?
Did they fail more often?
Let me know in the comments.

<!-- S91 -->
And finally, the whole turbo tape,
start to finish.
First the part at normal speed,
then the turbo.
For a program this small,
turbo doesn't pay off.
The loader takes longer
than the time it saves.
For a whole game, it could save minutes.
