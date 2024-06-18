import streamlit as st
import preprocessor2,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("whatsapp chat analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    datas=bytes_data.decode("utf-8")
    df=preprocessor2.process_chat_data(datas)
    st.dataframe(df)
    #fetch unique users
    user_list=df["sender"].unique().tolist()

    user_list.sort()
    user_list.insert(0,"overall")
    selected_user=st.sidebar.selectbox("show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages,words=helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")

        col1, col2, col3, col4 =st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col3:
            st.header("Total Words")
            st.title(words)



        #monthly timeline
        st.title("Monthly Timeline")
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline["time"], timeline["message"],color="green")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)
        #daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline["only_date"], daily_timeline["message"], color="black")
        plt.xticks(rotation="vertical")
        st.pyplot(fig)

        #activity map
        st.title("Activity Map")
        col1,col2=st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day=helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color="orange")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)


        st.title("Weekly activity map")
        user_heatmap=helper.activity_heatmap(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(user_heatmap)
        st.pyplot(fig)


        #finding the busiest users in the  group(Group level)
        if selected_user=="overall":
            st.title("Most Busy Users")
            x,new_df=helper.most_busy_users(df)
            fig,ax=plt.subplots()

            col2,col3=st.columns(2)

            with col2:
                ax.bar(x.index, x.values,color="red")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)

            with col3:
                st.dataframe(new_df)
