from selenium import webdriver
from time import sleep
from bca_pass import pw
import csv
from selenium.webdriver.common.keys import Keys
import requests

class bca:
    def __init__(self, username, pw):
        students = []
        with open('passwordreset.csv') as csv_file:
            students = list(csv.reader(csv_file, delimiter=','))   

        
        newp = []
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2fen-in%2fmicrosoft-365%2fbusiness%2foffice-365-administration&lc=16393&id=74335&aadredir=1")
        sleep(2)
        login = self.driver.find_element_by_id("i0116")
        login.send_keys(username)
        self.driver.find_element_by_id("idSIButton9").click()
        sleep(2)
        pas = self.driver.find_element_by_id("i0118")
        pas.send_keys(pw)
        self.driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
        sleep(25)
        self.driver.get("https://admin.microsoft.com/Adminportal/Home?source=applauncher#/users")
       
        for i in students:
            x = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
            x.send_keys(i[0])
            print(i[0])
            x.send_keys(Keys.ENTER)
            sleep(1)
            self.driver.find_element_by_name("reset").click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[3]/div[3]/div/button").click()
            sleep(2)
            newpass = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[3]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/span").text
            newp.append(newpass)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[3]/div[3]/div/button").click()
            self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.CONTROL + "a")
            self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.DELETE)
            
            sleep(2)
        print("\n")
        print(newp)

        
        #newp = ["abc","def","123"]
        with open('passwordreset.csv','r') as csvinput:
            with open('output.csv', 'w') as csvoutput:
                writer = csv.writer(csvoutput)
                i = 0
                for row in csv.reader(csvinput):
                    try:
                        writer.writerow(row+[newp[i]])
                        i+=1
                    except:
                        writer.writerow(row+["Some error"])
    

        with open('output.csv','r') as csvinput:
            newstudents = list(csv.reader(csvinput, delimiter=','))   
        for i in newstudents:
            mob = i[1]
            msg = "Your Admin has reset the password of user "+i[0]+" Your new password is "+i[2]+" on mobile number "+i[1]
            print(msg)
            #r="http://login.arihantsms.com/vendorsms/pushsms.aspx?user=bcaamroli&password=demo123&msisdn="+mob+"&sid=BCAAMR&msg="+msg+"&fl=0&gwid=2"
            #requests.post(r)

        n = int(input("Press an integer to contibue"))
        
        with open('output.csv','r') as csvinput:
            newstudents = list(csv.reader(csvinput, delimiter=','))   
        for i in newstudents:
            mob = i[1]
            msg = "Your Admin has reset the password of user "+i[0]+" Your new password is "+i[2]
            print(msg)
            r="http://login.arihantsms.com/vendorsms/pushsms.aspx?user=bcaamroli&password=demo123&msisdn="+mob+"&sid=BCAAMR&msg="+msg+"&fl=0&gwid=2"
            requests.post(r)
        """
        variants={}
        if(r):
            uglyjson = r.text
            parsed = json.loads(uglyjson)
        """
        


my_bot = bca('purvi.nair@amrolicollege.org', pw)
#my_bot.get_unfollowers()
