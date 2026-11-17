<!-- S01 -->
You press play on a cassette recorder.
And this comes out of the speaker.

<!-- S02 -->
It isn't music.
And it isn't a game's soundtrack.

<!-- S03 -->
It is the game.
Every squeal is part of a program,
and the computer is listening to it.

<!-- S04 -->
The cassette player has no idea.
As far as it knows, it's playing a song.

<!-- S05 -->
So how do you turn a song into a game?
And why could one wrong note
throw away five minutes of waiting?

<!-- S06 -->
Here's the trick,
on one particular machine:
the ZX Spectrum,
a British home computer from 1982.

<!-- S07 -->
It uses two kinds of pulse.
A short pair of pulses means zero.

<!-- S08 -->
A one is the same pair,
with each pulse twice as long,
so its tone sits an octave lower.

<!-- S09 -->
Send around fourteen hundred bits
every second,
and you get the noise you just heard.

<!-- S09b -->
It also means a program full of zeros
loads faster than one full of ones.
Every one takes twice as long to send.

<!-- S10 -->
Now, if you grew up in America,
you may never have heard it at all.

<!-- S11 -->
Which is odd,
because the idea itself was American.

<!-- S12 -->
In 1975, at a meeting in Kansas City,
computer hobbyists agreed on a way
to store data as sound
on ordinary audio cassettes.

<!-- S12b -->
A one was eight quick cycles
of a high tone,
a zero four slower cycles of a low one.
Three hundred bits a second.

<!-- S13 -->
Early machines like the Apple II
and the TRS-80
saved their programs
on everyday tape recorders.

<!-- S14 -->
But American home computing
moved on quickly.

<!-- S15 -->
In 1983, one magazine reported a survey:
nine in ten new Commodore 64 owners
were buying a disk drive
together with the computer.

<!-- S16 -->
In Britain, the story went the other way.

<!-- S17 -->
The Spectrum cost a hundred
and twenty-five pounds,
and it came with no storage at all.
You used whatever cassette player
you already had.

<!-- S18 -->
So for millions of kids across Europe,
this noise was the sound
of a game about to start.

<!-- S18b -->
After enough loads,
you could even tell which game it was
just from the screech.

<!-- S19 -->
So let's follow one game
from the tape into the computer.

<!-- S20 -->
You type LOAD, press enter,
and press play.

<!-- S21 -->
First comes a steady hum,
eight hundred cycles a second,
for about five seconds.

<!-- S22 -->
It carries no data at all.
It's there so the computer
can find the signal
and lock onto its rhythm.

<!-- S23 -->
Then two quick pulses, the sync.
They mean: from here on, it's data.

<!-- S24 -->
The first thing to arrive
is a short header.
Nineteen bytes:
a name of up to ten letters,
what kind of file it is,
and how long it's going to be.

<!-- S25 -->
Then a second, shorter hum,
two seconds this time,
and then the game itself.

<!-- S26 -->
Every byte is eight of those notes,
one after another,
with no gaps between bytes at all.

<!-- S27 -->
And the computer doesn't hear notes.
It times the gap between one edge
of the signal and the next.

<!-- S28 -->
A short pair is a zero.
A long pair is a one.

<!-- S28a -->
That's the whole decoder.

<!-- S28b -->
And the noise at the start of this video
isn't a sound effect.
We generated it from exactly these rules,
and a real Spectrum program is inside.

<!-- S28c -->
We'll play all of it at the very end.
Record it, and a Spectrum will load it.

<!-- S29 -->
Most games showed a picture first,
and it loaded in a strange order.

<!-- S30 -->
Thin stripes appeared, eight lines apart,
then filled in, line by line,
one third of the screen at a time.
And the colours came last,
sweeping down over everything.

<!-- S31 -->
That picture alone
took about forty seconds.
The whole game, around five minutes.

<!-- S32 -->
And at the end of each block
comes one more byte.

<!-- S33 -->
While saving, the Spectrum runs
every byte of the block
through a simple rule called XOR,
and records the result as one more byte.

<!-- S34 -->
While loading, it repeats the calculation.
If the results agree,
the block arrived intact.

<!-- S35 -->
If they don't, the Spectrum says this.

<!-- S36 -->
Five minutes of waiting,
and one byte decides
it was all for nothing.
Rewind, and start again.

<!-- S37 -->
Oddly, a broken header
gets no error at all.
The Spectrum simply ignores it,
and keeps listening for the next one.

<!-- S38 -->
Other computers made other bets.

<!-- S39 -->
The Commodore 64 recorded
every block twice,
so a damaged spot in one copy
could be rescued from the other.

<!-- S40 -->
Safer, but slow.
With Commodore's built-in routine,
a forty-kilobyte program
took about twelve and a half minutes.

<!-- S41 -->
So game publishers wrote
their own faster loaders,
some of them up to about ten times faster.

<!-- S42 -->
And then there was the cassette player.

<!-- S43 -->
Too quiet,
and the edges sink into the hiss.
Too loud,
and they smear into each other.

<!-- S44 -->
A tape running slightly fast or slow
stretches every pulse,
and the computer is measuring time.

<!-- S45 -->
Worst of all was the azimuth,
the angle of the tape head.
A tape recorded on one machine
might not line up with another.

<!-- S46 -->
So people pushed a tiny screwdriver
into a hole next to the head,
and turned it a fraction at a time,
listening.

<!-- S47 -->
It looked like superstition.
It was signal tuning.

<!-- S48 -->
But notice what the cassette player
never had to do.

<!-- S49 -->
It never understood a single bit.
It recorded sound,
and played it back.

<!-- S50 -->
Which means a program
didn't really need a cassette.
Anything that could carry sound
could carry software.

<!-- S50b -->
It also meant that copying a game
was as easy as copying an album.
Two cassette decks and a cable.

<!-- S51 -->
Atari used both stereo tracks.
The program on one,
and a voice on the other,
talking to you through the TV
while the game loaded.

<!-- S52 -->
In Yugoslavia, a show on Radio Belgrade
broadcast programs over the air.

<!-- S53 -->
Listeners recorded them on tape,
around a hundred and fifty programs
between 1983 and 1986.

<!-- S54 -->
In Czechoslovakia, it was television.
A program played as sound
under the closing credits.

<!-- S55 -->
And in 1983, the singer Pete Shelley
hid a Spectrum program
at the end of a vinyl album.

<!-- S56 -->
Copy it to tape, load it,
and the lyrics appeared on screen
in time with the songs.

<!-- S57 -->
But there was a catch.

<!-- S58 -->
The radio could carry the sound
to every computer in the country.
Only the right one could understand it.

<!-- S59 -->
Play a Spectrum game to a Commodore,
and the Commodore hears noise.
The bits only mean something
to a machine that knows the format.

<!-- S60 -->
So Dutch radio tried to fix that.
In 1982, it created BASICODE:
one sound format,
with a small translator program
for each kind of computer.

<!-- S61 -->
And that problem never went away.
A file is only useful
if something can still read it.

<!-- S62 -->
Cassettes lost, of course.
Floppy disks were faster,
then hard drives, then flash.

<!-- S63 -->
Except that tape never actually left.
Data centres still keep
their archives on magnetic tape.

<!-- S64 -->
One modern LTO-9 cartridge
holds eighteen terabytes.

<!-- S65 -->
Converted to Spectrum speed,
that capacity would fill roughly
twenty-nine million cassettes,
and take more than three thousand
years to load.

<!-- S66 -->
Still the same idea, though.
Patterns on a moving strip of tape,
turned back into numbers
when you need them.

<!-- S67 -->
So next time you hear that screech,
remember what it is.
Not noise.
A program, travelling as sound.

<!-- S68 -->
And somewhere in 1985,
a kid is sitting in front of a television,
waiting for it to stop.
Because when it does,
the game begins.

<!-- S69 -->
So here's a question for you.
If you ever loaded a game from a cassette,
what do you remember most about it?
Let me know in the comments.

<!-- S70 -->
And as promised, here's that program.
Just like Czechoslovak television,
we've put it under the closing credits.
