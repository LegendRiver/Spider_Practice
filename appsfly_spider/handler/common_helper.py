
import json
from datetime import datetime
from datetime import timedelta
import pytz


def read_json_file(file_path):
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        return json_data


def get_now_date(timezone_str='Asia/Shanghai'):
    tz = pytz.timezone(timezone_str)
    return datetime.now(tz).strftime('%Y-%m-%d')


def get_delta_date(days, timezone_str='Asia/Shanghai'):
    tz = pytz.timezone(timezone_str)
    date_time = datetime.now(tz) + timedelta(days=days)
    return date_time.strftime('%Y-%m-%d')
