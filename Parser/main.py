import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns


def get_currency_rate(date):
    url = "http://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx"
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://web.cbr.ru/GetCursOnDate",
    }

    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <GetCursOnDate xmlns="http://web.cbr.ru/">
          <On_date>{date}</On_date>
        </GetCursOnDate>
      </soap:Body>
    </soap:Envelope>"""

    response = requests.post(url, headers=headers, data=body)

    root = ET.fromstring(response.text)
    namespace = {
        "msdata": "urn:schemas-microsoft-com:xml-msdata",
    }

    aud_data = root.findall(".//ValuteCursOnDate", namespace)
    for valute in aud_data:
        vname = valute.find("Vname", namespace).text.strip()
        if vname == "Австралийский доллар":
            vcurs = float(valute.find("Vcurs", namespace).text)
            return date, vcurs
    return date, None


start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 10, 21)

data = []

current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    date, vcurs = get_currency_rate(date_str)
    data.append((date, vcurs))
    current_date += timedelta(days=1)

df = pd.DataFrame(data, columns=["Date", "AUD_Curs"])
df = df.dropna()

print(df)


df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(10, 6))
sns.lineplot(x="Date", y="AUD_Curs", data=df, marker="o")
plt.title("Курс Австралийского доллара за несколько дней")
plt.xlabel("Дата")
plt.ylabel("Курс")
plt.xticks(rotation=45)
plt.grid()
plt.show()
