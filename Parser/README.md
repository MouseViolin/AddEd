# Получение курса валют с сайта ЦБ с последующей визуализацией

## Необходимые библиотеки

```python
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
```

- **`xml.etree.ElementTree`**: Библиотека для работы с XML-документами
- **`datetime` и `timedelta`**: Библиотеки для работы с датами и временными интервалами
- **`matplotlib.pyplot`**: Библиотека для визуализации данных
- **`pandas`**: Библиотека для работы с табличными данными
- **`requests`**: Библиотека для отправки HTTP-запросов
- **`seaborn`**: Библиотека для создания статистических графиков

## Запрос

Запрос сформирован на основе примера на официальном [сайте](https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?op=GetCursOnDate).
<img width="1058" alt="image" src="https://github.com/user-attachments/assets/8dbf8fc3-3ad6-4e26-a921-e9b8cf27a545">


После успешного запроса мы получаем ответ в XLM формате, из которого ищем необходимый фрагмент `.//ValuteCursOnDate`.

Наша основная задача найти искомое значение из которого мы уже будем получать значение курса.

```python
if vname == "Австралийский доллар"
```

# Не успел оформить (((

позже дооформлю
![23ff55ce252295d2afba88df99e71010](https://github.com/user-attachments/assets/ee77495d-ad2f-450b-9fbc-ac7339170a8a)
