import os, os.path

# simple version for working with CWD
print( len([name for name in os.listdir('.') if os.path.isfile(name)]) )
# print( ([name for name in os.listdir('.') if os.path.isfile(name)]) )
# path joining version for other paths
DIR = '/home/l/CV_kursy/KnowledgePortfolio/coursera_img/'
#print( ([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
x = ( ([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
for each in x:
	print(each)
print( len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))