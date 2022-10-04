from html_table_extractor.extractor import Extractor

with open(r'C:/Users/Rene/github/temp/Bibel/Textkritik/manus.html', 'r', encoding='utf-8') as html_file:
     html_doc = html_file.read()

# table_doc = """
# <table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>
# """
# extractor = Extractor(table_doc)
extractor = Extractor(html_doc)
extractor.parse()
print(extractor.return_list())

# from html_table_extractor.extractor import Extractor
# table_doc = """
# <table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>
# """
# extractor = Extractor(table_doc, transformer=int)
# extractor.parse()
# extractor.return_list()
