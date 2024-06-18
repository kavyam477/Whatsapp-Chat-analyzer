import pandas as pd
from dateutil import parser
def process_chat_data(data):
    # Split the data into lines
    lines = data.strip().split('\n')
    datas = []

    # Iterate through each line and extract information
    for line in lines:
        # Split each line into components
        components = line.strip('[]').split('] ')
        # Extract date, time, sender, and message
        date_time = components[0]
        sender_message = components[1].split(': ', 1)
        sender = sender_message[0]
        message = sender_message[1]
        datas.append([date_time, sender, message])

    # Create a DataFrame
    df = pd.DataFrame(datas, columns=['Date/Time', 'Sender', 'Message'])
    df['Date/Time'] = df['Date/Time'].str.replace(r'[', '')

    # Define a function to remove the unwanted character
    def parse_and_clean(date_string):
        cleaned_string = date_string.lstrip("‎")
        return parser.parse(cleaned_string)

    # Apply the custom function to the "Date/Time" column
    df["Date/Time"] = df["Date/Time"].apply(parse_and_clean)

    # Extract additional date/time components
    df["Year"] = df["Date/Time"].dt.year
    df["Day"] = df["Date/Time"].dt.day
    df["Month"] = df["Date/Time"].dt.month
    df["Hour"] = df["Date/Time"].dt.hour
    df["Minute"] = df["Date/Time"].dt.minute

    return df

# Example usage:
#with open("_chat.txt", "r", encoding="utf_8") as file:
   # chat_data = file.read()

#result_df = process_chat_data(data)
#print(result_df)