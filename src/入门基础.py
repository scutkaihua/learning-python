

#在线测试工具
https://c.runoob.com/compile/9

#!/usr/bin/python3
import sys
#==============================================
#迭代器 使用class对象,并实现 __iter__  __next__
#==============================================
class MyNubmer:
	def __iter__(self):
		self.num = 2
		return self
		
	def __next__(self):
		while(self.num<10):
			r = "number:"+str(self.num);
			self.num+=2
			return r
		raise StopIteration
		

N = MyNubmer()
Niter = iter(N)

for n in Niter:
	print(n)
	
	
	
	
	
	

#!/usr/bin/python3
import sys
#==============================================
#生成器使用 yield
#==============================================
def MyNubmer(n):
	num=2;c=0;
	while(num<n):
		yield num,c
		c+=num;num+=1;
	
f = MyNubmer(10)

for n in f:
	print(n)
	
	
	
#!/usr/bin/python
#==============================================
# 函数入参数:可变参数:元组，字典 
#==============================================
# 计算面积函数
def area(width, height):
    return width * height
#调用
area(height=10,width=20)


#!/usr/bin/python3
import sys

def f1(fmt,*d):
	for a in d:
		print(fmt%a)
		
f1("%04x",1,15,343)

def f2(fmt,**d):
	print(d)
	
f2("字典",a=1,b=2,c=3)

def f3(name,a,*,c):
	print(a+c)
	
f3("name",c=12,a=23)



#!/usr/bin/python3
#==============================================
#lambda表达式
#==============================================
foo = [1,22,53,14,65,26,21,81,9]
#打印偶数
print(list(filter(lambda x:x%2==0,foo))) 
print([ x for x in foo if x%2 == 0])    

#转成其他列表x=x*2+1
print(list(map(lambda x:x*2+1,foo)))
print([x*2+1 for x in foo])


#==============================================
#列表推导式
#==============================================
#!/usr/bin/python
a = [1,2,3,4,5]
def trans(v):
	return v**2+5

print(list([trans(x) for x in a]))
print(list(x**2+5 for x in a))

#==============================================
#嵌套列表
#==============================================
#!/usr/bin/python
a = [[1,2,3,4,5],[9,8,7,6,5],[12,23,34,56,78]]
b = [[row[i] for row in a] for i in range(5)]
print(b)
#结果: [[1, 9, 12], [2, 8, 23], [3, 7, 34], [4, 6, 56], [5, 5, 78]]




#==============================================
#类
#==============================================
class people:
	
	hair = "black"
	eyes = "blue"
	
	
	def __init__(self):
		self.name="people"
		self.age=0
		
	def speak(self):
		print("people speak!")
		
		
class student(people):
	def __init__(self):
		self.name = "student"
		self.school="xiaoxue"
		
	def speak(self):
		print("student speak")
		
class study:
	grade = 60
	def readbook(self):
		print("i am reading books!")
				
		
class youxiu(student,study):
	
	def __init( self ):
		self.grade = 80
		
	def readbook(self):
		print(self.name+" is reading books")
		
		
yx = youxiu()

yx.speak()
yx.readbook()
		