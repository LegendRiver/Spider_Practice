import os.path as ospath
from basic import load_sys_path
from handler.dom_helper import AFPageHandler
from handler.request_helper import RequestAPIHandler
from handler.export_handler import ExportHelper
import handler.common_helper as comhelper

if __name__ == '__main__':
    current_path = ospath.dirname(ospath.realpath(__file__))
    conf_path = ospath.join(current_path, 'conf')
    page_info_file = ospath.join(conf_path, 'page_conf.json')
    api_info_file = ospath.join(conf_path, 'report_install_google_kwai.json')

    page_handler = AFPageHandler(page_info_file)
    cookies = page_handler.get_login_cookies()

    latest_date = comhelper.get_delta_date(-1)
    request_handler = RequestAPIHandler(api_info_file, cookies, latest_date)
    retention_data = request_handler.query_install_data()

    output_dir = ospath.join(current_path, 'output')
    file_name = 'install_data'
    export_helper = ExportHelper(output_dir, file_name)
    export_helper.export_install_data(retention_data)
