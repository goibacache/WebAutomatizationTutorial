from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def downloadVideo(videoURL):
    print ("Downloading: "+videoURL+"\n")
    #Open the webpage to download from
    driver.get("https://www.onlinevideoconverter.com/es/mp3-converter")
    #Wait at least for the "Downloader-input" textbox
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "texturl")))
    #Write the video URL
    elem = driver.find_element_by_id("texturl")
    elem.clear()
    elem.send_keys(f"{videoURL}")
    elem.send_keys(Keys.RETURN)
    #Wait for the Download button
    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "downloadq")))
    #Find downloadq
    elem = driver.find_element_by_id("downloadq")
    url = elem.get_attribute('href')
    driver.get(url)
    #Wait 2 seconds just because
    time.sleep(2)
    

if __name__ == "__main__":
    
    #Read the links
    videoList = open("videoList.txt","r") 
    
    videoURLs = videoList.read().split('\n');
    
    print("Press Enter to start Downloading.")
    
    #Open the browser / Start the driver
    driver = webdriver.Chrome()
    print('\n') #Just because I can
    
    #Iterate each and every video
    for video in videoURLs:
        if video.startswith('#'):
            print ("Found Comment, skipping.\n")
        else:
            downloadVideo(video)

    driver.get("http://portal.pushbullet.com/")
        
# driver.close()
