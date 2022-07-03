import random
import math

print("\n-------*****--- RSA(Rivest Shamir Adleman) ALGORITHM ---*****-------\n")

def prime_NOs(num=100):
 for i in range(2,num+1):
  for j in range(2,i):
   if i%j==0:
    break
  else:
   lst.append(i)
 
def encrypt_keys(n,phi):
 count=0
 possible_keys=[]
 for e in range(2,phi):
  if gcd(n,e)==1 and gcd(phi,e)==1:
    count+=1
    possible_keys.append(e)
 #print("Total number of generating encryption keys = ", count)
 return possible_keys

def decrypt_keys(phi,e):
 count=0
 possible_keys=[]
 for d in range(phi+1,phi+1000):
  if (d*e) % phi == 1:
   count+=1
   possible_keys.append(d)
 #print("Total number of generating decryption keys = ", count)
 return possible_keys

def gcd(a,b):
 if b==0:
  return a
 return gcd(b,a%b)
 
#p=int(input("Enter value of P: "))
#q=int(input("Enter value of q: "))
lst=[]
prime_NOs()
p=random.choice(lst)
q=random.choice(lst)
n=p*q
phi=(p-1)*(q-1)
ecp=""

e=encrypt_keys(n,phi)

#print("Possible encryption values are ",e)
re=random.choice(e)

d=decrypt_keys(phi,re)

rd=random.choice(d)
#print("Possible decryption values are ",d)


'''
print("p = ", p)
print("q = ",q)
print("n = ",n)
print("phi = ",phi)
print("e = ",re)
print("d = ",rd)
'''

msg=input("Type Your Message Here: ")



for ch in msg:
 c=pow(ord(ch),re) % n                  # Encrypt message character by character
 #print(ch, " = ", ord(ch))
 #print("(encrypt)", ch, " = ",c, " = ", chr(c))
 ecp+=chr(c)
#decrypt_msg=pow(c,rd) % n

print("Original Message = ",msg)
print("Encrypt Message= ",ecp)
#print("After Decryption(pain text) = ",decrypt_msg)





