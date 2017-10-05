#!/usr/bin/python
# coding: UTF-8

import sys # コマンドライン引数
import re  # 正規表現による探索

ld = open('./data_raw/'+sys.argv[1]+'.txt', 'r')
lines = ld.readlines()
ld.close()

f = open('./data_extracted/extracted_'+sys.argv[1]+'.txt', 'w')
for line in lines:
    match = re.search(r'([a-z]+)\s+([0-9]+)\.([0-9]+)\s+([0-9]+)\s+(?P<value>[0-9]+)', line)
    if match:
        # print 'matched:'+ match.group('value')
        f.write(match.group('value')+'\n') # 引数の文字列をファイルに書き込む
f.close()
