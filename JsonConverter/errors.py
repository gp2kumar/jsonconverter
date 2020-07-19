
class EmptyJson(Exception):
    def __init__(self):
        super().__init__("Can not make an empty HTML table")
