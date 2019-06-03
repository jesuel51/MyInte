# this script is modified based on useiniT2.py
if root['SETTINGS']['PHYSICS']['useiniEr'][0]==1:
    pvt_i=root['SETTINGS']['PHYSICS']['useiniEr'][1]
    drho_tgyro=root['SETTINGS']['PHYSICS']['drho_tgyro']
    num=int(pvt_i/drho_tgyro)+1
    diff_Er=root['SETTINGS']['PHYSICS']['omega_sparse'][num]-root['SETTINGS']['PHYSICS']['Er_TGYRO'][num]
    root['SETTINGS']['PHYSICS']['Er_TGYRO'][0:num]=root['SETTINGS']['PHYSICS']['omega_sparse'][0:num]-diff_Er
