"""
Problem Statement: https://leetcode.com/problems/ugly-number-ii/
"""

import os
import sys
import subprocess



def run_tests(path: str):
	# compile cpp files
	solution = os.path.join('..', path)
	files = [f'"{os.path.join(solution, f)}"' for f in os.listdir(solution) if f.endswith('.cpp')]
	cmd = f"c++ -std=c++17 {' '.join(files)}"
	if not os.system(cmd) == 0:
		print(f'[\u2718] Failed compilation of {path}.')
		return
	
	# uses verify to evaluate
	with open(os.path.join(solution, 'main.cpp')) as f:
		verify = 'verify' in f.read()
	
	# get test files
	passed = total = 0
	tests = sorted([os.path.splitext(f)[0] for f in os.listdir(path) if f.endswith('.in')])
	
	# run individual tests
	for test in tests:
		# run binary on input
		with open(os.path.join(path, test + '.in')) as f:
			process = subprocess.Popen('./a.out', stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
		out, err = process.communicate()
		if err:
			print(f'[\u2718] Error encountered on test case {test} for {path}.')
			return
		
		# output
		out = out.decode('ascii').strip()
		out = [line.strip() for line in out.splitlines()]

		# checker
		if not verify:
			with open(os.path.join(path, test + '.out')) as f:
				ans = f.read().strip()
				ans = [line.strip() for line in ans.splitlines()]
		else:
			ans = ['1']
		
		# verification
		if out != ans:
			print(f'[\u2718] Failed test case {test}.')
			print(f'{" " * 4}Output: {chr(10).join(out)}')
			print(f'{" " * 4}Expected: {chr(10).join(ans)}')
		else:
			passed += 1
		total += 1

		# terminate process
		process.terminate()
	
	# clean-up
	os.remove('./a.out')
	
	# display results
	if passed == total:
		print('[\u2714] ', end='')
	else:
		print('[\u2718] ', end='')
	print(f'Passed {passed}/{total} test cases for {path}.')



if __name__ == '__main__':
	# Sorting Algorithms
	run_tests('Sorting Algorithms/Selection Sort')
	run_tests('Sorting Algorithms/Bubble Sort')
	run_tests('Sorting Algorithms/Insertion Sort')
	run_tests('Sorting Algorithms/Merge Sort')
	run_tests('Sorting Algorithms/Quick Sort')
	run_tests('Sorting Algorithms/Counting Sort')

	# Search Algorithms
	run_tests('Search Algorithms/Binary Search')
	run_tests('Search Algorithms/Linear Search')
	run_tests('Search Algorithms/Find Peak 1D')
	run_tests('Search Algorithms/Find Peak 2D')

	# Dynamic Programming
	run_tests('Dynamic Programming/Maximum Subarray')

	# Bit Manipulation
	run_tests('Bit Manipulation/Lowest Set Bit')
	run_tests('Bit Manipulation/Highest Set Bit')
	run_tests('Bit Manipulation/Count Set Bits')