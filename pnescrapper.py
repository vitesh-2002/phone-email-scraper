import re
import pyperclip
phone = re.compile(r''' (((\(\d\d\d\))|(\d\d\d))  #area code in the phone number might be in paranthesis so you need to account for that
-
(\d\d\d-\d\d\d\d))

''',re.VERBOSE)

email = re.compile(r'''
\w+                     
@
\w+[.com|.net|.org]+                #any email provider can be detected (gmail, yahoo, etc.) and need to program in a class to account for .com, .net, etc.

''', re.VERBOSE)

file = open("phonesandemails.txt", "r")
if file.mode == "r":
    doc = file.read()
    phonenumbers = phone.findall(doc)
    emailaddresses = email.findall(doc)

allnumbers = []
for i in phonenumbers:
    allnumbers.append(i[0])

numbers_emails = '\n'.join(allnumbers) + '\n' + '\n'.join(emailaddresses)
print(numbers_emails)


'''
this is the code you'll want to use if you're planning on copying and pasting the information to be scrapped
just copy all the text and it will be automatically stored by the pyperclip module
'''

#use pyperclip module so that whatever text you have copied will be sensed by python
text=pyperclip.paste()
#use findall command to search through the text and detect phone numbers and emails
phonenumbers = phone.findall(text)
emailaddresses = email.findall(text)
#create a list to add all the phone numbers in to print out
allnumbers = []
for i in phonenumbers:
    allnumbers.append(i[0])

#return the phone numbers and emails detected

numbers_emails = '\n'.join(allnumbers) + '\n' + '\n'.join(emailaddresses)
print(numbers_emails)
pyperclip.copy(numbers_emails)
