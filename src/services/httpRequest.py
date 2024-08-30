import time
import requests
import pandas as pd


def dateStrToTimeStamp(date_string: str = '2024-08-30 11:35:00'):
    # 转为时间数组
    time_array: time.struct_time = time.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(time_array)
    # 结构体属性 tm_year、tm_mon、tm_mday、tm_hour、tm_min、tm_sec
    print("转换后的年份:" + format(time_array.tm_year))
    time_stamp = int(time.mktime(time_array))
    return time_stamp


def getLimitUpPool():
    params = {
        'page': '1',
        'limit': '100',
        'order_type': '0',
        'order_field': '330324',
        'filter': 'HS,GEM2STAR',
        'field': '199112,10,9001,9002,330329,133971,3475914,330325,9004',
        '_': int(round(time.time() * 1000))
    }

    url = "https://data.10jqka.com.cn/dataapi/limit_up/limit_up_pool"
    response = requests.get(
        url=url,
        params=params
    )

    # 检查请求是否成功
    if 200 == response.status_code:
        # 解析JSON响应
        data = response.json()

        name = []
        high_days = []
        reason_type = []
        limit_up_type = []
        result = {}

        for members in data['data']['info']:
            name.append(members['name'])
            reason_type.append(members['reason_type'])
            high_days.append(members['high_days'])
            limit_up_type.append(members['limit_up_type'])

            result.setdefault('name', members['name'])
            result.setdefault('high_days', members['high_days'])
            result.setdefault('reason_type', members['reason_type'])
            result.setdefault('limit_up_type', members['limit_up_type'])

        format_dic = {
            'name': name,
            'high_days': high_days,
            'reason_type': reason_type,
            'limit_up_type': limit_up_type
        }

        df = pd.DataFrame.from_dict(format_dic)
        print(df.to_markdown())

    else:
        print("Request failed with status code: {response.status_code}")


def blockTop():
    params = {
        'filter': 'HS,GEM2STAR',
        'order_field': '330324',
        'order_type': '0',
        '_': int(round(time.time() * 1000))
    }

    url = 'https://data.10jqka.com.cn/dataapi/limit_up/block_top'
    response = requests.get(
        url=url,
        params=params
    )

    # 检查请求是否成功
    if 200 == response.status_code:
        # 解析JSON响应
        data = response.json()
        for members in data['data']:
            name = []
            reason_info = []
            reason_type = []
            last_limit_up_time = []
            first_limit_up_time = []
            for stocks in members['stock_list']:
                name.append(stocks['name'])
                reason_type.append(stocks['reason_type'])
                reason_info.append(stocks['reason_info'])

                first_time = time.localtime(int(stocks['first_limit_up_time']))
                first_limit_up_time.append(time.strftime('%H:%M:%S', first_time))

                last_time = time.localtime(int(stocks['last_limit_up_time']))
                last_limit_up_time.append(time.strftime('%H:%M:%S', last_time))

            format_dic = {
                '名称': name,
                '原因类型': reason_type,
                '最终时间': last_limit_up_time,
                '触发时间': first_limit_up_time,
                '原因内容': reason_info,
            }

            df = pd.DataFrame.from_dict(format_dic)
            print(df.to_markdown())
            print("\n")
    else:
        print("Request failed with status code: {response.status_code}")
