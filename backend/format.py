from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

CommunicationCenter = "Los Angeles"

def reach_page(driver):
    driver.get("https://cad.chp.ca.gov/")  
    wait = WebDriverWait(driver, timeout=2)
        
    firstBox = driver.find_element(by=By.NAME, value="ddlComCenter")
    
    wait.until(lambda _ : firstBox.is_displayed())  

    submit = driver.find_element(by=By.NAME, value="btnCCGo")

    wait.until(lambda _ : submit.is_displayed())  
    
    firstBox.click()
    firstBox.send_keys(CommunicationCenter)
    
    submit.click()
    
    #6 elements per row

def accident_type(driver, collection):
    table = driver.find_elements(by=By.CLASS_NAME, value="gvRow")
    blueRows = driver.find_elements(by=By.CLASS_NAME, value="gvAltRow")
    table.extend(blueRows)
    
    for child in table:
        columns = child.find_elements(by=By.TAG_NAME, value="td")
        
        for c in columns:
            collection.append(c.text)
            
def getData(time, type, location, area, rows):
    length = int(len(rows) / 7)
                
    for i in range(0, length):      
        multiplier = 7 * i
        
        timeIndex = multiplier + 2
        typeIndex = multiplier + 3
        locationIndex = multiplier + 4
        areaIndex = multiplier + 6
        
        time.append(rows[timeIndex])
        type.append(rows[typeIndex])
        location.append(rows[locationIndex])
        area.append(rows[areaIndex])
        
    return time

def querySequence(driver, rows, time, type, location, area):
    reach_page(driver)
    accident_type(driver, rows)
    getData(time, type, location, area, rows)