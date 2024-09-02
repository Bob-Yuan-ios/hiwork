import requests
import pandas as pd


def baseInfo():
    url = "https://data.10jqka.com.cn/dataapi/new_stock_calendar/v2/base_info"
    params = {
        'module': 'wait_listing'
    }
    response = requests.get(
        url=url,
        params=params
    )

    if 200 == response.status_code:
        data = response.json()
        # print(data)

        stock_name = []
        order_date = []
        listing_date = []

        for stock in data['data']['stock']:
            stock_name.append(stock['stock_name'])
            order_date.append(stock['order_date'])
            listing_date.append(stock['listing_date'])

        format_dic = {
            '名称': stock_name,
            'order_date': order_date,
            'listing_date': listing_date
        }

        df = pd.DataFrame.from_dict(format_dic)
        print(df.to_markdown())

    else:
        print("request failed")


def baseInfoDetail(code: str = '001277', stock_type: str = 'stock'):
    url = "https://data.10jqka.com.cn/dataapi/new_stock_calendar/v1/base_info_detail"
    params = {
        'code': code,
        'type': stock_type
    }
    response = requests.get(
        url=url,
        params=params
    )
    if 200 == response.status_code:
        data = response.json()
        print(data)
    else:
        print("request failed")

