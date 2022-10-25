"""
<a class="navbar-brand" id="logo" href="/">Formy</a>
Un tag de tip a (anchor) este folosit pt link-uri
Acesta trebuie sa aiba in mod obligatoriu un atribut numit href (hiperreference),
care reprezinta locatia la care ne va duce link-ul

putem selecta un tag de tip a folosind LINK_TEXT sau PARTIAL_LINK_TEXT.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

formy_link = chrome.find_element(By.LINK_TEXT,"FORMY")
formy_link.click()
time.sleep(2)

complete_form_link = chrome.find_element(By.LINK_TEXT, "Complete Web Form")
complete_form_link.click()
time.sleep(2)

formy_link = chrome.find_element(By.LINK_TEXT,"FORMY")
formy_link.click()
time.sleep(2)

drag_link = chrome.find_element(By.PARTIAL_LINK_TEXT,"Drag and")
drag_link.click()
time.sleep(2)


