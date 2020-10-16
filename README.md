# Password Manager
**Pass.py**  A Command Line Tool for fast and safe credentials storage.

---
## Prerequisites:
Make sure to have python 3.6 or higher
*Python can be directly installed from the windows store.*

pass.py uses cryptography, install via pip with the following command: 

```
pip install cryptography
```

## Motivation: 
Strong passwords are an obvious component in online security. Most hacks occur simply by cracking user passwords, either by password leaks (most people re-use passwords for different sites) or by bruteforce attacks. 
For me, it's not feasable to remember a series of unrelated and strong passwords. A password manager solves this problem. It can safely store all my passwords which are encrypted with one single password (master password). 
I enjoy working with a simple commandline tool, since I feel it is faster and easier. 

I was mainly motivated by the following Computerphile videos: 

https://www.youtube.com/watch?v=w68BBPDAWr8

https://www.youtube.com/watch?v=7U-RbOKanYs

## Features:

* Simple setup: Create a master password / passphrase and that's it (pick a strong one).
* Command Line controlled: For experienced users, this is quicker to work with than most password managers.  
* Strong Encryption: AES 128, PBKDF2 key hardening, resistant to brute forcing and rainbow tables.
* Diceware Passphrase generation: Create strong, random but easy to remember passwords.
* Backup: Plain text backup option (use with caution).
* File encryption: Secure a file by encrypting it, using the same master password.
---

## Setup:
Place the following files in the same directory:
* pass.py
* diceware.py
* diceware_list.txt
From this directory you can run commands with: python pass.py [-command] [arguments]

**Run the following two commands to get started:** 

Run the setup command to setup your files and master pass. 
Information can be found below on how to pick a strong master password.
```
python pass.py -setup
```
This generates a credentials.txt file 

*(optionally, you can now add multiple credentials manually, by following this format for pairs of names and passwords name1:pw1-name2:pw2-name3:pw3 etc)*

Now encrypt your credentials.txt with: 
```
python pass.py -encrypt-file credentials.txt
```
Your are all set up to use the password manager! 
This means you can now add credentials to your manager to store them safely and retrieve them later.
Run the -help command for more info. 
```
python pass.py -h
```
This will print the "help menu". 

---

### Example1:
Store your credentials for Facebook: 
```
python pass.py --store fb mypass123
```
or
```
python pass.py -set fb mypass123
```
'fb' is the name of your choice for retrieving this password later, as shown below in the get command. This means you can store full credentials (not only password but alos username) simply by storing both.

Lookup password for facebook: 
```
python pass.py -get fb
```
-> *mypass123*

### Example2:

Storing full credentials:
```
python pass.py --store digidusername johndoe
python pass.py --store digidpassword mypass456
```

## Passwords: 
Having a good master password is very important. 

Three highly recommended resources on passwords and cyber security:
* How to Choose a Password - https://www.youtube.com/watch?v=3NjQ9b3pgIg
* Diceware & Passwords - https://www.youtube.com/watch?v=Pe_3cFuSw1E
* How Password Managers Work -https://www.youtube.com/watch?v=w68BBPDAWr8

In short: pick a password with 10 or more characters, not containing words found in the top 5000 most used words.


## Tips and Recommendations: 

Storing a (plain text) backup on your PC defeats the purpose of having encryption. its best to move it to an USB, cloud or even better just print it and delete the digital copy. 
```
python pass.py -backup
```
You can store more than just a (account/password) pair. there is an file encryption option. (it is strongly recommended to make a backup first) 

When picking a master password, try out the password generation command. It runs the diceware algorithm which returns a password of a given amount of words, separated with a given separator. The diceware algorithm creates passwords with high [entropy](https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength), that are still somewhat memorable. 

```
python pass.py -generate-pw 5 -
```
can give an output like:  
*align-elegy-flog-anton-stomp*




