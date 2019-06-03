#-*-Python-*-
# Created by xiangjian at 2015/05/21 20:41
# this file is used to copy the content of one file to another
# and here we use it to initialize the input for 12
for item in root['INPUTS']['ONETWOInput']['inone']['namelis1'].keys():
    root['INPUTS']['ONETWOInput']['inone']['namelis1'][item]=\
    root['INPUTS']['IniInput']['inone']['namelis1'][item]

for item in root['INPUTS']['ONETWOInput']['inone']['namelis2'].keys():
    root['INPUTS']['ONETWOInput']['inone']['namelis2'][item]=\
    root['INPUTS']['IniInput']['inone']['namelis2'][item]

for item in root['INPUTS']['ONETWOInput']['inone']['namelis3'].keys():
    root['INPUTS']['ONETWOInput']['inone']['namelis3'][item]=\
    root['INPUTS']['IniInput']['inone']['namelis3'][item]

for item in root['INPUTS']['ONETWOInput']['gfile'].keys():
    root['INPUTS']['ONETWOInput']['gfile'][item]=\
    root['INPUTS']['IniInput']['gfile'][item]
