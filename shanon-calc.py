import argparse
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

CHUNK_SIZE = 256

def main():
	# Get the args
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", help="Specify the file path")
	args = parser.parse_args()

	file_path = args.p

	# Check to see if a file path is given
	if (file_path == None):
		sys.exit("[#] Please enter a file path.\n exiting")

	print("[*] File: ", file_path)

	with open(file_path, 'rb') as f:
		data = f.read()
		if data:
			file_entropy = information_entropy(data)
			print("[*] The entropy is", file_entropy, "bits per byte")

			chunk_wise_entropy(data)



"""
	This function is responsible for plotting the entropy for each region
"""
def plot_entropy(entropy_chunk, offset_chunk):
	fig = plt.figure()

	ax = fig.add_subplot(1, 1, 1, autoscale_on=True)
	ax.set_title("Entropy Graph")
	ax.set_xlabel("Offset")
	ax.set_ylabel("Entropy")
	ax.plot(offset_chunk, entropy_chunk, 'y', lw=2)

	plt.show()


"""
	This function divides the entire file into chunks and computes the entropy
	for each chunk. The entropy values are then passed to another function to
	be plotted.
"""
def chunk_wise_entropy(file_data):
	entropy_chunk = []
	offset_chunk = []

	counter = 0
	data_len = len(file_data)
	if file_data:
		while counter <= data_len:
			entropy_chunk.append(information_entropy(file_data[counter:counter+CHUNK_SIZE]))
			offset_chunk.append(counter)
			counter += CHUNK_SIZE

	plot_entropy(entropy_chunk, offset_chunk)


"""
	This function is responsible for computing the Shanon entropy of the data
	passed to it.
"""
def information_entropy(data):
	# Create a counter for all the 256 different possible values
	possible_vals = dict(((chr(x), 0) for x in range(0, 256)))

	# Increment the counter if the byte has the same value as one of the keys
	for byte in data:
		possible_vals[chr(byte)] +=1

	data_len = len(data)
	entropy = 0.0

	# Compute the entropy of the data block
	for count in possible_vals:
		if possible_vals[count] == 0:
			continue

		# p is the probability of seeing this byte in the file
		p = float(possible_vals[count] / data_len)
		entropy -= p * math.log(p, 2)

	return entropy


if __name__ == "__main__":
	main()