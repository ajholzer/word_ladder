#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    s = []
    q = []
    s.append(start_word)
    q.append(s)
    stack_copy = []
    while len(q) != 0:
        q.pop()
        for word in dictionary_file:
            if _adjacent(word, s.pop()):
                if word == end_word:
                    stack.append(word) 
                    return stack
            stack_copy = s
            stack_copy.append(word)
        q.append(stack_copy)
        del dictionary_file[word]

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    mistakesAllowed = 1
    if word1 == word2:
        return False
    if len(word1) != len(word2):
        return False
    if(len(word1) == len(word2)):
          for i in range(len(word1)):
             if word1[i] != word2[i]:  
                mistakesAllowed-= 1
                if(mistakesAllowed < 0):  
                    return False
          return True
