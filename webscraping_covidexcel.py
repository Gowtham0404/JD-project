import pandas as pd #software library used for data manipulation and analysis
import numpy as np #Fast mathematical operations over arrays




from google.colab import drive
drive.mount('/content/drive')



 #used for webscrapping
!pip install selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin




def update_covid(link):
  import sys  #system-specific parameters and functions
  import pandas as pd
  # used fetch the data from the chrome driver
  sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
  from selenium import webdriver
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  wd.get(data)
  # identify elements with tagname <a>
  lnks=wd.find_elements_by_tag_name("a")
  for lnk in lnks:
    x=lnk.get_attribute("href") # get_attribute() to get all href
    
    if x.find("https://www.mohfw.gov.in/pdf/COVID19DistrictWisePositivity") != -1:
        file_path=x
        break
  wd.quit()
  xfiles=pd.read_excel(file_path) # reading excel file path
  row=xfiles[xfiles['Unnamed: 1'].str[0]=='S'].index.tolist()
  df=xfiles.iloc[row[0]:,1:7] 
  head=df.iloc[0]
  df=df[1:]
  df.columns=head
  df['State'].fillna(method='ffill',inplace=True) # filling the nan values as before value
  df['District'].fillna('Total',inplace=True) # filling the nan values as total
  df=df.reset_index() # resetting the index value
  df.drop(['index'],axis=1, inplace=True) # drop the index value
  df['S.No'].fillna('Total',inplace=True) # filling the nan values as total
  df=df[df['Positivity'].notna()]
  return df




data="https://www.mohfw.gov.in/" # read the url

data1=update_covid(data) # pushing the data to the function




data1.drop(data1.tail(1).index,inplace=True)




def update_covid(link):
  import sys  #system-specific parameters and functions
  import pandas as pd
  # used fetch the data from the chrome driver
  sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
  from selenium import webdriver
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  wd.get(data)
  # identify elements with tagname <a>
  lnks=wd.find_elements_by_tag_name("a")
  for lnk in lnks:
    x=lnk.get_attribute("href") # get_attribute() to get all href
    
    if x.find("https://www.mohfw.gov.in/pdf/COVID19DistrictWisePositivity") != -1:
        file_path=x
        break
  wd.quit()
  xfiles=pd.read_excel(file_path) # reading excel file path
  row=xfiles[xfiles['Unnamed: 8'].str[0]=='S'].index.tolist()
  df=xfiles.iloc[row[0]:,8:14] 
  head=df.iloc[0]
  df=df[1:]
  df.columns=head
  df['State'].fillna(method='ffill',inplace=True) # filling the nan values as before value
  df['District'].fillna('Total',inplace=True) # filling the nan values as total
  df=df.reset_index() # resetting the index value
  df.drop(['index'],axis=1, inplace=True) # drop the index value
  df['S.No'].fillna('Total',inplace=True) # filling the nan values as total
  df=df[df['Positivity'].notna()]
  return df
  




data2=update_covid(data)
data2.drop(data2.tail(1).index,inplace=True)
data2.tail()




def update_covid(link):
  import sys  #system-specific parameters and functions
  import pandas as pd
  # used fetch the data from the chrome driver
  sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
  from selenium import webdriver
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  wd.get(data)
  # identify elements with tagname <a>
  lnks=wd.find_elements_by_tag_name("a")
  for lnk in lnks:
    x=lnk.get_attribute("href") # get_attribute() to get all href
    
    if x.find("https://www.mohfw.gov.in/pdf/COVID19DistrictWisePositivity") != -1:
        file_path=x
        break
  wd.quit()
  xfiles=pd.read_excel(file_path) # reading excel file path
  row=xfiles[xfiles['Unnamed: 15'].str[0]=='S'].index.tolist()
  df=xfiles.iloc[row[0]:,15:21] 
  head=df.iloc[0]
  df=df[1:]
  df.columns=head
  df['State'].fillna(method='ffill',inplace=True) # filling the nan values as before value
  df['District'].fillna('Total',inplace=True) # filling the nan values as total
  df=df.reset_index() # resetting the index value
  df.drop(['index'],axis=1, inplace=True) # drop the index value
  df['S.No'].fillna('Grand Total',inplace=True) # filling the nan values as total
  df=df[df['Positivity'].notna()]
  return df




data3=update_covid(data)
data3




frames = [data1, data2, data3]

result = pd.concat(frames)




result