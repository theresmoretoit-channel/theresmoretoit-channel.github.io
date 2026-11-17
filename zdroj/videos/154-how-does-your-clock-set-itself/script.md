<!-- S01 -->
Somewhere in your home,
there might be a clock
that nobody has ever set.

<!-- S02 -->
It survives power cuts.
It changes for daylight saving time
on its own, in the middle of the night.

<!-- S03 -->
It has no internet connection.
No Wi-Fi, no GPS,
no app on your phone.

<!-- S04 -->
All it has is a tiny radio receiver.
And once every second,
it hears a single pulse.

<!-- S05 -->
So how does a clock
turn one pulse per second
into the exact time, the date,
and even the day of the week?

<!-- S06 -->
In Europe, those pulses come
from DCF77, near Frankfurt.
In America, from WWVB, in Colorado.
Different transmitters, the same idea.

<!-- S07 -->
Take the German one.
It sends a steady radio wave,
day and night.
And at the start of every second,
it briefly turns that wave down.

<!-- S08 -->
The trick is how long
it stays down.

<!-- S09 -->
A dip of a tenth of a second
means zero.
A dip of two tenths means one.

<!-- S10 -->
That's the whole idea.
No packets, no network.
Just a radio wave that dips
for a short time, or a longer one.

<!-- S11 -->
One bit every second.
Which means it would take a whole minute
to send just sixty bits.

<!-- S12 -->
And in fact, it sends only fifty-nine.

<!-- S13 -->
In the last second of every minute,
the wave doesn't dip at all.
And that missing dip
is the most important part
of the entire signal.

<!-- S14 -->
Because when the next dip arrives,
the clock knows
a new minute has just begun.

<!-- S15 -->
The gap works like a full stop.
Everything between two gaps
is one complete sentence.

<!-- S16 -->
So what fits into a sentence
of fifty-nine bits?

<!-- S17 -->
The minute. The hour.
The day of the month, the day of the week,
the month, and the year.

<!-- S18 -->
Most numbers are sent digit by digit.
Forty-seven minutes
isn't sent as forty-seven.
It's sent as two separate digits,
a four and a seven.

<!-- S19 -->
Four bits are enough for any digit
from zero to nine.
The tens of minutes never go past five,
so they get only three.

<!-- S20 -->
And the year gets just two digits.
As far as the transmitter is concerned,
2026 is simply twenty-six.
The clock supplies the century itself.

<!-- S21 -->
But radio isn't a clean channel.
A motor, a phone charger,
a cheap LED bulb...
any of them can smudge a dip.

<!-- S22 -->
So after each block of numbers
comes one extra bit, called a parity bit.

<!-- S23 -->
It's chosen so that the number of ones
in the block always comes out even.

<!-- S24 -->
If interference flips a single bit,
the count turns odd,
and the clock knows
something went wrong.

<!-- S25 -->
But if two bits flip,
the count is even again,
and the mistake slips through.

<!-- S26 -->
That's why many clocks
don't trust a single minute.
They wait for another valid one.

<!-- S27 -->
And that's why setting itself
can take several minutes,
and on a bad day, much longer.

<!-- S28 -->
Which leaves a strange problem.

<!-- S29 -->
The clock spends a whole minute
collecting the time for ten forty-eight.
But while it's collecting that message,
it's still ten forty-seven.

<!-- S30 -->
So when does it actually change?

<!-- S31 -->
Because the message is an announcement.
It says what the time will be
when the next minute begins.

<!-- S32 -->
The clock reads the whole sentence,
waits out the missing dip,
and when the next dip arrives,
that dip is the exact moment.

<!-- S33 -->
The bits tell the clock what time it is.
The dip tells it when.

<!-- S34 -->
But the sentence has a few more words
than just the time.

<!-- S35 -->
Two bits say whether Germany
is on winter time or summer time.

<!-- S36 -->
And a third one is a warning.
For a whole hour before the clocks change,
it's switched to one.

<!-- S37 -->
So your clock doesn't need to know
which Sunday in March
the clocks go forward,
or which Sunday in October they go back.
Nobody ever taught it the rule.
It's simply told, an hour in advance.

<!-- S38 -->
If Europe ever stops changing the clocks,
the warning will simply never come again.

<!-- S39 -->
Another bit used to warn of a leap second,
an extra second added now and then,
because the Earth's rotation
doesn't keep perfect time.
That minute could have sixty-one seconds.

<!-- S40 -->
The last one was added
at the end of 2016.
But in October 2026,
the world's metrology authorities
decided to end leap seconds.
From 20 May 2027,
UTC will run continuously.

<!-- S41 -->
And the first fourteen bits
of every minute
aren't about time at all.

<!-- S42 -->
Since 2006, they've also been used
to carry encrypted weather forecasts,
for compatible weather stations.

<!-- S43 -->
So the signal that sets your alarm clock
could also tell
someone else's weather station
whether it would rain on Thursday.

<!-- S44 -->
And yet most of these clocks
don't listen all the time.
Listening costs battery,
so many of them try once a night,
in the early hours.

<!-- S45 -->
Long waves reach a clock in two ways:
along the ground,
and bounced off the upper atmosphere.
After dark, that upper path changes,
and the signal often carries further.

<!-- S46 -->
And at three in the morning,
fewer machines, chargers and lights
are usually running nearby to drown it out.

<!-- S47 -->
Between those check-ins,
the clock runs on a quartz crystal,
which can drift by a second or so a day.

<!-- S48 -->
At the next successful check-in,
the radio corrects that drift.

<!-- S49 -->
Even where it listens matters.
The antenna is a small rod of ferrite,
wrapped in wire.

<!-- S50 -->
It hears best when the rod lies across
the direction of the transmitter,
not pointing at it.
Turn the clock around,
and a weak signal can vanish completely.

<!-- S51 -->
Which is why one clock works on a shelf,
and the same clock, two metres away,
behind a reinforced concrete wall, never sets itself.

<!-- S52 -->
So where does the transmitter
get its time from?

<!-- S53 -->
From PTB,
Germany's national metrology institute,
which runs atomic clocks.

<!-- S54 -->
The second itself is defined
by caesium atoms.
One second is exactly
9,192,631,770 oscillations
of the radiation they give off.

<!-- S55 -->
So a cheap alarm clock on a bedside table
is, quite literally,
following a time standard
defined by caesium atoms.

<!-- S56 -->
Not perfectly, though.
The signal travels at the speed of light,
and even that takes about three milliseconds
for every thousand kilometres.

<!-- S57 -->
The receiver adds a delay of its own,
and your clock corrects for none of it.
It doesn't need to.
It only shows seconds.

<!-- S58 -->
From one site near Frankfurt,
the signal reaches clocks
up to about two thousand kilometres away.
That's most of Europe.

<!-- S59 -->
Switzerland had its own transmitter,
called HBG, until the end of 2011.
Its antennas needed replacing,
too few people used it,
and Swiss clocks could simply listen
to Germany instead.

<!-- S60 -->
Others kept theirs.
Britain, France, Japan and China
all run their own.

<!-- S61 -->
And in North America, WWVB
has broadcast from Fort Collins since 1963,
with a time code since 1965.

<!-- S62 -->
Same principle, different dialect.
A zero is a dip of two tenths of a second.
A one lasts half a second.

<!-- S63 -->
And instead of one gap per minute,
a longer marker comes every ten seconds,
like commas in the sentence.
Two in a row mean a new minute.

<!-- S64 -->
The biggest difference
is which time it sends.
Germany broadcasts Central European civil time,
shared by much of the continent.

<!-- S65 -->
But the United States
spans several time zones.
So WWVB sends universal time, UTC,
and you tell the clock where you are.

<!-- S66 -->
It doesn't even send the month.
Just the day of the year,
from one to three hundred and sixty-six.

<!-- S67 -->
None of these stations
speak the same language.
A clock built for Germany
can't make sense of Colorado.

<!-- S68 -->
But on both sides of the Atlantic,
it's the same quiet routine.
Night after night, a small receiver
lines itself up with an atomic time standard,
hundreds or thousands of kilometres away.

<!-- S69 -->
So here's a question for you.
If every radio time signal
disappeared tonight,
would you even notice?
Let me know in the comments.
