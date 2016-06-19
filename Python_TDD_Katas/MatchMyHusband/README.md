# Match My Husband 

### Background
It is 2050 and romance has long gone, relationships exist solely for practicality.

MatchMyHusband is a website that matches busy working women with perfect house husbands. You have been employed by MatchMyHusband to write a function that determines who matches!!

The rules are... a match occurs providing the husband's "usefulness" rating is greater than or equal to the woman's "needs".

The husband's "usefulness" is the SUM of his cooking, cleaning and childcare abilities and takes the form of an array .

usefulness example --> [15, 26, 19]   (15 + 26 + 19) = 60

Every woman that signs up, begins with a "needs" rating of 100. However, it's realised that the longer women wait for their husbands, the more disatisfied they become with our service. They also become less picky, therefore their needs are subject to exponential decay of 15% per month. https://en.wikipedia.org/wiki/Exponential_decay

Given the number of months since sign up, write a function that returns "Match!" if the husband is useful enough, or "No match!" if he's not.:


### Examples
Test.describe("Basic tests")
Test.assert_equals(match([15,24,12], 4), "No match!")
Test.assert_equals(match([26,23,19], 3), "Match!")
Test.assert_equals(match([11,25,36], 1), "No match!")
Test.assert_equals(match([22,9,24], 5), "Match!")
Test.assert_equals(match([8,11,4], 10), "Match!")
Test.assert_equals(match([17,31,21], 2), "No match!")
Test.assert_equals(match([34,25,36], 1), "Match!")
Test.assert_equals(match([35,35,29], 0), "No match!")
Test.assert_equals(match([35,35,30], 0), "Match!")
Test.assert_equals(match([35,35,31], 0), "Match!")


