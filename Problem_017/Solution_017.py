'''
Problem 17:
    
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import time
start_time = time.time()

number_dict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',   
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
}

number_list =[]

for number in range(1,1000):
    if number<21:
        number_string = number_dict[str(number)]
    elif number<100:
        number_string = number_dict[str(number)[0]+str(0)]
        if int(str(number)[1])>0:
            number_string+=('-'+number_dict[str(number)[1]])
    else:
        number_string = number_dict[str(number)[0]] + ' ' + number_dict['100']
        if str(number)[1:]!='00':
            number_string+=' and '
            if int(str(number)[1])>1:
                number_string+=(number_dict[str(number)[1]+str(0)])
            if int(str(number)[1:])<10:
                number_string+=(number_dict[str(number)[2]])
            elif int(str(number)[1:])>9 and int(str(number)[1:])<20:
                number_string+=(number_dict[str(number)[1:]])  
            elif str(number)[2]!='0':
                number_string+=('-'+number_dict[str(number)[2]])
    number_list.append(number_string)
number_list.append('one thousand')

number_of_letters=0

for number in number_list:
    number_of_letters+=len(number.replace(" ","").replace("-",""))
    
print(number_of_letters)    
# calculation time: 0.006009340286254883 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   