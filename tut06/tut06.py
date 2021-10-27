import re
import os
import shutil
def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")
	# if(os.path.exists('./corrected_srt')):
	# 	shutil.rmtree('corrected_srt')

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))
	if webseries_num==1:
		if(os.path.exists('./corrected_srt/Breaking Bad')):
			shutil.rmtree('corrected_srt/Breaking Bad')		
		shutil.copytree('wrong_srt/Breaking Bad/','corrected_srt/Breaking Bad')
		files=os.listdir('corrected_srt/Breaking Bad')
		for file in files:
			regex="(.*) s([0-9]{2})e([0-9]{2}) (.*)"
			match=re.match(regex,file)
			arr=re.split(r'\.',match.group(4))
			season=match.group(2).zfill(season_padding)
			episode=match.group(3).zfill(episode_padding)
			ext=arr[-1]
			fileName=match.group(1)
			new_fileName=fileName+' Season '+season+' Episode '+ episode+'.'+ext
			os.rename(os.path.join('corrected_srt/Breaking Bad',file),os.path.join('corrected_srt/Breaking Bad',new_fileName))
	elif webseries_num==2:
		if(os.path.exists('./corrected_srt/Game of Thrones')):
			shutil.rmtree('corrected_srt/Game of Thrones')		
		shutil.copytree('wrong_srt/Game of Thrones','corrected_srt/Game of Thrones')
		files=os.listdir('corrected_srt/Game of Thrones/')
		for file in files:
			regex="(.*)([0-9]{1})x([0-9]{2})(.*)"
			match=re.match(regex,file)
			arr=re.split(r'\.',match.group(4))
			season=match.group(2).zfill(season_padding)
			episode=match.group(3).zfill(episode_padding)
			episode_name=arr[0]			
			ext=arr[-1]
			fileName=match.group(1)
			new_fileName=fileName+'Season '+season+' Episode '+ episode+episode_name+'.'+ext
			os.rename(os.path.join('corrected_srt/Game of Thrones',file),os.path.join('corrected_srt/Game of Thrones',new_fileName))
	else:
		if(os.path.exists('./corrected_srt/Lucifer')):
			shutil.rmtree('corrected_srt/Lucifer')		
		shutil.copytree('wrong_srt/Lucifer','corrected_srt/Lucifer')
		files=os.listdir('corrected_srt/Lucifer/')
		for file in files:
			regex="(.*)([0-9]{1})x([0-9]{2})(.*)"
			match=re.match(regex,file)
			arr=re.split(r'\.',match.group(4))
			season=match.group(2).zfill(season_padding)
			episode=match.group(3).zfill(episode_padding)
			episode_name=arr[0]			
			ext=arr[-1]
			fileName=match.group(1)
			new_fileName=fileName+'Season '+season+' Episode '+ episode+episode_name+'.'+ext
			os.rename(os.path.join('corrected_srt/Lucifer',file),os.path.join('corrected_srt/Lucifer',new_fileName))		

regex_renamer()