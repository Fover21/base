# 同步
import time
def A():
	print("开始处理A")
	C()
	print("结束处理A")
def B():
	print("开始处理B")
	print("结束处理B")
def C():
	print("开始耗时操作")
	time.sleep(5)
	print("结束耗时操作")

def main():
	A()	
	B()
if __name__=="__main__":
	main()
