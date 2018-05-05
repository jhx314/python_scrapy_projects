import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('item.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
