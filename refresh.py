import os
import datetime

# ファイル名を変更する
os.rename('input.md', 'input_' + datetime.datetime.now().strftime('%Y%m%d%H%M') + '.md')

with open('input.md', 'w') as f:
     f.write('私 > ')