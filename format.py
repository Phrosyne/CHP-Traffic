from selenium import webdriver
from selenium.webdriver.common.by import By

CommunicationCenter = "Los Angeles"

#KEEP BROWSER OPEN
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

def reach_page(driver):
    driver.get("https://cad.chp.ca.gov/")    
    firstBox = driver.find_element(by=By.NAME, value="ddlComCenter")
    submit = driver.find_element(by=By.NAME, value="btnCCGo")
    firstBox.click()
    firstBox.send_keys(CommunicationCenter)
    submit.click()
    
    
def accident_type(driver):
    br = driver.find_elements(by=By.TAG_NAME, value="td")
    allFields = ""
    for cell in br:
        allFields = allFields + cell.text
        
    return allFields.split("Details")
    
def getTime(collection, time):    
    length = len(collection)
    #Trimming the No. from each row; if/elif is for the ones that have 2 digits in hour
    for i in range(0, length):
        if collection[i][1:2] == ':':
            time.append(collection[i][:7])
        elif collection[i][2:3] == ':':
            time.append(collection[i][:8])

def getType(collection, type):
    length = len(collection)
    collection = ""
    
    # for i in range(0, length):
        
        

def main():
    driver = webdriver.Chrome()
    reach_page(driver)

    collection = accident_type(driver)
    
    for c in collection:
        c = c[4:]
        print(c)
            
    time = []
    getTime(collection, time)
    
    type = []
    getType(collection, type)
    
    # print(time)
    
    
    
if __name__ == "__main__":
    main()