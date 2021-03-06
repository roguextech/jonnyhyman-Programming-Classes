'''

This is a deep dive into FUNCTIONS


What is a function?

    A function is a bunch of commands bundled into a group

How do you write a function?

    Look below!

CHALLENGES: (in order of HEAT = difficulty)

    Siberian Winter:  Change the link of the Philly function

    Canada in Spring:  Make the link an input to Philly, not a constant

    Spring in California:  Convert Antonia's inputs to named inputs

    Summer in California:  Write a new function which adds two numbers

    Rocket Engine:  Convert these functions into a CLASS

'''

import webbrowser

def Franko():
    print('Hello from Franko, the simple function')

def Philly():
    print('Hello from Philly, the funky phunction')
    print('You see, you can do a lot of stuff in one function')

    print('Like taking the square root of 1,245 to the power of pi!')

    import math

    sqrt1245_pi = math.sqrt(1245)**math.pi
    print('Which is exactly... ', sqrt1245_pi)

    print('You can even do fun stuff in here... Check this out...')
    webbrowser.open('http://www.jonnyhyman.com')

def Antonia(argument1, argument2, TheyDontAllNeedToSayArgumentThough):
    print('Hello from Antonia, the fun function with fun inputs')
    print('These are my arguments:')
    print(argument1)
    print(argument2)
    print(TheyDontAllNeedToSayArgumentThough)

    webbrowser.open('https://media.giphy.com/media/R8n7YlPHe34dy/giphy.gif')

def Kevin(named_argument = 'Wut', other_one = 'Hah', herp = 'derp' ):
    print('Hello from Kevin the function with NAMED inputs...')
    print('My inputs were...', named_argument, other_one, herp)


#input(" ----> Notice how none of the functions run until you call them"
#        "  //// [ENTER] to continue")

print('_______________')  # some space to be able to read easier

Antonia()
