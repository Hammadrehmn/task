#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re


# In[ ]:


dic= {'WBC': [],
'RBC': [],
'HGB': [],
'HCT': [],
'MCV': [],
'MCH': [],
'MCHC': [],
'PLT': [],
'RDW-SD': [],
'RDW-CV': [],
'PDW': [],
'MPV': [],
'P-LCR': [],
'PCT': [],      
'NEUT%': [],
'LYMPH%': [],
'MONO%': [],
'EO%': [],
'BASO%': []
}


# In[ ]:


path= open("C:\\Users\\Enterprise solutions\\Desktop\\New folder (9)\\interview tasks\\sysmexdata24.log")



empty_list = []


for data in path:
    
    empty_list.append(data)


# In[ ]:


patternPatID= "\|\d{1}\|\|\^\^(.+)\^[M]\|.+\^\^\^\^"



ptID = []

#lista= []

for i in range(len(empty_list)):
    
    matches = str(re.findall(patternPatID,empty_list[i]))
    #print(matches)
    if(matches!='[]'):
        #print(matches)
        matches = matches.replace(" ","")
        #matches = matches[2:-4]
        matches = matches.replace('[','')
        matches = matches.replace(']','')
        matches = matches.replace("'",'')    
        ptID.append(matches)


# In[ ]:





# In[ ]:





# In[ ]:




patternfortest= "\^\d{1}\|(.+)\|.+\|\|.+\|\|.+\|\|"



patternfortestvalue="\^\^\^\^.+\^\d{1}\|.+\|\|\|\|"


pattern-variable = "\^\^\^\^(.+)\^\d{1}"


paternfordate = '\|\|\|\|(\d{8})\d{6}'

date_study =[]

for i in range(len(data_in_list)):
    
    matches = str(re.findall(patternfortestvalue,data_in_list[i]))
   
    if(matches!='[]'):
        print(matches)
        
        
        get_var = matches
        get_var = str(re.findall(pattern-variable,get_var)[0]) #for var
        
        if(get_var == 'WBC'):
            matches1 = str(re.findall(paternfordate,data_in_list[i])[0])
            
            date_study.append(matches1)
            print(matches1)
       
        
        if(get_var in dic.keys()):
            
            matches = str(re.findall(patternfortest,matches)) 
            print(matches)
            
        
            
            
            matches = matches.replace('[','')
            matches = matches.replace(']','')
            matches = matches.replace("'",'')
            print(matches)
            dic[get_var].append(matches)
            
            
        
       
        
    


# In[ ]:


for k in dic:
    print(k)
    print(dic[k])
    print(len(dic[k]))


# In[ ]:


ptID


# In[ ]:


input()
import csv


naming = "sysmexdata"+str(today)+".csv"

df1.to_csv(naming,index = True)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




