"""
1.
For http://query.nytimes.com/gst/fullpage.html?res=9D03E6DD1E3AF932A35752C0A9609D8B63
Traceback (most recent call last):
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 189, in <module>
    main()
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 185, in main
    nyt.printFullPageText(linksList)
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 134, in printFullPageText
    article = self.__driver.find_element_by_id('story')
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 269, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 752, in find_element
    'value': value})['value']
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 236, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 192, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="story"]

2.
Getting nextPageURL: http://query.nytimes.com/search/sitesearch/#/Trump/from20160105to20160105/document_type%3A%22article%22/1
Traceback (most recent call last):
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 272, in <module>

  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 263, in main
    while startdate <= enddate:
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 73, in getNumberOfResultsPages
    results = int(results)
ValueError: invalid literal for int() with base 10: ''

3. Getting nextPageURL: http://query.nytimes.com/search/sitesearch/#/Trump/from20160106to20160106/document_type%3A%22article%22/1
page 2 of 2
Traceback (most recent call last):
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 288, in <module>

  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 282, in main
    print('page ' + str(n) + ' of ' + str(results))
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 116, in getSubLinks
    for data in linkdata:
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webelement.py", line 307, in find_element_by_css_selector
    return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webelement.py", line 511, in find_element
    {"using": by, "value": value})['value']
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webelement.py", line 494, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 236, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 192, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: a


4.
http://www.nytimes.com/aponline/2016/01/05/us/ap-us-making-a-murderer-qa.html
Traceback (most recent call last):
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 203, in <module>
    nyt.goToNextResultsPage(startdate, n, query)
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 199, in main
    for n in range(1, results + 1, 1):
  File "C:/Users/Theodore/Desktop/Programming/Python/NYTScrape.py", line 136, in printFullPageText
    time.sleep(random.uniform(1, 10))
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 269, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 752, in find_element
    'value': value})['value']
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 236, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Theodore\Python36\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 192, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="story"]


"""