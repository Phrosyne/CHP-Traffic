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
    
    #6 elements per row
def accident_type(driver, collection):
    table = driver.find_elements(by=By.CLASS_NAME, value="gvRow")
    blueRows = driver.find_elements(by=By.CLASS_NAME, value="gvAltRow")
    table.extend(blueRows)
    
    for child in table:
        columns = child.find_elements(by=By.TAG_NAME, value="td")
        
        for c in columns:
            collection.append(c.text)
            
def fillArrays(time, type, location, area, rows):
    length = int(len(rows) / 7)
    map = {}
    
    # for i in range(0, length):
    #     cell = rows[i]
    #     for j in range(0, 120):
    #         if i == 2 + (7 * j):
    #             time.append(cell)
    #         if i == 3 + (7 * j):
    #             type.append(cell)
    #         if i == 4 + (7 * j):
    #             location.append(cell)
    #         if i == 6 + (7 * j):
    #             area.append(cell)      
                
    for i in range(0, length):
        cell = rows[i]        
        multiplier = 7 * i
        
        timeIndex = multiplier + 2
        typeIndex = multiplier + 3
        locationIndex = multiplier + 4
        areaIndex = multiplier + 6
        
        time.append(rows[timeIndex])
        type.append(rows[typeIndex])
        location.append(rows[locationIndex])
        area.append(rows[areaIndex])
        

    
    """
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> map = new HashMap<>();
        
            for (int i = 0; i < nums.length; i++) {
                int key = target - nums[i];
                if (map.containsKey(key)) {
                    return new int[] {map.get(key), i};
                } else {
                    map.put(nums[i], i);
                }
            }
        
            return new int[] {};
        }
    }
    """
    
            

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()

    reach_page(driver)

    rows = []
    accident_type(driver, rows)
    
    #six elements per row
    
    time = []
    type = []
    location = []
    area = []
    
    fillArrays(time, type, location, area, rows)
            
    print(time)
    print(type)
    print(location)
    print(area)
    
    
    
if __name__ == "__main__":
    main()