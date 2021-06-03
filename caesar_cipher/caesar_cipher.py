def encrypt(str,key):
    new_str='0'
    for i in str :
        print(f"old : {ord(i)}")
        print(f"new :  {((((ord(i) + key))+64)%90)}")
        new_str =new_str+chr(((ord(i) + key)+64)%90)
    return new_str


print(encrypt("ABCDZZZ",3))














