>>>>> What does it do? <<<<<<

Goes to Tinder.com, makes as much likes, as you have, starts dialogs with mutually liked persons, holds dialogs using specified pattern

>>>>> Install <<<<<<

You need to have: python >= 3.6, chrome, chrome webdriver (ChromeDriver)
Installation:
run install.bat
or do things manually from cmd:
python setup.py install
python setup.py clean

The meaning of installation process is to get all python dependencies. You can get them by means of PIP if you want. Then you do not need to run setup.py

>>>>> Set up <<<<<<

In TinderBot/settings.csv:
set your phone, phone code
headless regime doesn't work, always leave it 0
timeout - time before throwing timeout exception (adjust depending on your connection speed)
waitTime - minimum time to wait until JS rendering is done (adjust depending on your connection speed)
set your path to chrome webdriver

In TinderBot/SpamScript.csv:
write your pattern of dialog (or use that is already there)
New line means wait interlocutor answer.
Delimiter means do not wait answer, but write next message in separate message-bubble. This is needed in order to avoid large walls texts in one message that may look suspecious to your interlocutor.
Example of pattern:
Hi!
Nice to meet you.|Wanna go out?
This script will write "Hi" to every mutual liked person, then wait there answer, then write "Nice to meet you." and "Wanna go out?" in separate messages.

ATTENTION!!!
Do not chenge encoding or extension of settings and pattern-file. Encoding = UTF-8-BOM.!!! Better don't use windows standart pad - it can change encoding without notifying.

>>>>> Run <<<<<<

bot.bat
or in cmd
python TinderBot\main.py

ATTENTION!
Enter your sms-code in programm window, not in browser