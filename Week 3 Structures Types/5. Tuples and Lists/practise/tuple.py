# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:48:59 2019

@author: Sangye Tenphel
"""
def get_data(aTuple):
    num = ()
    uniq_words = ()
    for t in aTuple:
        num = num + (t[0],)
        if t[1] not in uniq_words:
            uniq_words += (t[1],)
            
    lowest = min(num)
    highest = max(num)
    unique = len(uniq_words)
    
    return (lowest, highest, unique)
        
        
(small, large, words) = get_data(((1, 'mine'),
                                 (3, 'yours'),
                                 (5, 'ours'),
                                 (7, 'mine')))

