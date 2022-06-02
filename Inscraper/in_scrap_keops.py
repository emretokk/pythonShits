from keops import welcomekeops
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import requests

welcomekeops()


class User:
    user_name = ""
    user_profile = ""
    user_counts = {}
    user_bio = ""
    user_followers = []
    user_followings = []


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


def opendriver():
    global driver_path
    driver_path = "../Drivers/chromedriver"
    global driver
    driver = webdriver.Chrome(driver_path)


def signin():
    opendriver()
    driver.get(
        "https://www.instagram.com/accounts/login/?source=private_profile")
    sleep(3)
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    login_button = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[3]/button')
    username.send_keys(myusername)
    password.send_keys(mypassword)
    login_button.click()
    sleep(4)


def goto(url):
    driver.get(url)
    sleep(2)


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


def getbasicinfo(userslist):
    opendriver()
    global users
    users = {}
    for username in userslist:
        users[username] = User()
        users[username].user_name = username
        users[username].user_profile = "https://instagram.com/{}/".format(
            users[username].user_name
        )
        driver.get(users[username].user_profile)
        sleep(2)
        page_source = driver.page_source
        print(page_source)
        soup = BeautifulSoup(page_source, "html.parser")
        print(soup.text)
        counts = soup.find_all("span", attrs={"class": "g47SY"})
        bio = soup.find("div", attrs={"class": "-vDIg"})
        post_count = counts[0].text
        follower_count = counts[1].text
        following_count = counts[2].text
        users[username].user_counts = {
            "post": post_count,
            "follower": follower_count,
            "following": following_count
        }
        users[username].user_bio = bio


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

opendriver()
driver.get("https://www.google.com")