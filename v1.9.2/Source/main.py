import tkinter as tk
import sys
from tkinter import simpledialog as sd
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import font
from tkinter import colorchooser as colour_chooser
from tkinter import scrolledtext as st
from tkinter import ttk
from runner import ragoae
import keyword as kw
import traceback as tb
import os
import getpass
if sys.platform != 'linux' and sys.platform !='win32':
    mb.showerror('Error', 'ScorPyon does not work on anything but linux and windows')
    sys.exit()
elif sys.platform == 'linux':
    plfm = 0
elif sys.platform == 'win32':
    plfm = 1
def wc():
	global kc
	global cc
	global icc
	global fbc
	global bbc
	global vfc
	global ffg
	global fbg
	global b
	global f
	global user
	global defaultdir
	global v
	file = open([f'/home/{user}/.local/ScorPyon/prefs.txt', f'C:/Users/{user}/ScorPyon/prefs.txt'][plfm], 'w+')
	list = [kc, cc, icc, fbc, bbc, vfc, ffg, fbg, b, f, defaultdir, v]
	for item in list:
		file.write(item + '\n')
	file.close()
user = getpass.getuser()
v = '1.9.2'
class ScorPyonFontError(Exception):
	pass
class ShowScorPyonSourceCodeError(Exception):
	pass
try:
	root = tk.Tk()
	root.title('ScorPyon - Untitled')
	image = tk.PhotoImage(file = ['/usr/share/ScorPyon/Icon.png', 'C:/Program Files/ScorPyon/Icon.png'][plfm])
	root.iconphoto(False, image)
	title = ''
	tfgoe = False
	hk = True
	hb = False
	hc = True
	hic = True
	hvf = True
	c = None
	try:
		os.mkdir([f'/home/{user}/.local/ScorPyon/', f'C:/Users/{user}/ScorPyon/'][plfm])
	except:
		pass
	try:
		file = open([f'/home/{user}/.local/ScorPyon/prefs.txt', f'C:/Users/{user}/ScorPyon/prefs.txt'][plfm], 'r')
	except:
		file = open([f'/home/{user}/.local/ScorPyon/prefs.txt', f'C:/Users/{user}/ScorPyon/prefs.txt'][plfm], 'w+')
		mb.showinfo('Message', 'Welcome to ScorPyon First installation!')
		while True:
			defaultdir = sd.askstring('Default Directory', 'What would you like the open and save file dialogs to default to:')
			if defaultdir != None:
				try:
					os.chdir(defaultdir)
				except:
					mb.showerror('Error', 'That directory does not exist')
					pass
				else:
					break
			else:
				mb.showerror('Error', 'Got blank')
				pass
		file.write(f'#d9d900\n#aebeb3\n#00ff00\n#ffffff\n#000000\n#00d9d9\n#ffffff\n#ff0000\n#003000\n#ffffff\n{defaultdir}\n{v}')
		file.close()
	file = open([f'/home/{user}/.local/ScorPyon/prefs.txt', f'C:/Users/{user}/ScorPyon/prefs.txt'][plfm], 'r')
	prefs = file.read().split('\n')
	kc = prefs[0]
	cc = prefs[1]
	icc = prefs[2]
	fbc = prefs[3]
	bbc = prefs[4]
	vfc = prefs[5]
	ffg = prefs[6]
	fbg = prefs[7]
	b = prefs[8]
	f = prefs[9]
	defaultdir = prefs[10]
	if v == prefs[11]:
		pass
	else:
		mb.showinfo('Message', 'Welcome to the new version of ScorPyon!')
		wc()
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
		global f
		global b
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
				b = nc
				code.configure(bg = nc)
				shellin.configure(bg = nc)
				shellout.configure(bg = nc)
			elif c == 'f':
				f = nc
				code.configure(fg = nc)
				shellin.configure(fg = nc)
				shellout.configure(fg = nc)
			elif c == 'ffg':
				ffg = nc
			elif c == 'fbg':
				fbg = nc
			wc()
	def settheme(theme):
		global kc
		global cc
		global icc
		global fbc
		global bbc
		global vfc
		global ffg
		global fbg
		global b
		global f
		if theme == 'default dark green':
			kc = '#d9d900'
			cc = '#aebeb3'
			icc = '#00ff00'
			fbc = '#ffffff'
			bbc = '#000000'
			vfc = '#00d9d9'
			ffg = '#ffffff'
			fbg = '#ff0000'
			b = '#003000'
			f = '#ffffff'
		elif theme == 'dark blue':
			settheme('default dark green')
			b = '#00205e'
		elif theme == 'butter':
			kc = '#c00000'
			cc = '#d9ff73'
			icc = '#006b00'
			fbc = '#ffffff'
			bbc = '#000000'
			vfc = '#d900d9'
			ffg = '#ffffff'
			fbg = '#ff0000'
			b = '#f0f3d4'
			f = '#000000'
		elif theme == 'old black':
			kc = 'orange'
			cc = 'cyan'
			icc = '#00ff00'
			fbc = 'white'
			bbc = 'light blue'
			vfc = 'red'
			ffg = 'yellow'
			fbg = 'cyan'
			b = 'black'
			f = 'white'
		elif theme == 'plain white':
			kc = '#c00000'
			cc = '#d9ff73'
			icc = '#006b00'
			fbc = '#ffffff'
			bbc = '#000000'
			vfc = '#d900d9'
			ffg = '#ffffff'
			fbg = '#ff0000'
			b = 'white'
			f = 'black'
		code.configure(bg = b, fg = f)
		shellin.configure(bg = b, fg = f)
		shellout.configure(bg = b, fg = f)
		wc()
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
	def prf(event = None):
		global code
		global shellin
		global shellout
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
		g = tk.Label(ct, text = '"""Select an option for the Change Colour Button to show"""\nSelect custom colours or readymade theme:', font = 'Monospace').grid(column = 0, row = 0)
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
		themes = ['default dark green', 'dark blue', 'butter', 'old black', 'plain white']
		theme = tk.StringVar(ct)
		theme.set('default dark green')
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
		occ = tk.Button(ct, text = 'Change Colour', font = 'Monospace', command = change_colour)
		tk.OptionMenu(ct, theme, *themes).grid()
		tk.Button(ct, text = 'Change Theme', font = 'Monospace', command = lambda: settheme(theme.get())).grid()
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
		global plfm
		answer = mb.askquestion('Warning', 'Are you sure you want to leave this document and open ScorPyon\'s source code ?', icon = 'warning')
		if answer == 'yes':
			try:
				ld(['/usr/share/ScorPyon/main.py', 'C:/Program Files/ScorPyon/main.py'][plfm])
				clt(['/usr/share/ScorPyon/main.py', 'C:/Program Files/ScorPyon/main.py'][plfm])
			except Exception as error:
				try:
					raise ShowScorPyonSourceCodeError(error)
				except:
					mb.showerror('Internal Error', tb.format_exc())
	def execute():
		global tfgoe
		global hist
		open('temporary.py', 'w').writelines(shellin.get(1.0, 'end'))
		runthingy_ = ragoae(shellin.get(1.0, 'end'))
		if type(runthingy_[1]) != str:
			runthingy = [False]
			str_ = ''
			for item in runthingy_[1]:
				str_ += str(item) + '\n'
			runthingy.append(str_)
		else:
			runthingy = runthingy_
		if runthingy[0] == True:
			error = runthingy[1]
			outputs = '\n'
		else:
			error = None
			outputs = runthingy[1]
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
			hist.insert('end', error)
		else:
			if outputs == '':
				pass
			else:
				if tfgoe == True:
					mb.showinfo('Output', outputs)
				elif tfgoe == False:
					shellout.config(state = tk.NORMAL)
					shellout.delete(1.0, tk.END)
					shellout.insert(tk.END, outputs)
					shellout.tag_add('normal_text_output', '1.0', 'end')
					shellout.tag_config('normal_text_output', foreground = '#00ff00')
					shellout.config(state=tk.DISABLED)
				hist.insert('end', outputs)
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
		global hist
		runthingy_ = ragoae(code.get(1.0, 'end'))
		if type(runthingy_[1]) != str:
			runthingy = [False]
			str_ = ''
			for item in runthingy_[1]:
				str_ += str(item) + '\n'
			runthingy.append(str_)
		else:
			runthingy = runthingy_
		if runthingy[0] == True:
			error = runthingy[1]
			outputs = '\n'
		else:
			error = None
			outputs = runthingy[1]
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
			hist.insert('end', error)
		else:
			if outputs == '':
				pass
			else:
				if tfgoe == True:
					mb.showinfo('Output', outputs)
				elif tfgoe == False:
					shellout.config(state = tk.NORMAL)
					shellout.delete(1.0, tk.END)
					shellout.insert(tk.END, outputs)
					shellout.tag_add('normal_text_output', '1.0', 'end')
					shellout.tag_config('normal_text_output', foreground = '#00ff00')
					tabs.select(shell_tab)
					shellout.config(state=tk.DISABLED)
				hist.insert('end', outputs)
	def lld():
		global defaultdir
		fn = fd.askopenfilename(initialdir = defaultdir, title = 'Open', filetypes = (('Python Files', '*.py'), ('Python Files', '*.pyw')))
		if type(fn) == str:
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
			try:
				root.title('ScorPyon' + ' - ' + nt)
			except:
				pass
		else:
			root.title('ScorPyon - Untitled')
		title = nt
	def sssv(event = None):
		global title
		if not title == '':
			ssssv(title)
		else:
			ssv()
	def about(event = None):
		global v
		global plfm
		abw = tk.Tk()
		abw.title('About ScorPyon')
		abw_ = ttk.Frame(abw)
		abw_.pack(fill = 'both', padx = 10, pady = 10)
		tk.Label(abw_, text = f'ScorPyon v{v}', font = ('Ubuntu Medium', 20)).grid(column = 0, row = 0)
		tk.Label(abw_, text = 'Rafey <https://github.com/rafugafu>', font = ('Ubuntu Medium', 15)).grid(column = 0, row = 1)
		tk.Label(abw_, text = 'ScorPyon Integrated Development Environment for Python', font = ('Ubuntu Medium', 12)).grid(column = 0, row = 2)
		tk.Button(abw, text = 'Close', command = abw.destroy).pack(side = 'bottom', fill = 'x', padx = 10, pady = 10)
		abw.mainloop()
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
			try:
				file = open(nm, 'w')
				file.writelines(code.get(1.0, tk.END))
				file.close()
				clt(nm)
				tabs.select(code_tab)
			except:
				pass
	def ssv(event = None):
		global defaultdir
		fn = fd.asksaveasfilename(initialdir = defaultdir, title = 'Save As', filetypes = (('Python Files', '*.py'), ('Python Files', '*.pyw')))
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
	def return_val(event):
		global hist
		global shell_in
		global tabs
		shell_in.delete(1.0, 'end')
		shell_in.insert('end', hist.get(hist.curselection()))
		tabs.select(shell_in)
	def selall(event):
		global code
		code.tag_add('sel', '1.0', 'end')
		return 'break'
	def selall_(event):
		global shellin
		shellin.tag_add('sel', '1.0', 'end')
		return 'break'
	def selall__(event):
		global shellout
		shellout.tag_add('sel', '1.0', 'end')
		return 'break'
	def kb(event = None):
		kbw_ = tk.Tk()
		kbw_.title('Known bugs')
		kbw = tk.Frame(kbw_)
		kbw.pack()
		tk.Label(kbw, text = '1. It does not open filenames with a space from the terminal (linux)').grid(column = 0, row = 0, padx = 10, pady = 10)
		tk.Label(kbw, text = '2. Does not work as an application on windows').grid(column = 0, row = 1, padx = 10, pady = 10)
		tk.Button(kbw_, text = 'Close', command = kbw_.destroy).pack(side = 'bottom', fill = 'x', padx = 10, pady = 10)
		kbw_.mainloop()
	def changes(event = None):
		global v
		cw_ = tk.Tk()
		cw_.title(f'Changes for v{v}')
		cw = tk.Frame(cw_)
		cw.pack()
		tk.Label(cw, text = '1. Now works on windows!').grid(column = 0, row = 0, padx = 10, pady = 10)
		tk.Label(cw, text = '2. Added and replaced a lot of menu options').grid(column = 0, row = 1, padx = 10, pady = 10)
		tk.Button(cw_, text = 'Close', command = cw_.destroy).pack(fill = 'x', side = 'bottom', padx = 10, pady = 10)
		cw_.mainloop()
	tabs = ttk.Notebook(root)
	code_tab = ttk.Frame(tabs)
	tabs.add(code_tab, text = 'Code')
	shell_tab = ttk.Frame(tabs)
	tabs.add(shell_tab, text = 'Shell')
	hist_tab = ttk.Frame(tabs)
	tabs.add(hist_tab, text = 'History')
	tabs.grid(column = 0, row = 0)
	code = st.ScrolledText(code_tab, width = 90, height = 50, wrap = tk.WORD, fg = f, bg = b, insertbackground = 'white', font = ('Ubuntu Medium', 12))
	code.grid(column = 0, row = 0)
	code.insert('end', '# \'ScorPyon\' Python IDE')
	code.bind('<KeyRelease>', kp)
	code.bind('<Button-3>', right_clicked_main_code)
	tk.Label(shell_tab, text = 'In: ', font = ('Sans', 20)).grid(column = 0, row = 0)
	shellin = st.ScrolledText(shell_tab, wrap = tk.WORD, fg = f, bg = b, insertbackground = 'white', font = ('Ubuntu Medium', 12))
	shellin.grid(column = 1, row = 0)
	shellin.bind('<KeyRelease>', kp)
	out = tk.Label(shell_tab, text = 'Out: ', font = ('Sans', 20))
	out.grid(column = 0, row = 1)
	shellout = st.ScrolledText(shell_tab, wrap = tk.WORD, fg = f, bg = b, insertbackground = 'white', font = ('Ubuntu Medium', 12), state = tk.DISABLED)
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
	ttk.Label(hist_tab, text = 'This is the history of all the outputs produced by the shell this time you have run this program.').pack()
	hist = tk.Listbox(hist_tab)
	hist.pack(fill = 'both')
	hist.bind('<Double-1>', return_val)
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
	o.add_command(label = 'Open Source  ->  Ctrl + O', command = ssc)
	root.bind('<Control-o>', ssc)
	h = tk.Menu(m)
	m.add_cascade(label = 'Help', menu = h)
	h.add_command(label = 'About ScorPyon', command = about)
	h.add_command(label = 'Known bugs', command = kb)
	h.add_command(label = f'Changes in v{v}', command = changes)
	code.bind('<Control-a>', selall)
	shellin.bind('<Control-a>', selall_)
	shellout.bind('<Control-a>', selall__)
	ha()
	if len(sys.argv) > 1:
		ld(sys.argv[1])
	root.mainloop()
except:
	mb.showerror('Internal Error', tb.format_exc())

