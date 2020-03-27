import requests
from bs4 import BeautifulSoup
from pandas import read_csv, read_html
from telegram.serializer import CountrySerializer
def send_msg(token, chat_id, text):
    # https://api.telegram.org/bot1087454045:AAHVr_4AtQFokNfQps2XZIeFBiqaeZm2zj0/getUpdates
    chat_id="-444155610"
    token="1087454045:AAHVr_4AtQFokNfQps2XZIeFBiqaeZm2zj0"
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + text
    response = requests.get(url)
    if not response.get("ok"):
        return None
    return "Success_fully sent to "+response.get("chat",{}).get("title")

def current_stats():
    html_pages = read_html("https://www.worldometers.info/coronavirus/")
    html_page = html_pages[0]
    html_page = html_page.fillna("0")
    data_format = html_page.to_dict(orient="records")


    # data = requests.get("https://www.worldometers.info/coronavirus/")
    # soup = BeautifulSoup(data.content, 'html.parser')
    # headers=[]
    # data_format=[]
    # table = soup.find(id="main_table_countries_today")
    # head_row = table("thead")[0] if len(table("thead")[0])>0 else None
    # for head in head_row("th"):
    #     headers.append(head.text)
    # country_rows = table("tbody")[0]
    # global_row = table("tbody")[1]("td")

    # global_dict={}

    # for index, head in enumerate(headers[:-3]):
    #         global_dict[head] = global_row[index].text

    # for country_row in country_rows("tr"):
    #     country_dict={}
    #     columns = country_row("td")
    #     for index, head in enumerate(headers[:-3]):
    #         country_dict[head] = columns[index].text
    #     data_format.append(country_dict)

    return data_format
    
def time_series_corona_data():
    csv_file = read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",",")

    headers, data_format=[],[]

    data_format = csv_file.to_dict(orient="records")

    # for head in csv.columns:
    #     headers.append(head)
    # rows,cols = csv.shape

    # for row in range(rows):
    #     country_dict={}
    #     for index,col in enumerate(headers):
    #         country_dict[col]=csv.iloc[row,index]
    #     data_format.append(country_dict)

    return data_format

def regular_update_task():
    datas = current_stats()
    
    for data in datas[:-1] :
        serializer = CountrySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
