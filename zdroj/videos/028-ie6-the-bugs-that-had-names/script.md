# Internet Explorer 6 — The Bugs That Had Names

Scenes are separated by `<!-- Sxx -->`.
The text below each marker is exactly what is sent to TTS.

<!-- S01 -->
This is part two.

If you haven't seen part one,
it's linked below.

Here's the short version anyway.

<!-- S02 -->
In two thousand and one
Microsoft released
Internet Explorer six,
and it arrived with Windows XP.

Within a couple of years
it had more than ninety percent
of the browser market.

<!-- S03 -->
Microsoft used that
to turn the browser
into an application platform.

It was a real idea.

Web developers just happened
to pay for it.

<!-- S04 -->
That was part one.

But I left something out.

I left out the part
where the bugs had names.

<!-- S05 -->
Normally a browser bug
is a number in a tracker.

Issue four one seven two.

Nobody remembers it.

Nobody talks about it at lunch.

<!-- S06 -->
In Internet Explorer six
the bugs had proper nouns.

And that turns out to be
the most telling thing
about the whole era.

<!-- S07 -->
Start with a gentle one.

You float an image to the left
and put a paragraph beside it.

The text should sit
right next to the image.

Instead it sits
three pixels away.

<!-- S08 -->
Not four.

<!-- S08b -->
Not two.

<!-- S08c -->
Three.

<!-- S08d -->
Every time.

It had a name.

The Three Pixel Jog.

<!-- S09 -->
Now float that image left
and give it a left margin
of ten pixels.

Internet Explorer six
gives it twenty.

It doubles the margin,
but only on the side
you floated it to.

<!-- S10 -->
The Double Margin Bug.

And the accepted fix
was to declare
a floated element inline.

<!-- S11 -->
Which is nonsense.

A float is a block.

Calling it inline
means nothing at all.

It worked, so people wrote it.

<!-- S12 -->
This next one is better.

You load a page,
and part of the content
simply isn't there.

You scroll down.

You scroll back up.

And it appears.

<!-- S13 -->
Nothing loaded.

Nothing changed.

It was just shy.

And it had the right name.

The Peekaboo Bug.

<!-- S14 -->
The remedy was to tell
the missing element
that its position was relative.

Nobody could fully explain why
that brought it back.

<!-- S15 -->
Then there is the one
where you hover over a link,
and the background
of the box below it
gets cut off in a straight line.

The Guillotine Bug.

<!-- S16 -->
There was a bug where text
crept away from where you put it.

Magic Creeping Text.

There was one where borders
came out in the wrong place,
in the wrong colour,
or not at all.

Border Chaos.

<!-- S17 -->
My favourite is quieter.

You lay out a row of boxes,
and letters from the last one
turn up again underneath it.

Not always.

Not predictably.

The Duplicate Character Bug.

<!-- S18 -->
And what decided whether
it happened to you,
and how many letters
came out doubled,
was the number of HTML comments
you had left in the markup.

Comments.

The one thing in the file
the browser is supposed
to throw away.

<!-- S19 -->
There is one more,
and it's different,
because people used it
on purpose.

If you set a height
and the content is taller,
the box should overflow.

Internet Explorer six
grew the box instead.

<!-- S20 -->
Which is wrong.

It is also exactly
what a minimum height does.

And Internet Explorer six
had no minimum height.

So developers stopped
reporting that one
and started depending on it.

<!-- S21 -->
Stop and look at that list.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

You don't name a bug
you meet once.

<!-- S22 -->
These had names
because everyone met them.

And here is the part
that makes it worse.

Most of them had
the same cause underneath.

<!-- S23 -->
Inside Internet Explorer six,
every element either did
or did not have
something called layout.

<!-- S24 -->
It decided whether the element
sized and positioned itself,
or left that to its parent.

And you could not set it.

<!-- S25 -->
There was no property
called layout,
and no way to ask for it.

It wasn't in any specification.

It was an internal flag
in the rendering engine.

<!-- S26 -->
But you could flip it
by accident.

Setting a width did it.

Setting a height did it.

Floating an element did it.

So half the fixes in this video
were people flipping a switch
they couldn't see.

<!-- S27 -->
Which is why they went looking
for the cheapest way
to flip it on purpose.

One was to set a height
of one percent.

<!-- S28 -->
Every other browser
had to be kept away from that,
so it went inside a hack
we'll get to in a minute.

<!-- S29 -->
And in Internet Explorer six
it did no harm,
because a height it can't fit
is one it grows past anyway.

The bug from two minutes ago
is what made the fix safe.

<!-- S30 -->
It had a name.

The Holly Hack.

<!-- S31 -->
The other way
was a Microsoft property
called zoom, set to one.

Zoom of one means
do not zoom.

<!-- S32 -->
It changed nothing you could see.

That was the point.

It sat in stylesheets
purely to set
an invisible flag
that made the bugs go away.

<!-- S33 -->
Which brings us to the hacks,
and the hacks are where
this gets strange.

To fix one browser
you first have to talk
to only that browser.

<!-- S34 -->
And Internet Explorer six
behaved as though there was
another element
above the html element.

No other browser did.

It wasn't documented.

It was simply how it acted.

<!-- S35 -->
So you wrote a rule
that matched the phantom,
and only that browser
could see it.

Star, space, html.

<!-- S36 -->
Every other browser looked at it,
found nothing that matched,
and moved on.

That is the star hack,
and for years it sat
in almost every stylesheet
on the web.

<!-- S37 -->
There was also
the underscore hack.

You put an underscore
in front of a property name.

<!-- S38 -->
A standards compliant browser
throws the line away
as invalid.

Internet Explorer six
ignores the underscore
and applies it.

<!-- S39 -->
So you deliberately broke
your own stylesheet,
and the breakage
was the instruction.

<!-- S40 -->
And then there is the one
Microsoft built on purpose.

You could write a comment
that only Internet Explorer obeyed.

<!-- S41 -->
To every other browser
it was an ordinary comment,
ignored the way comments are.

To Internet Explorer six
it was a door
into a second version
of the page.

<!-- S42 -->
Which means the vendor
looked at the situation,
agreed that this browser
needed a stylesheet of its own,
and shipped a feature
to make that easier.

<!-- S43 -->
Some of the damage
didn't need a bug at all.

Internet Explorer six
had two modes.

In the modern one
it followed the standard.

<!-- S44 -->
In the old one,
the width of a box
included its padding
and its border,
which is a completely
different number.

<!-- S45 -->
Which mode you got
depended on the first line
of the document.

And the version of HTML
that everyone was moving to
told you to put
an XML declaration up there.

<!-- S46 -->
That line pushed
Internet Explorer six
into the old mode.

Following the newer standard
was what broke it.

<!-- S47 -->
Then there is transparency.

Internet Explorer six couldn't
show a PNG with soft edges.

Where the image should fade,
it put grey.

<!-- S48 -->
Microsoft's answer was a filter
with a name like a serial number.

It worked.

<!-- S49 -->
But it painted outside
the browser's normal
rendering process,
so links you put on top of it
would often stop working.

You fixed the picture
and broke the link.

<!-- S50 -->
And fading anything else
was a second filter,
with its own syntax,
sitting in the stylesheet
right next to the ordinary property
that every other browser understood.

<!-- S51 -->
Some of this predates
the bugs entirely.

Before any of it,
layouts were built
out of nested tables.

<!-- S52 -->
And to hold a gap open
you used a transparent image
one pixel across,
stretched to whatever size
the gap needed to be.

It had a name too.

The spacer gif.

<!-- S53 -->
Hovering was another one.

In Internet Explorer six,
hover worked on links.

Only on links.

<!-- S54 -->
So a menu that opened
when you moved the mouse
over anything else
needed a small program
attached to the stylesheet.

<!-- S55 -->
Not a script in the page.

A separate file,
referenced from CSS,
holding code whose job
was to teach the browser
one selector.

People passed that file around
for years.

<!-- S56 -->
Part one mentioned
that you could put JavaScript
inside a stylesheet.

What it didn't mention
is how often that JavaScript ran.

<!-- S57 -->
Every mouse move.

Every keystroke.

Every scroll.

Over and over again,
to work out one width.

<!-- S58 -->
And the browser had ceilings
that nobody else had.

A stylesheet stopped applying
somewhere past
four thousand rules.

Anything after
the thirty first stylesheet
on a page was ignored.

<!-- S59 -->
Which sounds like a number
you would never reach,
until your site is large enough
that somebody has to write
a build step whose only job
is to merge stylesheets together
before the browser sees them.

<!-- S60 -->
And some of it wasn't
cosmetic at all.

Internet Explorer six
counted its page objects
and its script objects
in two different ways,
and neither side
could see the whole loop.

<!-- S61 -->
So if a script pointed
at part of the page,
and that part of the page
pointed back at the script,
neither was ever released.

Leave that window open long enough
and the browser ate the machine.

<!-- S62 -->
But the best one
isn't a layout bug at all.

You write an input tag.

You give it a type.

And you forget the equals sign.
<!-- S63 -->
That is a malformed attribute.

Every parser ever written
has an answer for that.

Ignore it.

Guess at it.

Carry on.
<!-- S64 -->
Internet Explorer crashed.

Inside, it wanted to know
whether the field was hidden,
so it compared what you had typed
against the word hidden.

You hadn't typed anything.
<!-- S65 -->
So it went to fetch
the thing you hadn't typed
from address zero.

Which would be
an ordinary browser crash,
except that the code doing it
was not in the browser.
<!-- S66 -->
It was in a shared system library.

So those three words
also took down the mail client,
and the preview pane
in the file manager.
<!-- S67 -->
A window listing files
on your own machine,
closed by a web page.

That is part one's argument
arriving as a crash report.

The browser wasn't a program
running on the system.

It was part of the system.
<!-- S68 -->
And you couldn't simply
test the fix somewhere else.

Internet Explorer was welded
to the operating system,
so one computer
ran exactly one version.

<!-- S69 -->
Which is why a front end job
in two thousand and six
came with a shelf
of spare machines.

<!-- S70 -->
And later with a folder
of virtual ones,
each carrying a whole
operating system
so that one page
could be opened inside it.

<!-- S71 -->
And then somebody did
the obvious thing.

If you can teach the browser
one missing feature,
you can teach it all of them.

<!-- S72 -->
A developer called Dean Edwards
wrote a library
whose entire purpose
was to make Internet Explorer six
behave like a later version
of itself.

People shipped that.

In production.

<!-- S73 -->
Which is where it stops
being funny.

For most of a decade,
a serious share of the world's
front end work went into
one browser's mistakes.

Not features.

Not products.

Compensation.

<!-- S74 -->
And it lasted because
of the thing part one was about.

Companies had built
real applications on it,
the kind that only ran there,
and those applications
still had to work on Monday.

<!-- S75 -->
So the browser that everybody
wanted gone
was the one nobody
was allowed to remove.

<!-- S76 -->
In two thousand and ten,
Google announced that its own
apps would stop working in it.

And a design studio in Denver
decided that deserved a funeral.

<!-- S77 -->
An actual one.

A coffin.

A eulogy.

Between eighty and a hundred people
came to watch a browser
get buried.

They had planned for thirty.

<!-- S78 -->
And Microsoft sent flowers.

The card said,
thanks for the good times,
Internet Explorer six.

<!-- S79 -->
One year later, to the day,
Microsoft launched a website.

It tracked how much of the world
was still running
Internet Explorer six,
country by country.

<!-- S80 -->
At that point
it was still twelve percent.

The goal was to push it
under one.

The company that built the browser
was running a public countdown
to its own product's death.

<!-- S81 -->
So why did the bugs have names?

Because you name the things
you cannot get around.

<!-- S82 -->
Nobody names the weather
in a country
they are passing through.

You name it where you live.

And for about ten years,
that was where the web lived.

<!-- S83 -->
But getting Internet Explorer six
off the web was another story.

And that is where we go next.

If you want that one,
there is a subscribe button,
and part one is linked below.
