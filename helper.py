#from urlextract import URLExtract
#extract=URLExtract()
def fetch_stats(selected_user,df):
    if selected_user != "overall":
        df = df[df["sender"] == selected_user]
    num_messages=df.shape[0]
    words = []
    for message in df["message"]:
        words.extend(message.split())

     #fetch number of leave messages
    #number_of_leave_info_messages=df[df["message"]=="I am on leave today"].shape[0]
     # fetch number of links shared


    return num_messages, len(words)


def most_busy_users(df):
    x = df["sender"].value_counts().head()
    df=round((df["sender"].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={"sender": "name", "count": "percent"})
    return x,df


def monthly_timeline(selected_user,df):
    if selected_user != "overall":
        df = df[df["sender"] == selected_user]
    timeline = df.groupby(["year", "month_num"]).count()["message"].reset_index()
    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                   7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    # Adding a new column "month_name" based on the "month_num" column
    timeline['month'] = timeline['month_num'].map(month_names)
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i] + "-" + str(timeline["year"][i]))
    timeline["time"] = time
    return timeline
def daily_timeline(selected_user,df):

    if selected_user != "overall":
        df = df[df["sender"] == selected_user]

    daily_timeline = df.groupby(["only_date"]).count()["message"].reset_index()
    return daily_timeline
def week_activity_map(selected_user,df):

    if selected_user != "overall":
        df = df[df["sender"] == selected_user]
    return df["day_name"].value_counts()


def month_activity_map(selected_user,df):

    if selected_user != "overall":
        df = df[df["sender"] == selected_user]
    return df["month_name"].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user != "overall":
        df = df[df["sender"] == selected_user]
    user_heatmap=df.pivot_table(index="day_name", columns="period", values="message", aggfunc="count").fillna(0)
    return user_heatmap
"""    
    
    if selected_user=="overall":
        #1. fetch number of messages
        num_messages=df.shape[0]
        #2. number of words
        words = []
        for message in df["message"]:
            words.extend(message.split())
        return num_messages,len(words)
    else:
        new_df=df[df["sender"]==selected_user]
        num_messages=new_df.shape[0]
        words = []
        for message in new_df["message"]:
            words.extend(message.split())
        return num_messages,len(words)
        
"""


