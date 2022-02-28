# 异步 回调函数
import time
import threading
def A():
	print("开始处理A")
	C(finish) #调用耗时操作C
	print("结束处理A")

def B():
	print("开始处理B")
	time.sleep(2)
	print("结束处理B")

def C(callback_C):
	def D(callback_D):
		print("在线程D中开始耗时操作C")
		time.sleep(5)
		print("在线程D中结束耗时操作C")
		# D使用回调函数传回数据
		callback_D("线程D返回的数据")
	# C将耗时操作交给新线程中的D函数操作
	threading.Thread(target=D,args=(callback_C,)).start() # 这句话是关键

def finish(data):
	# 这里的参数由线程中的D函数传回
	print("开始处理回调函数")
	print("回调函数获得的参数data：%s"%(data))
	print("结束处理回调函数")

def main():
	A()
	B()
if __name__=="__main__":
	main()
