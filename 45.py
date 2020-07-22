#!/usr/bin/env python
import re

def calculate_by_regex(expression_input):
	pattern = r"\s"
	elements = re.split(pattern, expression_input)
	expression_normalized = elements[0] + elements[2] + elements[1]
	result = eval(expression_normalized)
	return result


print("Enter a simple RPN expression\nFormat: A B +")
expression = input("Expression: ")
print("Output:", calculate_by_regex(expression))
