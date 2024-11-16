from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# '/home/saol/Documents/selenium_NBA/chromedriver/chromedriver'
df = pd.DataFrame(columns=['Player','Salary','Year']) 
service = Service('chromedriver/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://hoopshype.com/salaries/players/')


#players = driver.find_elements(By.XPATH, '//td[@class="name"]')
#players_list = [player.text for player in players]

#salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')
#salaries_list = [salary.text for salary in salaries]

#---------------------------------------------------------------------------
for yr in range(2018,2019):
    page_num = f"{yr}-{yr+1}/"
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)


    players = driver.find_elements(By.XPATH, '//td[@class="name"]')
    salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')

    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)
    
    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)



    data_tuples = list(zip(players_list[1:],salaries_list[1:])) # list of each players name and salary paired together
    temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) # creates dataframe of each tuple in list
    temp_df['Year'] = yr # adds season beginning year to each dataframe
    df = pd.concat([df, temp_df], ignore_index=True) # appends to master dataframe
    
driver.close()

df.to_csv('nba_salaries.csv', index=False)
print("Данные сохранены в файл nba_salaries.csv")















#     #if len(players_list) == len(salaries_list):
#     # Создаём временный DataFrame для этого года
#     if players_list and salaries_list:
#         temp_df = pd.DataFrame({
#             "Player": players_list,
#             "Salary": salaries_list,
#             "Year": year
#         })
    
#     # Объединяем с основным DataFrame
#     master_df = pd.concat([master_df, temp_df], ignore_index=True)


# driver.quit()

# print(master_df)