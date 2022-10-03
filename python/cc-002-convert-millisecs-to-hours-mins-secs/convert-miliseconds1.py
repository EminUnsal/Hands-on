def convert():
    millis=int(input("Enter time in milliseconds...: "))
    seconds=(millis/1000)%60    # 1 sec = 1,000 ms
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    hours=int(hours)
    print(f"{hours}:{minutes}:{seconds}")
convert()