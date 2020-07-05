from jinja2 import Template


class HtmlTable:
    template = """
    <table style="border-left: #{{table_border_color}} 1px solid;border-right: #{{table_border_color}} 1px solid;border-bottom: #{{table_border_color}} 1px solid;border-collapse: collapse;">
        <tr style="border-top: #{{table_border_color}} 1px solid;height:35px">
        {% for header in headers[:-1] %}
            <th style="border-right: #{{header_cell_border_color}} 1px solid;padding-left:5px;padding-right:5px;text-align:center;background-color:#{{header_background_color}}; color:#{{header_text_color}}; font-size:{{header_font_size}}px;">{{header}}</th>
        {% endfor %}    
            <th style="padding-left:5px;padding-right:5px;text-align:center;background-color:#{{header_background_color}}; color:#{{header_text_color}}; font-size:{{header_font_size}}px;">{{headers[-1]}}</th>
        </tr>
        {% for row in data %}
        <tr style="border-top: #{{table_border_color}} 1px solid;height:35px">
            {% for key in headers %}
            <td style="border-right: #{{table_border_color}} 1px solid;padding-left:5px;padding-right:5px;text-align:center;">{{row.get(key) }}</td>
            {% endfor %}
        </tr>
        {% endfor %}        
    </table>
    """

    def __new__(cls, *args, **kwargs):
        if len(kwargs["json_data"]) == 0:
            raise Exception("Can not make an empty HTML table")
        return super(HtmlTable, cls).__new__(cls)

    def __init__(self,
                 json_data: list,
                 table_border_color: str = "E1EcF4",
                 header_cell_border_color: str = "ccc",
                 header_background_color: str = "E1EcF4",
                 header_text_color: str = "6A737C",
                 header_font_size: str = "13"
                 ):
        self.table_border_color = table_border_color
        self.header_cell_border_color = header_cell_border_color
        self.header_background_color = header_background_color
        self.header_text_color = header_text_color
        self.header_font_size = header_font_size
        self.data = json_data

    def __str__(self):
        return Template(self.template).render(table_border_color=self.table_border_color,
                                              header_cell_border_color=self.header_cell_border_color,
                                              header_background_color=self.header_background_color,
                                              header_text_color=self.header_text_color,
                                              header_font_size=self.header_font_size,
                                              headers=list(self.data[0].keys()),
                                              data =self.data)


# json_data = [{"test_1": "val_1", "test_2": "val_2", "test_3": "val_3",  "test_4": "val_8"},
#                      {"test_1": "val_4", "test_2": "val_5", "test_3": "val_6", "test_4": "val_7"}]
# print(HtmlTable(json_data=json_data))