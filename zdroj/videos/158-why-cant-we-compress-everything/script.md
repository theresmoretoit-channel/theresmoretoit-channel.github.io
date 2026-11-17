<!-- S01 -->
Here's every script
ever written for this channel.
A hundred and fifty-eight videos,
almost one and a half million bytes of text.

<!-- S02 -->
Run them through an ordinary compressor
called gzip.
They come out at just over half a megabyte.
Almost two thirds gone.

<!-- S03 -->
And nothing is lost.
Unpack the file,
and every script comes back,
letter for letter.

<!-- S04 -->
Now compress it again.

<!-- S05 -->
It gets bigger.
Ninety-eight bytes bigger.

<!-- S06 -->
A third time.
Ninety-eight bytes bigger.
A fourth.
Ninety-eight again.

<!-- S07 -->
The first round throws away two thirds.
The second finds nothing at all.
So why can't we just keep compressing?

<!-- S08 -->
Let's look inside that second file.
gzip didn't compress anything.
It copied the data across, unchanged,
in sixteen blocks.

<!-- S09 -->
Each block got a five-byte label.
Add a small header and a footer,
and you get exactly ninety-eight.

<!-- S10 -->
When a compressor finds nothing to remove,
it stores the data as it is,
and adds only what it needs to undo it.

<!-- S11 -->
So why did the second round find nothing?
And would a cleverer program?

<!-- S12 -->
Text like this is full of repetition.
The same words, the same phrases,
the same little scene markers
at the top of every scene.

<!-- S13 -->
In 1977, Jacob Ziv and Abraham Lempel
published a simple trick.
Don't write a repeat again.
Point back to where it was.

<!-- S14 -->
Go back three hundred characters,
and copy the next twelve.
A few bytes instead of twelve.

<!-- S15 -->
The second trick:
give common letters short codes,
and rare ones long codes.

<!-- S16 -->
In 1951, David Huffman,
a graduate student at MIT,
could take the final exam,
or write a term paper instead.

<!-- S17 -->
The paper, set by Robert Fano,
was to find the most efficient code
of exactly this kind.

<!-- S18 -->
For months, Huffman got nowhere.
He gave up,
and started studying for the exam.
Then it came to him.

<!-- S19 -->
Take the two rarest symbols,
join them into one,
and repeat until a single tree is left.

<!-- S20 -->
He later called it
"the most singular moment of my life."

<!-- S21 -->
Fano hadn't told the class
that he'd struggled with it himself,
and so had Claude Shannon.

<!-- S22 -->
Huffman's code beat both their methods.
And it can be proven
that no code of its kind does better.

<!-- S23 -->
In the early 1990s,
Phil Katz put both tricks together
for ZIP files.
gzip uses the same method.

<!-- S24 -->
The first round already used up
the patterns gzip knows how to find.

<!-- S25 -->
What's left gives it nothing to work with.
To gzip, it looks like noise.

<!-- S26 -->
But a cleverer program
might see patterns gzip missed.
Could some program, someday,
shrink anything you give it?

<!-- S27 -->
No.
And you don't need to know how it works
to be sure of that.

<!-- S28 -->
Take every file
that's exactly three bits long.
There are eight of them.

<!-- S29 -->
Now count everything shorter.
Four files of two bits,
two of one bit,
and one empty file.

<!-- S30 -->
Seven.

<!-- S30b -->
Eight files, and seven shorter places
to put them.

<!-- S31 -->
If every one got shorter,
two would have to share a place.
And when you unpack it,
which one did you mean?

<!-- S32 -->
It's called the pigeonhole principle,
and it holds at any length.
There's always one fewer shorter file
to go around.

<!-- S33 -->
So any compressor that takes every file
and shrinks some of them
has to make others bigger.
Not because it's badly written.
There's nowhere else for them to go.

<!-- S34 -->
Those ninety-eight bytes
are how gzip pays that price.

<!-- S35 -->
Pick any compressor you like.
Of all files of a given size,
it can shrink fewer than one
in two hundred and fifty by a single byte.

<!-- S36 -->
Compression works anyway,
because the files we make aren't random.
They're text, pictures and programs,
full of patterns.

<!-- S37 -->
That hasn't stopped people
from promising more.

<!-- S38 -->
In 1992, WEB Technologies
announced software that could squeeze
almost any data under a kilobyte.
Even its own output,
again and again.

<!-- S39 -->
Its vice president said the method
was "not subject to the laws
of information theory."
The product never shipped.

<!-- S40 -->
So how do photos and music
get so much smaller?
They don't play by this rule at all.

<!-- S41 -->
A JPEG doesn't come back identical.
It comes back close enough.
Detail your eye won't miss
is thrown away for good.

<!-- S42 -->
Zoom in,
and you can see where it went.

<!-- S43 -->
That's lossy compression,
and it's a different game.
This video is about the other kind.
Every bit back, exactly.

<!-- S44 -->
So for files that do have patterns,
how small can they go?
Is there a bottom?

<!-- S45 -->
There is.
It was found in 1948,
in the same paper behind our video
on error-correcting codes.

<!-- S46 -->
There, Claude Shannon showed
how adding redundancy protects a message.
Here, he worked out
how much of it you can take away.

<!-- S47 -->
His answer was a number
he called entropy:
how hard it is to guess
what comes next.

<!-- S48 -->
No lossless code can beat that number
on average.
But you can get as close to it
as you like.

<!-- S49 -->
So how unpredictable is English?
In 1951, Shannon measured it
with a game.

<!-- S50 -->
He gave someone a passage
they'd never seen,
and asked them to guess it,
letter by letter.

<!-- S51 -->
If a guess was wrong,
they guessed again,
until they got it right.

<!-- S52 -->
People turned out to be very good at it.
With a hundred letters of context,
English came out at about one bit
per letter.

<!-- S53 -->
A computer stores each letter
in eight bits.
A human reader needs about one.

<!-- S54 -->
That gap is the room compression works in.
gzip got the channel's scripts down
to under three bits a character.

<!-- S55 -->
So how close to one bit
can a machine get?

<!-- S56 -->
There's a prize for exactly that.
It's called the Hutter Prize,
and since 2020, the task is one file:
a gigabyte of English Wikipedia.

<!-- S57 -->
gzip shrinks it to a third.
The best everyday compressors,
to about a fifth.

<!-- S58 -->
The record, set in July 2026,
is just over a hundred million bytes.
A tenth.

<!-- S59 -->
And the decompressor counts too.
Its size goes into the total,
so you can't hide Wikipedia
inside the program.

<!-- S60 -->
The fund is five hundred thousand euros.
Every one percent of improvement
pays five thousand.

<!-- S61 -->
Marcus Hutter, who funds it, explains why:
"being able to compress well
is closely related
to acting intelligently."

<!-- S62 -->
Because the programs at the top
don't hunt for repeats.
They predict.

<!-- S63 -->
Before each character,
they estimate how likely
every possible next one is.
A good guess costs a fraction of a bit.

<!-- S64 -->
It's Shannon's guessing game,
played by a machine.
The best players now use neural networks,
trained to predict what comes next.

<!-- S65 -->
It works even on finished files.
In 2016, Dropbox began re-packing
its users' JPEGs with a better predictor.
On average, over a fifth smaller.

<!-- S66 -->
Every file came back bit for bit,
and by 2017,
it had saved over forty-six petabytes.
That's over forty-six thousand terabytes.

<!-- S67 -->
Then there are the giants.
In 2023, researchers at DeepMind
used a large language model
as a compressor.

<!-- S68 -->
On small greyscale patches of photos,
it beat PNG:
forty-eight percent of the original size
against fifty-eight.

<!-- S69 -->
On recordings of read speech,
it beat FLAC:
twenty-one percent against thirty.

<!-- S70 -->
But that's without counting the model.
Add its size,
and the result comes out
a hundred and forty times
bigger than the data.

<!-- S71 -->
A compressor bigger than its data
hasn't saved anything.
The program is part of the description.

<!-- S72 -->
And that brings us to the strangest part.
Here are the first million digits of pi.

<!-- S73 -->
Feed them to four compressors.
The best gets them down to about
four hundred and twenty-six thousand bytes.

<!-- S74 -->
Now give the same compressors
a million random digits.
The same result,
within a tenth of a percent.

<!-- S75 -->
But pi isn't made at random.
It follows a mathematical rule.
Here's a program that prints
every one of those million digits.

<!-- S76 -->
Three hundred and sixty-two bytes.
Over two thousand times shorter than the file.

<!-- S77 -->
The compressors couldn't see
the mathematical rule behind pi.
They could only see the digits.

<!-- S78 -->
One way to measure the information
in data is to ask:
how short can a program be,
and still print it?

<!-- S79 -->
That length is called
Kolmogorov complexity,
after one of the men who described it.

<!-- S80 -->
Most data has no short program.
It's the pigeonhole principle again:
there aren't enough short programs
to go around.

<!-- S81 -->
A million random digits
very likely has nothing shorter.
Pi does.

<!-- S82 -->
So why not just find
the shortest program for any file?
Because it's been proven
that no algorithm can do that
for every file.

<!-- S83 -->
Every program gives you an upper limit.
But nothing can always tell you
whether a shorter one exists.
You never know you've reached the bottom.

<!-- S84 -->
gzip found the repeats in the scripts,
and nothing more.
It sees bytes,
not what the words mean.

<!-- S85 -->
To go further, a program
has to predict them better.
And predicting text well
starts to look a lot like understanding it.

<!-- S86 -->
So here's a question for you.
If a program could squeeze Wikipedia
smaller than anything else,
would you say it understands it?
Leave your answer in the comments.
