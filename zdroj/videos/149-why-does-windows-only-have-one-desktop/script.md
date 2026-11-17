<!-- S01 -->
Picture switching on a Windows PC
and finding no taskbar, no Start button,
and not a single icon on the desktop.

<!-- S02 -->
Instead there's a thin bar along the top,
a menu that pops up wherever you click,
and four virtual desktops side by side.

<!-- S03 -->
It looks like Linux.
But your programs, your drivers and your files
are exactly where you left them.
It's still Windows.

<!-- S04 -->
Only the desktop has changed.
And the switch that changes it
is a single setting.

<!-- S05 -->
Windows keeps it in the registry,
in a value called Shell.
On almost every Windows PC,
it says explorer.exe.

<!-- S06 -->
Write the name of a different program there,
sign out and sign back in,
and Windows starts that program instead.
Whatever it draws becomes your desktop.

<!-- S07 -->
And this isn't a trick someone found last year.
In 1990, Windows 3.0 had the same switch
in a plain text file called system.ini.
One line: shell=progman.exe.

<!-- S08 -->
If you changed that name,
Program Manager, the window full of icon groups,
never appeared at all.

<!-- S09 -->
So the question isn't whether Windows
can have a different desktop.
It always could.
The question is why almost nobody has seen one.

<!-- S10 -->
Start with what that line actually points to.
The taskbar, the desktop icons,
the little tray by the clock:
all of that is one program, Explorer.

<!-- S11 -->
Yes, the same Explorer
you open to look through your files.
It does two jobs,
and most people only ever notice one.

<!-- S12 -->
That second job has a name: the shell.
It's the layer you touch.
Underneath it sit the kernel, the drivers,
and the services that keep Windows running.

<!-- S13 -->
None of them need a taskbar.
End Explorer in Task Manager,
and the taskbar and icons vanish...
but Notepad, your browser,
every other window keeps working.

<!-- S14 -->
Start it again, and the desktop comes back.
That's about the clearest proof there is
that the desktop is just another program.

<!-- S14b -->
If you've ever changed the launcher
on an Android phone,
you've seen a similar idea.
Android makes it a normal setting.
Windows has the mechanism too,
but never gave ordinary users
a simple button for it.

<!-- S15 -->
Three words get mixed up here.
The shell is what you launch things from:
the taskbar, the menus, the desktop.
A window manager controls how windows
are positioned, stacked and focused.
A desktop environment
brings the whole experience together.

<!-- S16 -->
On Linux, these pieces can be combined
in many different ways.
On Windows, replacing the shell
doesn't replace the system's window management,
or the way applications draw their window frames.

<!-- S17 -->
That didn't stop people from trying.
By the early nineties, you could walk into a shop
and buy a replacement for Program Manager.

<!-- S18 -->
Norton Desktop for Windows
gave you its own desktop,
its own file tools and its own launcher,
on top of the same Windows underneath.

<!-- S19 -->
Some computer makers replaced it
before the customer ever switched on.
Packard Bell's Navigator greeted buyers
with a house you could walk through, room by room.

<!-- S20 -->
Then Windows 95 handed the job to Explorer,
and the line in system.ini
simply changed to explorer.exe.
The switch stayed exactly where it was.

<!-- S21 -->
In the late nineties,
a whole community grew up around that switch.
The best-known project was LiteStep.

<!-- S22 -->
It borrowed its look from AfterStep,
a Unix window manager modelled on NeXTSTEP,
from the company Steve Jobs founded after leaving Apple.

<!-- S23 -->
LiteStep had no Start menu unless you built one.
Everything was a module:
a dock here, a clock there,
a menu that opened wherever you right-clicked.

<!-- S24 -->
Its themes were shared like wallpapers.
Some looked futuristic.
Some looked like a Unix workstation.
Some left almost nothing on the screen at all.

<!-- S25 -->
Blackbox for Windows went the other way.
It copied Blackbox, a minimalist Unix window manager,
down to a single plain menu
and a slim toolbar.

<!-- S26 -->
Its successor, bbLean,
kept that idea alive on Windows 2000 and XP.

<!-- S27 -->
Emerge Desktop broke the shell into separate parts:
a launcher, a tray, a task list,
each one a small program you could keep or drop.

<!-- S28 -->
Why go to all that trouble?
Partly because the look of XP
was easy to recognise and hard to change.
Themes changed the colours and buttons.
The layout stayed.

<!-- S29 -->
Partly memory.
On a machine with a hundred and twenty-eight megabytes,
a lighter shell promised more room
for everything else.

<!-- S30 -->
And partly Linux.
There, choosing your desktop was normal,
and some Windows users wanted
the same choice.

<!-- S31 -->
Most of those projects are gone now.
LiteStep's last release was a preview
from 2014, still marked alpha.
Emerge Desktop and SharpEnviro stopped too.

<!-- S32 -->
Small volunteer teams were part of the reason.
But Windows changed too.
Over the years, its desktop became much more
than one executable.

<!-- S33 -->
The desktop experience is now spread
across multiple processes,
system components and packaged applications.
Even the Start menu runs as a program of its own.

<!-- S34 -->
Replacing Explorer doesn't mean replacing
everything that makes up the modern Windows interface.
And that's one reason why building
a complete alternative desktop
is harder than it used to be.

<!-- S35 -->
And yet it still works.
Cairo Desktop, an open-source project,
runs on Windows 11 today.

<!-- S36 -->
It brings its own menu bar along the top,
its own taskbar,
and folders you can pin to the bar as stacks.

<!-- S37 -->
It can run alongside Explorer,
or take over as the shell.
In that second mode,
parts of Windows 11 can misbehave,
Settings and Windows Security among them.

<!-- S38 -->
Seelen UI goes about it differently.
It doesn't replace Explorer.
It hides the taskbar and brings its own pieces:
a dock, a bar, widgets,
and a window manager that tiles your windows.

<!-- S39 -->
The result can look nothing like Windows.
But underneath, Explorer is still running.
It's a new face, not a new shell.

<!-- S40 -->
And Microsoft?
It actually has an official feature for this.
It's called Shell Launcher,
and it's designed for devices like kiosks.

<!-- S41 -->
You've probably used something like it
without knowing.
The ticket machine at a station.
A self-service checkout. A cash machine.

<!-- S42 -->
Many of them are Windows PCs
whose whole shell is one application.
An administrator names the program,
and after sign-in, that program is the whole desktop.

<!-- S43 -->
But it's only available
in the Enterprise, Education
and IoT Enterprise editions.

<!-- S44 -->
And the older registry mechanism
is still part of Windows.
Microsoft just never turned it
into a normal desktop setting
for ordinary users.

<!-- S45 -->
So why does Windows only seem to have one desktop?
Not because it can't have another.
Because the desktop is the product.

<!-- S46 -->
On Linux, the desktop is a choice.
Some distributions ask you to pick one
while you're still installing.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
On Windows, the desktop is what Microsoft shows
in every advert, every screenshot
and every support page.
One desktop means one set of instructions
for more than a billion machines.

<!-- S48 -->
That's a real advantage.
When something breaks,
the screen in the help article looks like yours.
The cost is that most people never learn
there was a choice.

<!-- S49 -->
People were swapping the Windows desktop
before Windows 95 even existed.
They built docks, bare menus,
and desktops that looked like nothing else.

<!-- S50 -->
Most of those projects are gone.
The idea isn't.
Under every taskbar you've ever clicked,
there's still that one setting, waiting for a different name.

<!-- S51 -->
The desktop is just another piece of software.
And software can be replaced.

<!-- S52 -->
So here's a question for you.
If Windows let you pick your desktop
while installing, the way some Linux distributions do,
would you switch, or keep the one you know?
Let me know in the comments.
