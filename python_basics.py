# # # word1="I LOve "
# # # word2="python";
# # # sentence=word1+word2;
# # # print(len(word1+word2))
# # # print(sentence);
# # # print(word1[0]);
# # # for ch in word1:
# # #     print(ch)

# # # Format Function 

# # a=5
# # b=6
# # sum=a+b
# # print("sum is {}".format(sum))
# # print("sum of {} & {} ={}".format(a,b,sum))

# # #Index_base_formatting

# # print("sum of {1} & {0} is equal to {2}".format(a,b,sum))

# # #variables in formattig

# # print("{a}value of {a} and {b} is equal to ".format(a=5,b=6))

# # #f string

# # print(f"sum of {a} and {b} is equal to {a+b}")

# #LISTS 

# # nums=[1,2,3,10,4]
# # x=10
# # indx=0
# # for val in nums:
# #  if(val==x):
# #   print(f"{x} found at indx={indx}")
# #   break
# #  indx+=1

# # TUPLES 

# # tup=(3,4,5,8,5)
# # print(tup)
# # print(type(tup))
# # print(len(tup))
# # sum=0
# # for val in tup:
# #     sum+=val
  
# # print(sum) 
# # print(tup.index(5))
# # print(tup.count(5))

# #DICTIONARY

# # info={
# #     "name":"AHMAD",
# #     "marks":45,
# #     "subjects":["math","science"] 
# # }
# # print(info)
# # print(type(info))
# # print(info["name"])
# # info["marks"]=50
# # print(info["marks"])
# # print(info.keys())
# # print(info.values())
# # dict_keys=list(info.keys())
# # print(dict_keys)
# # print(type(dict_keys))
# # print(info.get("marks2"))
# # print(info.items())
# # info.update({
# #     "city":"Pattoki"
# # })
# # print(info)

# # Sets
# # s={1,2,3,4,5,6}
# # empty_set=set()

# # print(type(empty_set))
# # s.add(9)
# # s.remove(5)
# # s.pop()
# # print(s)
# # s1={1,2,3,4,5}
# # s2={3,6,9}
# # print(s1.union(s2))
# # print(s1.intersection(s2))

# #ALL CONCEPTS

# info=[
#     ("FARAH","MATH"),
#     ("AHMAD","ENGLISH"),
#     ("WAQAS","MATH"),
#     ("AHMAD","Sociology"),
#     ("FARAH","ENGLISH"),
#     ("NEHA","Education"),
# ]
# # unique_courses=set()
# # english_students=set()
# # for tup in info:
# #     print(tup[1])
# #     unique_courses.add(tup[1])
# #     if tup[1]=="ENGLISH":
# #         english_students.add(tup[0])
# # print(unique_courses);    
# # print(english_students);   

# dict={} 
# for name,course in info:
#     if(dict.get(name)==None):
#         dict.update({name:set()})
#         dict[name].add(course)
#     else:
#          dict[name].add(course)

# print(dict)

#OOPS
# class Student:
#     def __init__(self,name,cgpa):
#         self.name=name
#         self.cgpa=cgpa
#     subject="Python"
#     college="ABC"
#     year="4th year"

#     def fun():
#         print(".../")
# stu1=Student("APPLE",2.8)
# stu2=Student("CHERRY",3.4)
# print(stu1.name,stu1.cgpa)
# print(stu2.name,stu2.cgpa)

# class Laptop:
#     storage_type="ssd"
    
#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage

#     @classmethod
#     def get_storage_type(cls):
#         print(f"storage type={cls.storage_type}")

#     @staticmethod
#     def calc_discount(price,discount):
#         final_price=price-(discount*price/100)
#         print(f"discounted price={final_price}")

#     def get_info(self):#instance method 
#         print(f"Storage_type:{self.storage_type} RAM={self.RAM} & storage={self.storage}")

# l1=Laptop("16gb","512gb")        
# l1.get_storage_type() 

# class Product:
#     count=0
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Product.count += 1

#     def get_info(self):   
#         print(f"price of {self.name} is {self.price}") 
#     @classmethod
#     def get_count(cls):
#         print(f"products available at store={cls.count}")
#     @staticmethod
#     def calc_discount(price,discount):
#         print(f"Price after discount={price-discount*price/100}")
       

# p1=Product("phone",10_000)
# p2=Product("Laptop",50_000)
# p3=Product("pen",10)

# p1.get_info();
# Product.get_count();
# p1.calc_discount(p1.price,10)

# class BankAccount: 
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance #protected
#     def get_balance(self):
#         return self.__balance
# acc1=BankAccount("Rahul",10_000)
# print(acc1.name,acc1.get_balance())        
# print(acc1.name,acc1._BankAccount__balance)       

# class Employee:
#     start_time="10am"
#     end_time="6pm"
#     def change_time(self,new_end_time):
#         self.end_time=new_end_time
# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject=subject
# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role=role

# t1=Teacher("Math")
# ad1=AdminStaff("manager")
# t1.change_time("7pm")
# print(t1.subject,t1.start_time,t1.end_time)
# print(ad1.role,ad1.start_time,ad1.end_time)

# class Employee:
#     start_time="10am"
#     end_time="6pm"
#     def change_time(self,new_end_time):
#         self.end_time=new_end_time

# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role=role
# class Accountant(AdminStaff):
#     def __init__(self,salary,role):
#         super().__init__(role)
#         self.salary=salary

# acc1=Accountant(25_000,"CA")
# print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)

# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary
# class Student:
#     def __init__(self,gpa):
#         self.gpa=gpa
# class TA(Teacher,Student):
#      def __init__(self,salary,gpa,name):
#         super().__init__(salary)
#         Student.__init__(self,gpa)
#         self.name=name
# ta1=TA(15_000,9.3,"Shradha")
# print(ta1.name,ta1.gpa,ta1.salary)

# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")
# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")
# lion=Lion()
# lion.make_sound()
# cow=Cow()
# cow.make_sound()

# class Employee:
#     def get_desination(self):
#         print("Employee")
# class Teacher(Employee):
#     def get_desination(self):
#        print("Teacher")
# t1=Teacher();
# t1.get_desination()

# f=open("sample.txt","r")
# data=f.readline()
# print(data)
# f.close()
# f=open("sample.txt","a")
# f.write("new text appended \n here")
# f.close()
# f=open("sample2.txt","r+")
# f.write("123")
# with open("sample.txt","r") as f:
#   data=f.read()
#   print(len(data))
# import os
# os.remove("operations_on_string.py")
# data=True
# line=1
# word="demo"

# with open("sample.txt","r") as f:
#     while data:
#      data=f.readline();
#      if(word in data):
#         print(f"{word} found at {line}")
#         break
#      line+=1tr
# try:
#     x=int(input("enter x:"))
#     ans=10/x
# except ZeroDivisionError:
#     print(f"Divide by zero is not allowed ")
# except ValueError:
#     print(f"Invalid input")
# else:
#     print(f"ans={ans}")
# finally:
#     print("end of code")

# squares=[]
# for i in range(6):
#     squares.append(i*i)
# print(squares)

# sq=[i*i for i in range(6) if i%2!=0]
# print(sq)
# nums=[-2,-4,3,5,2,-1]
# nums=[0 if val<0 else val for val in nums]
# print(nums)
# words=["python","hello","apnacollege"]
# words=[val.upper() for val in words]
# print(words)
# import json
# json_str='{ "name":"Shradha","isTeacher":true}'
# py_obj=json.loads(json_str)
# print(py_obj)
# print(type(py_obj))
# print(type(json_str))

# py_obj={
#     "name":"Shradha",
#     "isTeacher":None
# }
# py_string=json.dumps(py_obj)
# print(py_string)
# print(type(py_string))
# import json
# with open("data.json","r") as f:
#     py_dict=json.load(f)
#     print(py_dict)
import json
data={
    "name":"apple",
    "isLover":None
}
with open("data.json","w") as f:
    json.dump(data,f,indent=9,sort_keys=True)
     
