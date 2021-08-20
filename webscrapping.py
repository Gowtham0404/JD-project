

!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
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
  df=xfiles.iloc[:,15:].T # spliting from 15th column
  df=df.loc[:,9:] # spliting from 9th row
  df=df.T
  col=df.iloc[0]
  df.columns=col
  df=df[1:]
  df['State'].fillna(method='ffill',inplace=True) # filling the nan values as before value
  df['District'].fillna('Total',inplace=True) # filling the nan values as total
  df=df.reset_index() # resetting the index value
  df.drop(['index'],axis=1, inplace=True) # drop the index value
  df['S.No'].fillna('Total',inplace=True) # filling the nan values as total
  return df



  data="https://www.mohfw.gov.in/" # read the url

data=update_covid(data) # pushing the data to the functio

data


