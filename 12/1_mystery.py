import random
from numbers import Number

count = 0
score = 0
limit = input("Please enter a positive number: ")
while score < int(limit):
  spinner = random.randint(1, 4)
  if spinner == 1:
    score = score + 1
  elif spinner == 2:
    score = score + 2
  elif spinner == 3:
    score = score + -1
  count = score + 1
print(score)
print(count)



# This code will prompt the user for a number, and then continually generate a random number between 1 and 4, accumulating a score until the value entered by the user is reached. The score is modified based on the random number generated, with a 1 incrementing the score by 1, a 2 incrementing the score by 2, and a 3 derementing the score (a 4 does nothing). At the end it will print the score and the number of times a random number was generated in order to achieve the score.