import random
import time
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped

@background
def shellSort(arr, n):
	gap=n//2
	while gap>0:
		j=gap 
		while j<n:
			i=j-gap

			while i>=0:
				if arr[i+gap]>arr[i]:
					break
				else:
					arr[i+gap],arr[i]=arr[i],arr[i+gap]

				i=i-gap
			j+=1
		gap=gap//2

while True:
	arr = []
	l = int(input('Size of array: '))
	for i in range(l):
		arr.append(random.randint(1, 1000))
	#print('Array before sorting: ', arr)

	start = time.time()
	background(shellSort(arr, l))
	stop = time.time()

	#shellSort(arr,l)
	#print('Array after sorting: ', arr)

	print('Spend time: ', round((stop-start), 4))
	print('')
