# 异步 协程 基础版，问题：在调用函数A的时候并没有把他当成普通函数对待
import time
import threading
gen =None #定义全局变量
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
	def D():
		print("在线程D中开始耗时操作C")
		time.sleep(5)
		global gen # 使用全局变量
		try:
			gen.send("D返回的数据") 
		except Exception as e:
			pass		
		print("在线程D中结束耗时操作C")

	# C将耗时操作交给新线程中的D函数操作
	threading.Thread(target=D).start() # 这句话是关键

def finish(data):
	# 这里的参数由线程中的D函数传回
	print("开始处理回调函数")
	print("回调函数获得的参数data：%s"%(data))
	print("结束处理回调函数")

def main():

	global gen
	gen=A() # 生成一个生成器
	next(gen) # 执行生成器

	B()
if __name__=="__main__":
	main()
