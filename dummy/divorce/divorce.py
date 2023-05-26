
from ast import Global
from pickle import TRUE
from tokenize import Name
from traceback import print_tb
import urllib.parse
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


from bs4 import BeautifulSoup
import time 


path='D:\freelance\portifolo\data analyst\web scrapping\chromedriver.exe'
url="https://www.divorceematrimony.com/matchsummary/"

username="8610986216"
password="nallamuthu"

browser =webdriver.Chrome(path)
browser.get(url)
# Find the username/email field and send the username to the input field.
uname = browser.find_element("id", "idEmail") 
uname.send_keys(username)

# Find the password input field and send the password to the input field.
pword = browser.find_element("id", "password") 
pword.send_keys(password)

# Click sign in button to login the website.
browser.find_element("id", "frmsubmit").click()
# Set the maximum wait time in seconds

browser.get(url)

time.sleep(10)
    
html= BeautifulSoup(browser.page_source, "html.parser")


element_counts=0
element_counts_wants=50
Next_page=True
# list of variable for personal details store
url=[]
photo=[]
name=[]
age=[]
height=[]
gender=[]
marital=[]
no_of_children=[]
mother_tongue=[]
physical_status=[]

# list of variable for religion details store
religion=[]
caste=[]
star=[] 
raasi=[]

# list of variable for professional detail
education=[] 
occupation=[] 
occupation_detail=[] 
employed_in=[] 
annual_income=[]

#list of variable for location detail
country=[] 
state=[] 
city=[] 
citizenship=[] 

male_list={"Name":name,"URL":url,"Photo":photo,"Age":age,"Gender":gender,"Height":height,"Marital":marital,"No_of_children":no_of_children,"Mother_tongue":mother_tongue,"Physical_status":physical_status,"Religion":religion,"Caste":caste,"Star":star,"Raasi":raasi,"Education":education,"Occupation":occupation,"Occupation_detail":occupation_detail,"Employed_in":employed_in,"Annual_income":annual_income,"Country":country,"State":state,"City":city,"Citizenship":citizenship}
#elements = browser.find_element("id","resultcontent+str(0)")
elements = html.find_all('div', {'class': 'srch-profile-contents', 'style': 'display:block'})

print("========================elements pri========================")

def newtabprofile(urls):
    url.append(urls)
    # Open a new tab
    browser.execute_script("window.open();")

    # Switch to the second tab
    browser.switch_to.window(browser.window_handles[1])
    browser.get(urls)
    time.sleep(5)

    
    html1= BeautifulSoup(browser.page_source, "html.parser")
    # Find the element with class "vp-imgbg-1"

    # getting individual photo

    vp_imgbg_1 = html1.find('div', class_='vp-imgbg-1')
    # Find the element with class "posrelative" within vp-imgbg-1
    posrelative = vp_imgbg_1.find('div', class_='posrelative')

    # Find the div element with a style attribute containing the URL pattern
    div_element2 = posrelative.find('div')
    div_element1 = div_element2['style']
    url_start_index = div_element1.index('"') + 1
    url_end_index = div_element1.index('"', url_start_index)
    url2 = div_element1[url_start_index:url_end_index]
    photo.append(url2)

    
    
    div_element = html1.find('div', {'class': 'vp-details-bg ng-scope'})
    elements = div_element.find_all('div', {'class':'fleft w580 padt30'})
    element_text = elements[1].text.strip() # second element basic detail 
    ## second element basic detail # Name  # Age # Height # Gender  # Marital Status # No. of children # Children Living Status  # Mother Tongue # Physical Status
    # Name data
    name_text=element_text.split("Name")
    if len(name_text) > 1:
        temp = name_text[1].strip().split("Age")[0].strip()
        name.append(temp)
        #age_text = split_text[1].split()[0]
        print("============TAB TWO============ ", temp)
    else:
        name.append(None)
      
    # Age 

    age_text = element_text.split("Age")
    if len(age_text) > 1:
        #age_text = split_text[1].strip().split("Height")[0].strip()
        temp = age_text[1].split()[0]
        age.append(temp)
        print("============TAB TWO============", temp)
    else:
        age.append(None)
    
    # Height
    height_text = element_text.split("Height")
    if len(height_text) > 1:
        if "Weight" in height_text[1]:
            temp = height_text[1].split("Weight")[0].strip()
            print("============TAB TWO============", temp)
            height.append(temp)
        elif "Gender" in height_text[1]:
            temp = height_text[1].split("Gender")[0].strip()
            print("============TAB TWO============", temp)
            height.append(temp)
        else:
            temp = None
            print("============TAB TWO============", temp)
            height.append(temp)
        
    else:
        height.append(None)

    # Gender
    gender_text = element_text.split("Gender")
    if len(gender_text) > 1:
        temp = gender_text[1].strip().split("Marital Status")[0].strip()
        gender.append(temp)
        print("============TAB TWO============", temp)
    else:
        gender.append(None)

    # Marital Status
    marital_text = element_text.split("Marital Status")
    if len(marital_text) > 1:
        temp = marital_text[1].strip().split("No. of children")[0].strip()
        marital.append(temp)
        print("============TAB TWO============", temp)
    else:
        marital.append(None)
     
    # No. of children
    
    no_of_children_text = element_text.split("No. of children")
    if len(no_of_children_text) > 1:
        
        if "Children Living Status" in no_of_children_text[1]:
            temp = no_of_children_text[1].split("Children Living Status")[0].strip()
            print("============TAB TWO============", temp)
            no_of_children.append(temp)
        elif "Mother Tongue" in no_of_children_text[1]:
            temp = no_of_children_text[1].split("Mother Tongue")[0].strip()
            print("============TAB TWO============", temp)
            no_of_children.append(temp)
        else:
            temp = None
            print("============TAB TWO============", temp)
            no_of_children.append(temp)
        
        
    else:
        no_of_children.append(None)


    # Mother Tongue
    mother_text = element_text.split("Mother Tongue")
    if len(mother_text) > 1:
        temp = mother_text[1].strip().split("Physical Status")[0].strip()
        mother_tongue.append(temp)
        print("============TAB TWO============", temp)
    else:
        mother_tongue.append(None)

    # Physical Status
    physical_text = element_text.split("Physical Status")
    if len(physical_text) > 1:
        temp = physical_text[1].strip().split("Languages Known")[0].strip()
        physical_status.append(temp)
        print("============TAB TWO============", temp)
    else:
        physical_status.append(None)


    print("=========================================RELIGION ELEMENT=======================================")

    element_text3 = elements[3].text.strip() # four element religious information  # # Religion  r Subcaste   Caste    Star   Raasi    Gothram
    
    # Religion
    religion_text=element_text3.split("Religion")
    if len(religion_text) > 1:
        
        if "Subcaste" in religion_text[1]:
            temp = religion_text[1].split("Subcaste")[0].strip()
            print("============TAB TWO============", temp)
            religion.append(temp)
        elif "Caste" in religion_text[1]:
            temp = religion_text[1].split("Caste")[0].strip()
            print("============TAB TWO============", temp)
            religion.append(temp)
        else:
            temp = None
            print("============TAB TWO============", temp)
            religion.append(temp)
        
        
    else:
        religion.append(None)

    # Caste
    caste_text = element_text3.split("Caste")
    if len(caste_text) > 1:
        temp = caste_text[1].strip().split("Star")[0].strip()
        caste.append(temp)
        print("============TAB TWO============", temp)
    else:
        caste.append(None)

    # Star
    star_text = element_text3.split("Star")
    if len(star_text) > 1:
        temp = star_text[1].strip().split("Raasi")[0].strip()
        star.append(temp)
        print("============TAB TWO============", temp)
    else:
        star.append(None)

    # Raasi
    raasi_text = element_text3.split("Raasi")
    if len(raasi_text) > 1:
        temp = raasi_text[1].strip().split("Gothram")[0].strip()
        raasi.append(temp)
        print("============TAB TWO============", temp)
    else:
        raasi.append(None)

    print("=========================================PROFESSIONAL ELEMENT=======================================")

    element_text4 = elements[4].text.strip() # five element professional information  
    
    # Education  r Education Detail  Occupation   Occupation Detail   Employed in    Annual Income
    
    # Education
    education_text=element_text4.split("Education")
    if len(education_text) > 1:
        
        if "Education Detail" in education_text[1]:
            temp = education_text[1].split("Education Detail")[0].strip()
            print("============TAB TWO============", temp)
            education.append(temp)
        elif "Occupation" in education_text[1]:
            temp = education_text[1].split("Occupation")[0].strip()
            print("============TAB TWO============", temp)
            education.append(temp)
        else:
            temp = None
            print("============TAB TWO============", temp)
            education.append(temp)
        
        
    else:
        education.append(None)

    # Occupation
    Occupation_text = element_text4.split("Occupation")
    if len(Occupation_text) > 1:
        temp = Occupation_text[1].strip().split("Occupation Detail")[0].strip()
        occupation.append(temp)
        print("============TAB TWO============", temp)
    else:
        occupation.append(None)

    # Occupation Detail
    Occupation_detail_text = element_text4.split("Occupation Detail")
    if len(Occupation_detail_text) > 1:
        temp = Occupation_detail_text[1].strip().split("Employed in")[0].strip()
        occupation_detail.append(temp)
        print("============TAB TWO============", temp)
    else:
        occupation_detail.append(None)


    # Employed in
    Employed_in_text = element_text4.split("Employed in")
    if len(Employed_in_text) > 1:
        temp = Employed_in_text[1].strip().split("Annual Income")[0].strip()
        employed_in.append(temp)
        print("============TAB TWO============", temp)
    else:
        employed_in.append(None)

    # Annual Income
    Annual_Income_text = element_text4.split("Annual Income")
    if len(Annual_Income_text) > 1:
        temp = Annual_Income_text[1].strip()
        annual_income.append(temp)
        print("============TAB TWO============", temp)
    else:
        annual_income.append(None)
    
    print("=========================================LOCATION ELEMENT=======================================")

    element_text6 = elements[6].text.strip() # seven location detail
    
    # Country  State  City  Citizenship
    
    # Country
    Country_text = element_text6.split("Country")
    if len(Country_text) > 1:
        temp = Country_text[1].strip().split("State")[0].strip()
        country.append(temp)
        print("============TAB TWO============", temp)
    else:
        country.append(None)

    # State
    State_text = element_text6.split("State")
    if len(State_text) > 1:
        temp = State_text[1].strip().split("City")[0].strip()
        state.append(temp)
        print("============TAB TWO============", temp)
    else:
        state.append(None)

    # City
    City_text = element_text6.split("City")
    if len(City_text) > 1:
        temp = City_text[1].strip().split("Citizenship")[0].strip()
        city.append(temp)
        print("============TAB TWO============", temp)
    else:
        city.append(None)

    # Citizenship
    Citizenship_text = element_text6.split("Citizenship")
    if len(Citizenship_text) > 1:
        temp = Citizenship_text[1].strip()
        citizenship.append(temp)
        print("============TAB TWO============", temp)
    else:
        citizenship.append(None)


    
    
    
    # third contact details  # four element religious information   # five element professional information # seven location detail

    browser.close()

    # Switch back to the first tab
    browser.switch_to.window(browser.window_handles[0])

def begintab():
    global male_list
    global element_counts_wants
    global Next_page
    global elements

    for element in elements:
        if (len(male_list["Name"])==element_counts_wants):
            Next_page=False
            break
        else:
            #element_counts+=1
            print("*************NUMBER OF PERSON COLLECTED",len(male_list["Name"]))
           
        div_element = element.find('div', {'class': 'font16 boldtxt padl2 padt10 padb15 fleft'})
        if div_element is not None:
            name1 = div_element.find('a').text
       
            #print(name)
            anchor = div_element.find('a')

            onclick_value = anchor['onclick']
            url_encoded = onclick_value.split("'")[1]

            url1 = urllib.parse.unquote(url_encoded)
       
            newtabprofile(url1)
        #else:
            #print("Element not found")
       
       
    
    
    


    

    



begintab()
# Find the element with class "nextactive"
nextactive_element = html.find('span',{'class': 'nextactive'})
cou=0
# Check if the elements were found
while(Next_page==True):

    if nextactive_element:
        print("Class 'nextactive' is present.")
        try:
            next_element = browser.find_element(By.CLASS_NAME, 'nextactive')
            if next_element.is_displayed():
                browser.execute_script("arguments[0].click();", next_element)
                cou+=1
                print("nextpagenextpagenextpage   nextpagenextpagenextpage  nextpagenextpage  nextpagenextpage",cou )
            else:
                print("NEXT Element is not visible")
        except NoSuchElementException:
            print("NEXT Element not found")
        time.sleep(10)
        html= BeautifulSoup(browser.page_source, "html.parser")
        nextactive_element = html.find('span',{'class': 'nextactive'})
        elements = html.find_all('div', {'class': 'srch-profile-contents', 'style': 'display:block'})
        begintab()
        

    else:
        Next_page=False
        print("Class 'nextactive' is not present.")

# Create DataFrame from male_list
df = pd.DataFrame.from_dict(male_list, orient='index').T

# Display photos as images using URLs
df['Photo'] = df['Photo'].apply(lambda x: f'<img src="{x}" width="100" height="100">')

# Save DataFrame as CSV
df.to_csv('male_list.csv', index=False)

# Save DataFrame as HTML with image URLs
df.to_html('male_list.html', index=False, escape=False)


for key, value in male_list.items():
    print(f"{key}: {value}")



