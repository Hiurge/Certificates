import os, os.path
import re

def create_names_photos_descriptions(my_directory):

	coursera_titles = []
	coursera_html_packs = []

	DIR = my_directory
	coursera_items = []
	coursera_items = ([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

	
	photo_items = []
	desc_items = []
	tech_items = []

	main_photo = []
	for each in coursera_items:
		if "cate.jpg" in each:
			main_photo.append(each)

	if len(main_photo) > 0:
		main_jpg = main_photo[0]
		main_name = main_photo[0][3:-22]

	else:
		main_jpg = None
		main_name = "Section Headline"

	for each in coursera_items:
		
		if ".jpg" in each: photo_items.append(each)
		if "desc.txt" in each: desc_items.append(each)
		if "tech.txt" in each: tech_items.append(each)
		if "uber_file.txt" in each:
			print(each)
			if len(main_photo) == 0:
				with open(DIR + "/" + "uber_file.txt") as f:
					main_name = f.read()

	photo_items.sort()
	desc_items.sort()
	tech_items.sort()

	print(main_name)

	coursera_cycle_title = '''
				
				<tr>
					<td valign="top"><font size="2"><b>''' + str(" ") + '''</b></font></td> 
					<th valign="top"<font size="2"></font></th>
					<td valign="top"><font size="2">''' + str(" ") + '''</font></td>
					<th valign="top"><font size="2"></font></th> 
					<td valign="top"><font size="2"><p>''' + str(" ") + '''</p></font></td> 
					<th valign="top"<font size="2"></font></th>
				</tr>
				<tr onMouseOver="Context('context1', true)" onMouseOut="Context('context1', false)">
					<td valign="top"><font size="2"><b>''' + main_name + ":" + '''</b></font></td> 
					<th valign="top"<font size="2"></font></th>
					<td valign="top"><font size="2">''' + str("") + '''</font></td>
					<th valign="top"><font size="2"></font></th> 
					<td valign="top"><font size="2">''' + str("") + '''</font></td> 
					<th valign="top"<font size="2"></font></th>
				</tr>
				'''
									

	for each in photo_items:

		def load_file_content(my_file):

			# f = open(my_file,'r')
			# file_contents = f.read()

			with open(my_file) as f:
			    lines = f.readlines()
			

			controler = 0
			count_projects = 0
			true_lines = []
			for line in lines:
				if line[1:3] == ". ":
					count_projects += 1
				if lines[0][1:3] == ". ": 
					controler = 1
				if line.startswith("Proj"):
					line = '''<p><b>''' + line + '''</b></p>'''					
				elif line == lines[0]:
					if my_file.endswith("desc.txt"):
						line = '''<p><b>''' + line + '''</b></p>'''						
				else:
					line = '''<p>''' + line + '''</p>'''

				
				true_lines.append(line)


			count_projects = count_projects - controler
			if count_projects == 0:
				count_projects = " "

			file_contents = "".join(true_lines)
			f.close()

			return file_contents, count_projects
			
		
		temp_name = each[:-4]
		for item_name in desc_items:
			if temp_name in item_name:
				my_file = my_directory + "/" + temp_name + " desc.txt"
				temp_desc, count_projects = load_file_content(my_file)



		for item_name in tech_items:
			if temp_name in item_name:
				my_file = my_directory + "/" + temp_name + " tech.txt"
				temp_tech, placeholder = load_file_content(my_file)


		title = each[:-4]

		uni_list = ["deeplearning.ai","Michigan University", "Illinois University","Hopkins University"]
		
		for university in uni_list:
			string_university = "(" + university + ")"
			if string_university in title:
				title = title.replace(string_university,'')
		

		if "0. " in title:
			print("catched", title)
			coursera_title = ''
		else:		
			# coursera_title = '''
			# 		<p>'''+ title +'''</p>
			# 	'''
			# str(len(coursera_description_Overview))
			# str(coursera_description_Tech[:60])
			coursera_title = '''
				<tr onMouseOver="Context('context1', true)" onMouseOut="Context('context1', false)">
					<td valign="top"><font size="2">''' + title + '''</font></td> 
					<th valign="top"<font size="2"></font></th>
					<td valign="top"><font size="2">''' + str(temp_tech) + '''</font></td>
					<th valign="top"><font size="2"></font></th> 
					<td valign="top"><font size="2">''' + str((count_projects)) + '''</font></td> 
					<th valign="top"<font size="2"></font></th>
				</tr>
				'''

		coursera_titles.append(coursera_title)
		


		coursera_photo = '''
				<img src="''' + DIR + "/" + each + '''" alt="xd" width="600">
				'''

		coursera_description_Overview = '''<p>''' + temp_desc + '''</p>'''

		coursera_description_Tech = '''<p>''' + temp_tech + '''</p>'''

		coursera_html_pack = '''
				<tr onMouseOver="Context('context1', true)" onMouseOut="Context('context1', false)">
					<td valign="top"><font size="2">''' + coursera_photo + '''</font></td> 
					<th valign="top"<font size="2"></font></th>
					<td valign="top"><font size="2">''' + str(coursera_description_Overview) + '''</font></td>
					<th valign="top"><font size="2"></font></th> 
					<td valign="top"><font size="2">''' + str(coursera_description_Tech) + '''</font></td> 
					<th valign="top"<font size="2"></font></th>
				</tr>
		'''
		coursera_html_packs.append(coursera_html_pack)

	return coursera_html_packs, coursera_titles, coursera_cycle_title


DIR = '/home/l/CV_kursy/KnowledgePortfolio/coursera_img/'

DIR_ADSwP = DIR + "Applied Data Science with Python"
DIR_DL = DIR + "Deep Learning"
DIR_EDS = DIR + "Executive Data Science"
DIR_DM = DIR + "Data Mining Specialization"
DIR_Oth = DIR + "Others"
DIR_IP = DIR + "In progress"

dir_list = [DIR_ADSwP, DIR_DL, DIR_EDS, DIR_DM, DIR_Oth, DIR_IP]


All_coursera_mid_0 = []
All_coursera_html_packs = []

def all_strings_ready(dir_list):

	for each in dir_list:

		coursera_html_packs, coursera_titles, coursera_cycle_title = create_names_photos_descriptions(each)
		
		coursera_placeholder = ""

		coursera_mid_0 = coursera_cycle_title + "".join(coursera_titles)
		All_coursera_mid_0.append(coursera_mid_0)
		coursera_html_packs = "".join(coursera_html_packs)
		All_coursera_html_packs.append(coursera_html_packs)

	html_string_mid_0 = "".join(All_coursera_mid_0)
	html_string_packs = "".join(All_coursera_html_packs)

	return html_string_mid_0, html_string_packs

html_string_mid_0, html_string_packs = all_strings_ready(dir_list)



# Masterplik do każdego folderu z headlinem.
#







html_string_open = '''<!doctype html>

<html lang="pl">

<head>
    <meta charset="utf-8">

    <title>LP Kursy</title>
    <meta name="description" content="LP">
    <meta name="author" content="Leon & Łuke">
    <!-- BOOTSTRAP 4 STYLESHEET -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- FONTS -->
    <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville:400,700&amp;subset=latin-ext" rel="stylesheet">

    <!-- PROJECT STYLESHEET -->
    <link rel="stylesheet" href="stylesheets/style.css">

</head>

<body>
    <!-- header -->
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <div class="row main-header">
                    <div class="col-4 logo-box">

                        <a href="">
                        <span class="logo">
                            Łukasz Pintal
                        </span>
                        </a>

                    </div>

                    <nav class="col-8 main-nav">
                        <div class="row justify-content-end">
                            <div class="col-3 menu-action">
                                <button class="nav-btn">
                            <a href=""><span>Moje kursy</span></a>
                        </button>
                            </div>
                            <div class="col-2 menu-action">
                                <button class="nav-btn">
                            <a href=""><span>Moje projekty</span></a>
                        </button>
                            </div>
                        </div>
                    </nav>
                </div>

            </div>
        </div>
    </div>
    <div class="container-fluid">
        <div class="row justify-content-center">
            <div class="col-10">
                <h6>My courses</h6>
                <p>I still don't feel fluent but i know how and where to find what i am looking for. </p>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab mollitia deleniti minus maiores doloremque assumenda Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero fugit culpa ad quod sed quis, dolores ut nostrum saepe suscipit?  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis vero reprehenderit ut, sapiente numquam! Cupiditate molestiae, similique vitae numquam modi eos libero beatae consequuntur eaque labore enim quibusdam laudantium, illo!</p> 
            </div>
        </div>
        <hr>
        <div class="row justify-content-center">
            <div class="col-10">
				<h5>My courses</h5>
				<p>
				<p>
                <table style="width:100%">
					<tr>
						<th style="min-width:200px"><font size="2">Certificate</font></th> 
						<th style="min-width:1px"><font size="2"></font></th>
						<th style="min-width:20px"><font size="2">Tech</font></th> 
						<th style="min-width:5px"><font size="2"></font></th>
						<th style="min-width:200px"><font size="2">Projects</font></th> 
						<th style="min-width:5px"><font size="2"></font></th>
					</tr>
				'''

html_string_open2 = '''
				</table>
				<p></p>
				<p></p>
            </div>
        </div>
        <hr>
        <div class="row justify-content-center">
            <div class="col-10">
                <h6>My attitude towards learning</h6>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab mollitia deleniti minus maiores doloremque assumenda Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero fugit culpa ad quod sed quis, dolores ut nostrum saepe suscipit?  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corporis vero reprehenderit ut, sapiente numquam! Cupiditate molestiae, similique vitae numquam modi eos libero beatae consequuntur eaque labore enim quibusdam laudantium, illo!</p>
                '''

html_table = '''
				<p>
				<p>
                <table style="width:100%">
					<tr>
						<th style="min-width:200px"><font size="2">Certificate</font></th> 
						<th style="min-width:15px"><font size="2"></font></th>
						<th style="min-width:200px"><font size="2">Description & Projects</font></th> 
						<th style="min-width:15px"><font size="2"></font></th>
						<th style="min-width:100px"><font size="2">Tech</font></th> 
						<th style="min-width:5px"><font size="2"></font></th>
					</tr>
				'''



html_string_end = '''
				</table>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo eum incidunt nesciunt totam, necessitatibus deleniti Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit necessitatibus adipisci, aliquam laudantium quis! Est minima, ratione nobis vel impedit? Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio veritatis quasi numquam illum, quos, rem voluptatibus possimus fuga ipsa odio sunt amet distinctio cupiditate sequi maxime sapiente esse qui. Deserunt.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nam officiis at facilis architecto dolor quae, perspiciatis molestiae quam fuga laudantium?</p>
            </div>
        </div>
        <div class="row footer">
            <p>Courses portfolio</p>
        </div>
    </div>
    <!-- BOOTSTRAP 4 SCIPTS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

    <!-- PROJECT SCRIPTS -->
    <script src="js/scripts.js"></script>
</body>

</html>'''


#html_string_mid_0 = "".join(coursera_titles)
#html_string_packs = "".join(coursera_html_packs)

html_string = html_string_open + html_string_mid_0 + html_string_open2 + html_table + html_string_packs + html_string_end
f = open('/home/l/CV_kursy/KnowledgePortfolio/coursery.html','w+')
f.write(html_string)
f.close()
