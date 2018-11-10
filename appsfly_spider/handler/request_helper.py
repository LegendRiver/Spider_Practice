
from appsfly_spider.handler import common_helper as fhelper
from appsfly_spider.constants import spider_constants as sconstants
import requests
import requests.cookies
from urlparse import urljoin
import json


class RequestAPIHandler:

    def __init__(self, config_file, driver_cookies, default_date='', default_start_date=''):
        api_info = fhelper.read_json_file(config_file)
        if 'af_retention_conf' in api_info:
            self._app_config_list = api_info['af_retention_conf']
        elif 'af_install_conf' in api_info:
            self._app_config_list = api_info['af_install_conf']

        self._cookies = self._reconstruct_cookies(driver_cookies)
        self._default_date = default_date
        self._default_start_date = default_start_date
        if not self._default_date:
            self._default_date = fhelper.get_delta_date(-2)

    def query_install_data(self):
        install_data = []

        try:
            for config_item in self._app_config_list:
                data_info = {}
                app_id = config_item['af_app_id']
                app_name = config_item['app_name']
                request_url = urljoin(sconstants.AF_QUERY_INSTALL_URL, app_id)
                request_param = self._build_install_payload(app_id, config_item)
                header = {'content-type': 'application/json'}
                response = requests.post(request_url, data=json.dumps(request_param), cookies=self._cookies,
                                         headers=header)

                data_info[sconstants.RETENTION_KEY_ID] = app_id
                data_info[sconstants.RETENTION_KEY_NAME] = app_name
                data_info[sconstants.RETENTION_KEY_DATA] = response.text

                install_data.append(data_info)

            return install_data

        except Exception:
            print 'request exception'

    def query_retention_data(self):
        retention_data = []

        try:
            for config_item in self._app_config_list:
                data_info = {}
                app_id = config_item['af_app_id']
                app_name = config_item['app_name']
                request_url = urljoin(sconstants.AF_QUERY_RETENTION_URL, app_id)
                request_param = self._build_query_payload(config_item)
                header = {'content-type': 'application/json'}
                response = requests.post(request_url, data=json.dumps(request_param), cookies=self._cookies,
                                         headers=header)

                data_info[sconstants.RETENTION_KEY_ID] = app_id
                data_info[sconstants.RETENTION_KEY_NAME] = app_name
                data_info[sconstants.RETENTION_KEY_DATA] = response.text

                retention_data.append(data_info)

            return retention_data

        except Exception:
            print 'request exception'

    def _build_query_payload(self, config_info):
        start_date = config_info['start_date']
        end_date = config_info['end_date']
        if not start_date or not end_date:
            start_date = self._default_date
            end_date = self._default_date
            if self._default_start_date:
                start_date = self._default_start_date

        groups = config_info['groups']
        filters = config_info['filters']
        granularity = config_info['granularity']
        min_install = config_info['min_install']

        query_info = {sconstants.AF_QUERY_PARAM_START_TIME: start_date, sconstants.AF_QUERY_PARAM_END_TIME: end_date,
                      sconstants.AF_QUERY_PARAM_GROUP: groups, sconstants.AF_QUERY_PARAM_FILTER: filters,
                      sconstants.AF_QUERY_PARAM_GRANULARITY: granularity,
                      sconstants.AF_QUERY_PARAM_MIN_INSTALL: min_install}
        query_payload = {sconstants.AF_QUERY_PARAM_QUERY: query_info}
        return query_payload

    def _build_install_payload(self, app_id, config_info):
        start_date = config_info['start_date']
        end_date = config_info['end_date']
        if not start_date or not end_date:
            start_date = self._default_date
            end_date = self._default_date
            if self._default_start_date:
                start_date = self._default_start_date

        groups = config_info['groups']
        filters = config_info['filters']
        topics = config_info['topics']

        query_info = {sconstants.AF_QUERY_PARAM_APP_ID: app_id, sconstants.AF_QUERY_PARAM_START_DATE: start_date,
                      sconstants.AF_QUERY_PARAM_END_DATE: end_date, sconstants.AF_QUERY_PARAM_GROUP: groups,
                      sconstants.AF_QUERY_PARAM_FILTER: filters, sconstants.AF_QUERY_PARAM_TOPIC: topics,
                      sconstants.AF_QUERY_PARAM_LIMIT: 2000
                      }
        query_payload = {sconstants.AF_QUERY_PARAM_QUERY: query_info}
        return query_payload

    @staticmethod
    def _reconstruct_cookies(cookie_list):
        cookie_jar = requests.cookies.RequestsCookieJar()
        for cookie in cookie_list:
            if sconstants.COOKIE_KEY_HTTP_ONLY in cookie:
                cookie.pop(sconstants.COOKIE_KEY_HTTP_ONLY)
            if sconstants.COOKIE_KEY_HTTP_EXPIRY in cookie:
                cookie[sconstants.COOKIE_KEY_HTTP_EXPIRES] = cookie[sconstants.COOKIE_KEY_HTTP_EXPIRY]
                cookie.pop(sconstants.COOKIE_KEY_HTTP_EXPIRY)
            else:
                cookie[sconstants.COOKIE_KEY_HTTP_EXPIRES] = None

            cookie_jar.set(**cookie)

        return cookie_jar
