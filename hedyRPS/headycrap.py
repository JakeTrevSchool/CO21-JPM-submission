print 'Welcome to your own rock scissors paper!'
options is rock, paper, scissors
computer is options at random
user is ask 'What do you choose?'

print 'you chose: ' user
print 'computer chose: ' computer
if user is computer print 'tie' else print 'no tie'

if user is rock and computer is scissors print 'you win!'
if user is rock and computer is paper print 'computer wins'
if user is scissors and computer is paper print 'you win!'
if user is scissors and computer is rock print 'computer wins'
if user is paper and computer is rock print 'you win!'
if user is paper and computer is scissors print 'computer wins'

