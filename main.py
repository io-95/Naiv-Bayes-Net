import csv
import os

def main():
	array = []
	stream = os.popen('ls 20_newsgroups/Training/Ath >> buffer.csv')
	with open('buffer.csv', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter='\n')
		for row in reader:
			array.append([str(num) for num in row])

	string = []
	for i in range(len(array)):
		string.append('cat 20_newsgroups/Training/Ath/' 
		     				+ ''.join(array[i]) 
							+' | tr -d "[:punct:]" | tr -s "[:space:]" "\n" | sort | uniq -ci')
	
	print(string[1])
	stream = os.popen(string[3])
	output = stream.read()
	print(output)

if __name__ == '__main__':
	main()
