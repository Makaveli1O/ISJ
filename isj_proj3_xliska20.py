#!/usr/bin/env python3

import re
# ukol za 2 body
def first_odd_or_even(numbers):
    """Returns 0 if there is the same number of even numbers and odd numbers
       in the input list of ints, or there are only odd or only even numbers.
       Returns the first odd number in the input list if the list has more even
       numbers.
       Returns the first even number in the input list if the list has more odd 
       numbers.

    >>> first_odd_or_even([2,4,2,3,6])
    3
    >>> first_odd_or_even([3,5,4])
    4
    >>> first_odd_or_even([2,4,3,5])
    0
    >>> first_odd_or_even([2,4])
    0
    >>> first_odd_or_even([3])
    0
    """
    i = 0
    oddnum =[]
    evennum = []
    
    if(not len(numbers)):
        return 0
    for i in range (len(numbers)):
        if (numbers[i] % 2 == 0):
            evennum.append(numbers[i])
        else:
            oddnum.append(numbers[i])
    if(len(oddnum) == len(evennum) or len(evennum) == 0 or len(oddnum) == 0):
        return 0
    if(len(oddnum) > len(evennum)):
        return evennum[0]
    else:
        return oddnum[0]
    

# ukol za 3 body
def to_pilot_alpha(word):
    """Returns a list of pilot alpha codes corresponding to the input word

    >>> to_pilot_alpha('Smrz')
    ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """

    pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
   
    pilot_alpha_list = []
    word = word.upper()
    j = 0 
    result = ""
    res = ""
    while j < len(word):
        result = [i for i in pilot_alpha if i.startswith(word[j])]      #cyklus ktorý vráti elemty začínajúce na písmená z premennej 'word'
        for k in result:                                                #list -> string convert
            res = k
        pilot_alpha_list.append(res)
        j+=1
    return pilot_alpha_list
if __name__ == "__main__":
    import doctest
    doctest.testmod()
