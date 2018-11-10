
import pandas as pd
import numpy as np
from appsfly_spider.constants import spider_constants as sconstants
import json
import os.path as ospath


class ExportHelper:

    def __init__(self, save_path, file_name):
        self.export_dir = save_path
        self.file_name = file_name + '.xlsx'
        self.export_file = ospath.join(self.export_dir, self.file_name)

    def export_install_data(self, install_data):

        if not install_data:
            return

        excel_writer = pd.ExcelWriter(self.export_file)

        for retention in install_data:
            app_name = retention[sconstants.RETENTION_KEY_NAME]
            str_data = retention[sconstants.RETENTION_KEY_DATA]
            json_data = json.loads(str_data)
            if not len(json_data):
                continue
            df_retention_data = self._parse_install_data(json_data)

            df_retention_data.to_excel(excel_writer, sheet_name=app_name)

        excel_writer.save()

    def export_retention_data(self, retention_content, category_field=sconstants.PARSE_KEY_COUNTRY):

        if not retention_content:
            return

        excel_writer = pd.ExcelWriter(self.export_file)

        for retention in retention_content:
            app_name = retention[sconstants.RETENTION_KEY_NAME]
            str_data = retention[sconstants.RETENTION_KEY_DATA]
            json_data = json.loads(str_data)
            if not len(json_data):
                continue
            df_retention_data = self._parse_fields(json_data, category_field)

            df_retention_data.to_excel(excel_writer, sheet_name=app_name)

        excel_writer.save()

    def _parse_fields(self, json_data, category_field=sconstants.PARSE_KEY_COUNTRY):

        first_element = True
        all_data = []
        columns = []
        for json_element in json_data:
            dimension = json_element[sconstants.PARSE_KEY_DIMENSION]
            media_source = dimension[sconstants.PARSE_KEY_MEDIA_SOURCE]
            specified_field = dimension[category_field]
            date = dimension[sconstants.PARSE_KEY_INSTALL_PERIOD]
            install = json_element[sconstants.PARSE_KEY_INSTALL_PERIOD]
            retention_data = json_element[sconstants.PARSE_KEY_DATA]
            if first_element:
                columns = self._get_column_names(len(retention_data))
                first_element = False

            one_row_data = [media_source, specified_field, date, install]
            one_row_data.extend(retention_data)

            all_data.append(one_row_data)

        narray_data = np.array(all_data)
        return pd.DataFrame(narray_data, columns=columns)

    @staticmethod
    def _parse_install_data(json_data):
        first_element = True
        all_data = []
        columns = []
        for json_element in json_data:
            campaign = json_element[sconstants.PARSE_KEY_CAMPAIGN]
            install = json_element[sconstants.PARSE_KEY_INSTALL]
            session = json_element[sconstants.PARSE_KEY_SESSION]
            if sconstants.PARSE_KEY_LOYAL in json_element:
                loyal = json_element[sconstants.PARSE_KEY_LOYAL]
            else:
                loyal = 0

            if first_element:
                columns = ['campaign', 'install', 'session', 'loyal']
                first_element = False

            one_row_data = [campaign, install, session, loyal]
            all_data.append(one_row_data)

        narray_data = np.array(all_data)
        return pd.DataFrame(narray_data, columns=columns)

    @staticmethod
    def _get_column_names(day_num):
        columns = ['media_source', 'country', 'date', 'install_af']
        index_list = range(1, day_num+1, 1)
        for index in index_list:
            columns.append('day_' + str(index))

        return columns

