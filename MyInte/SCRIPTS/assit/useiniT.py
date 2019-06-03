# Since sometimes the temperature profile in the core region maybe quite peaked, which may result in high BS current in core region and thus bad confinement property.
# So here we need to re-deal with the temperature profile manually. there are 3 candicate:
#(1) flatcore.py: we just use a line of fixed slope to represent the Ti and Te near core; the resultant BS current profile may have some undesired peak and singular point which may result in instability;
#(2) chwich.py: here we use the temperature in the ion channel to represent the electron channel; Sometimes the ion channel will also have peak profile;
#(3) useiniT.py: here we use the initial temperature to represent the temperature profile;
nj=root['SETTINGS']['PHYSICS']['nj']
if root['SETTINGS']['PHYSICS']['useiniT'][0]==1:
    pvt_i=root['SETTINGS']['PHYSICS']['useiniT'][1]
    num=int(pvt_i*(nj-1))+1
    diff_Ti=root['SETTINGS']['PHYSICS']['TIIN'][num]-root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TIIN'][num]
    diff_Te=root['SETTINGS']['PHYSICS']['TEIN'][num]-root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TEIN'][num]
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TIIN'][0:num]=root['SETTINGS']['PHYSICS']['TIIN'][0:num]-diff_Ti
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TEIN'][0:num]=root['SETTINGS']['PHYSICS']['TEIN'][0:num]-diff_Te
