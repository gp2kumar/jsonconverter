# jsonconverter
A one step stop for all Json conversions.

# Installation
<pre>
pip install jsonConverter
</pre>

# Usage

<pre>
from jsonConverter import jsonConverter
json_converter = jsonConverter(ANY_JSON)
</pre>

## Invoke jsonConverter from json file
<pre>
from jsonConverter import jsonConverter
json_converter = jsonConverter.from_file(json_path)
</pre>

## Invoke jsonConverter from json string
<pre>
from jsonConverter import jsonConverter
json_converter = jsonConverter.from_string(json_str)
</pre>

# Get htmltable from json
<pre>
from jsonConverter import jsonConverter
json_converter = jsonConverter(ANY_JSON)
json_converter.get_html_table()
</pre>

## How to change default attributes for html table
Below attributes are exposed. So, pass these parameters to get_html_table method. 

<pre>
table_border_color
header_cell_border_color
header_background_color
header_text_color
header_font_size
</pre>

### Example 1 : get html table with header background color as red
<pre>
from jsonConverter import jsonConverter
json_converter = jsonConverter(ANY_JSON)
json_converter.get_html_table(header_background_color = "#ff0000")
</pre>