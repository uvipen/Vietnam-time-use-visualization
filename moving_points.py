import pandas as pd
from time import gmtime, strftime
from d3blocks import D3Blocks


def convert_time(minute):
    return strftime("%d-%m-%Y %H:%M:%S", gmtime(int(minute) * 60))


def get_activity(code):
    code = int(code)
    if code in [101, 102, 199, 201, 202, 299, 301, 302, 399, 401, 402, 499, 502]:
        return "Work"
    elif code in [198, 298, 298, 498, 598, 698, 798, 898, 998, 1098, 1198, 1298, 1398, 1498, 1598]:
        return "Travelling"
    elif code in [501]:
        return "Sell food"
    elif code in [504, 505, 506, 507, 508]:
        return "Provide services"
    elif code in [601]:
        return "Housework"
    elif code in [602]:
        return "Shopping"
    elif code in [701, 702]:
        return "Caring"
    elif code in [901, 902, 903]:
        return "Education"
    elif code in [1201, 1202, 1203, 1299]:
        return "Entertainment"
    elif code in [1301, 1302, 1399]:
        return "Sport"
    elif code == 1402:
        return "TV/Youtube"
    elif code == 1404:
        return "Surf web"
    elif code == 1501:
        return "Sleeping"
    elif code == 1502:
        return "Eating"
    elif code == 1503:
        return "Personal hygiene"
    elif code == 1506:
        return "Relaxing"
    else:
        return "Others"


data = pd.read_csv("4_diary_main.csv", usecols=["ID", "BEGIN", "Q401"],
                   encoding='latin-1',
                   converters={"Q401": get_activity, "BEGIN": convert_time})
data = data.sort_values(["ID", "BEGIN"])
data = data.rename(columns={"ID": "sample_id", "BEGIN": "datatime", "Q401": "state"})
data = data.iloc[:int(len(data) / 4)]
d3 = D3Blocks()

d3.movingbubbles(data, datetime="datatime", sample_id="sample_id", state="state", filepath="./moving_point.html",
                 note="How Vietnamese people spend their time", cmap="hsv", center="Travelling", figsize=(780, 800), size=2)
