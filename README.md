#Shillscript (also known as Powershill)

Hillary Clinton Programming Language :)

##Installation and Usage

###Prerequisites
- Python 3 (I have no current plans to port this to Python 2.7, but seeing as the code is by majority inefficient/unoptimized it should be easy to port if you intend to do so. I would be happy to merge pull requests that provide 2.7 functionality.) This comes preinstalled (i think) on Macs and Linux machines, and for Windows you can google.
- Internet Connection (if you want the smtp server to actually work)
- A text editor of your choice to create files with a choosable extension (Notepad and TextEdit both support this, but I would recommend Visual Studio Code as a personal favorite. There's also Vi, Vim, Nano, Atom)
- Know how to use Terminal or Command Prompt, or your equivalent (I haven't tested this on the new Linux subshell on Windows 10, but I imagine if you got python to run it would work on that as well)

###Installation
To install, you just need clinton.py in the same directory as your files or in the working path. It needs the ability to read and write to files so you may need to chmod if you have extensive security.
There are other files provided here. 
- backup.py in case you run
```bash
python clinton.py clinton.py
```
Which could have very disastrous results.
- helloworld.benghazi for sample code
- backup.benghazi if you accidentally delete helloworld.benghazi
- run.py is an experimental script that runs your code then starts up the email server. Same syntax as clinton.py for usage.

###Usage
To run code:
```
python clinton.py filename.benghazi
```
Where filename.benghazi is your script. It's that simple!


##Rules
###Basic rules:
- All filenames must end in .benghazi
- All scripts must start by declaring itself as a female and saying it will make history
```
I will make history as the first female president
```

###Output
To print statements, you must first
```
teleprompter prompt "hello world"
hillary read from teleprompter
```

###Email
You can email in this format
```
**email message $ to_address@example.com #Subject here
```
And run this command in a separate terminal window:
```
python email_server_init.py
```
Then run your code in a separate terminal window:
```
python clinton.py helloworld.benghazi
```
It (probably) won't actually send the email but it shows up in the email server window.

###Replacements
To make up for the fact that if/then isn't supported you can use
```
hillary repeat
```
to repeat the last command. You can't do this more than once because Madame Secretary only repeats herself once.

###Exclusions
Variables are not supported because you're not allowed to save anything.
Objects are not supported because Madame Secretary only takes money from Wall Street.
if/then are not supported because Madame Secretary doesn't need to consider anything or anyone else when making decisions.
