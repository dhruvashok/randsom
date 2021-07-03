#!/usr/bin/env python3
import random
import time

def gen_rand():
	random.seed(int(time.time()))
	return [random.randint(1, 255) for _ in range(len(flag))]

def xor(a, b):
	return bytes((x ^ y) % 256 for x, y in zip(a, b)).hex()

if __name__ == '__main__':
	flag = open("flag.txt", "rb").read()
	print(open("ascii_art.txt").read())
	print("Welcome!")
	while True:
		choice = input("Would you like an encrypted flag? (Y/n) ").lower()
		if choice != "y":
			print("Goodbye!")
			break
		print("Here you go:", xor(flag, gen_rand()))
