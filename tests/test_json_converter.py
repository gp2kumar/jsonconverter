from unittest import TestCase
from jsonConverter import jsonConverter
from bs4 import BeautifulSoup
import json
import os


class TestJsonConverter(TestCase):

    def __init__(self, *args, **kwargs):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.test_data_dir = os.path.join(current_directory, "test_data")
        self.json = None
        super().__init__(*args, **kwargs)

    def test_jsonConverter(self):
        json_converter = jsonConverter(self._get_json(os.path.join(self.test_data_dir, "json_1.json")))
        print(type(json_converter))
        self.assertTrue(isinstance(json_converter, jsonConverter))

    def test_get_html_table(self):
        json_path = os.path.join(self.test_data_dir, "json_1.json")
        json_converter = jsonConverter.from_file(json_path)
        html_data = json_converter.get_html_table(header_font_size=12)
        soup = BeautifulSoup(html_data)
        style_tag = soup.find("table").find("th")['style']
        self.assertIn("font-size:12px;", style_tag)

    def test_jsonConverter_from_file(self):
        json_path = os.path.join(self.test_data_dir, "json_1.json")
        json_converter = jsonConverter.from_file(json_path)
        self.assertListEqual(json_converter.input_json, self._get_json(json_path))

    def test_jsonConverter_from_string(self):
        json_path = os.path.join(self.test_data_dir, "json_1.json")
        with open(json_path) as fp:
            json_converter = jsonConverter.from_string(fp.read())
            self.assertListEqual(json_converter.input_json, self._get_json(json_path))

    def _get_json(self, file_path: str, reload: bool = False):
        if reload or not self.json:
            with open(file_path) as fp:
                self.json = json.load(fp)
                return self.json
        return self.json