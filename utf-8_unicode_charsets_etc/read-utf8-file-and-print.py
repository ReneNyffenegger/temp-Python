#
#  In Windows, set code page to 65001 to run program:
#     chcp 65001
#
with open('text.utf8', encoding='utf-8') as txt:
     for line in txt:
         print(line, end='')
