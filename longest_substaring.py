s = 'asdfasuykgffasglaguagfwegf'
old_substr = ''
for i in range(len(s)-1):
    new_substr = s[i]
    while s[i] <= s[i + 1]:
        new_substr += s[i + 1]
        i += 1  
        if i == (len(s) - 1):
            break
    if len(new_substr) > len(old_substr):
        old_substr = new_substr    
print("Longest substring in alphabetical order is:", old_substr)
