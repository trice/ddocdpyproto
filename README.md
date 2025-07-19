# The Prototype Project for DDO CD User Interface 
The DDO CD or Dungeons & Dragons Online Character Designer
is a project I plan to write in C++, but I also have other
things in process like Boot.Dev courses and work and family.

Speaking of Boot.dev, this project is my Boot.dev personal
project. Talk about killing two birds with one stone. I get 
to prototype the user interface in Python wxWidgets and complete
a project.

## Running it 
To be able to run the project you either need to have wxPython
installed or set up your venv using the following:

```
python3 -m venv .venv
pip install wxPython
source .venv/bin/activate
python3 ddocdpy.py
```
## The Completed Prototype
Did I mention this is a prototype. I wanted to get an idea of
the formulas, techniques, data structures, etc. that I would
need to pull off something like this. It turned out there were
many interesting problems to solve.

## Dynamic Ability Picking
I always wanted picking abilitity scores to be efficient. Other
character planners and builders have tried to emulate the in game
spinner controls.

Initially I wanted to have just text boxes. You
just type the score you want and deductions are made from the build
points. It turns out that is super difficult to implement. For example
when do you calculate? Do you do some silly thing like in JS where you
handle on-blur? Does wxPython support that?

Then I thought of wxChoice. It is a combo box/dropdown control and that
seemed really great. The player can choose the precise score they want.
Even more important I only have to deal with a choice event as the
selection is made. More on that later since that poses a new problem.
Anyway, I really like the wxChoice and it lets me calculate the remaining
build points and then I can populate each unused ability wxChoice with
the new set of possibilities seemlessy. That way min/max is very easy.

Now a word about the problem I mentioned. How to give build points back
if you change your mind. Well, I'm sure it isn't terrible, but that is
a problem to solve when I find some time to work on the real project.
For now I'm not going to solve that. I think I've got enough information
from this prototype to see that wxWidgets can work.

## I'm no UI/UX expert
Laugh if you want. The UI is not anything to brag about. I'm a backend
type person. UI makes everything slower lol. I'm sure I'll be making
improvements if/when I start the real project.

## Far far far from complete
To prevent this project from going on past the 80+ hours I spent on it,
I had to limit to a 28pt build, Human only and the core set of classes
that DDO has to offer.

You're probably asking why did it take 80 hours? I didn't know anything
about wxPython. I'd heard of wxWidgets but never used it either. So I had
to learn how to use the wxFormBuilder. It is a nice application but talk
about a learning curve. It was a life saver though becaues hand coding this
interface would have been a mess. With that said, I'm thinking and wondering
if just having wxFormBuilder generate the code is a better trade off. It
is nice to have something you can load it that defines the layout and such,
but you also have to still go capture all the controls into class members so
I don't know.

Then there was scraping and cleaning and positioning all the class descriptions.
That was a tricky problem to solve. wxWidgets and wxPython seem to have painting
problems. It's a lot like old VB sometimes where you'd have to for a repaint after
dynamically changing content. Also figuring out wrapping was really tricky. That
took probably four hours of mucking around to get right.

## The output
The character sheet is saved to a file called `new_<Class_Name>.txt` and then
you end up with something like this:

```
============================================================
Class: Artificer
Experience: 0XP
Hit Points: 10
============================================================
Equipment: Staff, Rags, A head full of hopes and dreams
============================================================
Ability Scores:
    STR:  8 -1 
    DEX: 14 +2 
    CON: 14 +2 
    INT: 16 +3 
    WIS:  8 -1 
    CHA: 14 +2 
============================================================
```

## The End
I'm not implementing New Character. It's far faster to Ctrl+Q and start over. The
app runs snappy enough. I've spent a ton of time on this and want to complete this
stage of the lifetime of this experiment and personal project for boot.dev.
