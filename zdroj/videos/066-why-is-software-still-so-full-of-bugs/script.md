<!-- S01 -->
Every few days, another serious bug
makes the news.
A bug that lets someone skip the login.
A bug that leaks private data.
A bug that hands an attacker your computer.

<!-- S02 -->
Sometimes it's Windows. Sometimes Linux.
A browser, a database, a cloud service...
or a small library
that millions of developers depend on.

<!-- S03 -->
And the reaction is almost always the same.
How did the programmers miss this?

<!-- S04 -->
These are professionals.
They have code reviews, automated tests,
security audits, fuzzing...
and the bugs keep coming anyway.

<!-- S05 -->
So is it even possible
to write complex software without bugs?

<!-- S06 -->
Let's start with a number.
Imagine a program with just a hundred settings,
each of them either on or off.

<!-- S07 -->
A hundred simple yes-or-no decisions.
How many combinations is that?

<!-- S08 -->
Two to the power of a hundred.
That's roughly a million trillion trillion.

<!-- S09 -->
Now imagine you could test
a billion combinations every second.
And you started at the Big Bang.

<!-- S10 -->
By today, you'd have tested
about one combination in three thousand.

<!-- S11 -->
And a hundred switches is nothing.
A real program has millions of them.
So "just test everything"
isn't expensive. It's impossible.

<!-- S12 -->
And those switches aren't exotic.
Take one of the simplest things
a program ever does.
A user asks for their account by its number.
We find it in the database.
We send it back.

<!-- S13 -->
But what if the user doesn't exist?
What if someone sends text instead of a number?
Or a negative number? Or an enormous one?

<!-- S14 -->
What if this person isn't allowed to see it?
What if someone deletes the account
at the exact moment we're loading it?
What if the same request arrives twice?

<!-- S15 -->
Every one of these questions is simple.
The problem is how they combine.
Each one is another switch.

<!-- S15b -->
By the way, if you like videos
like this, consider subscribing.

It really helps the channel.

<!-- S16 -->
And a computer won't sort them out for us.
It does exactly what we tell it to.
Not what we meant.

<!-- S17 -->
That's why we invented programming languages.
They let us describe complex things
without thinking about every detail.

<!-- S18 -->
But some of them take care of less
than you'd hope.
Take C. It's fast, it's simple,
and it gives you enormous control over memory.

<!-- S19 -->
So you can write this.
We reserve room for sixteen characters.
Then we say: copy the input here.

<!-- S20 -->
What if the input is
five hundred characters long?
C won't ask.
It just keeps writing past the end.

<!-- S21 -->
And what's right after those sixteen characters?
Often, something very important.

<!-- S22 -->
When a program calls a function,
it writes down where to go back
once the function is done.
A return address.
In a classic layout, it sits
not far past the end of our buffer.

<!-- S23 -->
So an attacker sends an input
of exactly the right length.
First, their own instructions.
Then, at the very end, a new return address...
pointing back at those instructions.

<!-- S24 -->
The function finishes.
The processor looks up where to return...
and jumps straight into the attacker's code.

<!-- S25 -->
Now it's running their program,
with all the permissions of yours.
That's what "executing arbitrary code" means.

<!-- S26 -->
And the processor didn't do anything wrong.
It followed the instructions.

<!-- S27 -->
In 1988, a mistake exactly like this
let the Morris worm spread
across the early internet.
And the same trick has been used
in attacks ever since.

<!-- S28 -->
So newer languages hand part of the job
to the compiler.
Rust, for example, refuses to build
many programs that could misuse memory.

<!-- S29 -->
The programmer says:
but I know exactly what I'm doing!
And the compiler says:
that's what everyone says.

<!-- S30 -->
And it's right to be suspicious.
Microsoft and Google's Chrome team
have both reported
that around seventy percent
of the security bugs they've studied
come from memory safety problems.

<!-- S31 -->
But a program can be perfectly memory-safe
and still completely wrong.

<!-- S32 -->
Imagine a user logs in.
Their password is checked correctly.
Nothing crashes. No memory is corrupted.

<!-- S33 -->
And then the program shows them
somebody else's data.
Because the permission check
was written slightly wrong.

<!-- S34 -->
No language can catch that on its own.
The language doesn't know
what the program was supposed to do.
Only we know that.

<!-- S35 -->
So back to testing.
A test can tell you:
for this input, I got this result.

<!-- S36 -->
It can't tell you:
the program is right for every input.
And we've already seen
why we can't try them all.

<!-- S37 -->
In 1970, the computer scientist
Edsger Dijkstra put it in one sentence.
Testing can show the presence of bugs,
but never their absence.

<!-- S38 -->
Fine. So instead of testing,
why not write a program
that checks other programs
and proves they're correct?
Feed it any code, and it tells you
whether that code does what it should.

<!-- S39 -->
That question was answered
before the first real computer was even built.
In 1936, Alan Turing proved
that a program like that cannot exist.

<!-- S40 -->
Not that nobody has built it yet.
That it can't exist at all.

<!-- S41 -->
He showed that no program can decide,
for every other program,
whether it will ever stop running.

<!-- S42 -->
And in 1953, Henry Rice went further.
The same is true for every non-trivial question
about what a program actually does.

<!-- S43 -->
Is it secure? Does it leak data?
Does it give the right answer?
There is no general method
that settles that for every program.

<!-- S44 -->
So is bug-free software impossible?
Not quite.
For one specific program,
you can sometimes prove it correct,
with enormous effort.

<!-- S45 -->
In 2009, a team in Australia proved
that a small operating system kernel,
called seL4,
does exactly what its specification says.

<!-- S46 -->
It was under ten thousand lines of code.
Building the kernel took
about two person-years.
Proving it correct took about twenty.
A modern web browser
has tens of millions of lines.

<!-- S47 -->
And even that proof has a catch.
It shows the program matches its specification.
It can't show that the specification
is what we actually wanted.

<!-- S48 -->
And the specification is written by people.
So the question comes back to us.

<!-- S49 -->
And it isn't only our own code.
A programmer today builds on frameworks,
libraries and hundreds of dependencies.
Every layer saves us enormous amounts of work.
But every layer is something
we have to understand...
or at least trust.

<!-- S50 -->
Which means you don't have to write a bug
to have one in your software.
You can simply install it.

<!-- S51 -->
Then add the pressure.
Nobody wants a perfect product in ten years.
They want a working one next month.
And a break-in that never happened
is very hard to show in a presentation.

<!-- S52 -->
And here's the strangest part.
Our tools keep getting better.
Safer languages, fuzzing, bug bounties...

<!-- S53 -->
And yet the number of known vulnerabilities
keeps growing.
In 2024 alone, around forty thousand
got an official number.

<!-- S54 -->
Partly because we're also writing
vastly more software than ever.
It's like making every road safer...
while building millions of times more roads.

<!-- S55 -->
So are programmers bad at their jobs?
No.
We've been asking them for something
that no general method can guarantee.

<!-- S56 -->
So maybe
"how do we write software without bugs?"
is the wrong question.

<!-- S57 -->
The better question is:
how do we build systems that stay safe
even when the software has bugs?

<!-- S58 -->
And that's exactly where security is heading.
It doesn't say: never make a mistake.
It says: assume you already have.

<!-- S59 -->
Remember that return address?
Today, the system guards it.
It shuffles where things sit in memory.
And it refuses to run instructions
hidden in data.

<!-- S60 -->
The bug in our C code is still there.
It's just much harder to turn into an attack.

<!-- S61 -->
And the same idea is everywhere.
Sandboxes, limited permissions,
isolated processes, encryption,
backups, monitoring...
layer after layer,
so that one bug doesn't become a disaster.

<!-- S62 -->
And it has a very practical consequence.
If bugs are inevitable,
fixing them isn't optional.

<!-- S63 -->
The software you're using today
may well contain a vulnerability
nobody has found yet.

<!-- S64 -->
And when someone does,
the update is the difference between
"a vulnerability was discovered"
and "we were hacked".

<!-- S65 -->
The same goes for the systems we build.
Old libraries and unsupported platforms
don't get safer by being ignored.
They turn into technical debt.

<!-- S66 -->
And why that debt has to be paid off
is what my video
"It Still Works. So Why Upgrade It?"
is about.

<!-- S67 -->
Because in software,
"it still works"
and "it's still safe"
are two very different things.
