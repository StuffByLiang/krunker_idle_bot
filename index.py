import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


acceptTermsButton = '/html/body/div[2]/div[5]/div/div/div[2]/div[2]'
gameCanvas = '/html/body/canvas[2]'
instructions = '//*[@id="instructions" and contains(text(), "PLAY")]'
path = r"D:\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe"
chromePath = r"D:\Downloads\chromedriver_win32\chromedriver.exe"

def thread_function(arg):
  header = "Thread " + str(arg) + ": " 
  # opts = webdriver.FirefoxOptions()
  # opts.add_argument("--headless")
  # d = DesiredCapabilities.FIREFOX
  # d['loggingPrefs'] = {'browser': 'ALL'}
  # # opts.add_argument("--width=400")
  # # opts.add_argument("--height=400")
  # driver = webdriver.Firefox(capabilities=d, options=opts, executable_path=path)

  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
  # driver = webdriver.Chrome(options=chrome_options, executable_path = chromePath)
  driver = webdriver.Chrome(options=chrome_options)

  driver.get("https://krunker.io/?game=SV:" + url)

  print(driver.execute_script("""
    console.error=function(msg){
      window.errs.push(msg);
    };
    console.log("bitch");
    window.errs = [];
    return "lol"
  """))

  send_space = ActionChains(driver).send_keys(Keys.SPACE)

  while True:
    try:
      element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, acceptTermsButton)))
      element.click()
      print(header + "accepted the terms & conditions")
      driver.save_screenshot('test.png')
      break
    except TimeoutException:
      print(header + "retrying accepting terms & conditions")
      # for entry in driver.get_log('browser'):
      #   print(entry)  
      print (driver.execute_script("return window.errs;"))
      driver.save_screenshot('test.png')

  while True:
    try:
      element = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, instructions)))
      driver.find_element(By.XPATH, gameCanvas).click()
      # driver.switch_to.window(driver.current_window_handle)
      print(header + "clicked!")
      driver.save_screenshot('test.png')
    except TimeoutException:
      # in game
      send_space.perform()
      print(header + "sending space to prevent afk")
      driver.save_screenshot('test.png')
  driver.close()
  
if __name__ == "__main__":
  nThreads = int(input("No of threads\n"))
  url = input("Enter server code\n")
  for index in range(nThreads):
      x = threading.Thread(target=thread_function, args=(index,))
      x.start()