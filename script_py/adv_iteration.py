# python .\script_py\adv_iteration.py jeff
import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in the words file')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('./script_py/words').readlines()

print([word.strip() for word in words if snippet in word.lower()])
