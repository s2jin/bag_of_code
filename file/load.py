import json

def load_json(filename):
	with open(filename, 'r') as f:
		return json.load(f)
	
def load_jsonl(filename):
	with open(filename, 'r') as f:
		return [json.loads(l) for l in f]

def load_txt(filename,sep='\t') as f:
	with open(filename, 'r') as f:
		return [l.strip().split(sep) for l in f]
