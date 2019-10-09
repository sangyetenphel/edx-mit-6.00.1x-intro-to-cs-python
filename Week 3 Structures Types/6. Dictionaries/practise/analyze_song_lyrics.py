# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:36:17 2019

@author: Sangye Tenphel
"""

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

lyrics = """There goes my heart beating
'Cause you are the reason
I'm losing my sleep
Please come back now
There goes my mind racing
And you are the reason
That I'm still breathing
I'm hopeless now
I'd climb every mountain
And swim every ocean
Just to be with you
And fix what I've broken
Oh, 'cause I need you to see
That you are the reason
There goes my hand shaking
And you are the reason
My heart keeps bleeding
I need you now
If I could turn back the clock
I'd make sure the light defeated the dark
I'd spend every hour, of every day
Keeping you safe
And I'd climb every mountain
And swim every ocean
Just to be with you
And fix what I've broken
Oh, 'cause I need you to see
That you are the reason, oh
(I don't wanna fight no more)
(I don't wanna hurt no more)
(I don't wanna cry no more)
(Come back, I need you to hold me closer now)
You are the reason, oh
(Just a little closer now)
(Come a little closer now)
(I need you to hold me tonight)
I'd climb every mountain
And swim every ocean
Just to be with you
And fix what I've broken
'Cause I need you to see
That you are the reason"""

lyrics_list = lyrics.split()
song = lyrics_to_frequencies(lyrics_list)

def most_common_words(freq):
    values = freq.values()
    most = max(values)
    words = []
    for word in freq:
        if freq[word] == most:
            words.append(word)
    return (words, most)

(w, m) = most_common_words(song)
    
def words_often(freq, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freq)
        if temp[1] >= minTimes:
            result.append(temp)
            for word in temp[0]:
                del(freq[word])
        else:
            done = True
    return result

# =============================================================================
# # Checking what happens if we just run a loop through the values
# # and if that value is greater than minTimes, append the key to the result?
    
# def practise(freq, minTimes):
#     values = freq.values()
#     result = []
#     for key, value in freq.items():
#         if value >= minTimes:
#             result.append(key)
#     return result 
# Output: In [193]:practise(song, 6)
#         Out[193]: ['you', 'are', 'the', 'And', 'every', 'to', 'I', 'need']
# =============================================================================
        
        