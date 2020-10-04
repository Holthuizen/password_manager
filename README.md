## password_manager
A Command Line Tool, for storing account credentials. 

---
### Prerequisites
Make sure to have python 3.6 or higher

## Features

* Simple setup, Create a master password / passphrase and that's it (pick a strong one).
* Command Line controlled, in the hands of experience user quicker than most password managers.  
* Encryption: AES 128, PBKDF2 key hardening. Strong encryption, resistant to brute forcing and rainbow tables
* Diceware random Passphrase generation. Create strong but easy to remember passwords
* Backup: a plain text backup option (uses with caution)
* File encryption, secure a file by encrypting it, using the same master password.



### setup:
Place the folowing files in the same direcory: 
* pass.py
* diceware.py
* diceware_list.txt
From this directory you can run command with python pass.y -command arguments
example:
```
python pass.py -help
```
This will print the "help menue",
use the setup command to setup your files.

--- 
