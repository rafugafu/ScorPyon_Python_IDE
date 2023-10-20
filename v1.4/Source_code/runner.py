import traceback as tb
def input(str):
	pass
def run_and_get_errors(code_to_run):
	try:
		exec(code_to_run)
	except:
		return tb.format_exc()
	else:
		return None
