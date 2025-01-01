import time

fish = ['dory', 'bruce', 'marlin', 'nemo']
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 
'gill', 'bloat', ' nigel', 'squirt', 'darla', 'hank']
large = [nemo] * 10

def findNemo2(fish):
	t0 = time.perf_counter()
	for i in range(len(fish)):
		if fish[i] == 'nemo':
			print("Found Nemo!!")

	t1 = time.perf_counter()
	print(f'call to find nemo took {(t1-t0)} milliseconds.')

findNemo2(everyone)