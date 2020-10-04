## password_manager
A Command Line Tool for fast and safely managing account credentials.

---
### Prerequisites:
Make sure to have python 3.6 or higher

## motivation: 
...


## Features:

* Simple setup: Create a master password / passphrase and that's it (pick a strong one).
* Command Line controlled: In the hands of experience user quicker than most password managers.  
* Encryption: Strong encryption, AES 128, PBKDF2 key hardening, resistant to brute forcing and rainbow tables.
* Diceware Passphrase generation: Create strong, random but easy to remember passwords.
* Backup: Plain text backup option (uses with caution).
* File encryption: Secure a file by encrypting it, using the same master password.
---

### setup:
Place the following files in the same directory:
* pass.py
* diceware.py
* diceware_list.txt
From this directory you can run command with: python pass.py [-command] [arguments]


Example:
```
python pass.py -help
```
This will print the "help menu",
use the setup command to setup your files and master pass. 

---

### passwords: 
Having a good master password is very important. 

Three highly recommended resource on passwords and cyber security:
* How to Choose a Password - https://www.youtube.com/watch?v=3NjQ9b3pgIg
* Diceware & Passwords - https://www.youtube.com/watch?v=Pe_3cFuSw1E
* How Password Managers Work -https://www.youtube.com/watch?v=w68BBPDAWr8

In short: pick a password with 10 or more characters, not containing words found in the top 5000 most used words.

## examples:
Store "acount password pair" of facebook: 
```
python pass.py -store fb mypass123
```


Lookup password for facebook: 
```
python pass.py -get fb
```
-> *mypass123*

....
