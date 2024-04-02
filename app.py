import pickle
import streamlit as st
import pandas as pd

new_df = pd.read_csv('data.csv')
similarity = pickle.load(open('similarity.pkl','rb'))


st.title("movie recommender System")

option = st.selectbox(
    'How would you like to be contacted?',
    options=new_df['title'].tolist())





def recommend(movie):
    l=[]
    index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        l.append(new_df.iloc[i[0]].title)
    return l
        

if st.button('Recommend'):
    l = recommend(option)
    for i in l:
        st.write(i)
     