import os
import time
lenghts = []
def head(he):
	for val in range(len(he)):
		lenghts.append(len(he[val])+4)
def check(lis):
	for a in range(len(lenghts)):
		if (len(lis[a])+4 > lenghts[a]):
			lenghts[a] = (len(lis[a])+4)

def head1(headings):
	linefill(h)
	for val in range(len(headings)):
		_1space = (lenghts[val]-len(headings[val]))//2
		_2space = (lenghts[val]-(len(headings[val])+_1space))		
		print(f'|{' '*_1space}\033[1m\033[34m{headings[val].upper()}\033[0m{' '*_2space}',end='')
		time.sleep(0.005)
	print('|')
	linefill(h)
def linefill(headings):
	for val in range(len(headings)):
		print(f'+{'-'*lenghts[val]}',end='')
	print('+')
def rows(values):
	for val in range(len(values)):
		_1space = 2  #(lenghts[val]-len(values[val]))//2
		_2space = (lenghts[val]-(len(values[val])+2))
		print(f'|{' '*_1space}{values[val]}{' '*_2space}',end='')
		time.sleep(0.005)
	print('|')
	linefill(h)
os.system('cls')
rowces = []
t_name = input('Enter table Name : ')
h = input('Enter table headings (join words using \',\') : ').split(',')
rowces.append(h)
for ro in range(int(input('\nHow many rows : '))):
	v = input(f'Row {ro+1} : ').split(',')
	rowces.append(v)
os.system('cls')
print('\n')
head(h)
for ro in rowces:
	check(ro)
print(f'{' '*int((sum(lenghts)/2)-(len(t_name)/2))}\033[33m{t_name.upper()}\033[0m')

head1(h)
for i in range(1,len(rowces)):
	rows(rowces[i])
print('\n')