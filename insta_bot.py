#code by vitthal
#code for insta bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Initializing....")
print("STARTING....")
def path():
    global obj_drive
    obj_drive=webdriver.Chrome(executable_path="C://Users/DELL/Desktop/CODING/chromedriver.exe")


username="Your email"                      #you can also link it from file
#print("Enter password")                   # with open('test.txt', 'r') as myfile:   
                                           #Password = myfile.read().replace('\n', '') 
                                           # user.send_keys(Password)       
password="Your password"
#print("enter url")
url="https://www.instagram.com/"

def url_name(url):
    obj_drive.get(url)
    time.sleep(3)
#login into insta
def login(username,pass_word):
    log_but=obj_drive.find_element_by_class_name("L3NKy")
    time.sleep(2)
    #click th login button
    log_but.click()
    time.sleep(3)
    #find the username box
    usern=obj_drive.find_element_by_name("email")
    #send the username
    usern.send_keys(username)
    #find the pass
    passw=obj_drive.find_element_by_name("pass")
    #send the entered password
    passw.send_keys(pass_word)
def fblog():
    log_cl=obj_drive.find_element_by_class_name("_4jy6")
    log_cl.click()
    time.sleep(3)
#liking first pi
def pic():
    pic=obj_drive.find_element_by_class_name("_9AhH0")
  #  pic.click()

def like_pics():
    
    like=obj_drive.find_element_by_class_name('_8-yf5')
    time.sleep(2)
    like.click()
def next_picture(): 
	time.sleep(2) 

	# finds the button which gives the next picture 
	nex = obj_drive.find_element_by_class_name("HBoOv") 
	time.sleep(1) 
	return nex 

#def continue():
def continue_liking(): 
	while(True): 
		next_elm = next_picture() 

		# if next button is there then 
		if next_elm != False: 

			# click the next button 
			next_elm.click() 
			time.sleep(2) 

			# like the picture 
			like_pics()	 
			time.sleep(2)			 
		else: 
			print("not found") 
			break
    
    

if __name__=="__main__":
    
    path()
    url_name(url)
    login(username,password)
    fblog()
    pic()
    like_pic()
    continue_liking()
    
