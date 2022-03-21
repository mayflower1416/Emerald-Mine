#!/usr/bin/env python
# coding: utf-8

# ##Business Analyst Interviews – Data Test Medical School Data and Analytics
# 
# 
# 
#
# 
# 
# 
# 
# Introduction
# In the email you received from the hiring manager you will have received a dataset. We will ask you to analyze this dataset, guided by the questions below. There are no right or wrong answers, and feel free to be creative.
# 
# Using any data visualization or statistical software you are comfortable with (e.g. Excel, Tableau, R, Stata, etc.), prepare an analysis of the dataset you received. This task is intended to take no longer than one hour.
# 
# 
# Instructions
# 
# 
# 1) Open the file on the desktop titled “Data Test”
# 
# 2) The file contains historical data on faculty salaries and FTEs. Also included are patient care revenue and research revenue. Please analyze the data, and make note of any trends, anomalies, or discoveries that leadership in the Medical School would be interested in seeing.
# 
# 3) During the interview process be ready to present/discuss the following:
# 
# a. The results of your analysis and what you discovered
# 
# b. What your limitations were
# 
# c. What further analysis you would do if you had additional time
# 

# In[1]:


import pandas as pd 

michMedtestRawdf =pd.read_excel(r'Data Test.xlsx', sheet_name='Raw Data Set')
michMedtestRawdf.head(25)


# In[2]:


michMedtestRawdf['Fiscal Date'] = pd.to_datetime(michMedtestRawdf['Fiscal Year'].astype(str) + '/' + michMedtestRawdf['Fiscal Month'].astype(str))
michMedtestRawdf


# In[3]:


michMedtestpatientCaredf =pd.read_excel(r'Data Test.xlsx', sheet_name='Patient Care Revenue')
michMedtestpatientCaredf


# In[4]:


michMedtestresearchdf =pd.read_excel(r'Data Test.xlsx', sheet_name='Research Revenue')
michMedtestresearchdf


# In[5]:


import numpy as np
payDepPivotTable =pd.pivot_table(michMedtestRawdf, values='Pay', index=['Fiscal Date'],columns=['Department']
           ,aggfunc=np.mean)


# In[7]:


import matplotlib.pyplot as plt

payDepPivotTable.plot( figsize=(15, 15)).set_ylabel('Average Salary  Department Employees', fontsize=15)
plt.title('Average Departmental Salary by Month ',fontsize=20)

plt.xlabel('Date (Month Year)', fontsize=15)




# In[8]:


payDepPivotTableTrackfund =pd.pivot_table(michMedtestRawdf, values='Pay', index=['Fiscal Date'],columns=[ 'Track']
           ,aggfunc=np.mean)



payDepPivotTableTrackfund.plot(figsize=(20, 25),).set_ylabel('Average Salary by Track' ,fontsize=20
                                                )
plt.title('Average Track Salary by Month ',fontsize=25)

plt.xlabel('Date', fontsize=20)




# In[9]:


payDepPivotTablefund =pd.pivot_table(michMedtestRawdf, values='Pay', index=['Fiscal Date'],columns=[ 'Fund']
           ,aggfunc=np.mean)
payDepPivotTablefund

payDepPivotTablefund.plot(figsize=(20, 25),).set_ylabel('Average Salary by Fund' ,fontsize=20
                                                )
plt.title('Average Fund Salary by Month',fontsize=20)

plt.xlabel('Date', fontsize=15)


# In[10]:


payDepPivotTableTrackfund


# In[11]:


payDepPivotTable


# Analysis: 
# 
# There are several important patterns that can be discerned after ordering the data by fiscal year and month and separating these into pivot tables by department track and fund which display the average salary. To begin, thre are times every few months where the salary increaess dramatically indicating that it may be a time in which bonuses are recieved or patient care increases dramatically. I would further investigate wheter or not Doctors are more likely to schedule patient care or other operations at that time which would result in a an increase in pay. When it comes to the different tracts of the staff there does not seem to be a similar pattern abut there are discernible differences betwen how much people of different tracks are paid with clinical and academic administrative track far outearning other categories especially supplmentary and research track. Briefly talking about the research revenue and patient care Revenue, both numbers indicate increase in research and patient care from 2015 to 2016. As for 2016 to 2017, the data is complete meaning it is only a probable continuation of the decreasing trend as there are 2 months omitted and it is highly unlikely that the difference between 2017 and 2016 would be made up in that time. 

# Limitations:
#     
# There were several limitations including the omission of the last two months, which made inference of annual trends ultimately speculative due to incomplete data. Additionally, the fact that the dpartments were unnamed. This prevented meaningful analysis of why certain departments had consistently higher average monthly slaries than others. Additionally, it would have helped to see if there are any commonalties between departments that earn around the same. Going back to the omission months, it makes any conclusions from the Patient Care Revenue and Research Revenue speculative as those were given annually and with 2 months missing meaning that the data was incomplete. Monthly revenue data could help make more refined conclussions since it would be a more compele data set. We overcame these by making educated guesses by using the data from the year to speculate on the trend.  

# Further Analysis:
# 
# With more time or information such as the last two months of salaries and the department names, I could perform more sophisticated anlaysis with logistic regression with the scikit learn library to determine which factors played the biggest role in influencing salary or pay. Without this, we can still see from the chart that the faculty type and the department play a huge role with different values in these columns having times having salaries several orders of magnitude than others. Logistic regression would make it more mathematically rigrous and precise in determining to what degree which other variables influenced how high the pay variable was. ADditionally, after isolating the impacctful variables with logistic regression chi squared, and several other methods. We can the variables which these libraries find to be correlative to pay coupled with the prophet library to predict the the last two months of missing values as we wiill have several rigrously proven and statistically significant correlates. 

# Data Definitions
# 
# 
# Fiscal Year: The year in which the FTE record and pay occurred. Michigan Medicine’s fiscal year runs from July to June. Fiscal Month: The month in which the FTE record and pay occurred. Fiscal month 1 is July.
# 
# Employee ID: The unique identifier of each faculty member.
#     
# Salary Bucket: The bucket into which the pay dollars are assigned.
#     
# FTE: Stands for “Full-Time Equivalent” and represents the effort of the faculty member. A full-time faculty member will have a FTE of 1 for the year.
#     
# Pay: The salary dollars paid to the faculty member.
#     
# Fund: The fund on which the dollars were paid to the faculty member.
#     
# Track: The promotional path and primary function of the faculty member. This can be used as a proxy for what mission (clinical, research, or education) the faculty member primarily supports.
#     
# Department: The de-identified department the faculty member belongs to.
#     
# Patient Care Revenue: The amount of patient care revenue from the income statement. This can be used as a proxy for the amount of clinical work done by Michigan Medicine.
#     
# Research Revenue: The amount of research revenue from the income statement. This can be used as a proxy for the amount of research work done by Michigan Medicine.
