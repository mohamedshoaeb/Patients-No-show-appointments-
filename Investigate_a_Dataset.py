#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [No-show appointments]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# >**Description** : This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.
# 
# **01 - PatientId** <br>
# Identification of a patient.<br>
# **02 - AppointmentID**<br>
# Identification of each appointment<br>
# **03 - Gender**<br>
# Male or Female . Female is the greater proportion, woman takes way more care of they health in comparison to man.<br>
# **04 - DataMarcacaoConsulta**<br>
# The day of the actuall appointment, when they have to visit the doctor.<br>
# **05 - DataAgendamento**<br>
# The day someone called or registered the appointment, this is before appointment of course.<br>
# **06 - Age**<br>
# How old is the patient.<br>
# **07 - Neighbourhood**<br>
# Where the appointment takes place.<br>
# **08 - Scholarship**<br>
# True of False .<br>
# <a href="#https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia">For more information</a><br>
# **09 - Hipertension**<br>
# True or False<br>
# **10 - Diabetes**<br>
# True or False<br>
# **11 - Alcoholism**<br>
# True or False<br>
# **12 - Handcap**<br>
# True or False<br>
# **13 -SMS_received**<br>
# 1 or more messages sent to the patient.<br>
# **14 - No-show**<br>
# True or False.<br>
# 
# 
# 
# > **Tip**: In this section of the report, provide a brief introduction to the dataset you've selected/downloaded for analysis. Read through the description available on the homepage-links present [here](https://docs.google.com/document/d/e/2PACX-1vTlVmknRRnfy_4eTrjw5hYGaiQim5ctr9naaRd4V9du2B5bxpd8FEH3KtDgp8qVekw7Cj1GLk1IXdZi/pub?embedded=True). List all column names in each table, and their significance. In case of multiple tables, describe the relationship between tables. 
# 
# 
# ### Question(s) for Analysis
# >**Tip**: Clearly state one or more questions that you plan on exploring over the course of the report. You will address these questions in the **data analysis** and **conclusion** sections. Try to build your report around the analysis of at least one dependent variable and three independent variables. If you're not sure what questions to ask, then make sure you familiarize yourself with the dataset, its variables and the dataset context for ideas of what to explore.
# 
# > **Tip**: Once you start coding, use NumPy arrays, Pandas Series, and DataFrames where appropriate rather than Python lists and dictionaries. Also, **use good coding practices**, such as, define and use functions to avoid repetitive code. Use appropriate comments within the code cells, explanation in the mark-down cells, and meaningful variable names. 

# In[ ]:





# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')



# In[2]:


#Create function to draw pie char
def pot_pie(data , labels1 , *args, **kwargs):  
    title1 = kwargs.get('title1', None) 
    use1 = kwargs.get('use1', None)
    text1 = kwargs.get('text1', None)
    if text1 is not None:
        plt.text(-4,-1.7 , text1)
    
    plt.axis('equal') 
    plt.pie(data,labels=labels1,radius=1.2,shadow=True,explode=(0,0.2),autopct='%1.2f%%',startangle=180,textprops = {"fontsize":15})
    plt.title(title1,y=1.2)
    plt.show


# In[3]:


#read data 
df = pd.read_csv('Database_No_show_appointments/noshowappointments-kagglev2-may-2016.csv')
df.head()


# In[4]:


df.shape


# In[5]:


df.describe()


# # 1- Change the "No Show" values to make it easier to deal with

# In[6]:


#change 'yes' and  'no' to 0 and 1 to be easy in the work
df["No-show"].replace({"Yes":0,"No":1},inplace=True)


# In[7]:


df.info()


# 2 - After displaying the data, we need to change the data type of the columns “ScheduledDay” and “AppointmentDay” to a data type of dates and 'PatientId' and 'AppointmentID' to string

# In[8]:


#convert ScheduledDay to datetime type
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])


# In[9]:


#convert AppointmentDay to datetime type

df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])


# In[10]:


#convert PatientId to string type
df['PatientId'] = df['PatientId'].astype(str)


# In[11]:


#convert AppointmentID to string type

df['AppointmentID'] = df['AppointmentID'].astype('str')


# In[12]:


df.describe()


# After looking at the data and determining the age, we notice that there are negative ages, so we must delete the negative columns

# In[13]:


#check invalid data
df[df['Age'] < 0]


# In[14]:


#drop invalid data
df = df.drop([99832])


# In[15]:


df['Age'].min()


# # Question 1
# What is the percentage of patients who show up on their appointements vs. who don't?

# In[16]:


df


# In[17]:


#count of 1 in No-show column in the data
num_no_show = df[df['No-show'] == 1].count()['No-show']
num_no_show


# In[18]:


#count of 0 in No-show column in the data

num_no_show2 = df[df['No-show'] == 0].count()['No-show']
num_no_show2


# In[ ]:





# In[19]:


#draw pie with pot_pie function

pot_pie(data = [num_no_show , num_no_show2] ,labels1 = ['They came on their date','They did not arrive on time'] , title1 = 'Percentage of patients who came and did not come' )


# The proportion of patients who came to their appointment is 79.8%
# 
# Percentage of patients who did not attend their appointment 20.2%

# # Question 2
# Do certain gender has more commitment to medical schedules than the other one?

# In[46]:


#calculate the count of of different gender whos go or no
x = df.groupby(['Gender', 'No-show']).count()
x


# In[21]:


#draw the count of of different gender whos go or no
x["PatientId"].unstack().plot(kind='bar',grid=True)
plt.legend(["didn't show up on time",'show up on time']) 
plt.suptitle('Number of attendees and non-attendances vs. gender') 
plt.ylabel('count of patients')


# 
# We note in the drawing that the attendance rate is high in terms of men and women, especially women more
# 

# In[22]:


#calculate the count of males
df_male = df[df['Gender'] == 'M'] 
df_m_count = df_male['PatientId'].count() 


# In[23]:


male_No_show = df_male[df_male['No-show'] == 1] 


# In[24]:


#calculate the count of males whos go
count_m_df = male_No_show['No-show'].sum() 


# In[25]:


#calculate the mean of males whos go
male_data = count_m_df / df_m_count * 100
print(f'Percentage of Males who show up on their appointments is around {male_data:.2f} of all male patients.')


# In[26]:


#calculate the count of fmales 
df_females = df[df['Gender'] == 'F']
df_f_count = df_females['PatientId'].count()


# In[27]:


females_No_show = df_females[df_females['No-show'] == 1]


# In[28]:


#calculate the count of fmales whos go
count_f_df = females_No_show['No-show'].sum()


# In[29]:


count_f_df


# In[30]:


#calculate the mean of fmales whos go

females_data = count_f_df / df_f_count * 100
print(f'Percentage of females who show up on their appointments is around {females_data:.2f} of all female patients.')


# # Question 3
# Is the duration between registration and appointment affect the ability to show up

# In[31]:


#calculate the time_duration
df['time_duration'] = (df.AppointmentDay.dt.date) - (df.ScheduledDay.dt.date)


# In[32]:


df['time_duration'] = df.time_duration.dt.days


# In[33]:


df.head(10)


# In[34]:


#draw pie with pot_pie function
x = df.groupby(['No-show'])['time_duration'].mean()
pot_pie(data = x ,labels1 = ["didn't attend","attend"] ,
        title1 = 'Percentage of average days late versus those who attended and did not attend' ,
        text1 = "Patients Who didn't show up have an average of 15 days between registeration day and their appointments.\nPatients Who show up have an average of 8 days between registeration day and their appointments.")


# Answer:
# Patients Who didn't show up have an average of 15 days between registeration day and their appointments.<br>
# Patients Who show up have an average of 8 days between registeration day and their appointments.
# 
# As Duration increases, the ability of patients to show up on their appointments decreases.

# # Question 4
# Where is the most appointments take place

# In[35]:


#draw bar with to Neighbourhood and time_duration
df.groupby(['Neighbourhood'])['time_duration'].sum().plot(kind='bar',figsize=(14,14),fontsize=10)


# # Question 5
# Do patients who recieves SMS to remind them of the appointement more likely to show up

# In[36]:


#draw pie with pot_pie function
x = df.groupby(['SMS_received'])['No-show'].mean()


 
pot_pie(data = x ,labels1 =["didn't received sms","SMS_received"] ,
        title1 = 'Percentage of Average SMS Received VS No Show' )


# In[37]:


#calculate percentage of SMS received and none received
SMS_df = df.loc[(df['SMS_received'] == 1 ) & df['Age']]['No-show'].mean()
SMS_No_df = df.loc[(df['SMS_received']== 0 ) & df['Age']]['No-show'].mean()

print(f'No-show percentage with SMS is {SMS_df*100:.2f}, while {SMS_No_df*100:.2f}  without SMS.')


# # Question 6
# What is percentage of patients who diagnosed with Diabetes, Hipertension, Alcoholism, and Handcap

# In[38]:




count = 110526 #number of data records

#calculate percentage of Diabetes
count_diabets = df[df['Diabetes']==1]['PatientId'].count()
print(f"Percentage of patients who diagnosed with Diabetes is {count_diabets*100/count:.2f}.")


# In[39]:


#calculate percentage of Hipertension
count_diabets = df[df['Hipertension']==1]['PatientId'].count()
print(f"Percentage of patients who diagnosed with Hipertension is {count_diabets*100/count:.2f}.")


# In[ ]:





# In[ ]:





# In[44]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# <a id='conclusions'></a>
# ## Conclusions
# 1. There is not big difference between the distribution of Age between patients who showed up for the appointment versus the patients that did not show up for the appointment. <br>
# 2. There is a higher percentage of people that received an SMS and did not show up when compared to people who received an SMS and did show up. <br>
# 3. People that have a disease are 3% more likely to show up for the appointment than people who do not have a disease. <br>
# 4. Handicap patients specifically,however, are more likely to show up to the appointment compared to people who are not Handicap. <br>
# 5. Being enrolled in the Scholarship program does not seem to make people more likely to show up to the appointment.<br> 
# ## Limitations: <br>
# 1- Most of our variables are categorical, which does not allow for a high level of statistical method that can be used to provide correlations etc <br><br>
# 2- The statistics used here are descriptive statistics, not inferential, meaning that we did not create any hypotheses or controlled experiments or inferences with our data.<br>
# 3- We do not have a lot of details for certain factors to draw conclusions. For the SMS_received example, the data shows that no-showers are more likely to receive an SMS. This may seem counter intuitive, but we do not have information on the conditions of when the SMS is sent. For example they may target No-showers with SMS, or they may send the SMS once the Patient has not checked in 30 minutes prior to their appointment etc.<br>
# 4- Cannot show strong correlations between factors since most of our data is categorical.<br>
# 

# In[ ]:




