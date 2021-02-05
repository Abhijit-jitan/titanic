import pandas as pd
import numpy as np
import streamlit as st
import random as rd
import pickle
np.random.seed(13) #random seed to keep predictions consistent

model = pickle.load(open("model.pickle",'rb'))


## STREAMLIT
st.write("""
         # Would you have survived the Titanic Disaster?""")
st.image("https://media1.faz.net/ppmedia/aktuell/83311481/1.1703919/format_top1_breit/der-untergang-der-titanic-1912.jpg",
         caption = "This disaster.")
st.write("""
         ## How it works:
         """)

st.markdown("[You can find more facts about the Titanic here](https://www.telegraph.co.uk/travel/lists/titanic-fascinating-facts/#:~:text=1.,2.)")        

st.sidebar.header("User Input Parameters")

def user_input():
    age = st.sidebar.slider("Your Age", 1,75,30)
    fare = st.sidebar.slider("Fare in 1912 $ (See Info)",15,500,40)
    SibSp = st.sidebar.selectbox("How many siblings or spouses are travelling with you?",[0,1,2,3,4,5,6,7,8])
    Parch = st.sidebar.selectbox("How many parents or children are travelling with you?",[0,1,2,3,4,5,6,7,8])
    cabin_multiple = st.sidebar.selectbox("How many additional cabins have you booked?",[0,1,2,3,4])
    numeric_ticket = rd.randint(0, 1)
    Sex = st.sidebar.selectbox("Select your Gender (due to the historical nature of the data only male/female are available)",["male","female"])
    Sex_female = 0 if Sex == "male" else 1
    Sex_male = 0 if Sex == "female" else 1
    Pclass = st.sidebar.selectbox("Which Class is your ticket from?  (For accurate predictions match with Fare)", [1,2,3])
    Pclass_1 = 1 if Pclass == 1 else 0; Pclass_2 = 1 if Pclass == 2 else 0; Pclass_3 = 1 if Pclass == 3 else 0
    boarding = st.sidebar.selectbox("Where did you board the Titanic?", ["Cherbourg","Queenstown","Southampton"])
    Embarked_C = 1 if boarding == "Cherbourg" else 0; Embarked_Q = 1 if boarding == "Queenstown" else 0; Embarked_S = 1 if boarding == "Southampton" else 0
    data = {"Age": age,"norm_fare":np.log(fare+1),"SibSp":SibSp,"Parch":Parch,"cabin_multiple": cabin_multiple,
            "numeric_ticket":numeric_ticket,"Sex_female":Sex_female,"Sex_male":Sex_male,"Pclass_1": Pclass_1, "Pclass_2": Pclass_2, "Pclass_3": Pclass_3,
            "Embarked_C":Embarked_C,"Embarked_Q":Embarked_Q, "Embarked_S":Embarked_S}
    df = pd.DataFrame(df, index = [0])
    return df

data = user_input()

prediction = model.predict(data)
st.title("Survival Prediction")
if prediction[0] == 1:
    st.write("**You probably would have made it!**")
else: 
    st.write("Well...how do I put this...**you're probably safer just watching the movie!**")
