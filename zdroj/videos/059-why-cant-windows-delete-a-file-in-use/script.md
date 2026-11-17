<!-- S01 -->
You try to delete a file.
Your computer says it is open
in another program.
It does not say which one.

<!-- S02 -->
That message is the visible end
of a much stranger question.
What does it actually mean
to open a file?

<!-- S03 -->
Because on another computer,
the same file, open in the same way,
deletes without complaining.

<!-- S04 -->
Same file.
Same action.
Two completely different answers.

<!-- S05 -->
Start with the part
that annoys everybody.
Which program?

<!-- S06 -->
Windows knows.
It has a kernel object
for that open file,
and it knows which process owns it.
It could name it.

<!-- S07 -->
So you close things at random.
You open Task Manager.
You stare at a list of processes
and recognise hardly any of them.

<!-- S08 -->
And for years,
the answer really was
to download a separate tool.
Unlocker came out in 2005,
and on Windows XP that was the answer.

<!-- S09 -->
Then Windows 7 shipped
Resource Monitor.
The CPU tab.
A list called Associated Handles.

<!-- S10 -->
Type the name of the file.
It gives you the program
and the process ID.
Nothing to install.
It has been there since 2009.

<!-- S10b -->
Although the separate tools
did more than just tell you.
They could close the handle
and let the file go.

<!-- S11 -->
Which brings us back
to the question.
What did that program acquire
when it opened the file?

<!-- S12 -->
Say a video player opens
a file called movie.mp4.
On Windows, opening a file
means filling in two things.

<!-- S13 -->
The first one is obvious.
What do I want to do with it?
Read it. Write to it.

<!-- S14 -->
The second one is the interesting one.
What may everybody else do
while I have it open?

<!-- S15 -->
That is a real setting.
You say what other programs
may do while you have it open.

<!-- S16 -->
They may read it.
They may also write to it.
They may delete or rename it.

<!-- S16b -->
Or nothing at all.
Nobody touches this
while I am using it.

<!-- S17 -->
The flag that permits deleting
is called FILE_SHARE_DELETE.
And Microsoft's documentation
adds one line underneath it.

<!-- S18 -->
Delete access allows
both delete and rename operations.

<!-- S19 -->
So a program that refuses
delete sharing
has blocked renaming as well.

<!-- S20 -->
And if the program that opened the file
did not grant it,
nothing else can take it.

<!-- S21 -->
Which is why the error
is not called file busy.
It is called a sharing violation.

<!-- S22 -->
The answer was sitting
in the name of the error
the whole time.

<!-- S23 -->
Now the same thing
on a Linux machine.
A player opens the video.

<!-- S24 -->
And you type
rm movie.mp4.

<!-- S24b -->
It works.
The video keeps playing.

<!-- S25 -->
So what did that program get,
if not a hold on the file?

<!-- S26 -->
This is the whole idea
of the video.
The name is not the file.

<!-- S27 -->
movie.mp4 is a line
in a directory.
That line points at an object
which holds the actual data.

<!-- S28 -->
When a program opens the file,
what it gets is a reference
to the object.
Not to the line.

<!-- S29 -->
So removing the file
deletes the line.
The object is untouched.

<!-- S30 -->
The manual page says it
in one sentence.
The file will remain in existence
until the last file descriptor
referring to it is closed.

<!-- S31 -->
Which sounds abstract
until you watch it happen.
So I made a log file
five hundred megabytes long,
and left one process holding it open.

<!-- S31b -->
Then I deleted it.

<!-- S32 -->
Listing the directory
shows nothing at all.
The tool that measures
the size of the folder says zero.

<!-- S33 -->
And the tool that measures
free space on the disk
says five hundred megabytes
are still missing.

<!-- S33b -->
An empty folder.
Half a gigabyte gone.

<!-- S34 -->
This happens often enough
that there is a command
just for finding files like this.
Deleted, invisible, still on the disk.

<!-- S35 -->
And the space comes back
the moment that one process
lets go of the file.

<!-- S36 -->
The same logic covers renaming.
Move the file while it is open,
and the program never notices.

<!-- S37 -->
The manual is blunt about that too.
Open file descriptors
for the old path are unaffected.

<!-- S37b -->
It was never using the name.

<!-- S38 -->
Which has one limit
worth knowing about.
You cannot overwrite
a running program in place.

<!-- S38b -->
Linux refuses.
Text file busy.

<!-- S39 -->
What you can do
is detach the name
and put a new file there.

<!-- S40 -->
The old process keeps running
from an object
that no longer has a name.
Anything started later gets the new one.

<!-- S41 -->
Which is the same idea again,
proving itself.
You can replace many things
without touching the object in place.

<!-- S41b -->
Which is why Linux can update
a program while it is running.
You just do not get the new version
until you restart it.

<!-- S42 -->
So is Windows
simply the worse design?

<!-- S42b -->
No.
And this is the part
that hardly anyone knows.

<!-- S43 -->
Windows has a way
to do exactly the same thing.

<!-- S43b -->
On NTFS, Windows can ask
for a POSIX style delete.

<!-- S44 -->
Microsoft describes
what happens when you use it.
The name is removed
from the visible namespace.

<!-- S45 -->
And applications that already had
the file open can still use it,
even though the name
they used to open it is gone.

<!-- S46 -->
That is the Unix behaviour.
On NTFS.
Documented by Microsoft.

<!-- S47 -->
Both systems can do both things.
What differs is the default.
What you get when you open a file
and never think about it.

<!-- S48 -->
On Windows, you get a contract.
On Unix, you get a reference
to an object.

<!-- S49 -->
Which sounds like a question
for programmers,
until you have seen
this particular message.

<!-- S50 -->
Please restart your computer
to finish installing updates.

<!-- S51 -->
Suppose Windows has to replace
a library that a running process
holds open under the strict contract.

<!-- S52 -->
It cannot swap the file
underneath that process.
So something has to let go.

<!-- S53 -->
Quit the application.
Stop the service.
Or hand the whole job
to the Restart Manager.

<!-- S54 -->
Which is a real component.
It shuts things down in order.
Windows applications,
then console programs,

<!-- S55 -->
then services,
and Windows Explorer last.
Then it starts them up again.

<!-- S56 -->
And it exists for one reason,
which Microsoft states plainly
in its own documentation.

<!-- S57 -->
The primary reason
that software installation
and updates require
a system restart...

<!-- S58 -->
is that some of the files
being updated are currently in use
by a running application
or service.

<!-- S59 -->
It would be too neat to stop there.
Sharing rules are not the only reason
a computer asks to restart.

<!-- S60 -->
A kernel update is different.
You cannot swap the kernel
underneath itself.

<!-- S61 -->
Linux has that problem too,
although live patching
can sometimes avoid a reboot.

<!-- S62 -->
So the honest version
claims less than
the satisfying one.

<!-- S63 -->
The way Windows treats files in use
made some components harder
to replace while running,
and that contributed.

<!-- S64 -->
Because every design choice
has a consequence somewhere.

<!-- S65 -->
Windows lets the program
that opens a file decide
how others may share it.

<!-- S66 -->
The cost is that sometimes
you cannot delete your own file,
because another program
has not allowed it.

<!-- S67 -->
Unix keeps the name
and the object apart,
so many things can be replaced
while the system is running.

<!-- S68 -->
The cost is half a gigabyte
that vanished from the disk
and belongs to no file at all.

<!-- S69 -->
And look at how each of those
gets resolved.
On Windows, one way out
is closing the program
that holds the file.

<!-- S70 -->
On Linux, one way to get
that disk space back
is restarting the service
that still has it open.

<!-- S71 -->
Different causes.
Sometimes, the same remedy.

<!-- S71b -->
By the way, if you'd like to see
where the next question takes us,
consider subscribing.

It really helps the channel.

<!-- S72 -->
So. The question from the start.
What does it mean
to open a file?

<!-- S73 -->
It means you are holding something.
The two systems simply hand you
different things to hold.

<!-- S74 -->
Which is why that message
never actually said
this file cannot be deleted.

<!-- S75 -->
It said the program
that opened it
did not agree to let you.

<!-- S75b -->
And it does know which program.
It just did not mention it.
