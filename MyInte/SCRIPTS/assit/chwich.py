# as we know, the Te in the core region is not well calculated , so we main use the profile shape of ion channel to replace the electron channel .
nj=root['SETTINGS']['PHYSICS']['nj']
if root['SETTINGS']['PHYSICS']['chwich'][0]==1:
    pvt_i=root['SETTINGS']['PHYSICS']['chwich'][1]
#    num=int(pvt_i/0.02)+1
    num=int(pvt_i*(nj-1))+1
    diff_Tie=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['tiin'][num]-root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['tein'][num]
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['tein'][0:num]=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['tiin'][0:num]-diff_Tie
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['tein'][0:num]=root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['tiin'][0:num]-diff_Tie
