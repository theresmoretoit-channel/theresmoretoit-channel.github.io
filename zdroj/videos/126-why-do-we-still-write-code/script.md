<!-- S01 -->
Here is a complete requirement
for a piece of business software.
A user can cancel an order.

<!-- S02 -->
Six words.
Any developer would nod.
Any customer would sign it.

<!-- S03 -->
So, can a user cancel an order
after the invoice has gone out?
After it has been shipped?

<!-- S04 -->
Does cancelling it also cancel
the reservation with the supplier?
And what if two people cancel
and approve the same order
in the same second?

<!-- S05 -->
The sentence answers none of that.
The code has to answer all of it.
And that gap, between the sentence
and the code, is what programmers
are actually paid for.
At least they used to be.

<!-- S06 -->
Today there is a tempting idea.
Write only the sentences.
Keep them in documents,
review them, version them.
And let an AI write the code.

<!-- S07 -->
The specification becomes
the source code.
The code becomes what assembly
is today: something that runs,
and that nobody reads.

<!-- S08 -->
It is a good idea.
It is also not a new one.

<!-- S09 -->
For nearly seventy years, people have tried
to raise the level
at which we tell computers what to do.
The tools were different,
and so were their goals.
But each one moved more of the work
from people to machines.

<!-- S10 -->
In 1957, a team at IBM
published a paper about FORTRAN.
Its title called it
an automatic coding system.

<!-- S11 -->
At the time, that was an accurate name.
You wrote formulas,
and the machine instructions,
the part people had written by hand,
were now produced by the machine.

<!-- S12 -->
Today we call FORTRAN code.

<!-- S13 -->
In the 1980s, CASE tools
and fourth-generation languages
went a level higher.
Draw the diagrams, fill in the forms,
and much of the application
is generated for you.

<!-- S14 -->
In 2001, the Object Management Group,
the body behind UML,
announced Model Driven Architecture.

<!-- S15 -->
The pitch will sound familiar.
You describe the system once,
as a model, independent of any technology.
Then tools generate the implementation
for whatever platform you need.

<!-- S16 -->
Same business rules.
Replaceable technology.

<!-- S17 -->
And in 2014, the analysts at Forrester
gave a name to platforms
for building business applications
with as little hand-written code
as possible.
They called it low-code.

<!-- S18 -->
So, did any of it work?

<!-- S19 -->
Partly.
In 2014, researchers at Lancaster University
published a survey
of four hundred and fifty people
who were actually using
model-driven development.

<!-- S20 -->
It did work,
more widely than many people thought.
But rarely for a whole system.
People used it for key parts,
and built the rest in other ways.

<!-- S21 -->
The biggest obstacles they found
were people and organisations,
not tools.
But there is a technical limit too,
and programmers have a joke about it.

<!-- S22 -->
A specification precise enough
to generate the whole program from...
already has a name.
It's called code.

<!-- S23 -->
To generate everything,
the model had to say everything.
Every state, every exception,
every "what if two people do it at once".

<!-- S24 -->
At that point
you haven't escaped programming.
You've just moved it into a diagram,
which is often harder to read,
to compare, and to review.

<!-- S25 -->
Back in the late 1970s,
Edsger Dijkstra put the other half of it
into a short note with a blunt title.
On the foolishness
of natural language programming.

<!-- S26 -->
His point was that formal notation
isn't a burden we put up with.
He called it an amazingly effective tool
for ruling out all sorts of nonsense.

<!-- S27 -->
Plain English doesn't rule it out.
It hides it.
A user can cancel an order.

<!-- S28 -->
So if none of that replaced code,
why try again?

<!-- S29 -->
Because one thing really is different.

<!-- S30 -->
Older generators couldn't fill a gap
on their own.
If the model didn't say what happens
to a shipped order,
someone had to add that rule explicitly.
Until they did, the gap was still there,
and you could find it.

<!-- S31 -->
An AI doesn't stop.
Give it the six-word requirement
and it will answer every question
we asked at the start.

<!-- S32 -->
It will decide that a shipped order
can be cancelled. Or that it can't.
It will decide about the invoice,
and about the supplier.
It will produce code that runs,
looks reasonable,
and passes the tests it wrote itself.

<!-- S33 -->
That is exactly what makes it useful.
And exactly what makes it dangerous.
Because a plausible guess
is not a business decision.

<!-- S34 -->
The gaps used to be errors.

<!-- S35 -->
Now they are decisions
that nobody noticed being made.

<!-- S36 -->
So if the specification really is
going to be the source code,
it can't be a few informal paragraphs.

<!-- S37 -->
Picture the repository.
One document describes orders
and every state they can be in.
Another says who can approve them,
and who can cancel them.

<!-- S38 -->
A third says when an invoice is issued,
and when it has to be reversed.
Another describes the accounting system,
including what happens when it's down.

<!-- S39 -->
Some of it is ordinary prose.
But wherever prose would be ambiguous,
there is something stricter:
a list of states and the moves between them,
a schema, a rule a machine can check.

<!-- S40 -->
And next to it, acceptance tests
that say exactly what must happen.

<!-- S41 -->
All of it lives in Git.
Changes are reviewed.
Every requirement can be traced
to the test that checks it.

<!-- S42 -->
So what does a change look like?
Say the customer decides
that a shipped order can still be cancelled,
as long as it hasn't been delivered.
And then the invoice must be reversed.

<!-- S43 -->
Nobody opens the backend.
A developer changes one rule
in the document about orders.

<!-- S44 -->
Then the system goes looking
for everything that rule touches.
The order states.
The invoice rules.
The tests about cancelling.
The reservation with the supplier.

<!-- S45 -->
And there, it should stop and ask.
The specification never said
what happens to a supplier reservation
once the goods are on the road.
That is a decision,
so it goes back to a person.

<!-- S46 -->
Only then is the new implementation
generated.
And it is checked in both directions.
The tests for the new rule should pass.
And every other test should still pass,
unchanged.

<!-- S47 -->
Because a change to cancelling
must not quietly change anything else.
Though passing tests only shows
what the tests check.

<!-- S48 -->
And because the rules
are not tied to the technology,
the same specification could produce
a PHP application today,
and something else entirely tomorrow.

<!-- S49 -->
Which is precisely what
Model Driven Architecture promised
twenty-five years ago.
The difference is that, this time,
the generator might be good enough.

<!-- S50 -->
That leaves the hardest question.
How do you know the AI
actually followed the specification?

<!-- S51 -->
Code that works in ordinary situations
can still fail in unusual ones.
And the unusual ones are exactly
the cases nobody thinks to test.

<!-- S52 -->
Amazon ran into this
on its own cloud systems.
In 2014, its engineers described
how they had started writing
precise, mathematical descriptions
of their designs,
in a language called TLA+.

<!-- S53 -->
Not the code. The design itself.
A tool then took a model of the system,
limited to a fixed size,
and tried every possible ordering
of failures and recoveries.

<!-- S54 -->
In DynamoDB, Amazon's database service,
it found a bug that could lose data.

<!-- S55 -->
The shortest way to trigger it
took thirty-five steps,
in exactly the right order.
It had passed design reviews,
code reviews, and testing.

<!-- S56 -->
So the honest version of the idea
isn't that AI writes the code
and we trust it.
It's that AI writes the code,
and something independent checks it.

<!-- S57 -->
Now look at what we've built.

<!-- S58 -->
Precise states.
Formal rules.
Checkable tests.
Versioned, reviewed, kept in a repository.

<!-- S59 -->
That doesn't look like
the end of programming.
It looks like programming,
in a new language.

<!-- S60 -->
And that is what happened every time.
FORTRAN was automatic coding,
until it became the code.
Each time the machine took over
the how, people moved up to the what.

<!-- S61 -->
And the what was always the hard part.
Not typing, but deciding.
What happens to a shipped order.
Who is allowed to touch which data.
What the system must never do.

<!-- S62 -->
Maybe the programmer of the future
won't write thousands of lines of code.

<!-- S63 -->
But someone will still have to understand
a problem well enough to say
exactly what a computer must do,
and to check that it did it.

<!-- S64 -->
And if the specification
becomes the source code,
the most important skill
might no longer be knowing
how to write a program.

<!-- S65 -->
It might be knowing
how to describe one.

<!-- S66 -->
So here is the question
I'd like to hear your answer to.
If you write a specification
precise enough
for a machine to build from...
are you still programming?
