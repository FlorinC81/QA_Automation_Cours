import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(1)


page_title = chrome.find_element(By.TAG_NAME, "h1")
print(page_title.text)


"""
Deoarece pot exista mai multe elemente cu acelasi tag,
metoda find_element il va gasi doar pe primul.
"""
imput_elem = chrome.find_element(By.TAG_NAME, "input")
imput_elem.send_keys("Acesta este primul input gasit")
time.sleep(2)


"""
Daca dorim sa luam toate inputurile, trebuie folosita metoda la plural (find_elements)
"""
imput_elements = chrome.find_elements(By.TAG_NAME, "input")
imput_elements[0].send_keys("First name here")
imput_elements[1].send_keys("Last name here")
imput_elements[2].send_keys("Job title here")
time.sleep(2)
