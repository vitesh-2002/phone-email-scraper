# phone-email-scrapper


This progam essentially searches for, detects, and scraps any phone numbers(program the format of the number according to the country) and email addresses.
You can use this program in two ways:

Option 1.) If the text that you are trying to scan and scrap phone numbers from is in a seperate file, save that file in to your current working directory,
then use the first block of code to set up a file object and allow the phone and email scrapper to read that file
All you need to do for this is edit the code so that instead of "phonesandemails.txt" it should contain the name of the file you have saved on your computer. 

Option 2.) If you would just like to copy and paste the text, then uncomment out the second block of code and comment out the first block of code.
This second block of code uses the pyperclip module, which allows python to automatically sense and store any text that you copy or click Ctrl+C on in your computer
Once you have copied the data, you should be able to simply run the code and all the phone numbers and emails will be printed out in an assorted manner.
