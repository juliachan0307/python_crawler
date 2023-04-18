import requests

r = requests.get("https://www.tmrt.com.tw/api/public/FareTime/95ea9819-79c6-4069-bee9-80e09f9ceb75", verify=False)
list_of_dicts = r.json()

print("起站", "訖站", "單程票票價", "電子票證", "敬老卡、愛心卡、愛心陪伴卡", "乘車時間(分鐘)")

for dic in list_of_dicts:
    print(dic["StartSiteName"], dic["StopSiteName"], dic["GeneralFare"], dic["ElectronicFare"], dic["RespectFare"], dic["SpendTime"])