'''
Created on 10 Aug 2022

@author: joris.verhulst
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from google.protobuf.internal import containers
#from hyperframe.frame import DataFrame



url ="https://test-dtxgo-portal.medicim.local/#/shared-cases?caseId=cad800cb-4ffa-4529-b71f-23a5c28f03ed"
path ="C:/Users/joris.verhulst/OneDrive - Envista/Documents/Chromedriver/chromedriver.exe"
filepath = "C:/DTX Studio/Clinic17"
options = Options()
options.headless = False
#wb = Workbook()
#wb.save(filepath)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
driver.implicitly_wait(2)
cookiebutton = driver.find_element(by ="xpath", value='//*[@id="Username"]')
cookiebutton.send_keys("joris.verhulst2")
cookiebutton = driver.find_element(by ="xpath", value='//*[@id="Password"]')
cookiebutton.send_keys("Tester%123")
cookiebutton = driver.find_element(by ="xpath", value='//*[@id="btnLogin"]')
cookiebutton.click()
cookiebutton = driver.find_element(by ="xpath", value='//*[@id="lnkNAVIGATION.Logout"]')
cookiebutton.click()
containers= driver.find_elements(by ="xpath", value='div[@class="teaser__copy-container"]')
print(containers)


#subtitles= []
#links= []

#for container in containers:

    #subtitle = container.find_element(by="xpath", value = './a/p').text
    #link = container.find_element(by='xpath', value = './a').get_attribute("href")
    #titles.append(title)
    #subtitles.append(subtitle)
    #links.append(link)
#excel_writer = pd.ExcelWriter(excel_file_pathn,engine='xlsxwriter')
#my_dictionary = {'titles':titles}   
#df_headlines = pd.DataFrame(my_dictionary)
#print(df_headlines)
#writer = pd.ExcelWriter('output.xlsx')#
#"df_headlines.to_excel(writer)
#writer.save()

print('DataFrame is written successfully to Excel File.')
