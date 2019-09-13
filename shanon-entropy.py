import argparse
import math
import platform
import sys
import time
import threading
from multiprocessing import Process

file_path = ""

def main():
	global file_path

	# Get the args
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", help="Specify the file path")
	args = parser.parse_args()

	file_path = args.p

	# Check to see if we got the MAC address
	if (file_path == None):
		sys.exit("[#] Please enter a file path.\n exiting")

	print("[*] File: ", file_path)

	possible_vals = dict(((chr(x), 0) for x in range(0, 256)))

	entropy = 0

	with open(file_path, 'rb') as f:
		data = f.read()
		if data:
			for byte in data:
				possible_vals[chr(byte)] +=1

			data_len = len(data)

			for count in possible_vals:
				if possible_vals[count] == 0:
					continue

				# p - probability of seeing this byte in the file
				p = float(possible_vals[count] / data_len)
				#entropy -=  p * math.log(p, 2) # equivalent to below if we divide the final entropy by 8
				entropy -= p * math.log(p, 256)
			#entropy = entropy / 8

	print(entropy)

if __name__ == "__main__":
	main()
