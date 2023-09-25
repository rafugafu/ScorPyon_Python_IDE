import tkinter as tk
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import font
from tkinter import colorchooser as colour_chooser
from tkinter import scrolledtext as st
from tkinter import ttk
from runner import run_and_get_errors
import keyword as kw
import traceback as tb
import os
# import getpass (if it was local installation)
# os.chdir(f{'/home/{getpass.getuser()}/.local/share/ScorPyon/'}) (if it was local installation)
# os.chdir('/usr/share/ScorPyon/') (if it was system-wide installation)
class ScorPyonFontError(Exception):
	pass
class ShowScorPyonSourceCodeError(Exception):
	pass
try:
	root = tk.Tk()
	root.title('ScorPyon - Untitled')
	title = ''
	tfgoe = False
	hk = True
	hb = False
	hc = True
	hic = True
	hvf = True
	c = None
	kc = 'orange'
	cc = 'cyan'
	icc = '#00ff00'
	fbc = 'white'
	bbc = 'light blue'
	vfc = 'red'
	ffg = 'yellow'
	fbg = 'cyan'
	interpreter = 'python3'
	text_to_find = None
	def cfs(f, s):
		global code
		global shellin
		global shellout
		global tabs
		global shellout
		try:
			code.configure(font = (f, s))
			shellin.configure(font = (f, s))
			shellout.configure(font = (f, s))
		except:
			try:
				raise ScorPyonFontError('Expected an integer but got ' + s)
			except:
				mb.showerror('Internal Error', tb.format_exc())
	def get_fonts():
		return font.families()
	def change_colour():
		global c
		global kc
		global icc
		global fbc
		global bbc
		global cc
		global vfc
		global ffg
		global fbg
		global code
		global shellin
		global shellout
		nc = colour_chooser.askcolor(title = 'Choose a colour')[1]
		if not nc == None:
			if c == 'kc':
				kc = nc
			elif c == 'icc':
				icc = nc
			elif c == 'fbc':
				fbc = nc
			elif c == 'bbc':
				bbc = nc
			elif c == 'cc':
				cc = nc
			elif c == 'vfc':
				vfc = nc
			elif c == 'b':
				code.configure(bg = nc)
				shellin.configure(bg = nc)
				shellout.configure(bg = nc)
			elif c == 'f':
				code.configure(fg = nc)
				shellin.configure(fg = nc)
				shellout.configure(fg = nc)
			elif c == 'ffg':
				ffg = nc
			elif c == 'fbg':
				fbg = nc
	def setvar(var = None, var1 = None):
		global c
		global hk
		global hb
		global hc
		global hic
		global hvf
		if var == 'hk':
			if hk == True:
				hk = False
			else:
				hk = True
		elif var == 'hb':
			if hb == True:
				hb = False
			else:
				hb = True
		elif var == 'hc':
			if hc == True:
				hc = False
			else:
				hc = True
		elif var == 'hic':
			if hic == True:
				hic = False
			else:
				hic = True
		elif var == 'hvf':
			if hvf == True:
				hvf = False
			else:
				hvf = True
		elif var == 'c':
			c = var1
	def set_intp(inpt):
		global interpreter
		if os.system(f'which {inpt}') != '256':
			interpreter = inpt
	def prf(event = None):
		global code
		global shellin
		global shellout
		global interpreter
		root = tk.Tk()
		root.title('Preferences')
		tbs = ttk.Notebook(root)
		gt = ttk.Frame(tbs)
		tbs.add(gt, text = 'General')
		ct = ttk.Frame(tbs)
		tbs.add(ct, text = 'Colours')
		ft = ttk.Frame(tbs)
		tbs.add(ft, text = 'Font Options')
		it = ttk.Frame(tbs)
		tbs.add(it, text = 'Interpreter')
		tbs.grid(column = 0, row = 0)
		v = 0
		a = tk.Checkbutton(gt, text = 'Highlight Keywords                           ', font = 'Monospace', command = lambda: setvar('hk'))
		a.grid(column = 0, row = 0)
		b = tk.Checkbutton(gt, text = 'Highlight pre-defined variables and functions', font = 'Monospace', command = lambda: setvar('hvf'))
		b.grid(column = 0, row = 1)
		c_1 = tk.Checkbutton(gt, text = 'Highlight Inverted commas and inside         ', font = 'Monospace', command = lambda: setvar('hic'))
		c_1.grid(column = 0, row = 2)
		d = tk.Checkbutton(gt, text = 'Highlight Comments                           ', font = 'Monospace', command = lambda: setvar('hc'))
		d.grid(column = 0, row = 3)
		e = tk.Checkbutton(gt, text = 'Highlight Text Inside Brackets               ', font = 'Monospace', command = lambda: setvar('hb'))
		e.grid(column = 0, row = 4)
		f = tk.Button(gt, text = 'Toggle GUI outputs\nand errors', font = 'Monospace', command = goe).grid(column = 0, row = 5)
		g = tk.Label(ct, text = '"""Select an option for the Change Button to show"""\nChange colour of:', font = 'Monospace').grid(column = 0, row = 0)
		if hk == True:
			a.select()
		if hvf == True:
			b.select()
		if hic == True:
			c_1.select()
		if hc == True:
			d.select()
		if hb == True:
			e.select()
		c = None
		tk.Radiobutton(ct, text = 'Keywords                           ', font = 'Monospace', variable = v, value = 1, command = lambda: [setvar('c', 'kc'), occ.grid()]).grid(column = 0, row = 1)
		tk.Radiobutton(ct, text = 'Pre-defined variables and functions', font = 'Monospace', variable = v, value = 2, command = lambda: [setvar('c', 'vfc'), occ.grid()]).grid(column = 0, row = 2)
		tk.Radiobutton(ct, text = 'Text Inside Inverted Commas        ', font = 'Monospace', variable = v, value = 3, command = lambda: [setvar('c', 'icc'), occ.grid()]).grid(column = 0, row = 3)
		tk.Radiobutton(ct, text = 'Text Inside Brackets               ', font = 'Monospace', variable = v, value = 4, command = lambda: [setvar('c', 'fbc'), occ.grid()]).grid(column = 0, row = 4)
		tk.Radiobutton(ct, text = 'Background of Text Inside Brackets ', font = 'Monospace', variable = v, value = 5, command = lambda: [setvar('c', 'bbc'), occ.grid()]).grid(column = 0, row = 5)
		tk.Radiobutton(ct, text = 'Comments                           ', font = 'Monospace', variable = v, value = 6, command = lambda: [setvar('c', 'cc'), occ.grid()]).grid(column = 0, row = 6)
		tk.Radiobutton(ct, text = 'Background                         ', font = 'Monospace', variable = v, value = 7, command = lambda: [setvar('c', 'b'), occ.grid()]).grid(column = 0, row = 7)
		tk.Radiobutton(ct, text = 'Normal Text Colour                 ', font = 'Monospace', variable = v, value = 8, command = lambda: [setvar('c', 'f'), occ.grid()]).grid(column = 0, row = 8)
		tk.Radiobutton(ct, text = 'Found text colour                  ', font = 'Monospace', variable = v, value = 9, command = lambda: [setvar('c', 'ffg'), occ.grid()]).grid(column = 0, row = 9)
		tk.Radiobutton(ct, text = 'Found text background colour       ', font = 'Monospace', variable = v, value = 10, command = lambda: [setvar('c', 'fbg'), occ.grid()]).grid(column = 0, row = 10)
		occ = tk.Button(ct, text = 'Change', font = 'Monospace', command = change_colour)
		tk.Label(ft, text = 'New Font: ').grid(column = 0, row = 0)
		nf = ttk.Combobox(ft)
		nf['values'] = get_fonts()
		nf.focus_set()
		nf.grid(column = 1, row = 0)
		tk.Label(ft, text = 'New Font Size: ').grid(column = 0, row = 1)
		ns = ttk.Combobox(ft)
		ns['values'] = list(range(10, 51))
		ns.grid(column = 1, row = 1)
		ttk.Button(ft, text = 'Change', command = lambda: cfs(nf.get(), ns.get())).grid(column = 0, row = 2)
		tk.Button(root, text = 'Ok', font = 'Monospace', command = lambda: [ha(), root.destroy()]).grid(column = 0, row = 5)
		intp = ttk.Entry(it)
		intp.grid(column = 0, row = 0)
		ttk.Button(it, text = 'Set', command = lambda: set_intp(intp.get())).grid(column = 0, row = 1)
		ttk.Label(it, text = 'If it is not a valid input, the interpreter will not change.').grid(column = 1, row = 0)
	def goe():
		global tfgoe
		global shellout
		global out
		if tfgoe == True:
			tfgoe = False
			out.grid(column = 0, row = 1)
			shellout.grid(column = 1, row = 1)
		elif tfgoe == False:
			tfgoe = True
			out.grid_forget()
			shellout.grid_forget()
	def rplce(find, replace):
		global code
		global shellin
		if str:
			n = '1.0'
			searchstr = r'\y' + find + r'\y'
			while True:
				n = code.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(find))
				code.delete(n, nn)
				code.insert(n, replace)
				n = nn
			n = '1.0'
			searchstr = r'\y' + find + r'\y'
			while True:
				n = shellin.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(find))
				shellin.delete(n, nn)
				shellin.insert(n, replace)
				n = nn
	def fnd(str):
		global code
		global shellin
		global text_to_find
		global ffg
		global fbg
		text_to_find = str
		if str:
			code.tag_remove('found', '1.0', 'end')
			shellin.tag_remove('found', '1.0', 'end')
			n = '1.0'
			searchstr = r'\y' + str + r'\y'
			while True:
				n = code.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(str))
				code.tag_add('found', n, nn)
				n = nn
			code.tag_config('found', foreground = ffg, background = fbg)
			n = '1.0'
			searchstr = r'\y' + str + r'\y'
			while True:
				n = shellin.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(str))
				shellin.tag_add('found', n, nn)
				n = nn
			shellin.tag_config('found', foreground = ffg, background = fbg)
	def find(event = None):
		global text_to_find
		root = tk.Tk()
		root.title('Find')
		tk.Label(root, text = 'Text to Find: ').grid(column = 0, row = 0)
		find = tk.Entry(root)
		find.grid(column = 1, row = 0)
		o1 = tk.Button(root, text = 'Find', command = lambda: fnd(find.get()))
		o1.grid(column = 0, row = 1)
		tk.Button(root, text = 'Close', command = lambda: root.destroy()).grid(column = 0, row = 2)
	def find_replace(event = None):
		root2 = tk.Tk()
		root2.title('Find & Replace')
		tk.Label(root2, text = 'Text to Find: ').grid(column = 0, row = 0)
		find = tk.Entry(root2)
		find.grid(column = 1, row = 0)
		tk.Label(root2, text = 'Replace with: ').grid(column = 0, row = 1)
		replace = tk.Entry(root2)
		replace.grid(column = 1, row = 1)
		o1 = tk.Button(root2, text = 'Replace', command = lambda: rplce(find.get(), replace.get()))
		o1.focus_set()
		o1.grid(column = 0, row = 2)
		tk.Button(root2, text = 'Close', command = lambda: root2.destroy()).grid(column = 0, row = 3)
	def ssc(event = None):
		answer = mb.askquestion('Warning', 'Are you sure you want to leave this document and open ScorPyon\'s source code ?', icon = 'warning')
		if answer == 'yes':
			try:
				ld(os.getcwd() + '/main.py')
				clt(os.getcwd() + '/main.py')
			except:
				try:
					raise ShowScorPyonSourceCodeError('It was expected to be in ' + os.getcwd() + ', but it is not there !')
				except:
					mb.showerror('Internal Error', tb.format_exc())
	def execute():
		global tfgoe
		global interpreter
		open('temporary.py', 'w').writelines(shellin.get(1.0, 'end'))
		error = run_and_get_errors(shellin.get(1.0, 'end'))
		if error != None:
			if tfgoe == True:
				mb.showerror('Error', error)
			elif tfgoe == False:
				shellout.config(state = tk.NORMAL)
				shellout.delete(1.0, tk.END)
				shellout.insert(tk.END, error)
				shellout.tag_add('error', '1.0', 'end')
				shellout.tag_config('error', foreground = 'red')
				tabs.select(shell_tab)
				shellout.config(state = tk.DISABLED)
		else:
			if not os.popen(interpreter + '  temporary.py').read() == '':
				if tfgoe == True:
					mb.showinfo('Output', os.popen(interpreter + ' temporary.py').read())
				elif tfgoe == False:
					shellout.config(state = tk.NORMAL)
					shellout.delete(1.0, tk.END)
					shellout.insert(tk.END, os.popen(interpreter + ' temporary.py').read())
					shellout.tag_add('normal_text_output', '1.0', 'end')
					shellout.tag_config('normal_text_output', foreground = '#00ff00')
					shellout.config(state=tk.DISABLED)
		os.remove('temporary.py')
	def ha():
		global hk
		global hb
		global hc
		global hic
		global hvf
		global text_to_find
		code.tag_remove('kf', 1.0, tk.END)
		shellin.tag_remove('kf', 1.0, tk.END)
		code.tag_remove('okf', 1.0, tk.END)
		shellin.tag_remove('okf', 1.0, tk.END)
		code.tag_remove('cf', 1.0, tk.END)
		shellin.tag_remove('cf', 1.0, tk.END)
		code.tag_remove('icf', 1.0, tk.END)
		shellin.tag_remove('icf', 1.0, tk.END)
		code.tag_remove('oicf', 1.0, tk.END)
		shellin.tag_remove('oicf', 1.0, tk.END)
		code.tag_remove('bf', 1.0, tk.END)
		shellin.tag_remove('bf', 1.0, tk.END)
		keywords = kw.kwlist
		other_keywords = ['file', 'open', 'map', 'int', 'str', 'print', 'range', 'set', 'input', 'list', 'len', 'self', 'type', 'exec', 'sum', 'iter', 'dir', 'compile', 'eval', 'format', 'locals', 'cls', 'xrange', 'dict', 'repr', 'hasattr', 'setattr', 'super', 'isinstance', 'object', 'tuple', 'float']
		if hk == True:
			for i in range(len(keywords)):
				highlight_keyword(keywords[i])
		if hvf == True:
			for i in range(len(other_keywords)):
				highlight_other_keyword(other_keywords[i])
		if hc == True:
			highlight_comments()
		if hb == True:
			highlight_brackets_and_inside()
		if hic == True:
			highlight_inverted_commas()
		fnd(text_to_find)
	def highlight_keyword(str):
		global code
		global shellin
		global kc
		if str:
			n = '1.0'
			searchstr = r'\y' + str + r'\y'
			while True:
				n = code.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(str))
				code.tag_remove('change font', n, nn)
				code.tag_remove('change size', n, nn)
				code.tag_add('kf', n, nn)
				n = nn
			code.tag_config('kf', foreground = kc)
			n = '1.0'
			while True:
				n = shellin.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(str))
				shellin.tag_remove('change font', n, nn)
				shellin.tag_remove('change size', n, nn)
				shellin.tag_add('kf', n, nn)
				n = nn
			shellin.tag_config('kf', foreground = kc)
	def highlight_other_keyword(str):
		global code
		global shellin
		global vfc
		if str:
			n = '1.0'
			searchstr = r'\y' + str + r'\y'
			while True:
				n = code.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(str))
				code.tag_add('okf', n, nn)
				n = nn
			code.tag_config('okf', foreground = vfc)
			n = '1.0'
			while True:
				n = shellin.search(searchstr, n, nocase = 1, stopindex = tk.END, regexp = True)
				if not n: break
				nn = '%s+%dc' % (n, len(str))
				shellin.tag_add('okf', n, nn)
				n = nn
			shellin.tag_config('okf', foreground = vfc)
	def highlight_comments():
		global code
		global shellin
		global cc
		n = '1.0'
		searchstr = r'#.+?\n'
		while True:
			count = tk.IntVar()
			n = code.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			code.tag_add('cf', n, nn)
			n = nn
		code.tag_config('cf', foreground = cc)
		n = '1.0'
		searchstr = r'#.+?\n'
		while True:
			count = tk.IntVar()
			n = shellin.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			shellin.tag_add('cf', n, nn)
			n = nn
		shellin.tag_config('cf', foreground = cc)
	def highlight_inverted_commas():
		global code
		global shellin
		global icc
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'\'.+?\''
		while True:
			count = tk.IntVar()
			n = code.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			code.tag_add('icf', n, nn)
			n = nn
		code.tag_config('icf', foreground = icc)
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'".+?"'
		while True:
			count = tk.IntVar()
			n = code.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			code.tag_add('oicf', n, nn)
			n = nn
		code.tag_config('oicf', foreground = icc)
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'\'.+?\''
		while True:
			count = tk.IntVar()
			n = shellin.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			shellin.tag_add('icf', n, nn)
			n = nn
		shellin.tag_config('icf', foreground = icc)
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'".+?"'
		while True:
			count = tk.IntVar()
			n = shellin.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			shellin.tag_add('oicf', n, nn)
			n = nn
		shellin.tag_config('oicf', foreground = icc)
	def highlight_brackets_and_inside():
		global code
		global shellin
		global fbc
		global bbc
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'\(.+\)'
		while True:
			count = tk.IntVar()
			n = code.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			code.tag_add('bf', n, nn)
			n = nn
		code.tag_config('bf', foreground = fbc, background = bbc)
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'\(.+\)'
		while True:
			count = tk.IntVar()
			n = shellin.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			shellin.tag_add('bf', n, nn)
			n = nn
		shellin.tag_config('bf', foreground = fbc, background = bbc)
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'\[.+\]'
		while True:
			count = tk.IntVar()
			n = code.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			code.tag_add('bf', n, nn)
			n = nn
		code.tag_config('bf', foreground = fbc, background = bbc)
		n = '1.0'
		maxinv = 10
		i = 1
		searchstr = r'\[.+\]'
		while True:
			count = tk.IntVar()
			n = shellin.search(searchstr, n, nocase = 1, count = count, stopindex = tk.END, regexp = True)
			if not n: break
			nn = '%s+%dc' % (n, count.get())
			shellin.tag_add('bf', n, nn)
			n = nn
		shellin.tag_config('bf', foreground = fbc, background = bbc)
	def save_run(event = None):
		sssv()
		global tfgoe
		global title
		global interpreter
		error = run_and_get_errors(code.get(1.0, 'end'))
		title_global = '"' + title + '"'
		if error != None:
			if tfgoe == True:
				mb.showerror('Error', error)
			elif tfgoe == False:
				shellout.config(state = tk.NORMAL)
				shellout.delete(1.0, tk.END)
				shellout.insert(tk.END, error)
				shellout.tag_add('error', '1.0', 'end')
				shellout.tag_config('error', foreground = 'red')
				tabs.select(shell_tab)
				shellout.config(state = tk.NORMAL)
		else:
			if not os.popen(interpreter + ' ' + title_global).read() == '':
				if tfgoe == True:
					mb.showinfo('Output', os.popen(interpreter + ' ' + title_global).read())
				elif tfgoe == False:
					shellout.config(state = tk.NORMAL)
					shellout.delete(1.0, tk.END)
					shellout.insert(tk.END, os.popen(interpreter + ' ' + title_global).read())
					shellout.tag_add('normal_text_output', '1.0', 'end')
					shellout.tag_config('normal_text_output', foreground = '#00ff00')
					tabs.select(shell_tab)
					shellout.config(state = tk.DISABLED)
	def lld():
		fn = fd.askopenfilename(initialdir = '/', title = 'Open', filetypes = (('Python Files', '*.py'), ('Python Files', '*.pyw')))
		ld(fn)
	def ssssv(nm):
		ha()
		file = open(nm, 'w')
		file.writelines(code.get(1.0, tk.END))
		file.close()
		clt(nm)
	def clt(nt):
		global title
		if not nt == '':
			root.title('ScorPyon' + ' - ' + nt)
		else:
			root.title('ScorPyon - Untitled')
		title = nt
	def sssv(event = None):
		global title
		if not title == '':
			ssssv(title)
		else:
			ssv()
	def shv(event = None):
		vw = tk.Tk()
		vw.title('Version')
		version = tk.Text(vw, height = 1, width = 20)
		version.grid(column = 0, row = 0)
		version.insert('end', '1.2')
		version.config(state = 'disabled')
	def qt(event = None):
		global root
		answer = mb.askquestion('Warning', 'Are you sure you want to quit ScorPyon ?', icon = 'warning')
		if answer == 'yes':
			root.destroy()
	def ld(nm):
		global code
		global root
		if not nm == '':
			file = open(nm, 'r')
			lines = file.readlines()
			code.delete('1.0', tk.END)
			for i in range(len(lines)):
				code.insert(tk.END, lines[i])
			file.close()
			clt(nm)
			tabs.select(code_tab)
		ha()
	def llld(event = None):
		answer = mb.askquestion('Warning', 'Are you sure you want to close this document ?', icon = 'warning')
		if answer == 'yes':
			lld()
	def sv(nm):
		if not nm == '':
			file = open(nm, 'w')
			file.writelines(code.get(1.0, tk.END))
			file.close()
			clt(nm)
			tabs.select(code_tab)
	def ssv(event = None):
		fn = fd.asksaveasfilename(initialdir = '/', title = 'Save As', filetypes = (('Python Files', '*.py'), ('Python Files', '*.pyw')))
		sv(fn)
		clt(fn)
	def nw(event = None):
		global code
		global code_tab
		global tabs
		answer = mb.askquestion('Warning', 'Are you sure you want to open a new document ?', icon = 'warning')
		if answer == 'yes':
			code.delete(1.0, 'end')
			clt('')
			tabs.select(code_tab)
	def kp(event):
		ha()
	def right_clicked_main_code(event):
		global fm
		fm.tk_popup(event.x_root, event.y_root)
		fm.grab_release()
	def right_clicked_shellin(event):
		global rcmin
		rcmin.tk_popup(event.x_root, event.y_root)
		rcmin.grab_release()
	def right_clicked_shellout(event):
		global rcmout
		rcmout.tk_popup(event.x_root, event.y_root)
		rcmout.grab_release()
	tabs = ttk.Notebook(root)
	code_tab = ttk.Frame(tabs)
	tabs.add(code_tab, text = 'Code')
	shell_tab = ttk.Frame(tabs)
	tabs.add(shell_tab, text = 'Shell')
	tabs.grid(column = 0, row = 0)
	code = st.ScrolledText(code_tab, width = 90, height = 50, wrap = tk.WORD, fg = 'white', bg = 'black', insertbackground = 'white', font = ('Ubuntu Medium', 12))
	code.grid(column = 0, row = 0)
	code.insert('end', '# \'ScorPyon\' Python IDE')
	code.bind('<KeyRelease>', kp)
	code.bind('<Button-3>', right_clicked_main_code)
	tk.Label(shell_tab, text = 'In: ', font = ('Sans', 20)).grid(column = 0, row = 0)
	shellin = st.ScrolledText(shell_tab, wrap = tk.WORD, fg = 'white', bg = 'black', insertbackground = 'white', font = ('Ubuntu Medium', 12))
	shellin.grid(column = 1, row = 0)
	shellin.bind('<KeyRelease>', kp)
	out = tk.Label(shell_tab, text = 'Out: ', font = ('Sans', 20))
	out.grid(column = 0, row = 1)
	shellout = st.ScrolledText(shell_tab, wrap = tk.WORD, fg = 'white', bg = 'black', insertbackground = 'white', font = ('Ubuntu Medium', 12), state = tk.DISABLED)
	shellout.grid(column = 1, row = 1)
	rcmin = tk.Menu(shell_tab, tearoff = 0)
	rcmin.add_command(label = 'Clear', command = lambda: shellin.delete(1.0, 'end'))
	rcmin.add_separator()
	rcmin.add_command(label = 'Cancel')
	rcmout = tk.Menu(shell_tab, tearoff = 0)
	rcmout.add_command(label = 'Clear', command = lambda: [shellout.config(state = tk.NORMAL), shellout.delete(1.0, 'end'), shellout.config(state = tk.DISABLED)])
	rcmout.add_separator()
	rcmout.add_command(label = 'Cancel')
	shellin.bind('<Button-3>', right_clicked_shellin)
	shellout.bind('<Button-3>', right_clicked_shellout)
	tk.Button(shell_tab, text = 'Execute', font = ('Sans', 20), command = execute).grid(column = 1, row = 2)
	m = tk.Menu(root)
	root.config(m = m)
	fm = tk.Menu(m)
	m.add_cascade(label = 'File', menu = fm)
	fm.add_command(label = 'New  ->  Ctrl + N', command = nw)
	root.bind('<Control-n>', nw)
	fm.add_command(label = 'Open  ->  Ctrl + L', command = llld)
	root.bind('<Control-l>', llld)
	fm.add_separator()
	fm.add_command(label = 'Save  ->  Ctrl + S', command = sssv)
	root.bind('<Control-s>', sssv)
	fm.add_command(label = 'Save as  ->  Shift + Ctrl + S', command = ssv)
	root.bind('<Control-S>', ssv)
	fm.add_separator()
	fm.add_command(label = 'Save & Run  ->  Ctrl + R', command = save_run)
	root.bind('<Control-r>', save_run)
	fm.add_separator()
	fm.add_command(label = 'Quit  ->  Ctrl + Q', command = qt)
	root.bind('<Control-q>', qt)
	e = tk.Menu(m)
	m.add_cascade(label = 'Edit', menu = e)
	e.add_command(label = 'Find  ->  Ctrl + F', command = find)
	root.bind('<Control-f>', find)
	e.add_command(label = 'Find & Replace  ->  Shift + Ctrl + F', command = find_replace)
	root.bind('<Control-F>', find_replace)
	o = tk.Menu(m)
	m.add_cascade(label = 'Options', menu = o)
	o.add_command(label = 'Preferences  ->  Ctrl + P', command = prf)
	root.bind('<Control-p>', prf)
	o.add_separator()
	o.add_command(label = 'Version', command = shv)
	o.add_command(label = 'Open ScorPyon Source code  ->  Ctrl + O', command = ssc)
	root.bind('<Control-o>', ssc)
	ha()
	if len(sys.argv) > 1:
		ld(sys.argv[1])
	root.mainloop()
except:
	mb.showerror('Internal Error', tb.format_exc())
