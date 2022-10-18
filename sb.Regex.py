import os
os.system('cls' if os.name == 'nt' else 'clear')
import re

import mrtxee


res = re.match(r'AV', 'AV Analytics Vidhya AV')
print( f'подстрока',res.group(),'найдена в символах',res.span() )
#подстрока AV найдена в символах (0, 2)

res = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print( f'подстрока',res.group(),'найдена в символах с #',res.start(),'по',res.end() )
#подстрока Analytics найдена в символах с # 3 по 12

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print( result )
#['AV', 'AV']

result = re.split(r'i', 'Analytics Vidhya')
print( result )
#['Analyt', 'cs V', 'dhya'] # все возможные участки.

result = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
print( result )
#'AV is largest Analytics community of the World'

pattern = re.compile('AV')
result = pattern.findall('AV Analytics Vidhya AV')
print( result )
result2 = pattern.findall('AV is largest analytics community of India')
print( result2 )
'''
['AV', 'AV']
['AV']
'''
