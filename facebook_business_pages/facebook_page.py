

from itertools import filterfalse
from multiprocessing import Value
from pickle import FALSE
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
import time 
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import re
import random
import os.path

# passing district wise loaction in australia to list
df=pd.read_csv(r"D:\freelance\portifolo\data analyst\client\faccebook pages\facebook_page\facebook_page\Copy of Australian.csv")
df.LGA_region
data_list = df['LGA_region'].tolist()
for i in range(len(data_list)):
    if '/' in data_list[i]:
        parts = data_list[i].split('/')
        data_list[i] = parts[0]
        data_list.append(parts[1])
    elif '-' in data_list[i]:
        parts = data_list[i].split('-')
        data_list[i] = parts[0]
        data_list.append(parts[1])

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  # Disable other types of notifications (optional)
#chrome_options.add_argument("--headless")

# Set the unexpected_alert_behaviour capability to 'dismiss'
chrome_options.add_experimental_option('prefs', {
    'profile.default_content_setting_values': {
        'notifications': 2
    },
    'unexpectedAlertBehaviour': 'dismiss'
})



path='D:\freelance\portifolo\data analyst\web scrapping\chromedriver.exe'
url="https://www.facebook.com/"

username="aneek.quin@fullangle.org"
password="940aneek5quin"

driver =webdriver.Chrome(path,options=chrome_options)
driver.get(url)   



print("facebook page scrapping")
# Find the username/email field and send the username to the input field.
uname = driver.find_element("id", "email") 



uname.send_keys(username)
time.sleep(2)
# Find the password input field and send the password to the input field.
pword = driver.find_element("id", "pass") 
pword.send_keys(password)

time.sleep(1)
driver.find_element(By.CLASS_NAME, '_6ltg').click() 
# Set the maximum wait time in seconds
try:
    alert = driver.switch_to.alert
    alert.dismiss()
except NoAlertPresentException:
    pass

driver.get("https://www.facebook.com/search/pages?q=business")
#driver.get("https://www.facebook.com/search/pages?q=business&filters=eyJmaWx0ZXJfcGFnZXNfbG9jYXRpb246MCI6IntcIm5hbWVcIjpcImZpbHRlcl9wYWdlc19sb2NhdGlvblwiLFwiYXJnc1wiOlwiMTExODc1Njg1NDk2NjEzXCJ9Iiwic2hvcHM6MCI6IntcIm5hbWVcIjpcImZpbHRlcl9wYWdlc19zaG9wc1wiLFwiYXJnc1wiOlwiXCJ9IiwidmVyaWZpZWQ6MCI6IntcIm5hbWVcIjpcInBhZ2VzX3ZlcmlmaWVkXCIsXCJhcmdzXCI6XCJcIn0ifQ%3D%3D")

time.sleep(2)

country_name="Australia"
# list of variable
facebook_url=[] 
page_name=[]
lga_region=[] 
country=[]


page_link_store={"Page_Name":page_name,"Facebook_url":facebook_url,"LGA_region":lga_region}

# save page link function
def save_pagelink():

    
    # Check if the file exists
    if os.path.isfile('page_list_f.csv'):
        # Check if the file is empty
        if os.stat('page_list_f.csv').st_size > 0:
            # File is not empty, append new data to it
            df1 = pd.DataFrame.from_dict(page_link_store, orient='index').T
            df1.to_csv('page_list_f.csv', mode='a', header=False, index=False)
        else:
            # File is empty, write new data to it
            df1 = pd.DataFrame.from_dict(page_link_store, orient='index').T
            df1.to_csv('page_list_f.csv', index=False)
    else:
        # File does not exist, write new data to it
        df1 = pd.DataFrame.from_dict(page_link_store, orient='index').T
        df1.to_csv('page_list_f.csv', index=False)
    # Clear the dictionary values
    page_link_store["Page_Name"].clear()
    page_link_store["Facebook_url"].clear()
    page_link_store["LGA_region"].clear()
    '''
    for key, value in page_link.items():
        print(f"{key}: {value}")
    '''

#setup page limi
page_count=-1



    

def random_time():
    sleep_duration1 = random.uniform(5, 7)
    time.sleep(sleep_duration1)


def block_facebook_blocks():
    time.sleep(3)
    try:
        interfering_element = driver.find_element(By.CSS_SELECTOR, '.x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.x14yjl9h.xudhj91.x18nykt9.xww2gxu.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1')
        #interfering_element.click()
        driver.execute_script("arguments[0].click();", interfering_element)

    except NoSuchElementException:
        print("Interfering element not found. Skipping interference removal.")

page_end=False
## ----------------------------------------------------- part 1 program -----------------------------------------------------------------------------------
'''
# getting all page link and location field handle checking reach bottom of page and scroll down and calling save page link function
def all_pages_link(location_store):
   
    global page_end

    # entering location district for required country

    location=location_store
    #location="chennai"
    def text_presence():
        location_field = driver.find_elements(By.XPATH, "//*[@aria-label='Location']")
        # Select the second element
        second_element_location_field = location_field[1]
        text_presence=False
        text_existing=second_element_location_field.get_attribute("value")
        if text_existing:
            text_presence=True
            print("Text exists in uname field:", text_existing)
            time.sleep(2)
            # Clear the field
            second_element_location_field.clear()
            # .x6s0dn4.x78zum5.xdt5ytf.x193iq5w.x1t2pt76.xh8yej3
            empty_area=driver.find_element(By.CSS_SELECTOR, ".x6s0dn4.x78zum5.xdt5ytf.x193iq5w.x1t2pt76.xh8yej3")
            empty_area.click()
            time.sleep(2)
        return text_presence

    def locstion_feeding():
        global page_end
        time.sleep(2)

        location_field = driver.find_elements(By.XPATH, "//*[@aria-label='Location']")
        # Select the second element
        second_element_location_field = location_field[1] 
        random_time()
        block_facebook_blocks()

        second_element_location_field.send_keys(location)
        time.sleep(5)

        # selecting drop option in location field
    
        drop_class = driver.find_elements(By.CSS_SELECTOR, ".x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha")
        print("drop number:",len(drop_class))
        if len(drop_class) >= 2:
            second_element_drop_class = drop_class[1]
            # Check if the <li> tag is present within the second element
            if second_element_drop_class.find_elements(By.TAG_NAME, "li"):
                first_li = second_element_drop_class.find_element(By.TAG_NAME, "li")
                first_li.click()
                time.sleep(5)
            else:
                print("line element not found")
                page_end=True  #
                print("line element not found pag end 1:", page_end)

        else:
            print("location not found")
    
    
    try:
        
        block_facebook_blocks()
        location_click = driver.find_element(By.CSS_SELECTOR, ".x9f619.x78zum5.xurb0ha.x1y1aw1k.xwib8y2.x1yc453h.xh8yej3")
        text_detector=text_presence()
        if text_detector==True:
            print("text presencce detected and removed")
            location_click.click()
            locstion_feeding()
        else:
            location_click.click()
            locstion_feeding()
    
    except ElementNotInteractableException:
        print("................... ElementNotInteractableException........................")
        close_pre_location=driver.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1n2onr6.x87ps6o.x1lku1pv.x1a2a7pz")
        block_facebook_blocks()
        close_pre_location.click()
       
        time.sleep(2)
        block_facebook_blocks()
        location_click.click()
        locstion_feeding()
      

    # extracting detail of page appear

    ## extract url and business name in each element in page list of elements
    def list_of_page():
        print("list_of_page calling.............")
        page_list=driver.find_elements(By.CLASS_NAME, 'x1yztbdb')   
        #page_list_elements=page_list.find_elements(By.CSS_SELECTOR, '.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.xzsf02u.x1s688f')
        for page_list_element in page_list:
            page_list_element1=page_list_element.find_element(By.CSS_SELECTOR, '.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.xzsf02u.x1s688f')

            # Get the href attribute and business name
            href = page_list_element1.get_attribute('href')
            business_name = page_list_element1.text
            
            lga_region.append(location_store)
            facebook_url.append(href)
            page_name.append(business_name)

            # Print the href and business name
            #print('Href:', href)
            #print('Business Name:', business_name)
        save_pagelink()

    print("line element not found pag end 2:", page_end)
    ## checking we reach end of page and scrolling page
    while (page_end==False):
    # Check if the element is visible

        try:
            end_page = driver.find_element(By.CSS_SELECTOR, '.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xo1l8bm.xi81zsa.x2b8uid')
            print("end_page is visible")
            page_end=True
            list_of_page()
        
        except:
            print("end_page is not visible")
            page_list = driver.find_elements(By.CLASS_NAME, 'x1yztbdb')

            if page_list:
                print("Elements with class 'x1yztbdb' are present.")
            else:
                print("Elements with class 'x1yztbdb' are not present.")
                page_end=True


            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

itern=0 # number of page want for testing

# iterate each LGA region in list
for data_child in data_list:
    
    if(page_count==itern):
        print("cut cut cut...................",itern)
        break
    print("@@@@@@@@@@@@@@@@@@ iterate page @@@@@@@@@@@@@@@@@@@2")
    itern+=1
    page_end=False # reset the page end bool
    all_pages_link(data_child)
    
'''
    
## ----------------------------------------------------- part 2 program -----------------------------------------------------------------------------------

page_created_date=[] 
website_link=[] 
address_details=[] 
phone_number=[] 
email_id_link=[] 

facebook_url_page=[] 
page_name_idu=[]
lga_region_cover=[] 



IND_page_link_store={"Facebook_url":facebook_url_page,"LGA_region":lga_region_cover,"Page_Name":page_name_idu,"Page_Created_date":page_created_date,"Address":address_details,"Phone_number":phone_number,"Email":email_id_link,"Website_url":website_link}

# load csv existing page link we scrappped
df_pl=pd.read_csv(r"D:\freelance\portifolo\data analyst\client\faccebook pages\facebook_page\facebook_page\sydney1.csv")

Facebook_page_URL = df_pl['Facebook_url'].tolist()
Lga_covered_region=df_pl['LGA_region'].tolist()
business_page_name=df_pl['Page_Name'].tolist()

#setup break loop in page link counts and store data after this much in list
break_count=-1
store_count=10
for_inc=0

#store each detail
def save_page_details():

    
    # Check if the file exists
    if os.path.isfile('Australia_facebook_business_page_details.csv'):
        # Check if the file is empty
        if os.stat('Australia_facebook_business_page_details.csv').st_size > 0:
            # File is not empty, append new data to it
            df11 = pd.DataFrame.from_dict(IND_page_link_store, orient='index').T
            df11.to_csv('Australia_facebook_business_page_details.csv', mode='a', header=False, index=False)
        else:
            # File is empty, write new data to it
            df11 = pd.DataFrame.from_dict(IND_page_link_store, orient='index').T
            df11.to_csv('Australia_facebook_business_page_details.csv', index=False)
    else:
        # File does not exist, write new data to it
        df11 = pd.DataFrame.from_dict(IND_page_link_store, orient='index').T
        df11.to_csv('Australia_facebook_business_page_details.csv', index=False)
    # Clear the dictionary values
    for key in IND_page_link_store:
        IND_page_link_store[key].clear()




# extract individual pages information of contact detail and page created date
#urls = [  "https://www.facebook.com/pages/Thomase-Ramapuram-Memorial/212160725994123", "https://www.facebook.com/Sri-ponniamman-trans-269591060175398/", "https://www.facebook.com/SandytownRiverCruises/",    "https://www.facebook.com/chennailoanservice/",    "https://www.facebook.com/bsindia/",    "https://www.facebook.com/HBR/",    "https://www.facebook.com/profile.php?id=100063968106669",    "https://www.facebook.com/profile.php?id=100092563683204",    "https://www.facebook.com/AlburyBusinessConnect/",    "https://www.facebook.com/instagramforbusiness/",    "https://www.facebook.com/TechBossIndia/",    "https://www.facebook.com/profile.php?id=100054371327820",    "https://www.facebook.com/iamalishaabdullah/",  "https://www.facebook.com/EconomicTimes/",  "https://www.facebook.com/Ideapluskv/"]

id_pattern = r"\?id=\d+"  # Pattern to match URLs with ID

#for url in urls:
for url, region_lga, bs_name in zip(Facebook_page_URL, Lga_covered_region,business_page_name):
    
    for_inc+=1
    if for_inc<800:
        continue
    print("after continue0000000000000000000000000000000000 DATA COUNT    :", for_inc)
    if(for_inc%store_count==0): # for every required store count
        print("calling store ..........................................#######################")
        save_page_details()

    if(break_count==for_inc):
        break

    
   
    #print("URL:", url)
    driver.get(url)
    time.sleep(5)
    pop_up_message=driver.find_element(By.CSS_SELECTOR, '.xvijh9v.xhhsvwb.x1ty9z65.xgzva0m') if driver.find_elements(By.CSS_SELECTOR, '.xvijh9v.xhhsvwb.x1ty9z65.xgzva0m') else None
    
    block_facebook_blocks()
    
    # Check if element is present
    if pop_up_message:
        print("Element is present")
        driver.find_element(By.CSS_SELECTOR, '.xvijh9v.xhhsvwb.x1ty9z65.xgzva0m').click() 
    else:
        print("Element is not present")

    front_page = driver.find_element(By.CLASS_NAME, 'x1hmvnq2') if driver.find_elements(By.CLASS_NAME, 'x1hmvnq2') else None
    if front_page:
        #front_page = driver.find_element(By.CLASS_NAME, 'x1hmvnq2')
        print("front page")

        #  Page transparency navigate and extract data for front page

        section_div_frontpage=driver.find_elements(By.CSS_SELECTOR, ".x9f619.x1n2onr6.x1ja2u2z.x2bj2ny.x1qpq9i9.xdney7k.xu5ydu1.xt3gfkd.xh8yej3.x6ikm8r.x10wlt62.xquyuld")   
        for section_check_page3 in section_div_frontpage:
            
            html_page3 = section_check_page3.get_attribute('innerHTML')
            soup_page3 = BeautifulSoup(html_page3, 'html.parser')
            soup_page3_text=soup_page3.text.strip()
            if "Page transparency" in soup_page3_text:
                print("Page transparency is present in soup_page3")
                section_check_page31=section_check_page3.find_element(By.CSS_SELECTOR, ".x9f619.x1n2onr6.x1ja2u2z.x2lah0s.x193iq5w.xeuugli.xqcrz7y.x78zum5.xdt5ytf.xl56j7k.x1i64zmx")
            
                #driver.execute_script("arguments[0].click();", section_check_page31)
                # Scroll to the element
                driver.execute_script("arguments[0].scrollIntoView();", section_check_page31)
                time.sleep(1)

                action_chains = ActionChains(driver)
                action_chains.click(section_check_page31).perform()
                # Scroll to the element
                #driver.execute_script("arguments[0].scrollIntoView(true);", section_check_page31)
                #time.sleep(1)
                #section_check_page31.click()
                time.sleep(2)
            
                section_check_page311=driver.find_elements(By.CSS_SELECTOR, ".x9f619.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.x1nhvcw1.x6s0dn4.xozqiw3.x1q0g3np.x1pi30zi.x1swvt13.x1y1aw1k.xykv574.xbmpl8g.x4cne27.xifccgj")
                section_check_page3112=section_check_page311[0].find_elements(By.CSS_SELECTOR, ".xu06os2.x1ok221b")
            
                soup_page31 = BeautifulSoup(section_check_page3112[1].get_attribute('innerHTML'), 'html.parser')
                
                page_created_date.append(soup_page31) #store page created date
                print(soup_page31.text)
            
            else:
                pass
                #print("Page transparency is not present in soup_page3")
            if "Page transparency" in soup_page3_text:
                break
            
        # about page navigate and extract data for front page

        slash_pattern = r"^(.*[^/])$"
        # Check if the URL matches the pattern
        if re.match(slash_pattern, url):
            print("URL does not have a backslash at the end")
            print("URL:",url+"/about/")
            driver.get(url+"/about/")
        else:
            print("URL has a backslash at the end")
            print("URL:",url+"about/")
            driver.get(url+"about/")
  
        sleep_duration = random.uniform(5, 7)
        time.sleep(sleep_duration)
        #finding class address about page by using class name and check the match contact info
        address_about = driver.find_elements(By.CLASS_NAME, 'x9orja2')
        
        def search_address(link_text,phone_text):
            
            email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
            #email_pattern =r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            #phone_pattern = r"\d{3}\s\d{4}\s\d{4}"
            phone_pattern = r"\d[\d\s(),-]*\d"
            url_pattern = r"https?://[^\s]+"
            #url_pattern= r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            #address_pattern = r"(?:\d+\s[A-Z][a-z]+\s[A-Za-z]+(?:\s[A-Za-z]+)*)?(?:\s*,\s*\w+)*"
            #address_pattern= r'[^\n]+'
            email_p=False
            url_p=False 
            phone_p=False 
            #print(email_p)
            print("========================= contact detail============================")
            for text in link_text:
                html_about1 = text.get_attribute('innerHTML')
                soup_about2 = BeautifulSoup(html_about1, 'html.parser')
                soup_about2_text=soup_about2.text.strip()

                email = re.search(email_pattern, soup_about2_text)
                url = re.search(url_pattern, soup_about2_text)
                if email:
                    #print("Email:", soup_about2_text)
                    email_id_link.append(soup_about2_text) 
                    email_p=True

                if url:
                    print("URL:", soup_about2_text)
                    website_link.append(soup_about2_text) 
                    url_p=True
            
            if email_p:
                pass
            else:
                #print("Email: None")
                email_id_link.append(None)

            if url_p:
                pass
            else:
                #print("URL: None")
                website_link.append(None)
                

                

            for text1 in phone_text:
                html_about11 = text1.get_attribute('innerHTML')
                soup_about22 = BeautifulSoup(html_about11, 'html.parser')
                soup_about22_text=soup_about22.text.strip()

                phone = re.search(phone_pattern, soup_about22_text)
                
                if phone and not phone_p:
                    #print("Phone:", soup_about22_text)
                    phone_number.append(soup_about22_text)
                    phone_p=True
            
            if phone_p:
                pass
            else:
                #print("Phone: None")
                phone_number.append(None)
            
            address = None
            address_details.append(address) 
            
            
            facebook_url_page.append(url)
            page_name_idu.append(bs_name)
            lga_region_cover.append(region_lga)


            #print("address:",address)
            print("========================= END OF CONTACT============================")
        
        for address_about1 in address_about:
            html_about1 = address_about1.get_attribute('innerHTML')
            soup_about1 = BeautifulSoup(html_about1, 'html.parser')
            soup_about1_text=soup_about1.text.strip()

            # Additional contact info
            if "Additional contact info" in soup_about1_text:
            
                address_about_link_text=address_about1.find_elements(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.x1fey0fg")
                address_about_phone_text=address_about1.find_elements(By.CSS_SELECTOR, ".x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x6prxxf.xvq8zen.xo1l8bm.xzsf02u")
                search_address(address_about_link_text,address_about_phone_text)
                print("Additional contact info 1")
        
    else:

        print("not front page")
        has_id = re.search(id_pattern, url) is not None

        def search_contact_profile(conact_url,profile_date_url):
            
            driver.get(conact_url)
            sleep_duration = random.uniform(5, 7)
            time.sleep(sleep_duration)

            html_contact_content = driver.page_source
            # Create a BeautifulSoup object to parse the HTML
            contact_soup = BeautifulSoup(html_contact_content, 'html.parser')
            # Select the parent element using the class name
            parent_contact_element = contact_soup.select_one('.xyamay9.xqmdsaz.x1gan7if.x1swvt13')
             #find direct child element only not sub child
            child_contact_elements = parent_contact_element.find_all(recursive=False)
            
            email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
            
            phone_pattern = r"\d[\d\s(),-]*\d"
            url_pattern = r"https?://[^\s]+"
            address_pattern = r"(?:\d+\s[A-Z][a-z]+\s[A-Za-z]+(?:\s[A-Za-z]+)*)?(?:\s*,\s*\w+)*"
            
            email_p=False
            url_p=False 
            phone_p=False
            address_p=False
            #find direct child element only not sub child
                     
            print("===================== website info=========================")
            # Iterate over each child element
            for child1 in child_contact_elements:
                
                title_check1=child1.find('div', {'class': 'xieb3on x1gslohp'})
                
                if "Contact info" == title_check1.text.strip():
                    inside_title=child1.find_all('span', {'class':'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h'})
                    
                    print("Contact info count")
                    
                    for check_text in inside_title:
                        email_id = re.search(email_pattern, check_text.text.strip())
                        
                        if email_id and not email_p:
                            #print("Email:", check_text.text.strip())
                            email_id_link.append(check_text.text.strip())
                            email_p=True
                        
                    for check_text1 in inside_title:
                        phone_no = re.search(phone_pattern, check_text1.text.strip())
                        
                        if phone_no and not phone_p:
                            #print("Phone:", check_text1.text.strip())
                            phone_number.append(check_text1.text.strip())
                            phone_p=True
                   
                    
                    address=child1.find('div', {'class': 'xzsf02u x6prxxf xvq8zen x126k92a x12nagc'})
                    if address and not address_p:
                        #print("Address:",address.text.strip())
                        address_details.append(address.text.strip())
                        address_p=True
                    

                if "Websites and social links" == title_check1.text.strip():
                    inside_title=child1.find_all('a', {'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u'})

                    print("Websites and social links")
                    for check_text in inside_title:
                        url_id = re.search(url_pattern, check_text.text.strip())
                        
                        if url_id and not url_p:
                            #print("Website:", check_text.text.strip())
                            website_link.append(check_text.text.strip())
                            url_p=True

            if email_p:
                pass
            else:
                #print("Email: None")
                email_id_link.append(None)


            if phone_p:
                pass
            else:
                #print("Phone: None")
                phone_number.append(None)

            if url_p:
                pass
            else:
                #print("URL: None")
                website_link.append(None)

            if address_p:
                pass
            else:
                #print("Address: None")
                address_details.append(None)
            

            driver.get(profile_date_url)
            sleep_duration = random.uniform(5, 7)
            time.sleep(sleep_duration)
            
            
            html_profile_content = driver.page_source
            # Create a BeautifulSoup object to parse the HTML
            profile_soup = BeautifulSoup(html_profile_content, 'html.parser')

            creation_date=profile_soup.find_all('div', {'class': 'xzsf02u x6prxxf xvq8zen x126k92a x12nagc'})
            creation_date_text=creation_date[1].text.strip()
            #print("PAge created date:",creation_date_text)
            
            page_created_date.append(creation_date_text)  

            facebook_url_page.append(url)
            page_name_idu.append(bs_name)
            lga_region_cover.append(region_lga)



            

            print("===================== End website info=========================")
        
        slash_pattern = r"^(.*[^/])$"
        if has_id:
            print("match the ID pattern")
            modified_contact_idurl = url + "&sk=about_contact_and_basic_info"
            modified_profile_idurl = url + "&sk=about_profile_transparency"
            
            search_contact_profile(modified_contact_idurl,modified_profile_idurl)
        
        elif re.match(slash_pattern, url):
            print("URL does not have a backslash at the end")
            #print("URL:",url+"/about/")
            modified_contact_url = url + "/about_contact_and_basic_info"
            modified_profile_url = url + "/about_profile_transparency"
            search_contact_profile(modified_contact_url,modified_profile_url)
        else:
            print("Does not match the ID pattern")
            modified_contact_url = url + "about_contact_and_basic_info"
            modified_profile_url = url + "about_profile_transparency"
                       
            search_contact_profile(modified_contact_url,modified_profile_url)


            