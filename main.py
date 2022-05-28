
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "D:/chromedriver/chromedriver.exe"
file = open('videos.txt', 'w')

driver = webdriver.Chrome(PATH)
print("Paste the link to the playlist: ")
playlist = input()
scroll = True
driver.get(playlist)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span').click()
numberOfVideos = driver.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]/span[1]')
numberOfVideos = numberOfVideos.get_attribute('innerHTML')
stringNumberOfVideos = str(numberOfVideos)
videosList = driver.find_elements_by_xpath('//*[@id="video-title"]')

videos = []
for i in range(len(videosList)):
    videoLink = videosList[i].get_attribute('href')

    if ('index=' + stringNumberOfVideos) not in videoLink:
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(0.5)
    else:
        break

videosList = driver.find_elements_by_xpath('//*[@id="video-title"]')
file = open("videos.txt", "w")
for i in range(len(videosList)):
    videoLink = videosList[i].get_attribute('href')
    print(videoLink)
    file.write(videoLink)
    file.write('\n')

file.close()
time.sleep(100)
driver.quit()