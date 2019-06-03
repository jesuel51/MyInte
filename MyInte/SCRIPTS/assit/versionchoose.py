version=root['SETTINGS']['PHYSICS']['version']
if version==4:
    root['SETTINGS']['PHYSICS']['nj']=51
elif version==57:
    root['SETTINGS']['PHYSICS']['nj']=201
else:
    print('the 12 version is wrong ,please check!')

