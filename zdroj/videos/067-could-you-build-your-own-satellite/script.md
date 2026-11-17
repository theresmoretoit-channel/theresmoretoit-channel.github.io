<!-- S01 -->
Imagine you have a crazy idea.
You want to build your own satellite.
Not a billion-dollar
communications satellite.
Something small.

<!-- S02 -->
A box about the size
of a loaf of bread.
Inside: a computer, solar panels,
a radio, a few sensors.
Maybe even a camera.

<!-- S03 -->
You build it in your garage.
And then somehow...
you put it into orbit.
Sounds impossible.
But it isn't.

<!-- S04 -->
People have been doing
almost exactly this for years.
They're called CubeSats.

<!-- S05 -->
And the surprising part
is that the hardest thing
isn't building the satellite.
It's everything else.

<!-- S06 -->
The basic unit is called 1U —
roughly a ten-centimetre cube.
Stack units together
and you get 2U, 3U, 6U
and larger.

<!-- S07 -->
The idea is simple.
Instead of designing a new spacecraft
from scratch,
you reuse standardised sizes
and standardised interfaces.
And suddenly, space is open
to universities, start-ups,
and maybe even you.

<!-- S07b -->
By the way, if you like videos
like this, consider subscribing.

It really helps the channel.

<!-- S08 -->
So what would our little satellite
actually contain?
First, it needs a computer.
Something has to run the software,
control the hardware,
and decide what to do.

<!-- S09 -->
Then there's power.
Solar panels make electricity.
Batteries store it
for when the satellite
slips into Earth's shadow.

<!-- S10 -->
Then communication.
A radio. An antenna.
And, back on Earth,
a ground station listening.

<!-- S11 -->
Then sensors.
Temperature. Voltage. Current.
Acceleration. Magnetic field.
And some way of telling
which way the satellite is pointing.
Because in orbit,
saying "up" is surprisingly hard.

<!-- S12 -->
But before we build one,
there's an awkward question.
How much does this little box cost?
The answer is...
more than it looks like it should.

<!-- S13 -->
A simple 1U CubeSat
can easily cost
tens of thousands of dollars —
just in flight hardware.
The power system. Solar panels.
Batteries. The computer. The radio.
The attitude control. The structure.
And the payload.

<!-- S14 -->
Then come the things
that aren't on the parts list.
Testing. Integration.
Documentation.
Ground-station operations.
Licensing.
And finally...
the launch.

<!-- S15 -->
A rideshare for a tiny CubeSat
can cost tens of thousands.
Bigger missions and bigger CubeSats
reach hundreds of thousands.
And that's just
getting the thing into space.

<!-- S16 -->
And now
an even more ridiculous problem.
Remember all those parts?
How on earth does all of that
fit inside one tiny box?

<!-- S17 -->
In space, there's no room
for a random pile of electronics.
Every centimetre matters.
Every gram matters.
Every watt matters.
The satellite is a three-dimensional puzzle
that has to survive a rocket launch.

<!-- S18 -->
So where do you get
all these parts?
You don't have to design
everything yourself.
There's a whole industry
selling components for small satellites:
computers, power systems,
radios, antennas and solar panels.
There are even marketplaces
built specifically for CubeSat parts.

<!-- S18b -->
And the parts are standardised, too.
Many share one board format
and simply stack together,
so pieces from different makers
fit into one unit.
Companies like EnduroSat
and GomSpace sell them,
and a single subsystem can cost
anywhere from a few thousand
to tens of thousands of dollars.

<!-- S19 -->
And these aren't
exotic processors.
One current CubeSat computer
uses an ARM Cortex-M7,
with familiar interfaces —
SPI, I²C, UART and CAN.

<!-- S19b -->
And it isn't a custom space chip.
It's a real, off-the-shelf board
you could hold in your hand.

<!-- S20 -->
A spacecraft needs something
more important than raw speed:
predictable behaviour,
low power and reliability.
More demanding missions
can use ARM Cortex-A processors —
and even Linux.

<!-- S20b -->
But it isn't fast.
A typical CubeSat computer
runs at a couple of hundred megahertz.
Your laptop runs at
four or five gigahertz,
with many more cores.
It trades raw speed
for using almost no power.

<!-- S21 -->
And if you're a programmer,
this is where it gets interesting.
You don't write
some mysterious "space language".
You write embedded software.
Often in C or C++.

<!-- S22 -->
It might run directly
on the hardware,
or on a real-time operating system
like FreeRTOS, Zephyr or RTEMS.
There are even open frameworks
built for spacecraft.
NASA's F Prime, for example,
is a flight-software framework
for embedded and spaceflight systems.

<!-- S23 -->
So your code might look
something like this.

<!-- S24 -->
But there's one huge difference
from a normal computer.
You don't get to SSH into it.
You can't attach a debugger.
And if your software crashes...
your computer is
a few hundred kilometres up.

<!-- S25 -->
So it needs watchdogs,
safe modes, fault detection
and automatic recovery.
It has to fix some problems
without you there to help.

<!-- S25b -->
And one big reason it needs all that
is radiation.
In space, cosmic rays
can flip a bit in memory,
or even knock out a chip.
There's no heavy shielding —
that would weigh far too much.
Instead, the computer watches itself,
corrects errors,
and resets when something goes wrong.

<!-- S26 -->
But if you actually
want to launch it...
things get serious.
A part that works on your desk
isn't automatically ready
for a rocket.
It has to survive vibration,
vacuum, temperature extremes
and radiation.

<!-- S27 -->
Now, back to that problem
of knowing which way
the satellite is pointing.
Picture it tumbling
through space.
No floor. No ceiling.
GPS can tell you
where you are...
but not which way
you're facing.

<!-- S28 -->
So satellites combine
gyroscopes, magnetometers
and sun sensors
to work out their attitude.
And then they have to change it.
One common trick
is a magnetorquer.

<!-- S29 -->
It pushes against
Earth's magnetic field
and makes a tiny torque.
It's not a rocket engine.
It doesn't move the satellite.
It just turns it.
And that's enough
to point the satellite
exactly where you want.

<!-- S30 -->
But none of this
is the reason
we built the satellite.
We need a mission.
That's the payload.
Measure radiation.
Photograph Earth.
Study the atmosphere.
Test a new sensor.
Or simply prove
a new technology works.

<!-- S31 -->
The satellite itself
is mostly there
to keep the payload alive.
Power it. Point it.
Keep it warm.
Store its data.
And send it home.

<!-- S32 -->
When your desktop locks up,
you restart it.
When your satellite locks up...
you have a very expensive object
silently orbiting Earth.

<!-- S33 -->
So let's say we built it.
Everything works...
The computer boots...
The radio talks.
The panels make power.
The payload runs...
Can we launch it?
...Not yet.

<!-- S34 -->
A satellite has to prove
it can survive the launch.
That means testing.
A lot of testing.

<!-- S35 -->
First, bolt it
to a giant shaker.
Then shake it, hard...
That's vibration testing.
Rocket launches are not gentle.
It has to survive
noise, vibration and shock
without anything
coming loose or breaking.
Every screw matters.
Every connector matters.
Every piece of cable matters.

<!-- S36 -->
Then comes vacuum.
On Earth, air carries heat away.
In space, there is no air.
One side can get extremely hot,
another extremely cold,
and the electronics
still have to stay
inside their limits.
So the satellite needs
thermal straps, coatings,
insulation
and carefully chosen materials.
Satellites don't have
air conditioning.
They have physics.

<!-- S37 -->
And the battery
gets interesting.
Charge it with sunlight.
Then the satellite
slips into Earth's shadow,
and the panels make almost nothing.
The battery keeps it alive.
Then back into sunlight.
Charge. Discharge.
Charge. Discharge.
Again and again.
For years.
One mistake in power
could quietly end the mission.

<!-- S38 -->
And now, how do you talk to it?
You need a radio.
An antenna.
And a frequency
you're legally allowed to use.
And a ground station.
The satellite
doesn't have the internet.
It just flies overhead
and transmits.

<!-- S39 -->
Your ground station
catches the signal.
The computer decodes it.
And suddenly you have data
from your own spacecraft.
Imagine opening a terminal
and seeing this.

Except the machine
printing those numbers...
is hundreds of kilometres
over your head.

<!-- S40 -->
So how do we
actually get it up there?
You could build a rocket...
Please don't...
You don't need one.
CubeSats fly
as secondary payloads.

<!-- S41 -->
A rocket is already going up.
It has spare room.
Your satellite rides along
in a standard deployer.
No personal rocket required.

<!-- S42 -->
And now it's sitting
on top of a rocket.
You can't touch it.
You can't open the box.
You can't plug in a cable.
The rocket launches.
About nine minutes later,
you're in orbit.

<!-- S43 -->
The deployer
releases your satellite.
It springs free
and begins to tumble.

<!-- S43b -->
But how does it know it's out?
...
Spring-loaded switches, pressed in
while it sat in the deployer,
pop free the moment it's ejected,
and the computer boots.
Then, by the rules,
it stays silent for about half an hour.
Only then does it power up its radio,
unfold its antennas,
and finally call home.
And somewhere on Earth...
your ground station hears it.

<!-- S44 -->
You built a machine.
And now that machine
is orbiting the planet.

<!-- S44b -->
Except, we're not done.
A dead satellite can't just
stay up there forever.
Left in orbit for centuries,
it becomes space debris.

<!-- S45 -->
That means modern missions
increasingly have to plan
for the end
of the spacecraft's life.
Ideally, the thin upper atmosphere
slowly drags it down.
Its orbit decays.
It re-enters.
And it burns up.
The end of the mission...
is part of the mission.

<!-- S46 -->
So... could you build
your own satellite?
Technically, yes.
You don't need to be NASA.
You don't need
to own a rocket.
You don't even necessarily need
a huge company.

<!-- S47 -->
The satellite has to
survive launch.
Survive space.
Communicate legally.
Run on its own.
And, in the end,
clear out of orbit.
All of that
has to be proven
before anyone
puts it on a rocket.

<!-- S48 -->
CubeSats didn't make space easy.
They made it standardised.
Instead of building everything
from scratch,
you can build something
that fits an existing standard.
And that's a surprisingly big change.

<!-- S49 -->
So somewhere, right now,
there are tiny machines
orbiting Earth.
Built by universities,
research teams,
companies and students.

<!-- S50 -->
Some carry cameras.
Some measure radiation.
Some test
brand-new technology.
And some are just experiments
asking one question:
"can we make this thing
work in space?"

<!-- S51 -->
And that's what makes
building your own satellite
so fascinating.
Because the distance
between you and space
isn't a rocket anymore.
It might be...
a ten-centimetre box.
And a very, very
long checklist.
