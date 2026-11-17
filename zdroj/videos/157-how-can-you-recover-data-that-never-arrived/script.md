<!-- S01 -->
This is a QR code.
It holds one short line of text.

<!-- S02 -->
The phone reads it straight away.

<!-- S03 -->
Now let's tear a piece out of it.

<!-- S04 -->
And scan it again.
The same text.
Every letter.

<!-- S05 -->
Part of that code is gone.
Not hard to read.
Gone.

<!-- S06 -->
So how can a phone read something
that is no longer there?

<!-- S07 -->
Here's the same problem, made smaller.
Someone sends you eight bits.
On the way, three of them are lost.

<!-- S08 -->
Each missing bit is a zero or a one,
so there are eight ways to fill the gaps.
And nothing in what arrived
tells you which one is right.

<!-- S09 -->
And yet the phone just did exactly that.
It wasn't guessing.
The answer was sent
before anything was lost.

<!-- S10 -->
The trick is to send more
than the message itself.

<!-- S11 -->
The simplest way
is to say everything three times.
A zero is sent as three zeros,
a one as three ones.

<!-- S12 -->
Noise flips one of them,
and you receive one, zero, one.
Two votes against one.
It was almost certainly a one.

<!-- S13 -->
If noise flips one bit in ten,
at random and independently,
a vote of three goes wrong
less than three times in a hundred.

<!-- S14 -->
But you've tripled
everything you send.
To get closer to perfect,
you'd repeat five times, then nine,
then a hundred...
and the message slows to a crawl.

<!-- S15 -->
For a long time,
that looked like the price.
Fewer errors, slower messages.
Keep that in mind.

<!-- S16 -->
In the late 1940s,
Richard Hamming at Bell Labs
had a problem of his own.

<!-- S17 -->
He mostly got time on a relay computer
at weekends,
when nobody was there to watch it.

<!-- S18 -->
The machine could tell
when it had made a mistake.
It would try the step again,
three times...
and then drop his job.
Two weekends in a row,
he lost his work.

<!-- S20 -->
His question, in his own words:
"If the machine can locate
there is an error,
why can it not locate where it is?"
The actual language, he admitted,
was probably a bit stronger.

<!-- S22 -->
His answer takes four bits of message
and adds three check bits.
Seven bits in all.

<!-- S23 -->
Each check bit looks after
a different group of positions,
and makes sure that group
holds an even number of ones.

<!-- S24 -->
The groups overlap in a careful pattern.
Every position belongs
to its own combination of groups.

<!-- S25 -->
Now flip one bit.
Say, the one in position six.

<!-- S26 -->
The receiver runs the three checks again.
The first one passes.
The second fails.
The third one fails.

<!-- S27 -->
Write a failed check as one,
a passed check as zero,
and read them from the last to the first.
One, one, zero.
In binary, that's six.

<!-- S28 -->
The checks don't just say
that something went wrong.
They point at the exact bit.

<!-- S29 -->
Flip it back,
and the message is whole again.
Nobody had to send anything twice.

<!-- S30 -->
So that's the answer.
The receiver doesn't rebuild
lost information out of nothing.
The sender packed it in,
ahead of time.

<!-- S32 -->
Not every check can do that.
A checksum, like the one in our video
about Btrfs,
can tell you a block is damaged,
but not what the original data were.

<!-- S33 -->
And there's a second kind of damage.
Sometimes a bit isn't wrong.
It's just missing,
and you know exactly where the gap is.

<!-- S34 -->
That's called an erasure,
and erasures are easier.

<!-- S35 -->
Send four numbers,
four, seven, two and nine,
and a fifth one:
their sum, twenty-two.

<!-- S36 -->
If any one of them goes missing,
the others tell you what it was.
Four, seven, something, nine,
twenty-two.
It has to be two.

<!-- S37 -->
Servers protect their disks
with a similar kind of check,
spread across the drives.
When one drive dies,
its contents are worked out from the rest.

<!-- S38 -->
So how much extra do you need?
Repetition says:
to get errors down to nothing,
you have to slow down to nothing.

<!-- S39 -->
Two years before Hamming's paper
came out,
his colleague Claude Shannon
had published a stranger answer.

<!-- S40 -->
Every channel,
a radio link, a cable, a disc,
has a limit.
A top speed for information.

<!-- S41 -->
Below that limit,
errors can be made as rare as you like,
without slowing down.
Not by repeating more.
By coding smarter.

<!-- S42 -->
Above it,
no code in the world will help.

<!-- S43 -->
But there was a catch.
Shannon proved that such codes exist.
He didn't show how to build one
that anybody could use.

<!-- S44 -->
His proof said a code picked at random
would almost certainly be good.
But the obvious way to decode it
means comparing what arrived
with every possible message...
and for a block of a thousand bits,
there are more of those
than atoms in the universe.

<!-- S46 -->
So Shannon's paper wasn't a solution.
It was a promise.
And engineers spent the next
forty-five years trying to keep it.

<!-- S47 -->
Hamming's code was a first step.
It fixes one wrong bit in seven.

<!-- S48 -->
But real damage comes in bursts.
A scratch or a crackle of static
takes out hundreds of bits in a row.

<!-- S49 -->
In 1960, Irving Reed and Gustave Solomon,
at MIT's Lincoln Laboratory,
published a paper five pages long.

<!-- S50 -->
Their codes work on whole bytes,
not single bits.
If a burst wrecks all eight bits
of a byte,
that's still just one bad byte.

<!-- S51 -->
One common version adds
thirty-two check bytes
to two hundred and twenty-three
bytes of data.

<!-- S52 -->
It can fix any sixteen bytes
that arrive wrong...
or rebuild thirty-two
that never arrive at all.

<!-- S53 -->
That's how a CD plays through a scratch.
Its two Reed-Solomon codes
can fully repair a gap
of about four thousand bits,
two and a half millimetres of track.

<!-- S54 -->
And it's why the torn QR code
still worked.
At its strongest setting,
a QR code can rebuild
up to about thirty percent of its bytes
and still give back every letter.

<!-- S56 -->
Voyager 2 left Earth in 1977
already carrying a Reed-Solomon encoder.

<!-- S57 -->
But at Jupiter and Saturn,
it guarded everything but the pictures
with an older code, by Marcel Golay,
which sent one extra bit
for every bit of data.

<!-- S58 -->
For Uranus and Neptune,
with the signal getting weaker,
engineers switched Reed-Solomon on,
on top of a second code
that every bit already went through.

<!-- S59 -->
With that second code alone,
about five bits in a thousand
were still wrong.
With Reed-Solomon on top,
about one in a million.

<!-- S60 -->
Noise also comes in bursts,
so Voyager shuffled
the bytes of four blocks together
before sending them.

<!-- S61 -->
A burst that would have wrecked one block
now takes a few bytes from each...
few enough for every block
to repair itself.

<!-- S62 -->
The rest of how Neptune's pictures
got home
is in our video about Voyager.

<!-- S63 -->
But even this
was still short of Shannon's limit...
and a code that could get much closer
already existed.

<!-- S65 -->
In 1960, in his doctoral thesis at MIT,
Robert Gallager described codes
made of many simple checks,
each one looking at only a few bits.

<!-- S66 -->
Decoding them meant the checks
passing guesses back and forth,
round after round...
far too much
for the computers of the 1960s.
So the idea was put away,
and mostly forgotten for thirty years.

<!-- S68 -->
In 1993,
a team led by two French engineers,
Claude Berrou and Alain Glavieux,
presented turbo codes
at a conference in Geneva.

<!-- S69 -->
Their results were so close
to Shannon's limit
that many experts assumed
they'd made a mistake.
Probably a factor of two,
somewhere in their calculations.

<!-- S70 -->
Within a year,
other labs had confirmed it.

<!-- S71 -->
Turbo codes also worked
by passing guesses back and forth,
and that sent people back to Gallager.

<!-- S72 -->
In 1995 and 1996,
David MacKay and Radford Neal
rediscovered his codes,
and showed they could get
just as close.

<!-- S73 -->
By 2001,
a refined version of Gallager's codes
came within four hundredths of a decibel
of Shannon's limit.

<!-- S74 -->
That's less than one percent
more signal power
than the theoretical minimum.
The promise of 1948 had been kept.

<!-- S75 -->
Today, Gallager's codes carry
much of the data in 5G phones,
in modern Wi-Fi,
and in satellite television.

<!-- S77 -->
Now, back to our eight bits.
Three were lost,
and there are eight ways
to fill the gaps.

<!-- S78 -->
But these eight bits
were never just a message.
They carried four bits of data,
Hamming's three checks,
and one more check over all eight.

<!-- S79 -->
Of all two hundred and fifty-six
possible patterns of eight bits,
only sixteen follow those rules.

<!-- S80 -->
Test the eight candidates.
One by one, they fail.
Only one is left.

<!-- S81 -->
The missing bits were never really gone.
Their information was still there,
in the bits that survived.

<!-- S82 -->
So here's a question for you.
Have you ever noticed error correction
at work in something you use every day?
Let me know in the comments.
