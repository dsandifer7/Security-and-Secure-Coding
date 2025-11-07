#caesars cypher

alphabets = 'abcdefghijklmnopqrstuvwxyz'
shift = 4

rearranged = alphabets[shift:] + alphabets[:shift]
print(rearranged)