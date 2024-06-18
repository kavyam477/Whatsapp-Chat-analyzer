import streamlit as st
#import preprocessor
import pickle
Model = pickle.load(open(r"Model", 'rb'))
st.sidebar.title("whatsapp chat analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    datas=bytes_data.decode("utf-8")
    df=preprocessor.process_chat_data(datas)
    st.dataframe(df)
    #fetch unique users
    user_list=df["Sender"].unique().tolist()
    st.sidebar.selectbox("show analysis wrt",user_list)