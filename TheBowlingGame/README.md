# Good Enough

Good
-----
- Small, focused tests
- descriptive test names
- OO, Domain-driven design
- Small, focused methods

Neutral
-------
- "Mostly" test-driven, however I do see that quite a bit of functionality was added with only 1 test.  Overall it is light on tests


Not so good
-----------
- misspelling of "spare" (but I like "spear" much more, it makes bowling more exciting :-) )
- method naming; using "4" in place of the word "for"
- returning a string in an exception case instead of throwing an exception
- misnamed variables ("number" in moveToNextRollOrReset)


# Scoring Bowling

The game consists of 10 frames as shown above.  In each frame the player has
two opportunities to knock down 10 pins.  The score for the frame is the total
number of pins knocked down, plus bonuses for strikes and spares.

A spare is when the player knocks down all 10 pins in two tries.  The bonus for
that frame is the number of pins knocked down by the next roll.  So in frame 3
above, the score is 10 (the total number knocked down) plus a bonus of 5 (the
number of pins knocked down on the next roll.)

A strike is when the player knocks down all 10 pins on his first try.  The bonus
for that frame is the value of the next two balls rolled.

In the tenth frame a player who rolls a spare or strike is allowed to roll the extra
balls to complete the frame.  However no more than three balls can be rolled in
tenth frame.


# The Requirements

Write a class named “Game” that has two methods

roll(pins : int) is called each time the player rolls a ball.  The argument is the number of pins knocked down.

score() : int is called only at the very end of the game.  It returns the total score for that game.


