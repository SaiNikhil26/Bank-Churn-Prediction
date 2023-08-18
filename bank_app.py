import streamlit as st
import pickle 
pickle_in = open("bank_churn2.pkl","rb")
clf = pickle.load(pickle_in)

def prediction(credit,geo,gender,age,tenure,balance,products,creditcard,active,estimated_salary):
    pred = clf.predict([[credit,geo,gender,age,tenure,balance,products,creditcard,active,estimated_salary]])
    if(pred == 1):
        print("The Customer will exit the bank")
    else:
        print("The Customer will retain their account with the bank")
    return pred


def main():
    st.title("Bank Customer Churn Predictor")
    credit = st.number_input('Enter your Credit Score')
    geography =st.selectbox ('Select Geography',['France','Germany','Spain'])
    if (geography=='France'):
        geo = 0
    if(geography=='Germany'):
        geo = 1
    if(geography=='Spain'):
        geo = 2
    gen =st.selectbox ('Select Gender',['Male','Female'])
    if(gen=='Male'):
        gender = 1
    if(gen=='Female'):
        gender = 0
    age = st.number_input("Enter Age")
    tenure= st.number_input ("Tenure in months ")
    balance = st.number_input("Balance Amount")
    products = st.number_input("Number of Products")
    credit = st.checkbox("Does customer have a credit card?")
    if credit:
        creditcard = 1
    else:
        creditcard = 0
    act_member = st.checkbox("Does customer is active member of the bank?")
    if act_member:
        active = 1
    else:
        active = 0
    estimated_salary = st.number_input("Estimated Salary of the customer")
    if st.button("Predict"):
        result = prediction(credit,geo,gender,age,tenure,balance,products,creditcard,active,estimated_salary)
        if(result == 1):
            st.success("The customer will exit the bank")
        else:
            st.success("The customer will retain their account with the bank")

if __name__ =='__main__':
    main()