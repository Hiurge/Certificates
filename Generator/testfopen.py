

z = "1. Introduction to Data Science in Python (Michigan University) desc.txt"
x = "Applied Data Science with Python"
my_path_string = "/home/l/CV_kursy/KnowledgePortfolio/coursera_img/" + x + "/"+ z

f = open(my_path_string,'r')
file_contents = f.read()
print(file_contents)
f.close()



with open(my_path_string) as f:
    lines = f.readlines()

for each in lines:
	print(each)

true_lines = []
for each in lines:
	each = '''<p>''' + each + '''</p>'''
	true_lines.append(each)

for each in true_lines:
	print(each)