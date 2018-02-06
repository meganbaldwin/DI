
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

PCIPR= pd.read_csv("Physician_Compare_2015_Individual_EP_Public_Reporting___Performance_Scores.csv")


print(PCIPR.shape)


# In[23]:


PCGPE= pd.read_csv("Physician_Compare_2015_Group_Public_Reporting_-_Patient_Experience.csv",
dtype ={"Organization legal name or 'doing business as' name":object,
 'Group PAC ID':object,
 ' State':object,
 'Measure Identifier':object,
 'Measure Title':object,
 'Measure Performance Rate':object,
 'Footnote':object})
print(PCGPE)


# In[55]:


PCGRP = pd.read_csv("Physician_Compare_2015_Group_Public_Reporting___Performance_Scores.csv")
list(PCGRP)
PCGRP = pd.DataFrame(PCGRP)


# In[4]:



PCNDF = pd.read_csv("Physician_Compare_National_Downloadable_File.csv",  dtype= {'NPI': int,'PAC ID':int,
 'Professional Enrollment ID':object,'Last Name':object,'First Name':object,'Middle Name':object,'Suffix':object,
 'Gender':object,'Credential': object,'Medical school name': object,'Graduation year': object,'Primary specialty': object,
 'Secondary specialty 1': object,'Secondary specialty 2': object,'Secondary specialty 3': object,'Secondary specialty 4': object,
 'All secondary specialties': object,'Organization legal name': object,'Group Practice PAC ID': object,
 'Number of Group Practice members': object,'Line 1 Street Address': object,'Line 2 Street Address': object,
 'Marker of address line 2 suppression': object,'City': object, 'State': object,'Zip Code': object,'Phone Number': object,
 'Hospital affiliation CCN 1': object, 'Hospital affiliation LBN 1': object,'Hospital affiliation CCN 2': object,
 'Hospital affiliation LBN 2': object,'Hospital affiliation CCN 3': object,'Hospital affiliation LBN 3': object,
 'Hospital affiliation CCN 4': object,'Hospital affiliation LBN 4': object,'Hospital affiliation CCN 5': object,
 'Hospital affiliation LBN 5': object,'Professional accepts Medicare Assignment': object,'Reported Quality Measures': object,
 'Used electronic health records': object,'Committed to heart health through the Million Hearts® initiative.': object})
list(PCNDF.shape)


# In[19]:


len(PCNDF.NPI.unique())


# In[22]:


len(PCNDF['PAC ID'].unique())


# In[11]:


def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )


API_dupes = list_duplicates(PCNDF.iloc[:,1])
len(API_dupes)


# In[16]:


PCNDF['FullID'] = PCNDF['NPI'] + PCNDF['PAC ID']


# In[25]:


len(PCNDF['FullID'].unique())


# In[26]:


unique= PCNDF.drop_duplicates(subset=['FullID'], keep=False)


# In[27]:


unique.groupby(['Gender']).size().reset_index(name='counts')


# In[42]:


GCtable =  unique.groupby(['Credential', 'Gender']).size().reset_index(name='counts')
print(GCtable)


# In[17]:


PCGPE['Group PAC ID'] = PCGPE['Group PAC ID'].apply(tuple)
PCGPE[' State'] = PCGPE[' State'].apply(tuple)


# In[21]:


PCtable =  PCGPE.groupby([' State', 'Group PAC ID']).size().reset_index(name='counts')
print(PCtable)


# In[22]:


PCtable.groupby([' State']).size().reset_index(name='counts')


# In[2]:


iPtable = PCIPR.groupby(['PAC ID']).size().reset_index(name='counts')


# In[18]:


highlyrated = iPtable[iPtable['counts'] >10]
list(highlyrated)
doctorlist = highlyrated['PAC ID']
doctorlist.tolist()


# In[37]:


selecteddoctors=PCIPR[PCIPR['PAC ID'].isin(doctorlist)]
averagestable = selecteddoctors.groupby(['PAC ID'], as_index=False).agg({'Measure Performance Rate':['mean']})
averageslist = averagestable['Measure Performance Rate']


# In[39]:


averageslist["mean"].std()

