import random
import timeit
import python_example as aaa
import numpy as np

import python.algorithms

test_data = [random.randint(0, 10) for _ in range(1000)]
mutable_test_data = [random.randint(0, 10) for _ in range(1000)]

NUM_SAMPLES = 1000

def is_even(x):
	return x % 2 == 0

def greater_than2(x):
	return x > 2


def test_len_cpp():
	aaa.len(test_data)

def test_len():
	len(test_data)

def test_len2():
	len(list(test_data))

def test_len3():
	sum(1 for x in test_data)


def test_len_generator_cpp():
	aaa.len((x for x in test_data))

def test_len_generator():
	len(list(x for x in test_data))


def test_count_cpp():
	aaa.count(test_data, 5);

def test_count():
	sum(x == 5 for x in test_data);


def test_count_if_cpp():
	aaa.count_if(test_data, is_even);

def test_count_if():
	sum(1 for x in test_data if is_even(x));


def test_fill_cpp():
	aaa.fill(mutable_test_data, 5);

def test_fill():
	for i, _ in enumerate(mutable_test_data):
		mutable_test_data[i] = 5


def test_add_cpp():
	aaa.add(test_data, test_data, mutable_test_data);

def test_add():
	for i, _ in enumerate(mutable_test_data):
		mutable_test_data[i] = test_data[i] + test_data[i]


FUNCTIONS = [
	["test_len_cpp", "test_len", "test_len2", "test_len3"],
	["test_len_generator_cpp", "test_len_generator"],
	["test_count_cpp", "test_count"],
	["test_count_if_cpp", "test_count_if"],
	["test_fill_cpp", "test_fill"],
	["test_add_cpp", "test_add"],
]

if __name__ == '__main__':
	for group in FUNCTIONS:
		print()
		for f in group:
			t = timeit.timeit(
				"{}()".format(f),
				setup="from __main__ import {}".format(f), 
				number=NUM_SAMPLES,
			)
			print("{:24s} {:.4f}".format(f, t))
