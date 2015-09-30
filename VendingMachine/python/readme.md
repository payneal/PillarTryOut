# Try again

Good:
Unit test coverage against individual classes
Multiple classes, attempted OO design


Bad:
minor spelling mistakes
inconsistent formatting
lots of single-line comments in the tests (these indicate that helper methods or separate tests could be extracted)
invalid test for return coins test (inserting the coin ‘half’ results in .50 being added to the returnCoinsAmount)
test variables are not descriptive (test, test2, test3)
large tests, “state train” (I do this, and then this, and then this, and then assert)
loops inside of the tests
duplicate magic strings instead of constants
extremely large methods
lots of duplicate logic
high degree of cyclic complexity
lots of magic numbers
commented out code


