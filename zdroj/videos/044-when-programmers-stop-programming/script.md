# When Programmers Stop Programming

<!-- S01 -->
Imagine you are a programmer.

Maybe you have been one for twenty years.

You know what a race condition is.

You know why NULL is evil.

<!-- S02 -->
And you have spent part of your life
arguing about whether the opening brace
belongs on the same line as the if...

or on its own line underneath.

<!-- S03 -->
Then one day you come to work.

You open your editor.

And you realise there is nothing
in there left for you to write.

<!-- S04 -->
Because the machine can do it.

You tell it: build me an API
for user management.

It writes it.

<!-- S04b -->
Add authentication.

It writes it.

Add tests.

It writes them.

Fix this bug.

It fixes it.

<!-- S05 -->
And you review the result.

<!-- S06 -->
Congratulations.

You have become a manager.

Just without the manager's salary.

<!-- S06b -->
And suddenly you are leading
a team of programmers.

Not one of them is human.

<!-- S07 -->
But look at what we actually did.

We spent decades teaching programmers
to write code that other programmers
could read.

<!-- S08 -->
And now we are building machines
that write code
programmers may never read.

<!-- S09 -->
So the question is not
whether you still have a job.

The question is what all of that
readability was for.

<!-- S10 -->
Start with the thing programmers say
whenever this comes up.

Programming has always been automated.

<!-- S11 -->
And that part is true.

The first programmers worked
directly in machine instructions.

Then came assembly.

Then languages you could almost read.

Every time, a piece of the work
moved from the person to the tool.

<!-- S12 -->
On the 10th of November, 1954,
a group at IBM published a report
about a system they were building.

They called it FORTRAN.

<!-- S13 -->
Page two says this.

"Since FORTRAN should virtually
eliminate coding and debugging..."

And the sentence goes on to promise
the work will cost less than half
of what it cost before.

<!-- S14 -->
FORTRAN arrived
two and a half years later.

Coding was not eliminated.

The programmers wrote FORTRAN.

<!-- S15 -->
In 1959, a committee sat down
to design a language for business.

They agreed on two things.

That more people should be able
to program at all...

and that the language should use
as much plain English as possible.

<!-- S16 -->
That was a design goal,
not a side effect.

COBOL was shaped around
what a human could read.

Hold on to that one.

<!-- S17 -->
Then, in 1982, a man called James Martin
published a book.

It is worth hearing the title in full.

"Application Development
Without Programmers."

<!-- S18 -->
It was not about robots.

It was about report generators
and application generators.

And the promise was exactly the one
you have been hearing this year.

<!-- S19 -->
So here is the obvious question.

After all of that, how many
programmers were left?

<!-- S20 -->
More of them. Every time.

In 1980, the United States had
more than three hundred thousand
computer programming jobs.

By the early 2000s,
more than seven hundred thousand.

<!-- S21 -->
But watch what happened
to the word programmer.

In 2003, the American labour survey
added a new job title,
right next to the old one.

<!-- S22 -->
Computer programmer.

And software engineer.

Today that second one
is called software developer.

<!-- S22b -->
Right now, about three hundred
and eighty thousand Americans
are computer programmers.

And about two and a quarter million
are software developers.

<!-- S23 -->
That is six developers
for every one programmer.

Almost nobody doing this work
is still called a programmer.

<!-- S23b -->
The job did not disappear.

It got renamed.

<!-- S24 -->
And that is the shape of the thing
that is happening now,
except faster.

<!-- S25 -->
Because every earlier step
had one thing in common.

You were still programming.
Just further from the metal.

Assembly to C: still a program.

C to Python: still a program.

<!-- S26 -->
Not this time.

You describe what you want
in ordinary sentences.

I need a system where users
can change their email address.

The new address must be verified.

Until then, the old one stays active.

<!-- S27 -->
And out comes the database change,
the backend, the API, the front end,
the tests, the documentation.

And you have not written a line.

<!-- S28 -->
That is not a higher-level language.

It is a different kind of thing entirely.

<!-- S29 -->
And at that point it stops being
a philosophical question
and becomes an arithmetic one.

<!-- S30 -->
If one programmer with these tools
does the work that used to take five,
a company will use that.

The company does not have to be evil.

It does not even have to want
to let anyone go.

It just needs a competitor
who is faster and cheaper.

<!-- S31 -->
So the centre of gravity moves.

From writing to instructing.

From implementation to review.

From programming to architecture.

From writing the code
to managing the thing that writes it.

<!-- S32 -->
Which is strange, because that path
already existed.

Team leader. Architect.
Engineering manager.

<!-- S33 -->
Some programmers wanted it.

Plenty of them did not.

They did not want meetings
or budgets or deciding
who takes leave next week.

<!-- S34 -->
They wanted to sit down,
look at something,
and think: how on earth
am I going to make this work?

<!-- S35 -->
And now the work is moving them
in exactly the opposite direction.

Not because they got older.

Because the craft got automated.

<!-- S36 -->
There is a quieter cost, too.

When you solve it yourself,
you have to think about it.

You try something. You get it wrong.
You take it apart.

<!-- S37 -->
And a year later you remember.

Oh. I have had this before.

<!-- S38 -->
When the machine solves it,
the job takes ten minutes.

And a week later you open
your own project and think:
why did I do it this way?

<!-- S39 -->
And the honest answer is:
I don't know. AI wrote it.

<!-- S40 -->
Which is a very odd place to end up.

More productive programmers,
slowly becoming less able to program.

<!-- S40b -->
If you'd like to see where the next question takes us,
consider subscribing.
It really helps the channel.

<!-- S41 -->
And then there are the things
that used to matter enormously.

Coding style.

<!-- S42 -->
We had entire arguments
about where to put a curly brace.

Tabs or spaces.

Two spaces or four.

CamelCase or snake_case.

<!-- S43 -->
Arguments that outlasted
the code they were about.

<!-- S44 -->
But if a machine writes
thousands of lines,
and people barely read them,
and nobody will maintain them by hand...

how much does the brace matter?

<!-- S45 -->
Coding style becomes
an implementation detail.

Something that matters to the machine...

and less and less to the human.

<!-- S46 -->
Now think about spaceships
in science fiction.

<!-- S47 -->
The ship has a computer
that runs everything.

Engines. Sensors. Life support.

<!-- S48 -->
And there is a medical bay,
an engineering deck, a bridge.

<!-- S49 -->
What it does not have is a room
with a sign on the door saying:

software engineering.

<!-- S50 -->
Nobody on the bridge is arguing
about library versions.

Nobody says life support is down
because of a null pointer.

<!-- S51 -->
The captain says: analyse the anomaly.

And it gets analysed.

<!-- S52 -->
For decades that looked like the part
the writers had not thought about.

It may turn out to be
the part they got right.

<!-- S53 -->
Because the problem does not go away.

Somebody still has to know
what the system should do.

<!-- S54 -->
What it must never do.

What the security requirements are.

What data it is allowed to touch.

What happens when it fails.

<!-- S55 -->
And above all, somebody has to answer
the question underneath all of those.

How do we know it built
the right thing?

<!-- S56 -->
That may turn out to be harder
than writing the code was.

<!-- S57 -->
And it leads somewhere odd.

Why would a machine write Python?

<!-- S58 -->
Python, C sharp, PHP —
every one of them was designed
so that a person could read
and write it.

<!-- S59 -->
A machine does not need that.

What it needs is a precise description
of the thing it has to build.

What must always be true.

What must never happen.

<!-- S60 -->
And if that is what we end up writing,
then the thing we keep is not the diff.

<!-- S61 -->
Not 37 changed files.

Not 4,821 lines added
and 1,734 removed.

<!-- S62 -->
The thing we keep is the specification.

The test scenarios.

The security rules.

The data model.

<!-- S63 -->
And the code becomes
a means of production.

Nobody asks how the factory
made the screw.

They ask whether the screw
meets the spec.

<!-- S63b -->
Which makes the specification
the source code.

And the code underneath it
becomes what assembly is today.

Something that still runs,
and that almost nobody reads.

<!-- S64 -->
So perhaps the sentence everybody says
is the wrong sentence.

Not: this will replace programmers.

<!-- S65 -->
Closer to it would be:
this will replace programming
as the main thing programmers do.

<!-- S66 -->
The programmers may not go anywhere.

The programming may go
out of their jobs.

<!-- S67 -->
Which brings us back
to the question from the start.

What was the readability for?

<!-- S68 -->
All those English-like keywords.
All those arguments about braces.

The machine never needed any of it.

<!-- S69 -->
It was for us.

So that a person could pick up
something somebody else had made,
and understand it.

<!-- S70 -->
Maybe you are a programmer.

Maybe you were one, once.

<!-- S71 -->
And maybe, in a while, someone young
will find one of these old repositories
and ask:

wait. You wrote these yourselves?

<!-- S72 -->
Yes.

<!-- S72b -->
Did you write
the boring parts too?

<!-- S72c -->
Yes, everything.

<!-- S72d -->
Why?

<!-- S73 -->
And the honest answer is:
because we enjoyed it.
