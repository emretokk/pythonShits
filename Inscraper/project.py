from keops import welcomekeops
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

welcomekeops()

#users' class
class User:
    user_name = ""
    user_tname = ""
    user_profile = ""
    user_counts = {}
    user_bio = ""
    user_followers = []
    user_followings = []

#variables
myusername = "emre.tok05"
mypassword = "şevval52207+"
myprofile = "https://www.instagram.com/{}/".format(myusername)
mydata = {
    "username": myusername,
    "password": mypassword,
    "profileurl": myprofile,
    "counts": {},
    "bio": "",
    "followers": [],
    "followings": []
}

#opens chrome driver
def opendriver():
    global driver_path
    driver_path = "chromedriver"
    global driver
    driver = webdriver.Chrome(driver_path)

#signin's to instagram
def signin():
    opendriver()
    driver.get(
        "https://www.instagram.com/accounts/login/?source=private_profile")
    sleep(2)
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    login_button = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    username.send_keys(myusername)
    password.send_keys(mypassword)
    login_button.click()
    sleep(3)

#goes to url
def goto(url):
    driver.get(url)
    sleep(2)

#gets my profile's detailed info 
def getmyinfo():
    driver.get(myprofile)
    sleep(2)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    counts = soup.find_all("span", attrs={"class": "g47SY"})
    post_count = counts[0].text
    follower_count = counts[1].text
    following_count = counts[2].text
    bio = soup.find("div", attrs={"class": "-vDIg"}).text
    mydata["bio"] = bio
    mydata["counts"] = {
        "post": post_count,
        "follower": follower_count,
        "following": following_count
    }
    follower_element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    follower_element.click()
    sleep(2)
    scroll_follower_element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    follower_scroll_count = ((int(follower_count) // 6) + 1) * 2
    follower_scroll_time = 0
    while follower_scroll_time <= follower_scroll_count:
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_follower_element)
        sleep(0.6)
        follower_scroll_time += 1
    page_source1 = driver.page_source
    soup1 = BeautifulSoup(page_source1, "html.parser")
    myfollowers = soup1.find_all("a", attrs={"class": "FPmhX"})
    for myfollower in myfollowers:
        mydata["followers"].append(myfollower.text)
    driver.get(myprofile)
    sleep(1)
    following_element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    following_element.click()
    sleep(2)
    scroll_following_element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    following_scroll_count = ((int(following_count) // 6) + 1) * 2
    following_scroll_time = 0
    while following_scroll_time <= following_scroll_count:
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_following_element)
        sleep(0.6)
        following_scroll_time += 1
    page_source2 = driver.page_source
    soup2 = BeautifulSoup(page_source2, "html.parser")
    myfollowings = soup2.find_all("a", attrs={"class": "FPmhX"})
    for myfollowing in myfollowings:
        mydata["followings"].append(myfollowing.text)
    close_button = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div/div[1]/div/div[2]/button")
    close_button.click()
    return mydata

#gets the detailed info of an user
def getinfo(username):
    signin()
    getbasicinfo([username])
    follower_element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    follower_element.click()
    sleep(2)
    scroll_follower_element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    follower_scroll_count = ((int(users[username].user_counts["follower"]) // 6) + 1) * 2
    follower_scroll_time = 0
    while follower_scroll_time <= follower_scroll_count:
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_follower_element)
        sleep(0.6)
        follower_scroll_time += 1
    page_source1 = driver.page_source
    soup1 = BeautifulSoup(page_source1, "html.parser")
    followers = soup1.find_all("a", attrs={"class": "FPmhX"})
    for follower in followers:
        users[username].user_followers.append(follower.text)
    driver.get(users[username].user_profile)
    sleep(1)
    following_element = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    following_element.click()
    sleep(2)
    scroll_following_element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    following_scroll_count = ((int(users[username].user_counts["following"]) // 6) + 1) * 2
    following_scroll_time = 0
    while following_scroll_time <= following_scroll_count:
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll_following_element)
        sleep(0.6)
        following_scroll_time += 1
    page_source2 = driver.page_source
    soup2 = BeautifulSoup(page_source2, "html.parser")
    followings = soup2.find_all("a", attrs={"class": "FPmhX"})
    for following in followings:
        users[username].user_followings.append(following.text)
    close_button = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div/div[1]/div/div[2]/button")
    close_button.click()

#gets the infos of every user in a list  
def getbasicinfo(userslist):
    global users
    users = {}
    for username in userslist:
        users[username] = User()
        users[username].user_name = username
        users[username].user_profile = "https://instagram.com/{}/".format(
            users[username].user_name
        )
        # r = requests.get("https://instagram.com/{}".format(username))
        # soup = BeautifulSoup(r.text,"html.parser")
        # counts = soup.find_all("span", class_="g47SY")
        # bio = soup.find("div", class_="-vDIg")
        # post_count = counts[0].text
        # follower_count = counts[1].text
        # following_count = counts[2].text
        # this is not working because the these elements are loading dynamically

        #with help :)
        r = requests.get("https://instagram.com/{}".format(username))
        
        soup = BeautifulSoup(r.content,"html.parser")
        
        element = soup.find("meta",{"property":"og:description"})
        counts = element.get("content").split(", ")
        follower_count = counts[0]
        following_count = counts[1].strip()
        post_count = counts[2].split("-")[0].strip()
        name = counts[2].split("from")[1].strip().rsplit(" ",1)[0]
        users[username].user_counts = {
            "post": post_count,
            "follower": follower_count,
            "following": following_count
        }
        users[username].user_tname = name
        element1 = soup.find("script",{"type":"application/ld+json"}).text
        attrs = element1.strip().split(",")
        for attr in attrs:
            if attr.startswith('"description"'):
                bio = attr.split(":")[1]
                users[username].user_bio = bio

signin()
