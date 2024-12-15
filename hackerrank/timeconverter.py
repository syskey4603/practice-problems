def timeconverter(s):
    news = s.split(":")
    if "12" in news[0] and "PM" in s:
        returns = news[0] + ":" + news[1] + ":" +  news[2].replace("PM", "")
    elif "12" in news[0] and "AM" in s:
        returns = "00:" + news[1] + ":" + news[2].replace("AM", "")
    elif "PM" in s:
        returns = str(int(news[0])+12) + ":" + news[1] + ":" +  news[2].replace("PM", "")
    elif "AM" in s:
        returns = news[0] + ":" + news[1] + ":" +  news[2].replace("AM", "")
    return returns


s = "12:01:00AM"
print(timeconverter(s))