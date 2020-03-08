import pandas as pd
import warnings

warnings.filterwarnings('ignore')

entry= []
username= input("What would you like your username to be?")
entry.append(username)


print("Hello, this is discrimiTalk and we're here to help you meet other people going through the same thing as you. This is an anonymous platform and so all you have to enter on",
      "registration is your story, we will give you a template and you can right the story of your experience. If you give consent this story will also be shown to people who are similar to you.",
      "If you do not consent to this your story will be kept completely confidential and will only be used to pair you with others.")

story= input("Please write about what is happening to you and what you are feeling.")

gender= ['woman', 'man', 'feminist', 'gender', 'female', 'male', 'sexism', 'sex', 'girl', 'boy', 'women', 'men']

sexual_harassment= ['sex', 'rape', 'consent', 'exploitation', 'impropriety', 'victimisation', 'inappropriate', 'assault', 'sexual', 'harassment', 'coercion', 'pressure', 'unwanted', 'involuntary', 'non-consential',
                    'interaction', 'groping', 'fondling', 'touching']
religionOrViews= [ 'opinion', 'religion', 'view', 'idea', 'politic', 'thought', 'jew', 'judaism', 'christian', 'islam', 'athiest', 'secular', 'agnostic', 'hindu', 'budh', 'indigenous', 'diasporic', 'sikh', 'jain']

sexual_orientation= ['gay', 'bi', 'queer', 'straight', 'love', 'LGBT', 'lesbian', 'pan', 'a-sexual', 'a-romantic', 'orientation', 'sexual']

types={'gender': ['woman', 'man', 'feminist', 'gender', 'female', 'male', 'sexism', 'sex', 'girl', 'boy', 'women', 'men'],
       'sexual_harassment': ['sex', 'rape', 'consent', 'exploitation', 'impropriety', 'victimisation', 'inappropriate', 'assault', 'sexual', 'harassment', 'coercion', 'pressure', 'unwanted', 'involuntary', 'non-consential',
                    'interaction', 'groping', 'fondling', 'touching'],
       'religionOrViews': [ 'opinion', 'religion', 'view', 'idea', 'politic', 'thought', 'jew', 'judaism', 'christian', 'islam', 'athiest', 'secular', 'agnostic', 'hindu', 'budh', 'indigenous', 'diasporic', 'sikh', 'jain'],
       'sexual_orientation': ['gay', 'bi', 'queer', 'straight', 'love', 'LGBT', 'lesbian', 'pan', 'a-sexual', 'a-romantic', 'orientation', 'sexual']}



def finder(category):
    occurrence = 0 

    for i in range(len(category)):
        
        if category[i] in story.lower():
            occurrence += 1

    return occurrence

for t in types:
    occurrence= finder(types[t])

    if occurrence>=3:
        entry.append(True)
    else:
        entry.append(False)
df = pd.read_excel('hackathonexcel.xlsx', index_col= 0)
df2 = pd.DataFrame([entry], columns= ['username', 'gender', 'sexual_harassment', 'religionOrViews', 'sexual_orientation'])
df= df.append(df2)
df.to_excel('hackathonexcel.xlsx')

amount = 0 




