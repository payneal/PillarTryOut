# Categorize New Member

## Instructions
contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

### Example Input
* [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

### Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.
* ["Open", "Open", "Senior", "Open", "Open", "Senior"]

### Test Cases
* [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]] =>  ["Open", "Open", "Senior", "Open", "Open", "Senior"] 
* [[45, 12],[55,21],[19, -2],[104, 20]] => ['Open', 'Senior', 'Open', 'Senior']
* [[3, 12],[55,1],[91, -2],[54, 23]] => ['Open', 'Open', 'Open', 'Open']
* [[59, 12],[55,-1],[12, -2],[12, 12]] => ['Senior', 'Open', 'Open', 'Open']
