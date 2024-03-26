from tkinter import simpledialog as sd
import traceback as tb
def print(str__):
	outputs.append(str__)
def input(str_ = ''):
	ans = str(sd.askstring(str_ + ' ?', str_))
	return ans
def ragoae(code_to_run):
	global outputs
	outputs = []
	code_to_run = 'global outputs\noutputs = []\n' + code_to_run
	try:
		exec(compile(code_to_run, 'ScorPyon', 'exec'))
	except:
		return [True, tb.format_exc()]
	return [False, outputs]
