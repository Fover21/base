# 异步 协程 03版 改造装饰器和C()
import time
import threading
# gen =None #定义全局变量

# 装饰器
def genCoroutine(func):
	def wrapper(*args,**kwargs):
		# global gen
		gen1=func(*args,**kwargs) # A()的生成器
		gen2=next(gen1) # C()的生成器
		def run(g):
			res=next(g) # C()的生成器执行后得到C的yield的值
			try:
				gen1.send(res) #将send的值传递给A中的yield，并赋值给A中的res
			except Exception as e:
				pass
		threading.Thread(target=run,args=(gen2,)).start()
	return wrapper

# 使用装饰器
@genCoroutine
def A(): # A用了yield就成了一个生成器
	print("开始处理A")
	res=yield C() # C在生成器next时在新线程中执行
	print("A获得的返回值：%s"%(res))
	print("结束处理A")

def B():
	print("开始处理B")
	time.sleep(2)
	print("结束处理B")

def C():
	print("开始耗时操作C")
	time.sleep(5)
	print("结束耗时操作C")
	# 返回数据
	yield "C函数的返回值"

def main():
	A()
	B()

if __name__=="__main__":
	main()
