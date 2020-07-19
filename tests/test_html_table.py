from unittest import TestCase
from jsonConverter import jsonConverter
from jsonConverter.errors import EmptyJson
from bs4 import BeautifulSoup
import os
import json


class TestHtmlTable(TestCase):

    def __init__(self, *args, **kwargs):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.test_data_dir = os.path.join(current_directory, "test_data")
        self.json = None
        super().__init__(*args, **kwargs)

    def test_html_table_json_1(self):
        json_path = os.path.join(self.test_data_dir, "json_1.json")
        converter = jsonConverter.from_file(json_path)
        html_table = converter.get_html_table()
        soup = BeautifulSoup(html_table)
        headers = [header.text for header in soup.find("table").findAll("th")]
        self.assertEqual(len(self._get_json(json_path)[0]), len(soup.find("table").find_all("tr")))
        self.assertListEqual(headers, [header for header in self._get_json(json_path)[0].keys()])

    def test_html_table_with_empty_json(self):
        json_path = os.path.join(self.test_data_dir, "json_2.json")
        self.assertRaises(EmptyJson, jsonConverter.from_file(json_path).get_html_table)

    def _get_json(self, file_path: str, reload: bool = False):
        if reload or not self.json:
            with open(file_path) as fp:
                self.json = json.load(fp)
                return self.json
        return self.json
