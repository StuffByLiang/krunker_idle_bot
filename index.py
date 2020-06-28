import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

acceptTermsButton = '/html/body/div[2]/div[5]/div/div/div[2]/div[2]'
gameCanvas = '/html/body/canvas[2]'
instructions = '//*[@id="instructions" and contains(text(), "CLICK")]'
path = r"C:\Users\lili3\Documents\python\geckodriver-v0.26.0-win64\geckodriver.exe"

def thread_function(arg):
  header = "Thread " + str(arg) + ": " 
  opts = webdriver.FirefoxOptions()
  # opts.add_argument("--headless")
  opts.add_argument("--width=400")
  opts.add_argument("--height=400")
  driver = webdriver.Firefox(options=opts, executable_path=path)
  driver.get("https://krunker.io/?game=SV:" + url)

  send_space = ActionChains(driver).send_keys(Keys.SPACE)

  while True:
    try:
      element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, acceptTermsButton)))
      element.click()
      print(header + "accepted the terms & conditions")
      break
    except TimeoutException:
      print(header + "retrying accepting terms & conditions")
      # driver.save_screenshot('test.png')

  while True:
    try:
      element = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, instructions)))
      driver.find_element(By.XPATH, gameCanvas).click()
      print(header + "clicked!")
    except TimeoutException:
      # in game
      send_space.perform()
      print(header + "sending space to prevent afk")
  driver.close()
  
if __name__ == "__main__":
  nThreads = int(input("No of threads\n"))
  url = input("Enter server code\n")
  for index in range(nThreads):
      x = threading.Thread(target=thread_function, args=(index,))
      x.start()