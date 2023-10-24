import time

while True:
	corrent_time = time.strftime("%H:%M:%S")
	print(corrent_time, end="\r")
	time.sleep(3)