#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 11. Write a python program to find the factorial of a number.


# In[2]:


num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial) 


# In[ ]:


# 12. Write a python program to find whether a number is prime or composite.


# In[3]:


num = int(input("Enter the number: "))
if num>1:
    for i in range(2,num):
        if (num%i) == 0:
            print(num, " is a composite number")
            print(i, "times", num//i,"is", num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is a composite number")


# In[ ]:


# 13. Write a python program to check whether a given string is palindrome or not.


# In[1]:


my_str = 'aibohPhobia'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")


# In[ ]:


# 14. Write a Python program to get the third side of right-angled triangle from two given sides.


# In[5]:


from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )


# In[ ]:


# 15. Write a python program to print the frequency of each of the characters present in a given string.


# In[6]:


string=input("Enter the string: ")
str1=list(string)
strlist=[]

for j in str1:
    if j not in strlist:
       strlist.append(j)
       count=0
        
       for i in range(len(str1)):
         if j==str1[i]:
           count+=1
       print("{},{}".format(j,count))


# In[ ]:




