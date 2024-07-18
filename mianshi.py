import re
from datetime import datetime


def reg_search(text, regex_list):
        # 定义正则表达式
    patterns = {
        '标的证券': re.compile(r'股票代码：(\S+)'),
        '换股期限': re.compile(r'换股期限：.*?(\d{4} 年 \d{1,2} 月 \d{1,2} 日)至(\d{4} 年 \d{1,2} 月 \d{1,2} 日)')
    }

    result_dict = {}

    for key in regex_list[0]:
        if key in patterns:
            match = patterns[key].search(text)
            if match:
                if key == '标的证券':
                    result_dict[key] = match.group(1)
                elif key == '换股期限':
                    start_date_str, end_date_str = match.groups()
                    start_date = datetime.strptime(start_date_str, '%Y 年 %m 月 %d 日').strftime('%Y-%m-%d')
                    end_date = datetime.strptime(end_date_str, '%Y 年 %m 月 %d 日').strftime('%Y-%m-%d')
                    result_dict[key] = [start_date, end_date]

    if result_dict:
        return [result_dict]
    else:
        return []
