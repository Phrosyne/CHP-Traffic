from selenium import webdriver
from selenium.webdriver.common.by import By

#KEEP BROWSER OPEN
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
CommunicationCenter = "Los Angeles"
time = []
driver = webdriver.Chrome()

driver.get("https://cad.chp.ca.gov/")

def reach_page():
    firstBox = driver.find_element(by=By.NAME, value="ddlComCenter")
    submit = driver.find_element(by=By.NAME, value="btnCCGo")
    firstBox.click()
    firstBox.send_keys(CommunicationCenter)
    submit.click()
    
    
def accident_type():
    return driver.find_elements(by=By.TAG_NAME, value="td")
    
driver.implicitly_wait(0.5)

reach_page()
list = accident_type()

allFields = ""
for cell in list:
    allFields = allFields + f"{cell.text}"
    
row = allFields.split("Details")

len = len(row)

#Trimming the No. from each row
for i in range(0, len):
    row[i] = row[i][4:]
    time.append(row[i][:7])
print(row)
time.pop(0)
print(time)