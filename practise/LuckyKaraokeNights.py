# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:18:28 2019

@author: Sangye Tenphel
"""
def convert(money):
    return float(money.strip('$'))

def promotionaLoss(table_data, lucky_no):
    value = table_data.values()
    max_val = max(value)
    total_discount = convert(max_val[1])
    total_discount += 0.5 * convert(table_data[lucky_no][1])
    
    for key, value in table_data.items():
        if key != lucky_no and key % lucky_no == 0:
            total_discount += 0.25 * convert(table_data[key][1])
            
    return '$' + str(round(total_discount, 2))
    
d = { 1: ('35dB', '$72.80'), 2: ('45dB', '$27.35'), 3: ('60dB', '$102.15'), 4: ('40dB', '$32.35'), 5: ('85dB', '$17.25'), 7: ('62dB', '$39.11'), 9: ('72dB', '$18.24'), 10: ('37dB', '$103.15'), 11: ('89dB', '$62.55'), 17: ('81dB', '$16.75'), 15: ('78dB', '$92.73'), 25: ('69dB', '$24.24'), 16: ('23dB', '$97.43'), 18: ('46dB', '$5.24'), 12: ('67dB', '$38.23'), 23: ('79dB', '$88.49'), 27: ('83dB', '$64.78'), 34: ('87dB', '$56.91'), 33: ('68dB', '$22.49'), 24: ('55dB', '$18.00'), 35: ('66dB', '$85.23'), 30: ('74dB', '$9.20'), 26: ('59dB', '$76.82'), 29: ('44dB', '$47.90'), 6: ('49dB', '$81.98'), 37: ('88dB', '$117.73'), 42: ('61dB', '$255.89'), 8: ('29dB', '$30.00'), 52: ('75dB', '$14.28'), 51: ('63dB', '$36.49') }    
lucky_no = 4
#d = { 1: ('75dB', '$42.30'), 2: ('60dB', '$23.40'), 4: ('55dB', '$45.65'), 5: ('62dB', '$33.25') }
print(promotionaLoss(d, lucky_no))