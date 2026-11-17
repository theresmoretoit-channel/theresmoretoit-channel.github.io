# Why Can't Computers Predict Every Deadlock?
**Script v0.4**

<!-- S01 -->
Four cars arrive at a crossroads
at exactly the same moment.
No lights. No signs.
Just the rule many countries use:
give way to the car on your right.

<!-- S02 -->
Every driver looks right,
and sees a car they have to wait for.
So every driver waits.

<!-- S03 -->
Nobody is breaking the rule.
Everybody is following it perfectly.
And nobody will ever move.

<!-- S04 -->
Computer scientists call this a deadlock.
And it doesn't only happen on roads.
It happens inside databases,
operating systems and ordinary software.

<!-- S05 -->
Computers are often good at spotting
a deadlock once it has happened.
But could a program read another program
and tell you, for certain,
whether it will ever get stuck?

<!-- S06 -->
For many programs, yes.
But a method that works
for every possible program
can't exist.
And not because computers
aren't fast enough yet.
No faster computer will ever change it.

<!-- S07 -->
Here's how a program gets stuck.
Imagine an online shop,
with two tasks running at the same time.

<!-- S08 -->
Before a task changes anything,
it takes a lock on it,
so that nobody else can touch it.
Like taking the only key to a room.

<!-- S09 -->
The first task locks a customer's account,
then reaches for their order.
The second locks the order,
then reaches for the account.

<!-- S10 -->
One holds the account
and waits for the order.
The other holds the order
and waits for the account.
Neither will let go of what it's holding.

<!-- S11 -->
And the strange part is,
this code can run a million times
without any trouble.
Only when the two tasks overlap
in exactly the wrong order
does everything stop.

<!-- S12 -->
The bug was there all along.
The timing just exposed it.

<!-- S12b -->
By the way, if you like videos
like this, consider subscribing.

It really helps the channel.

<!-- S13 -->
Databases run into this all the time,
so they keep watch.
They draw a map of who is waiting for whom.

<!-- S14 -->
The first waits for the second.
The second waits for the first.
When the arrows close into a loop,
that's a deadlock.
No guessing. The loop is right there.

<!-- S15 -->
Then the database does something brutal.
It picks one of the tasks
and throws its work away.

<!-- S16 -->
Microsoft's SQL Server even tells the loser
that it has been chosen
as the deadlock victim,
and should try again.

<!-- S17 -->
The other task carries on,
and the victim can simply try again.

<!-- S18 -->
Notice what that does and doesn't fix.
The jam is cleared.
But the code that caused it is still there,
waiting for the next unlucky moment.

<!-- S19 -->
So spotting a deadlock
that has already happened
is the easy part.
The hard question is a different one.

<!-- S20 -->
Not: is this program stuck right now?
But: give it this input.
Could it ever get stuck?

<!-- S21 -->
The first is a photo of the present.
You can just look at it.
The second is a prediction
about every possible future.

<!-- S22 -->
And programs make that very hard.
They make decisions. They repeat things.
They can run calculations that take
a second, or a thousand years.

<!-- S23 -->
A program might get stuck at once,
after a million steps,
for one rare input,
or never at all.

<!-- S24 -->
You could just run it and watch.
But if it hasn't got stuck after an hour,
what does that tell you?

<!-- S25 -->
Nothing.
It might get stuck in the next second,
or never.

<!-- S26 -->
In 1936, a young mathematician
called Alan Turing showed
that some questions about programs
can't be answered by any program.
The most famous one sounds even simpler.

<!-- S27 -->
Take any program, and its input.
Will it eventually stop?
Or will it run forever?

<!-- S28 -->
It's now called the halting problem.
And no program can answer it
correctly in every case.

<!-- S29 -->
The idea behind the proof
is surprisingly short.
Suppose someone hands you
a perfect halting checker.

<!-- S30 -->
Now you write a contrary little program.
It asks the checker about itself,
and then does the opposite.

<!-- S31 -->
If the checker says it will stop,
it loops forever.
If the checker says it will run forever,
it stops at once.

<!-- S32 -->
Whatever the checker says about it,
the checker is wrong.
So a perfect checker can't exist.

<!-- S33 -->
So what does this have to do with deadlocks?
Everything.

<!-- S34 -->
Imagine someone claims to have built
a perfect deadlock predictor.
Give it any program and its input,
and it always tells you, correctly,
whether that program will ever get stuck.

<!-- S35 -->
Let's use it
to solve the halting problem.

<!-- S36 -->
Take any program you like,
and wrap it inside a new program.

<!-- S37 -->
First, the new program
simply runs the old one,
step by step, on a single thread.
No locks. Nothing shared.
Nothing that could ever get stuck.

<!-- S38 -->
Then, if the old program ever finishes,
the new one starts two tasks.
Each grabs one lock,
waits until the other has grabbed its own,
and then reaches for the other's.
A deadlock, on purpose, every time.

<!-- S39 -->
If the old program never finishes,
the new one never gets that far.
No deadlock. Ever.

<!-- S40 -->
So the new program gets stuck
if, and only if, the old one stops.

<!-- S41 -->
Now ask the predictor
about the new program.
Yes, it will deadlock,
means the old program stops.
No means it runs forever.

<!-- S42 -->
We've just solved the halting problem.
And that's exactly what can't be done.

<!-- S43 -->
So the perfect deadlock predictor
can't exist either.

<!-- S44 -->
The trouble isn't locks,
or databases, or bad programmers.
A program can hide any calculation
in front of a deadlock.
To predict the deadlock,
you'd have to predict the calculation.

<!-- S45 -->
But hold on.
A real computer isn't infinite.
Its memory has a limited number of states.
So couldn't you just check them all?

<!-- S46 -->
For a machine with a fixed amount
of memory, in principle, yes.
In practice, count them.

<!-- S47 -->
The memory of a laptop
with eight gigabytes
can be arranged in so many ways
that just writing that number down
takes about twenty billion digits.

<!-- S48 -->
The number of atoms
in the observable universe
has about eighty.

<!-- S49 -->
So on a real machine, checking everything
is possible in theory,
and hopeless in practice.

<!-- S50 -->
But that's a different wall.
Turing's limit isn't about too many states.
It applies to programs
that can always ask for more memory.
For those, no perfect predictor can exist,
however big the computer.

<!-- S51 -->
Does that make deadlocks hopeless?
No.
It means there's no perfect checker.
So programmers write programs
that are easier to check.

<!-- S52 -->
The simplest trick is an order.
Every task must lock the account
before the order.
Never the other way round.

<!-- S53 -->
If every task really sticks to that order,
the loop can't form,
and this kind of deadlock can't happen.

<!-- S54 -->
Other systems give up after a timeout,
take all their locks in one go,
or let the database pick a victim
and simply try again.

<!-- S55 -->
And for small, carefully described designs,
tools can check every possible state.
Engineers at Amazon used one
to find a bug that took thirty-five steps,
in exactly the right order, to appear.

<!-- S56 -->
These tools work
because the problem has been made smaller.
They check a model of the system,
not every program that could ever exist.

<!-- S57 -->
For real code, though,
a checker that takes any program
has to give something up.
It may warn about deadlocks
that can't happen,
miss some that can,
or sometimes give no answer at all.

<!-- S58 -->
A checker that never cries wolf,
never misses one,
and always gives an answer,
for every program,
is exactly what Turing ruled out.

<!-- S59 -->
Back at the crossroads,
the four drivers don't sit there forever.

<!-- S60 -->
Somebody waves.
One driver gives up their turn,
and the jam is over in seconds.

<!-- S61 -->
That's what the database does, too.
It doesn't predict the jam.
It notices it,
and makes someone give way.

<!-- S62 -->
Some problems need a faster computer.
Some need a better idea.

<!-- S63 -->
And some, like this one,
have no perfect solution at all.
Only good rules,
and someone ready to wave.
