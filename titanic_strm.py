import pandas as pd
import streamlit as st
import pickle

model = pickle.load(open("titanic_v4.pkl", 'rb'))

def main():
    st.title("Titanic Survival Prediction")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/St%C3%B6wer_Titanic.jpg/450px-St%C3%B6wer_Titanic.jpg", caption="Sinking of 'RMS Titanic' : 15 April 1912 in North Atlantic Ocean")
    st.write("""
             ## Would you have survived the Titanic Disaster?""")



    st.write("""
             # How it's working: Here we have taken some Parameters like
             ### Age , Gender , Passenger Class , Boarding Location , Fare , Siblings , Parents
             
    
             ## Inside Srvival Tips: 
             - *Only about 32% of passengers survived.*\n
             
             - *Women & Children are Most likely to Survive*\n
               *Women are 74% & Children(between 18) are 50% chances to Survive.*\n
               *Survival Rate for Men are very low (only 17%)*\n
               
             - Ticket price:\n
                            1st class: $150-$435 \n
                            2nd class: $60 \n
                            3rd class: $15-$40 \n
               Survival Percentage : 63% in *1st-class* ; 47.3% in *2nd-class* ; 24.2% in *3rd-class*  
                
             - Boarding Locations: *"Cherbourg" , "Queenstown" ,"Southampton"* \n
               Survival Percentage: 41% in *"Cherbourg"* ; 40% in *"Queenstown"* ; 34% in *"Southampton"*                 
                
             - About Family Factor:\n
                If You Boarded with your atleast one family member 51% Survival rate
               """)

    st.sidebar.header("More Details:")
    st.sidebar.markdown("[For More facts about the Titanic here](https://www.telegraph.co.uk/travel/lists/titanic-fascinating-facts/#:~:text=1.,2.)")
    st.sidebar.markdown("[and here](https://titanicfacts.net/titanic-survivors/)")

    st.title("--- Check Your Survival Chances ---")

    ## Input
    age = st.slider("Enter Age :", 1, 75, 30)
    fare = st.slider("Fare (in 1912 $) :", 15, 500, 40)
    SibSp = st.selectbox("How many Siblings or spouses are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    Parch = st.selectbox("How many Parents or children are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8])
    sex = st.selectbox("Select Gender:", ["male","female"])
    Sex= 1 if sex == "female" else 0
    #Sex_male = 0 if Sex == "female" else 1

    Pclass= st.selectbox("Select Passenger-Class:",[1,2,3])
    boarding = st.selectbox("Boarded Location:", ["Cherbourg","Queenstown","Southampton"])
    Embarked_C=1 if boarding=="Cherbourg" else 0;Embarked_Q=1 if boarding=="Queenstown" else 0;Embarked_S=1 if boarding=="Southampton" else 0

    data={"Age":age,"Fare":fare,"SibSp":SibSp,"Parch":Parch,"Sex":Sex,
    "Pclass":Pclass,"Embarked_C":Embarked_C,"Embarked_Q":Embarked_Q,"Embarked_S":Embarked_S}


    df=pd.DataFrame(data,index=[0])
    return df

#def predict(df):
data=main()
if st.button("Predict"):
    result = model.predict(data)
    st.success('The output is {}'.format(result))

    if result[0] == 1:
        st.write("congratulation !!!.... **You probably would have made it!**")
        st.image(
            "https://thumbs-prod.si-cdn.com/pn1W-PCw0pwa_EpefSOduW74gcM=/fit-in/1072x0/https://public-media.si-cdn.com/filer/Titanic-survivors-drifting-2.jpg")
    else:
        st.write("Better Luck Next time !!!!...**you're probably Ended up like 'Jack'**")
        st.image(
            "https://i2-prod.irishmirror.ie/incoming/article9830920.ece/ALTERNATES/s615b/0_Kate-Winslet-as-Rose-DeWitt-Bukater-and-Leonardo-DiCaprio-as-Jack-Dawson-in-Titanic.jpg")



if st.button("Author"):
    st.write("## @ Abhijit")
    st.write("### Built with Streamlit")
