# Five In A Row

## Prerequisites

You may need to pip install the following packages:
```
flask
requests
numpy
```

### Language:
```
Python 3.7
```

## How To Run
 1) Start the Server application
 2) Start the first Client application
 3) Start the second Client application
 4) Enter user name in Client one.
 5) Enter user name in Client one.
 6) PLAY!
 
## How to leave game
If a player wishes to leave the game at a given time press 
```
Ctrl+C
```

## Future Improvements 
For this challenge I had to spend a lot of time learning how to work with HTTP and REST because we havn't done
much of it in college. If I had more time I would like to fix the following issues:
```
1) The game does not recognise when a player inputs their token in a full or invalid column,
causing the players turn to be void and the opposing player then gets to make their move.

2) The game doesn't recognise that a player has left the game if they close their client window. 
Instead a user must use Ctrl + C

3) The game doesn't recognise when a player inputs a value other than 1 or 2 when selecting a token
color.
```