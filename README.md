# Password Manager
**Pass.py**  A Command Line Tool for fast and safely managing account credentials.

---
## Prerequisites:
Make sure to have python 3.6 or higher

## motivation: 
Strong passwords are an obvious component in online security. Most hacks ocour simplly by cracking user passwords, eigher by password leaks (most people re-use passwords from different sites) or by brutforce attacks. 
For me, its not fesable to remember a series of unrelated strong passwords. A password manager solves this problem, it can safly store al my password witch are encrypted with one single password (master password). 
I enjoy working with a simple commandline tool, sinds i feel it is faster and easyer. 


## Features:

* Simple setup: Create a master password / passphrase and that's it (pick a strong one).
* Command Line controlled: In the hands of experience user quicker than most password managers.  
* Strong Encryption: AES 128, PBKDF2 key hardening, resistant to brute forcing and rainbow tables.
* Diceware Passphrase generation: Create strong, random but easy to remember passwords.
* Backup: Plain text backup option (uses with caution).
* File encryption: Secure a file by encrypting it, using the same master password.
---

## setup:
Place the following files in the same directory:
* pass.py
* diceware.py
* diceware_list.txt
From this directory you can run command with: python pass.py [-command] [arguments]

**Run the following two commands to get started:** 
Use the setup command to setup your files and master pass. 
```
python pass.py -setup
```
This generates a password_pairs.txt 
*(optional you can now add accounts manually, by following the format name1:pw1-name2:pw2 etc)*

Now encrypt your password_pairs.txt with: 
```
python pass.py -encrypt_file password_pairs.txt
```
Your are setup to use the password manager! 
Run the -help command for more info. 
```
python pass.py -help
```
This will print the "help menu". 

---

## passwords: 
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


## Tips and Recomondations : 

Storing a (plain text) backup on your PC defeats the purpose of having encryption. its best to move it to an USB, cloud or even better just print it and delete the digital copy. 

You can store more than just a (account/password) pair. there is an file encryption option. (it is strongly recommended to make a backup first) 

When picking a master password, try out the password generation command. it runs the diceware algorithm which returns an password of a given amount of words, separated with a given separator. The diceware algorithm creates passwords with high [entropy](https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength), that are still somewhat memorable. 

```
python pass.py -generate_pw 5 -
```
can give an output like:  
*align-elegy-flog-anton-stomp*





