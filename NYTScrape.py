# Theodore Chu
# February 2, 2017
# For the USC Lab on Non-Democratic Politics under the direction of Erin Ashley Baggott and Brett Logan Carter
# Scrapes the NYT public archive. A login is required
# Use ISO-8859-1 Encoder to read the txt files

# the archive has 30m articles over 1851-present.
# there are no terms of service issues with scraping the NYT public archive; scraping is not prohibited.
# the archive freezes after 1000 results (100 pages), which is ~2 days.
# so I'm going to tear down the browser every day.

# from __future__ import division # this lets you divide numbers and get floating results
import math  # this lets you do math
import re  # this lets you make string replacements: 'hi there'.replace(' there') --> 'hi'
import os  # this lets you set system directories
import time  # this lets you slow down your scraper so you don't crash the website =/
import codecs  # symbols are annoying. this lets you replace them.
import random  # this lets you draw random numbers.
import datetime  # this lets you create a list of dates
from datetime import timedelta  # same
from selenium import webdriver  # the rest of these let you create your scraper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# set your working directory
writedir = 'C:\\Users\\Theodore\\Desktop\\Programming\\Scraping\\'


#prompt for start date
#prompt for end date
#name the file out
#load first date
#get the number of results
#go to the first page on the first date
#get all links from the first page on the first date
#go to each article from first page on first date. print to file
#repeat for all links on first date (for loop)
#repeat for all dates until the last date (for loop)


#def resultsdate(startdate, enddate, directry, fileOut):

class nytScrape(object):
    def __init__(self, directory, fileOut):
        self.__driver = webdriver.Firefox()
        self.__fileOut = open(directory + fileOut, "a")
        self.__pageCounter = 0


    def login(self):
        print("Warning: You have reached 10 articles. You will not be able to view full articles unless you log in.")
        login = input("Would you like to login? (y/n):")
        if login == "y":
            username = input("Input username/email:")
            password = input("Input password (case sensitive):")


            self.__driver.get("https://myaccount.nytimes.com/auth/login")
            emailelement = self.__driver.find_element_by_name("userid")
            emailelement.send_keys(username)
            passwordelement = self.__driver.find_element_by_name("password")
            passwordelement.send_keys(password)
            passwordelement.send_keys(Keys.RETURN)
            time.sleep(random.uniform(10, 15))


    def formatDate(self, unformatteddate):
        date = datetime.datetime.strptime(unformatteddate, "%Y%m%d")
        return date

    def urlDate(self, formattedDate):
        date = str(formattedDate).split(' ')[0].replace('-', '')
        return date

    def loadFirstResultsPage(self, date, query):
        date = self.urlDate(date)
        if query == "none":
            query = "*"
        firstPage = 'http://query.nytimes.com/search/sitesearch/#/' + query + '/from' + str(date) + 'to' + str(date) + '/document_type%3A%22article%22/1'
        self.__driver.get(firstPage)


    def getNumberOfResultsPages(self):
        resultsdiv = self.__driver.find_element_by_id('totalResultsCount')
        results = resultsdiv.text
        print('Results:', results)
        results = results.split(' Result')[0]
        results = results.split(' ')[(len(results.split(' ')) - 1)]
        results = int(results)
        resultPages = math.ceil(results / 10)
        print('Result pages:', resultPages)
        time.sleep(random.uniform(2, 10))
        return resultPages

    def goToNextResultsPage(self, date, numResultsPages, query):
        date = self.urlDate(date)
        print("page", numResultsPages, "done")     # put at end of each page rather than beginning
        if query == "none":
            query = "*"
        nextPage = "http://query.nytimes.com/search/sitesearch/#/" + query + "/from" + str(date) + 'to' + str(date) + '/document_type%3A%22article%22/' + str(numResultsPages)
        self.__driver.get(nextPage)
        print("Getting nextPageURL:", nextPage)
        time.sleep(random.uniform(2, 5))

    def getSubLinks(self):
        div = self.__driver.find_element_by_id('searchResults')
        # linkdata = div.find_element_by_class_name("story")
        linkdata = div.find_elements_by_tag_name("li")
        linksList = []
        for data in linkdata:
            link = data.find_element_by_css_selector('a').get_attribute('href')
            print(link)
            linksList.append(link)
        print("List of links:", linksList, end="\n")
        time.sleep(random.uniform(5, 10))
        return linksList

    # I'm still playing around with the ways to get sublinks. Here is another way.
    # This method doesn't work as well because not all articles in the search have "story" as their class. Some have "story no thumb" if they don't have a thumbnail photo
    """
    def getSubLinks(self):
        div = self.__driver.find_element_by_id('searchResults')
        time.sleep(random.uniform(5, 10))
        linkdata = div.find_elements_by_class_name('story')
        links = []
        for data in linkdata:
            link = data.find_element_by_css_selector('a').get_attribute('href')
            print(link)
            links.append(link)
            return links"""


    def printFullPageText(self, linksList): # I'm exploring different ways to write into the file: print(text, file=filename), f.write, utf-8
        for url in linksList:
            self.__driver.get(url)
            time.sleep(random.uniform(1, 10))

            # Print article title, date, and author
            article = self.__driver.find_element_by_id('story')
            header = article.find_element_by_id("story-header")
            title = article.find_element_by_id("headline")
            authorDate = header.find_element_by_css_selector("p")

            #Title
            titleText = title.text
            print(titleText)
            #titleUTF = titleText.encode("utf-8")
            print(titleText, file=self.__fileOut)
            #self.__fileOut.write(titleUTF)


            #Author and Date
            authorDateText = authorDate.text
            print(authorDateText)
            #authorDateUTF = authorDateText.encode("utf-8")
            print(authorDate.text, file=self.__fileOut)
            #self.__fileOut.write(authorDateUTF.text.encode("utf-8"))


            # Print the story in the article
            storydata = article.find_elements_by_css_selector(".story-body-text.story-content")
            for story in storydata:
                print(story.text)
                print(story.text, file=self.__fileOut)
                #self.__fileOut.write(story.text.encode("utf-8"))
            self.__pageCounter += 1
            print("Article", self.__pageCounter, "printed")
            print("Article", self.__pageCounter, "printed", file=self.__fileOut)
            print("\n\n************************************\n\n", file=self.__fileOut)
            print("\n\n************************************\n\n")
            # Adjust counter for login
            time.sleep(random.uniform(2, 5))
            if self.__pageCounter == 10:
                self.login()


# Need to make inputs their own functions for error checking
def main():
    # Initial inputs
    startdate = input("Enter Start Date (ex: 20170101):")
    enddate = input("Enter End Date (ex: 20170201):")
    directory = input("Enter Directory: (ex: C:/Users/Theodore/Desktop/Programming/Scraping/). Press Enter for example:")
    if directory == "":
        directory = "C:/Users/Theodore/Desktop/Programming/Scraping/"
    fileOutName = input("FileOutName (ex: nyt2017.txt):")
    if ".txt" not in fileOutName:
        fileOutName = fileOutName + ".txt"
    queryInput = input("Insert search term (if none, enter \"none\"):")
    query = queryInput.strip()


    # Main loop
    nyt = nytScrape(directory, fileOutName)
    startdate = nyt.formatDate(startdate)
    enddate = nyt.formatDate(enddate)
    nyt.loadFirstResultsPage(startdate, query)
    while startdate <= enddate:
        results = nyt.getNumberOfResultsPages()
        for n in range(1, results + 1, 1):
            print('Page ' + str(n) + ' of ' + str(results))
            linksList = nyt.getSubLinks()
            nyt.printFullPageText(linksList)
            nyt.goToNextResultsPage(startdate, n+1, query)
        startdate += timedelta(days=1)

main()