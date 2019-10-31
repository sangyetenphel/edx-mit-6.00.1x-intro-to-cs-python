# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:21:48 2019

@author: Sangye Tenphel
"""
import string
class PHPGoAway(object):
    def __init__(self, key):
        self.key = key  
        self.alpha = string.ascii_lowercase
    
    def setKey(self, key):
        """
        input: only lower space ascii characters and no punctuations
        update the key
        """
        self.key = key
        
    def build_shift(self, msg):
       
        i, j = 0, 0      # start index of i at len of key  
        global_key = ''
        while len(global_key) < len(msg):
            if msg[i] == ' ':
                global_key += ' '
                i += 1
            else:
                if j < len(self.key):
                    global_key += self.key[j]
                    i += 1
                    j += 1
                else:
                    j = 0
        return global_key
            
    def forLove(self, decryp_msg):
        '''
        input: a message
        returns: the encrypted message
        '''
        global_key = self.build_shift(decryp_msg)
        alpha = self.alpha
        encryp_msg = ''
        for i in range(len(decryp_msg)):
            if decryp_msg[i] == ' ':
                encryp_msg += ' '
            else:
                encryp_idx = (alpha.index(decryp_msg[i]) + alpha.index(global_key[i])) % 26
                encryp_msg += alpha[encryp_idx]
        
        return encryp_msg
        
    def fromLove(self, encryp_msg):
        '''
        input: a encrypted message
        returns : decrypted message
        '''
        global_key = self.build_shift(encryp_msg)
        alpha = self.alpha
        decryp_msg = ''
        for i in range(len(encryp_msg)):
            if encryp_msg[i] == ' ':
                decryp_msg += ' '
            else:
                decryp_idx = alpha.index(encryp_msg[i]) - alpha.index(global_key[i])
                decryp_msg += alpha[decryp_idx]
                
        return decryp_msg
        
        

        