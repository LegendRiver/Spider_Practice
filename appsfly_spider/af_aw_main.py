import os.path as ospath
from basic import load_sys_path
from handler.dom_helper import AFPageHandler
from handler.request_helper import RequestAPIHandler
from handler.export_handler import ExportHelper
import handler.common_helper as comhelper
from appsfly_spider.constants import spider_constants as sconstants

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        days = -2
    else:
        days = sys.argv[1]

    current_path = ospath.dirname(ospath.realpath(__file__))
    conf_path = ospath.join(current_path, 'conf')
    page_info_file = ospath.join(conf_path, 'page_conf.json')
    api_info_file = ospath.join(conf_path, 'aw_conf.json')

    page_handler = AFPageHandler(page_info_file)
    phantomjs_path = '/home/ubuntu/anaconda2/envs/eli_analysis/bin/phantomjs'
    cookies = page_handler.get_login_cookies(phantomjs_path)

    latest_date = comhelper.get_delta_date(-2)
    start_date = comhelper.get_delta_date(-9)
    request_handler = RequestAPIHandler(api_info_file, cookies, latest_date, start_date)
    retention_data = request_handler.query_retention_data()

    # output_dir = ospath.join(current_path, 'output')
    today = comhelper.get_now_date()
    output_dir = ospath.join("/var/www/html/eli/server/awConversion", today)
    file_name = 'retention_data'
    export_helper = ExportHelper(output_dir, file_name)
    export_helper.export_retention_data(retention_data, sconstants.PARSE_KEY_CAMPAIGN)


