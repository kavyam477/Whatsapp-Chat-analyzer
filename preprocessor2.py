import pandas as pd
from dateutil import parser
def process_chat_data(data):
    # Split the data into lines
    lines = data.strip().split('\n')
    datas = {'date': [], 'sender': [], 'message': []}

    current_date, current_sender, current_message = None, None, None

    for line in lines:
        if line.startswith('['):
            split_line = line.split('] ', 1)
            if len(split_line) == 2:
                current_date, full_sender = split_line
                current_sender = full_sender.split(':', 1)[0].strip()
                current_date = pd.to_datetime(current_date[1:], errors='coerce', utc=True)
        else:
            current_message = line.strip()
            if current_date is not None and current_sender is not None:
                datas['date'].append(current_date)
                datas['sender'].append(current_sender)
                datas['message'].append(current_message)

    df = pd.DataFrame(datas)
    df["year"] = df["date"].dt.year
    df["month_num"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["only_date"] = df["date"].dt.date
    df["day_name"] = df["date"].dt.day_name()
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.month_name()
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute
    period = []
    for hour in df[["day_name", "hour"]]["hour"]:
        if hour == 23:
            period.append(str(hour) + "-" + str("00"))
        elif hour == 0:
            period.append(str("00") + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df["period"] = period
    return df