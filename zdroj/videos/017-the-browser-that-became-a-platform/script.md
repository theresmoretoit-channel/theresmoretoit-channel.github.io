# Internet Explorer 6 — The Browser That Became a Platform

Scenes are separated by `<!-- Sxx -->`.
The text below each marker is exactly what is sent to TTS.

<!-- S01 -->
Imagine being a web developer
in the early two thousands.

You have written
a perfectly reasonable web page.

<!-- S02 -->
It works in Netscape.

It works in Opera.

It works in the new Firefox.

And then you open it
in Internet Explorer.

Everything is broken.

<!-- S03 -->
The layout is wrong.

The buttons have moved.

The PNG images look terrible.

And somehow,
adding one line break to your HTML
has created a three pixel gap.

<!-- S04 -->
Welcome to web development
in the age of Internet Explorer six.

But here's the interesting part.

Internet Explorer six
wasn't simply a terrible browser.

<!-- S05 -->
Microsoft was trying to solve problems
that the web genuinely had.

They just had one enormous advantage
over everyone else.

Windows.

<!-- S06 -->
And eventually, that advantage
allowed Microsoft to turn the browser
into something much bigger
than a browser.

<!-- S07 -->
In the mid nineteen nineties,
the web was dominated
by Netscape Navigator.

Microsoft wasn't happy about that.

<!-- S08 -->
So Internet Explorer
was bundled with Windows
and made available for free.

You bought a Windows computer.

Internet Explorer was already there.

Nothing to download.

Nothing to pay for.

<!-- S09 -->
And most importantly,
Microsoft controlled
the operating system.

By the early two thousands,
Internet Explorer had
more than ninety percent
of the browser market.

<!-- S10 -->
Internet Explorer six arrived
in two thousand and one,
together with Windows XP.

And for a while, it looked like
Microsoft had simply won
the browser wars.

<!-- S11 -->
Microsoft had a problem.

The web was extremely limited.

HTML could display documents.

CSS could style them.

JavaScript could make them interactive.

<!-- S12 -->
But that was about it.

Anything more complicated
ran straight into
the limits of the browser.

<!-- S13 -->
What if you wanted to scan a document?

Or communicate with a smart card?

Or talk to some piece
of Windows hardware?

<!-- S14 -->
The browser couldn't really
do those things.

So Microsoft came up with a solution.

ActiveX.

<!-- S15 -->
The basic idea was simple.

Why restrict a web application
to what the browser can do?

Just let it use
native Windows components.

<!-- S16 -->
And suddenly a web page
could do things
that ordinary HTML
couldn't even dream of.

<!-- S17 -->
Today, ActiveX sounds terrifying.

And for good reason.

An ActiveX component could reach
the files, the applications,
the hardware
and the operating system.

<!-- S18 -->
From today's security perspective,
that sounds absolutely insane.

But in the early two thousands,
it made perfect sense
for corporate applications.

<!-- S19 -->
Companies didn't want
a pretty document viewer.

They wanted applications.

They wanted web pages
that could behave
almost like desktop software.

<!-- S20 -->
And Microsoft gave them exactly that.

Even Windows Update itself
originally relied on ActiveX
to inspect the system
and work out which updates
were required.

<!-- S21 -->
So ActiveX wasn't simply
a stupid mistake.

It was an early attempt
to turn the browser
into an application platform.

<!-- S22 -->
And in that sense, Microsoft
was actually ahead of its time.

The problem was how much power
they gave that platform.

<!-- S23 -->
ActiveX wasn't
the only Microsoft extension.

There was VBScript.

There was DHTML.

There was even CSS expression.

Yes.

<!-- S24 -->
Internet Explorer could evaluate
JavaScript directly inside CSS.

You could do something like this.

<!-- S25 -->
It was ridiculous.

It was also sometimes
surprisingly useful.

And none of it was guaranteed
to work anywhere else.

<!-- S26 -->
Microsoft wasn't simply
implementing the web.

Microsoft was extending the web
in its own direction.

And with ninety percent
of the market,
it had enough power
to make that work.

<!-- S27 -->
One of the most famous examples
was the CSS box model.

The standard model said
that if an element
was two hundred pixels wide,
with twenty pixels of padding
and a five pixel border,

<!-- S28 -->
then the total width
was two hundred and fifty pixels.

<!-- S29 -->
Older versions of Internet Explorer
read it differently.

In quirks mode, the declared width
could include the padding
and the border.

<!-- S30 -->
This was not necessarily
an insane way to think about width.

In fact, today we often deliberately
use exactly this kind of behaviour.

It is called border box sizing.

<!-- S31 -->
The real problem was
that different browsers
behaved differently.

And that meant
the developer had to care.

A lot.

<!-- S32 -->
There was something called `hasLayout`.

It wasn't a normal CSS property.

It wasn't part of the standard.

But it decided
how Internet Explorer
laid out elements.

<!-- S33 -->
And sometimes a broken layout
could mysteriously be fixed
by adding a single line.

Zoom one.

Why?

Because zoom one could trigger
the internal `hasLayout` mechanism.

<!-- S34 -->
There were problems
with PNG transparency.

There were problems with select elements
appearing above
absolutely positioned popups,
regardless of how high
you set the `z-index`.

<!-- S35 -->
Web development wasn't just about
implementing your design.

It was about learning the bugs
of a particular browser engine.

<!-- S36 -->
Here's another wonderful example.

Whitespace.

And this one wasn't even
Internet Explorer's fault.

You could put two images
right next to each other
in the markup,
with nothing between the tags,
and get one result.

<!-- S37 -->
Then someone would nicely format the HTML
and put each tag on its own line.

And suddenly there was
a few pixel gap between the images.

The newline became significant.

<!-- S38 -->
Your code formatter
could literally break your web page.

And if you were using
an old version of Visual Studio,
it might happily format
your HTML for you.

Thank you, Microsoft.

<!-- S39 -->
Developers accumulated
an entire toolbox of workarounds.

Conditional comments.

<!-- S40 -->
And sometimes completely
bizarre looking HTML
whose only purpose was to make
Internet Explorer behave.

<!-- S41 -->
You didn't write ugly code
because you were a bad programmer.

You wrote ugly code
because the browser forced you to.

<!-- S42 -->
Internet Explorer also crashed
spectacularly, and often took
every open window with it.

<!-- S43 -->
Which led to a wonderful category
of office entertainment.

Hey, check out this link.

And twenty Internet Explorer windows
disappear.

<!-- S44 -->
This was the web
before browsers were sandboxed.

Today's browser says this.

This website is untrusted.

I'll isolate it.

<!-- S45 -->
Internet Explorer six
sometimes felt more like this.

You're a web page?

Sure.

Here's the keys to the building.

<!-- S46 -->
Why did developers
actually use these hacks?

Because they had to.

<!-- S47 -->
Imagine a company
with five hundred employees.

Every computer runs Windows XP.

Every computer has Internet Explorer.

<!-- S48 -->
The developer has two options.

Option one.

Build for Internet Explorer,
which everyone already has.

<!-- S49 -->
Option two.

Build for every browser,
test everything everywhere,
and explain to the IT department
why everyone needs a second one.

The answer was usually obvious.

<!-- S50 -->
They weren't choosing
Microsoft technology
because they loved Microsoft.

They were choosing what solved
the customer's problem.

And sometimes ActiveX
was the best tool available.

<!-- S51 -->
And eventually someone had enough.

JavaScript libraries started
hiding the browser differences.

One of the most important
was jQuery.

<!-- S52 -->
Instead of writing
browser specific event handling,
you could write a single line
that worked everywhere.

<!-- S53 -->
Instead of manually dealing
with different AJAX implementations,
you could use a common abstraction.

<!-- S54 -->
jQuery didn't make
Internet Explorer disappear.

But it made it much easier
to pretend it didn't exist.

And for web developers of that era,
that was a beautiful thing.

<!-- S55 -->
Firefox appeared.

Opera continued developing.

Safari arrived.

And eventually Google released Chrome.

<!-- S56 -->
The browser wars were back,
and this time
the competition was different.

JavaScript engines
became dramatically better.

HTML five arrived.

<!-- S57 -->
The browser itself started learning
all the things developers
had previously needed plugins for.

<!-- S58 -->
Video.

Audio.

Canvas.

SVG.

WebGL.

WebSockets.

And eventually WebRTC.

The web was becoming
an application platform.

<!-- S59 -->
Which was exactly
what Microsoft had been trying
to achieve with ActiveX.

But now it was happening
through open standards.

<!-- S60 -->
Microsoft did try once more.

Silverlight let developers build
rich browser applications
using C sharp and dot NET.

It even powered
Netflix's early streaming.

<!-- S61 -->
But the web didn't want plugins forever.

Apple refused to support Flash
on the iPhone.

And suddenly the future wasn't this.

Browser plus plugin.

It was this.

The browser itself.

<!-- S62 -->
Silverlight disappeared.

Flash disappeared.

ActiveX disappeared.

And Internet Explorer
eventually disappeared too.

<!-- S63 -->
And this is where
the story gets interesting.

Because Microsoft
wasn't completely wrong.

They had correctly predicted
that the browser would become
an application platform.

<!-- S64 -->
They were just trying to get there
through proprietary technologies.

The web reached the same destination
through standards.

<!-- S65 -->
The browser won.

But it won by becoming
something far more powerful
than the browser
of two thousand and one.

<!-- S66 -->
So was Microsoft the villain?

Not really.

And that's what makes
the story more interesting.

<!-- S67 -->
Microsoft had brilliant engineers.

They had enormous resources.

And they built many technologies
that were genuinely ahead of their time.

<!-- S68 -->
But Microsoft also had
an overwhelming market position.

And that created
a dangerous incentive.

<!-- S69 -->
If almost everyone
uses your browser,
why wait for standards?

Why not simply implement
your own solution?

For a while, that worked.

Until the rest of the web caught up.

<!-- S70 -->
Today, Internet Explorer is gone.

The old browser wars
seem like ancient history.

But look at
the modern browser market.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
And many others
are based on Chromium.

Different products.

Often the same
underlying browser engine.

<!-- S72 -->
So perhaps we've traded this.

One browser everyone had to support.

For this.

One engine everyone builds on.

Does that sound familiar?

<!-- S73 -->
Because a dominant browser engine
doesn't just decide
how websites are displayed.

<!-- S74 -->
It influences what developers build.

Which technologies become popular.

And ultimately,
what the web itself becomes.

<!-- S75 -->
There is, however,
one very important difference.

Today's web is built
around open standards.

Firefox still has its own engine.

Safari has WebKit.

Chromium is open source.

<!-- S76 -->
And modern browsers
update automatically.

We are nowhere near
the situation
of two thousand and three.

<!-- S77 -->
But the basic question remains.

How much influence
should one company have
over the platform
used by almost everyone?

That's the question
that never really went away.

<!-- S78 -->
So, was Internet Explorer six terrible?

Yes.

Sometimes spectacularly terrible.

<!-- S79 -->
But that's not the whole story.

It was also a product of its time.

<!-- S80 -->
The problem was
that Microsoft had won
the browser wars so completely
that it could define the rules.

<!-- S81 -->
And web developers paid the price.

They learned the mysteries
of `hasLayout`.

They discovered that zoom one
could magically fix things.

And they prayed.

<!-- S82 -->
And eventually, Internet Explorer
became what it had spent
twenty years creating.

A legacy platform
that nobody wanted
to support anymore.

<!-- S83 -->
The web didn't reject
Microsoft's vision.

It simply built
a better version of it.

And if there's one thing
that era should teach us,
it's this.

<!-- S84 -->
Technology doesn't become a standard
just because it's good.

<!-- S85 -->
Sometimes it becomes a standard
because one company has enough power
to make everyone use it.

<!-- S86 -->
And sometimes,
twenty years later...
we realise we've done it again.
