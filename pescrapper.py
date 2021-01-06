import re
phone = re.compile(r''' (((\(\d\d\d\))|(\d\d\d))  #area code in the phone number might be in paranthesis so you need to account for that
-
(\d\d\d-\d\d\d\d))

''',re.VERBOSE)
print('\nphone numbers:')
#use findall command to search a string of text and numbers or just directly enter string into the paramters
#this is the string the command will be detecting and scrapping phone numbers from
phonenumbers = phone.findall('you can call or text me at 919-123-4567, you can contact my client at 323-123-4567')
#use lists and for loop to splice the full number from the findall method's resutls
allnumbers = []
for i in phonenumbers:
    allnumbers.append(i[0])

print(allnumbers)

email = re.compile(r'''
\w+                     
@
\w+[.com|.net|.org]+                #any email provider can be detected (gmail, yahoo, etc.) and need to program in a class to account for .com, .net, etc.

''', re.VERBOSE)
print('\nemail addresses: ')
#return emails by just printing out the findall command
print(email.findall('their emails include: rando@something.com, hello@random.net, and goodevening@sunnyfuture.org'))
