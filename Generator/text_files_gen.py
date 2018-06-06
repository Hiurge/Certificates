import os, os.path

DIR = '/home/l/CV_kursy/KnowledgePortfolio/coursera_img/'

my_sub_DIRs = [
"Applied Data Science with Python",
"Deep Learning",
"Executive Data Science",
"Data Mining Specialization",
"Others"]

def enter_each(DIR, my_sub_dir):


	DIR = DIR + my_sub_dir

	coursera_items = ([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	coursera_items.sort()
	x = len(coursera_items)

	count = 0 # if main file in

	for each in coursera_items:

		File_name = each[:-4]
		
		def create_file(File_sufix, html_string):
			
			my_path_string = DIR + "/" + File_name + File_sufix
			
			f = open(my_path_string,'w+')
			f.write(html_string)
			f.close()
		
		html_string_desc_COURSE = File_name[:] + '''

Course description: Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab mollitia deleniti minus maiores doloremque assumenda Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero fugit culpa ad quod sed quis, dolores ut nostrum saepe suscipit?

4 weeks of 4h study

Projects:
1. Projekt 1
2. Projekt 2 
3. Projekt 3 
4. Projekt 4
		'''
		html_string_desc_MAIN = File_name + '''

Course description: 
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab mollitia deleniti minus maiores doloremque assumenda Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero fugit culpa ad quod sed quis, dolores ut nostrum saepe suscipit?

5 courses 4 weeks of 4h study each

Projects in perspective:
Course description: Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab mollitia deleniti minus maiores doloremque assumenda Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero fugit culpa ad quod sed quis, dolores ut nostrum saepe suscipit?


		'''

		html_string_tech_COURSE = '''

Tech: 
- Python (numpy, pandas)
- SQL
- Alghorithms (SVM,Random Trees, GBoost)

Others:
- Hacker mindset
- Open thinkinking
		'''

		html_string_tech_MAIN = '''

Tech: 
- Python (numpy, pandas)
- SQL
- Alghorithms (SVM,Random Trees, GBoost)

Others:
- Hacker mindset
- Open thinkinking
		'''

		if ").jpg" in each:
			create_file(" desc.txt", html_string_desc_COURSE)
			create_file(" tech.txt", html_string_tech_COURSE)
		elif "cate.jpg" in each:
			create_file(" desc.txt", html_string_desc_MAIN)
			create_file(" tech.txt", html_string_tech_MAIN)
			count += 1

	if count == 0:	
		html_string_uber = coursera_items[0][-3:-4]
		my_path_string = DIR + "/" + "uber_file.txt"
		f = open(my_path_string,'w+')
		f.write(html_string_uber)
		f.close()

for each in my_sub_DIRs:
	enter_each(DIR,each)
