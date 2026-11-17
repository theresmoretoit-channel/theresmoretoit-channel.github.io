<!-- S01 -->
Imagine you had a computer program
containing three billion characters
of instructions.

<!-- S02 -->
Now imagine that every time
you created a new process,
you copied the entire program into it.

<!-- S02b -->
Twice.

<!-- S03 -->
Not just the functions
that process needs.
The entire thing.
Every module.
Every dependency.
Every piece of ancient legacy code.

<!-- S04 -->
And then the process simply ignored
ninety-nine percent of it.
That would be terrible
software engineering.

<!-- S05 -->
And yet...

<!-- S06 -->
...that's more or less
what your cells do.

<!-- S07 -->
Almost every cell in your body
that has a nucleus
contains essentially the same
complete copy of your genome.

<!-- S08 -->
A neuron has it.
A liver cell has it.
A skin cell has it.
And yet they behave
completely differently.

<!-- S09 -->
The code is there.
Most of it simply isn't being used.

<!-- S10 -->
A gene can be thought of,
very roughly,
as a function or a module.

<!-- S11 -->
It contains information
that can ultimately be used
to produce a particular
functional product,
often a protein.
So we can imagine something like this.

<!-- S12 -->
But having the function in the code
doesn't mean it is running.
Something has to activate it.
And that's where biology
gets interesting.

<!-- S13 -->
Because in a computer,
I can simply write this.
Or in machine code.

<!-- S14 -->
The processor knows exactly what to do.
There is an instruction.
There is an address.
There is an instruction pointer.

<!-- S15 -->
But a cell doesn't have a CPU
sitting there executing
DNA instructions one by one.

<!-- S16 -->
So...

<!-- S17 -->
...how does it know what to use?

<!-- S18 -->
This is where the computer analogy
starts getting weird.
In a computer, you can jump
to a specific memory address.

<!-- S19 -->
You can have access permissions.
You can have processes.
You can have configuration files.
You can have events
triggering specific pieces of code.

<!-- S20 -->
Biology has things
that play surprisingly similar roles.

<!-- S21 -->
Transcription factors can bind
to particular DNA sequences
and influence whether
a gene is transcribed.

<!-- S22 -->
Regulatory DNA sequences can affect
when and where genes are expressed.
The structure of chromatin affects
how accessible
particular regions of DNA are.

<!-- S23 -->
And cells constantly receive signals
from their environment.

<!-- S24 -->
So instead of a CPU,
an instruction pointer,
a memory address, and execute...

<!-- S25 -->
...you have something more like this.

<!-- S26 -->
There isn't one instruction pointer.
There is an enormous network
of molecular interactions.

<!-- S27 -->
The DNA is there.
But different parts of it
are more or less accessible
to the molecular machinery
that reads them.

<!-- S28 -->
So, having the code
is not the same
as having access to the code.
A liver cell doesn't need to delete
all the neuron related genes.
It can simply regulate
whether they're used.

<!-- S29 -->
Let's go back
to our software project.
Suppose you're developing
a huge application.

<!-- S30 -->
You create a new module called finger.
And instead of importing
the few functions it needs...

<!-- S31 -->
...you copy the entire
human repository into it.

<!-- S32 -->
The brain.
The liver.
The heart.
The immune system.
The reproductive system.
Everything.

<!-- S33 -->
And you do this again...

<!-- S34 -->
...for every cell.

<!-- S35 -->
As a programmer,
you would probably ask...
Who designed this?

<!-- S36 -->
And the answer is...

<!-- S37 -->
Nobody.

<!-- S38 -->
Well... Not nobody.
Evolution.

<!-- S39 -->
And evolution has a very different
development philosophy.

<!-- S40 -->
Imagine opening a repository
called human,
with a commit history
stretching back billions of years.

<!-- S41 -->
There was no architect sitting down
and designing version one point zero.
There was no clean rewrite.
There was no human version two
with a redesigned architecture.

<!-- S42 -->
Instead...
Add feature.
Patch bug.
Duplicate module.
Reuse old module.

<!-- S43 -->
Work around limitation.
Add another workaround.
Keep old API
because something depends on it.

<!-- S44 -->
Again.
And again.
And again.
For billions of years.

<!-- S45 -->
Evolution doesn't ask
what the cleanest architecture is.
It asks a much simpler question.
Does this organism
reproduce successfully?

<!-- S46 -->
If the answer is yes,
the code survives.

<!-- S47 -->
Imagine inheriting a software project
that has been maintained
by millions of programmers,
over billions of years,
with absolutely no possibility
of rewriting the whole thing.

<!-- S48 -->
You discover something and ask...
Why does this exist?
Because something depended on it.

<!-- S49 -->
Why is this API so weird?
Legacy.

<!-- S50 -->
That is evolution.
It is the ultimate legacy system.
It doesn't refactor.
It modifies what already exists.

<!-- S51 -->
And after billions of years...

<!-- S52 -->
...you get us.

<!-- S53 -->
Modern software development
has a fairly sensible idea.
You make a change.
Then you test it.

<!-- S54 -->
Commit.
Build.
Unit tests.
Integration tests.
Deployment.

<!-- S55 -->
Biology has something
that looks vaguely similar.
A mutation occurs.

<!-- S56 -->
And then...
The organism either survives
and reproduces.
Or it doesn't.

<!-- S57 -->
There is no staging environment.
There is no rollback.

<!-- S58 -->
And occasionally
something much worse happens.
A mutation can make a cell
better at surviving and reproducing
inside the organism.
That can contribute to cancer.

<!-- S59 -->
So biology has a rather terrifying
version of continuous integration.
The tests are performed
on the production system.

<!-- S60 -->
But this is where
the software analogy
becomes even more interesting.
When you look at the human body,
it's tempting to imagine
something like this.

<!-- S61 -->
But that's not really
how the system works.
There is no central server
sending instructions to every cell.

<!-- S62 -->
Your cells constantly monitor
their local environment.
They receive chemical signals.
They interact with neighbouring cells.
They respond to hormones.

<!-- S63 -->
A cell doesn't receive
a message saying...

<!-- S64 -->
...cell number seven million,
three hundred and ninety-two thousand,
one hundred and eighty-four.
Please express gene X now.

<!-- S65 -->
If you're a programmer,
there's another concept
that suddenly becomes useful.
Distributed systems.

<!-- S66 -->
Your cells are effectively
enormous numbers
of individual agents.
Each one has its own state.
Its own sensors.
Its own inputs.
Its own responses.

<!-- S67 -->
There isn't one giant loop
telling every cell what to do.
That's closer
to a multi-agent system.
Or a swarm.
Or a cellular automaton.

<!-- S68 -->
Simple local rules...

<!-- S69 -->
...producing astonishingly
complicated global behaviour.

<!-- S70 -->
Here's another thing that would be
unacceptable in normal software.
Your body has been running
continuously for decades.

<!-- S71 -->
No reboot.
No scheduled maintenance window.

<!-- S72 -->
And yet the system
is constantly changing.
Cells die.
New cells are created.
Proteins are produced and destroyed.

<!-- S73 -->
DNA is copied.
Damage is repaired.
Components are replaced.

<!-- S74 -->
The system doesn't shut down
so that maintenance can happen.
It performs maintenance
while running.

<!-- S75 -->
It's almost as if you had a server
that could replace parts of itself
while the server
was processing requests...

<!-- S76 -->
...without ever going offline.

<!-- S77 -->
Cells have their own machinery.
They communicate.
They respond.
They regulate one another.
They form tissues.
Tissues form organs.
Organs form systems.
And systems form an organism.

<!-- S78 -->
And there is no single component
holding the entire architecture
in its head.

<!-- S79 -->
And somehow...

<!-- S80 -->
...it works.

<!-- S81 -->
Not perfectly.
Far from perfectly.

<!-- S82 -->
But well enough to build eyes.
Hearts.
Immune systems.
Brains.

<!-- S83 -->
And organisms capable
of writing software to complain
about how badly
the system is designed.

<!-- S84 -->
We've been calling DNA code.
And the analogy is useful.
Genes look a bit like functions.
Mutations look a bit like
changes to source code.

<!-- S85 -->
But there is
an important difference.
DNA isn't actually
a complete blueprint for a human.

<!-- S86 -->
There isn't literally a line saying...
Create arm.
Create eye.
Create heart.

<!-- S87 -->
Instead, DNA participates
in a gigantic system of interactions
involving molecules, cells,
physical forces, chemical gradients,
timing and environment.

<!-- S87b -->
The organism emerges from all of this.

<!-- S88 -->
So DNA is perhaps better thought of
as a set of instructions and rules
embedded in a physical system...

<!-- S89 -->
...rather than a complete
source code listing for a human.
And that's actually much stranger.

<!-- S90 -->
We can sequence a human genome,
identify genes
and measure proteins.

<!-- S91 -->
But we still can't take the DNA
from one ordinary human cell,
put it into a computer,
press run...

<!-- S92 -->
...and watch that human develop.

<!-- S93 -->
We have the genome.
But the genome
isn't the whole machine.

<!-- S94 -->
And that's where we end up.
We started with a familiar idea.
DNA is like computer code.

<!-- S95 -->
And the analogy turns out
to be surprisingly useful.
But the deeper we look,
the stranger the system becomes.

<!-- S96 -->
There is no CPU.
There is no operating system.
There is no central server.

<!-- S97 -->
There is no programmer.
There is no GitHub.
There is no code review.
There is no staging environment.
There is no rollback.
There is barely even
a clean architecture.

<!-- S98 -->
There are trillions of tiny agents,
each following local rules,
communicating with their neighbours,

<!-- S99 -->
using a gigantic, ancient,
continuously modified repository...
And somehow producing
a functioning organism.

<!-- S100 -->
So if biology is software...

<!-- S101 -->
...it may be the oldest,
messiest, most overengineered
legacy system imaginable.

<!-- S102 -->
A system with billions of years
of commits.
Almost no refactoring.
No central administrator.
And absolutely no reboot.

<!-- S103 -->
And somehow...

<!-- S104 -->
...it's been running in production
for billions of years.
