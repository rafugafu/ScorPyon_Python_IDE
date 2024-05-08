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
def translate(code):
	code = code.replace('अगर', 'if').replace('नहीतो', 'else').replace('नहीऔर', 'elif').replace('गलतीदेख', 'try').replace('गलतीतो', 'except')
	code = code.replace('इधरला', 'import').replace('बोल', 'print').replace('खतम', 'exit').replace('खुलजा', 'open').replace('गलत', 'False')
	code = code.replace('सच', 'True').replace('खाली', 'None').replace('और', 'and').replace('केसमान', 'as').replace('राज', 'assert')
	code = code.replace('तोड', 'break').replace('कक्षा', 'class').replace('आगेचल', 'continue').replace('नयामतलब', 'def').replace('कचरा', 'del')
	code = code.replace('बादमे', 'finally').replace('हरएक', 'for').replace('उसमेसे', 'from').replace('दुनियाभर', 'global').replace('अन्दर', 'in')
	code = code.replace('हैय', 'is').replace('बाहर', 'nonlocal').replace('नही', 'not').replace('यातो', 'or').replace('जानेदो', 'pass')
	code = code.replace('गलतीबढा', 'raise').replace('वापस', 'return').replace('जबतक', 'while').replace('केसाथ', 'with')
	code = code.replace('इसकेजगह', 'replace').replace('पूछ', 'input').replace('छोटा', 'lower').replace('बडा', 'upper').replace('खुदका', 'self')
	code = code.replace('१', '1').replace('२', '2').replace('३', '3').replace('४', '4').replace('५', '5').replace('६', '6')
	code = code.replace('७', '7').replace('८', '8').replace('९', '9').replace('०', '0').replace('इसकेआगे', 'range')
	return code
def ragoae_other(code_to_run):
	global outputs
	outputs = []
	open('अजगर_translated.py', 'w+').write(translate(code_to_run))
	code_to_run = translate('global outputs\noutputs = []\n' + code_to_run)
	try:
		exec(compile(code_to_run, 'ScorPyon', 'exec'))
	except:
		return [True, tb.format_exc()]
	return [False, outputs]