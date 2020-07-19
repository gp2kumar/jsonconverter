import json
from jsonConverter.htmltable import HtmlTable


class jsonConverter:
    def __init__(self, input_json: list):
        self.input_json = input_json

    def get_html_table(self, **kwargs) -> str:
        """
        converts given json a html code
        :return: str
        """
        kwargs.update({"json_data": self.input_json})
        return str(HtmlTable(**kwargs))

    @classmethod
    def from_string(cls, json_in_string):
        return cls(json.loads(json_in_string))

    @classmethod
    def from_file(cls, file_path: str):
        with open(file_path) as f:
            return cls(json.load(f))