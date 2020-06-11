import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


acceptTermsButton = '/html/body/div[2]/div[5]/div/div/div[2]/div[2]'
gameCanvas = '/html/body/canvas[2]'
instructions = '//*[@id="instructions" and contains(text(), "CLICK")]'

def thread_function(arg):
  driver = webdriver.Firefox(executable_path="D:\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")
  driver.get(url)

  element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, acceptTermsButton)))
  element.click()
  print("loaded = accepted terms")

  while True:
    try:
      element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, instructions)))
      driver.find_element(By.XPATH, gameCanvas).click()
      print("clicked!")
    except TimeoutException:
      print("timeout, retrying")
  driver.close()
  

nThreads = int(input("No of threads\n"))
url = input("Enter server url\n")
for index in range(nThreads):
    x = threading.Thread(target=thread_function, args=(0,))
    x.start()