<!-- S01 -->
You buy a brand-new drive.
One terabyte, completely empty.
Before it will hold a single file,
it first has to be formatted.

<!-- S02 -->
So you format it with ext4,
the standard filesystem
on many Linux computers.
With the default settings,
before you've saved anything at all,
about seventeen gigabytes are gone.

<!-- S03 -->
Nothing has been stored yet.
No photos, no documents.
So what's taking up all that space?

<!-- S04 -->
And why does a drive need formatting
in the first place?
It can already store data.
It can read and write trillions of bits.

<!-- S05 -->
Why can't the computer just start writing
wherever there's room?

<!-- S06 -->
Because storing data
and finding it again
are two very different problems.

<!-- S07 -->
Imagine an office that hands out
blank paper instead of forms.
Everything gets written down somewhere...
and nobody can find anything.

<!-- S08 -->
A drive without a filesystem
is that pile of paper.
A better picture, though,
is a notebook.

<!-- S09 -->
Picture a notebook
with a thousand pages,
and a few rules for using it.

<!-- S10 -->
First, every page has a number.
Now every spot in the notebook
has an address.
Page four hundred and twelve
means exactly one place.

<!-- S11 -->
Second, the first few pages
are a table of contents.
Each entry gives a name,
and the page where it lives.
Pancakes: page twelve.

<!-- S12 -->
Third, at the very back,
there's a list of the pages
that are still blank.

<!-- S13 -->
Now add a recipe.
You check the back for a blank page.
You write the recipe there.
You add a line to the contents.
And you cross that page off
the blank list.

<!-- S14 -->
One recipe, three places.
And all three have to agree.

<!-- S15 -->
Then the pancake recipe grows.
Page twelve is full,
and page thirteen is already taken.
So it carries on at page eighty-seven,
and the contents has to say so.

<!-- S16 -->
And here's the catch.
If you want room for a thousand entries
in the table of contents,
you have to set those pages aside
before you write a single recipe.

<!-- S17 -->
That's the analogy.
Here's what's actually on the drive.

<!-- S18 -->
A drive doesn't know about files,
folders or names.
All it offers is a long row
of numbered slots, called sectors.

<!-- S19 -->
On a hard drive,
the data sits on spinning platters.
An SSD keeps it in flash memory.
Either way, the computer only ever asks
for a sector by its number,
and the drive works out where that is.

<!-- S20 -->
A sector is small.
Usually 512 bytes,
or 4,096
on newer drives.

<!-- S21 -->
Filesystems usually work
in bigger pieces, called blocks.
On ext4, a block is four kilobytes,
the size of eight old-style sectors.

<!-- S22 -->
Those numbered blocks
are the notebook's pages.
What the filesystem still needs
are the other two parts:
a table of contents,
and a list of what's free.

<!-- S23 -->
That's what formatting builds.
And that's where
those seventeen gigabytes went.

<!-- S24 -->
Ext4 sets aside a record
for every file and folder
the drive will be able to hold at once.
Each record is
256 bytes.
It's called an inode.

<!-- S25 -->
One day, each inode will say
how big a file is,
when it was changed,
who may open it,
and which blocks hold its contents.

<!-- S26 -->
On a one terabyte drive,
ext4 prepares about
sixty-one million of them.
All empty, all waiting.
That's almost sixteen gigabytes
of blank records.

<!-- S27 -->
Why sixty-one million?
Ext4 makes a simple guess:
one inode for every sixteen kilobytes
of space on the drive.
On a typical computer,
most of those records
will never be used.

<!-- S28 -->
About one more gigabyte
goes to a journal,
which we'll come back to.
The rest is other bookkeeping,
including a map with one bit per block,
saying whether it's used or free.

<!-- S29 -->
That number is fixed, too.
Use up every record
with millions of tiny files,
and the drive will tell you it's full...
even with gigabytes of space left.

<!-- S30 -->
So let's watch it work.
We'll create a file called hello.txt.
Inside, just one word: hello.
Five letters. Five bytes.

<!-- S31 -->
The filesystem picks an empty inode.
Let's say number thirteen.
Then it finds a free block in the map,
and marks it as used.

<!-- S32 -->
It writes the five bytes into that block.
Then it fills in the inode:
five bytes long, created just now,
and stored in that one block.

<!-- S33 -->
And finally, in the folder,
it adds one line:
the name hello.txt,
and the number thirteen.

<!-- S34 -->
Notice where the name ended up.
Not in the file.
Not in the inode.
The name lives in the folder,
which is really just a list
of names and numbers.

<!-- S35 -->
And a folder is just another file.
What it happens to contain
is that list.

<!-- S36 -->
That's also why moving a file
to another folder on the same filesystem
is instant, however big it is.
One folder loses a line,
the other gains one,
and usually, the contents
don't move at all.

<!-- S37 -->
Five bytes of text...
and on the drive, it takes up
4,096.
A block is the smallest piece
the filesystem hands out,
so even a tiny file costs a whole one.

<!-- S38 -->
When the file outgrows its block,
the filesystem finds another free one.
Maybe right next door.
Maybe somewhere else entirely.
And the inode keeps track of both.

<!-- S39 -->
Over time, a big file can end up
in pieces all over the drive.
A hard drive has to jump between them.
An SSD copes with that much better.

<!-- S40 -->
The program that saved the file
knows none of this.
It said "save hello.txt",
and everything else happened underneath.

<!-- S41 -->
Now delete it.
The name is removed from the folder.
The inode is marked as free.
The block goes back on the free list.

<!-- S42 -->
On a traditional hard drive,
the five bytes themselves stay put.
Nobody touched them.
They remain until something new
is written on top.

<!-- S43 -->
That's why a deleted file
can sometimes be recovered.
Deleting usually doesn't erase
the contents.
It just marks the space as available.

<!-- S44 -->
On an SSD, it's less certain.
The filesystem can tell the drive
that those blocks are no longer needed,
and the drive may discard what's in them.
After that, getting the file back
is much less likely.

<!-- S45 -->
So a filesystem is really a bookkeeper.
Creating this one file
meant updating three things:
the folder, the inode,
and the map of free blocks.

<!-- S46 -->
Now cut the power
halfway through saving a file.

<!-- S47 -->
Maybe the block was marked as used,
but no inode points to it yet.
That space is simply lost.
Annoying, but harmless.

<!-- S48 -->
Or maybe the inode points to a block
that the map still calls free.
The next file can be written
right on top of it.
And the first one is quietly destroyed.

<!-- S49 -->
That's why ext4 keeps a journal.
Before it changes its bookkeeping,
it writes down what it's about to do.
After a crash, it replays only the changes
it had finished writing down,
and marked as complete.
Anything unfinished is ignored.

<!-- S50 -->
And there's a quieter problem.
Sometimes a drive changes a bit
and doesn't tell anyone.

<!-- S51 -->
Ext4 protects its own records
with checksums,
so it can spot damage there.
But the contents of your files?
Those, it simply trusts.

<!-- S52 -->
Some filesystems check both.
And some keep a second copy,
so when one copy is damaged,
they can repair it from the other.
Spotting a problem and fixing it
are not the same thing.

<!-- S53 -->
So every filesystem does the same job:
numbered blocks, a list of names,
and a map of what's free.

<!-- S54 -->
But the choices differ.
Ext4 prepares sixty-one million records
before you save a thing.
NTFS, on Windows, keeps its records
in one big table that grows as you go.

<!-- S55 -->
And Btrfs doesn't prepare
a fixed table of inodes in advance.
It creates them as files arrive.
And normally, it doesn't overwrite
data in place.
It writes a new copy,
and only then lets go of the old one.

<!-- S56 -->
By default, it also checksums your files,
so it can tell when they've been damaged.

<!-- S57 -->
And because the old copy
isn't overwritten,
a snapshot can keep it alive.
That changes the answer
to almost every question in this video:
what a crash does,
what deleting means,
and even what a copy is.

<!-- S58 -->
That's where the next video begins.

<!-- S59 -->
So here's a question for you.
Should a filesystem just store your files,
or should it protect them too?
Let me know in the comments.
