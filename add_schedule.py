'''
have to compulsory include -
date = 2 digits ex - 23
time = 2 digits ex - 10,11
subject = optional
staff = must cause I programmed it that way later i will remove it
links = must!!
'''
import os
import pandas as pd 
import numpy as np

class create_schedule:
    def __init__(self):
        self.path = os.getcwd()
        self.filename="sch.csv"

    def if_exists(self):
        if self.filename in os.listdir(self.path):
            
            return True
        else:
            
            return False

    
    def append(self,date,time,subj,staff,link):
        if not self.if_exists():
            
            print("creating a new one")
            df = pd.DataFrame({'date':date,'time':time,'subject':subj,'staff':staff,
                                   'links':link},index=[0])
            df.to_csv("sch.csv",index=False)

        else:
                print('file already exists appending now')
                df = pd.read_csv(self.filename,index_col=0)
                data=[date,time,subj,staff,link]
                se = pd.DataFrame({'date':date,'time':time,'subject':subj,'staff':staff,
                                   'links':link},index=[0])
                df = pd.merge(df,se,how='outer')
                df.to_csv(self.filename,index=False)
        print("Added!!")

print("Enter your schedule - 0")
print("Display your schedule - 1")
print("Exit - 2")
val = int(input('Enter response : '))

f = create_schedule()
if val==0:
        f.if_exists()
        date = int(input('date(max 2 digits) : '))
        time = int(input('time(max 2 digits) : '))
        subject = input('Subject(optional) : ')
        staff = input('lecturer(mandatory) : ')
        link = input('online-class-link : ')
        if len(str(date))>2 or len(str(time))>2 or len(staff)==0 or len(link)==0:
            print('Invalid data')
            pass
        else:
            if len(subject)==0:
                subject=np.nan
            f.append(date,time,subject,staff,link)
if val==1:

        if f.if_exists():
            df =pd.read_csv('sch.csv',index_col=0)
            print(df)
        else:
            print("no file found enter your schedule first")

 


