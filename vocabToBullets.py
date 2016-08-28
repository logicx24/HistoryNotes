import glob
import argparse

def loadFiles(path):
	fileToText = {}
	for filename in glob.glob(path):
		with open(filename) as f:
			fileToText[filename] = f.read().replace("\\", "").replace("-","").lower().split("\n")
	return fileToText

def loadVocab(wordpath):
	with open(wordpath) as w:
		ws = w.read().lower().strip().split("\n")
	return ws

def wordSearch(word, fileToText):
	resultsDict = {key: [] for key in fileToText.keys()}
	for key in fileToText:
		for line in fileToText[key]:
			if word in line:
				resultsDict[key].append(line)
	return resultsDict


def main(vocabFile, outFile):
	fTT = loadFiles("./notes/*.rtf")
	with open(outFile, 'w') as f:
		for word in loadVocab(vocabFile):
			f.write("\n" + word.title() + ": \n")
			resultsDict = wordSearch(word, fTT)
			for key in resultsDict:
				if resultsDict[key]:
					f.write("\n\t" + key + ": \n")
					for line in resultsDict[key]:
						f.write("\t\t - " + line.strip() + "\n ")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Find relevant bullets.')
	parser.add_argument('-v', type=str, help='the input vocab file', action='store', required=True)
	parser.add_argument('-o', type=str, help='the output file', action='store', required=False, default="out.txt")
	args = vars(parser.parse_args())
	main(args['v'], args['o'])
	print("Finished. Check " + args['o'] + " for your definitions.")
