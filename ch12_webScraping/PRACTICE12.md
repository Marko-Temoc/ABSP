1. from the top of page: 'webbrowser' comes with python and opens a browser to a specific page,
'requests' downloads files and web pages from the internet,
'bs4' parses HTML, the format that web pages are written in,
'selenium' launches and controls a web browser; can fill in forms, simulate mouse clicks, and key presses
2. a Response object; the `.text` attribute of said object
3. `.raise_for_status()`
4. access the `.status_code` attribute of the Response object
5. its a multi-step process to save a requests response file:
   1. call `requests.get('url')` to get a Response object
   2. call `open()` with 'wb' as second argument
   3. call the `.iter_content(100000)` method, and iterate on the resulting generator object, with each
   iteration writing a chunk to the desired file
   ```
   for chunk in responseObject.iter_content(100000):
       theFile.write(chunk)
   ```
6. F12 apparently
7. go to 'Inspect Element'
8. '#main'
9. '.highlight'
10. 'div div'
11. 'button[value='favorite']
12. `spam.getText()`
13. `linkElem = spam.attrs`
14. `from selenium import webdriver`
15. `find_element()` returns a single Web Element of first match, while `find_elements()`
returns a list of each WebElement matched
16. `.clikc()` and `.send_keys()`
17. WebElement method `.submit()`
18. WebDriver methods `.forward()`, `.back()`, `.refresh()`
