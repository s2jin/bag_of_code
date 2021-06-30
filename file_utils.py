import json

def load(ext, file_path, sep='\t'):
	if ext in ['json']: load_json(file_path)
	elif ext in ['jsonl']: load_jsonl(file_path)
	elif ext in ['csv']: load_csv(file_path, sep=',')
	elif ext in ['tsv']: load_csv(file_path, sep='\t')
	elif ext in ['txt']: load_txt(file_path)
	else: load_file(file_path)

def load_json(file_path):
	with open(file_path, 'r') as f:
		return json.load(f)
	
def load_jsonl(file_path):
	with open(file_path, 'r') as f:
		return [json.loads(l) for l in f]

def load_csv(file_path,sep='\t'):
	with open(file_path, 'r') as f:
		return [l.strip().split(sep) for l in f]

def load_txt(file_path):
	with open(file_path, 'r') as f:
		return f.readlines()

def load_file(file_path):
	with open(file_path, 'r') as f:
		return f.read()
