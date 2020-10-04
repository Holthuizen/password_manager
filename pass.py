#standard:
import os
import base64
import argparse
import diceware
import json 
#non standard libs:
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

save_as = "password_pairs.txt"
password_default_file = "password_pairs.txt"
password_provided = 'password'  # This is input in the form of a string

#create json app_config file for storing, salt, checksum and iterations
def user_setup(path, salt,n):
    if os.path.exists(path): 
        print("already setup an master password, backup your files in plain text befor changing your masterpass, exiting .. ")
        exit()
    
    if not os.path.exists(password_default_file): 
        write_file(password_default_file,"default:password") #create file, and add a example value

    try:
        salt = salt.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        pass
      
    print("create your masterpassword, your masterpassword acts like a key to encrypt/decrypt your data, dont lose it! ")
    masterpass =  input(" \t create your masterpassword >> ")
    try:
        key = generate_key(masterpass)
        key =  key.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        pass  

    checksum = key[0:10]
    config = {}
    config["salt"]= salt 
    config["checksum"] = checksum
    config["iteration_count"] = n 
    with open(path, "w") as outfile:  
        json.dump(config, outfile) 
    

#read app_config.json into dict or exit. call from login()
def load_config(path): 
    # Opening JSON file 
    try:
        with open(path) as json_file: 
            data = json.load(json_file) 
        return data
    except: 
        print('file could not be loaded')
        exit()

#string to dict
def custom_parser(data_string): 
    _data={}
    for value in data_string.split('-'): 
        a,p = value.split(':')
        _data[a]= p 

    return _data


def custom_parser_to_string(data_dict): 
    data_string = str(data_dict)
    return data_string.replace(',','-').replace('{','').replace('}','').replace(' ','').replace("'",'') 


#find value in string 
def get_value(lookup_key, decrypted_data): 
    data_dir = custom_parser(decrypted_data.decode())
    if lookup_key in data_dir:
        return data_dir[lookup_key]
    else: 
        return False

def update_value(lookup_key, decrypted_data, new_value): 
    data_dir = custom_parser(decrypted_data.decode())
    if lookup_key in data_dir:
       data_dir[lookup_key] = new_value
       return data_dir #updated copy, type string
    else: 
        return False
def delete_value(lookup_key, decrypted_data): 
    data_dir = custom_parser(decrypted_data.decode())
    if lookup_key in data_dir:
       del data_dir[lookup_key]
       return data_dir #updated copy, type string
    else: 
        return False


def generate_key(password):
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    base64key = base64.urlsafe_b64encode(kdf.derive(password.encode()))  # Can only use kdf once
    return base64key


def read_file(path): 
        if not os.path.exists(path):
            print("\n error in read_file:  file not found \n")
            exit()
        file = open(path, 'r')  # Open file as read
        contents = file.read()
        file.close()
        return contents

def write_file(path,data):
        try:
            data = data.decode()
        except:
            pass

        file = open(path, 'w')  # Open file as write
        file.write(data)
        file.close()
    
#arguments: tupl of strings, base64key
def encrypt(data,key): 
    try:
        secret = data.encode()
    except: 
        secret = data
    try:
        f = Fernet(key)
        return f.encrypt(secret)
    except:
        print("error try again? ")
        return login()

#argument types: strings, base64key    
def decrypt(encrypted,key):
    
    if len(encrypted) < 1: 
        print("error in decrypt, cannot encrypt less than 1 byte")
        exit()

    try: 
        encrypted = encrypted.encode() #to bytes
    except: 
        pass

    try:
        f = Fernet(key)
        return f.decrypt(encrypted)
    except:
        print("decryption unsuccesfull, likely a incorrect master password")
        exit()


def encrypt_file(path,key): 
    if input("note that you can encrypt a file multiple times, check if the file is in plain text before encrypting it, continue (y/n) ")[0] =='n':
        exit()
    data = read_file(path)
    encrypted = encrypt(data, key)
    write_file(path,encrypted)
    print(f"file {path} encrypted")

def decrypt_file(path,key): 
    data = read_file(path)
    print(f"DECRYPT_FILE: path->{path}, key->{key}, data->{data}")
    decrypted = decrypt(data, key)
    write_file(path,decrypted)
    print(f"file {path} decrypted")


def login():
    #setup 
    config = load_config("app_config.json")

    print("\n by entering your master password you will unlock your stored data")
    masterpass = input("\t ENTER MASTER PASSWORD TO LOGIN >> ")
    key = generate_key(masterpass)

    if key[0:10] == config['checksum'].encode():
        return key
    else: 
        print("master password doesn't match")
        exit()


def output_formatter(title, message): 
    print(f" <{'-'*100}")
    print(f" |{title}  --> {message}"); 
    print(f" {'-'*100}>\n")
#output_formatter("output","hello world")

#user_setup("app_config.json",'salt_',10000)
#print(load_config("app_config.json"))

parser = argparse.ArgumentParser()
#for these examples, use a pre defined password    
parser.add_argument('-setup', action="store_true", help="setup master password (usually a one time action)")

parser.add_argument('-encrypt_file', nargs=1,help="encrypt a file with your master password,expects: filepath")
parser.add_argument('-decrypt_file', nargs=1,help="decrypt a file with your master password,expects: filepath")

parser.add_argument('-store', nargs=2, help="enter account password value")
parser.add_argument('-get', nargs=1, help="enter account name, returns account password")
parser.add_argument('-update', nargs=2, help="enter account name and new password, returns account password value")
parser.add_argument('-delete', nargs=1, help="remove / delete  account name and new password")
parser.add_argument('-create_decrypted_backup', action="store_true", help="create a plain text file with all your account, expects: master password, returns backup file path")

parser.add_argument('-generate_pw', dest='dice', nargs=2, help="generate human readable password, expects: number of words, divider")

#parse
args = parser.parse_args()


if args.setup:  
    user_setup("app_config.json",'salt_',10000)

if args.encrypt_file: 
    key = login()
    encrypt_file(args.encrypt_file[0],key)
    exit()

if args.decrypt_file: 
    key = login()
    decrypt_file(args.decrypt_file[0],key)

if args.store:
    key = login()
    _data = decrypt(read_file(password_default_file), key)
    value = get_value(args.store[0],_data) 
    if value: 
        print("value is already stored, use the update command to change its value")
        print(value)
    else: 
       data = _data.decode() + '-' + args.store[0]+":"+args.store[1]
       edata = encrypt(data,key)
       write_file(password_default_file,edata)
       #print result
       edata = '' #remove 
       key = '' #remove


if args.get:
    key = login()
    _data = decrypt(read_file(password_default_file), key)
    value = get_value(args.get[0],_data) 
    if value: 
        # output
        print(f"login is -> {value}")
    exit()


if args.update:
    key = login()
    decrypted = decrypt(read_file(password_default_file), key)
    
    if decrypted: 
        # update copy of decrypted data into into a dictionary 
        data = update_value( args.update[0] , decrypted, args.update[1])
        #transform dictionary to string, encrypt, overwrite the original data in file
        write_file(password_default_file, encrypt(custom_parser_to_string(data),key) )
        exit()
    else: 
        print("value not found")
    exit()


if args.delete:
    key = login()
    decrypted = decrypt(read_file(password_default_file), key)    
    if decrypted: 
        #parse and modify 
        updated_dict = delete_value(args.delete[0],decrypted)
        updated_string = custom_parser_to_string(updated_dict)
        #encrypt string and overwrite old file
        write_file(password_default_file,encrypt(updated_string,key))
        exit()
    else: 
        print("value not found")


if args.create_decrypted_backup: 
    key = login()
    user_input = input("WARNING, make sure to move the created backup file to a save location (do NOT keep it on this pc), continue? (y/n)  ")
    if user_input[0] == 'y':
        decrypted = decrypt(read_file(password_default_file), key)
        path = "backup_"+save_as
        write_file(path, decrypted)
        print(f'backup file at --> {os.getcwd()}\{path}')
    else:
        print("exiting ..")
        exit()


if args.dice: 
    print(args.dice[0],args.dice[1])
    diceware = diceware.Diceware()
    print(diceware.throw(int(args.dice[0]),args.dice[1]) )


