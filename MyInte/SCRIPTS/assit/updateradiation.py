# this script is used to updata radiation power according the ONETWO run with W included
# Due to ONETWO are limited to only 4 ion species at most, the input.profiles generated are based on the ONETWO run with DT, He and Ar, with W excluded.
# first we need to get the total radiation power
trpltout=root['OUTPUTS']['ONETWOOutput']['trpltout.nc']
prad=trpltout['prad']['data'][-1]
prad=prad/1.e6
tgyroinput=root['INPUTS']['TGYROInput']['input.profiles']
# get the total heating power
tgyroinput['pow_e']=tgyroinput['pow_e']-tgyroinput['pow_e_line']
tgyroinput['pow_e']=tgyroinput['pow_e']+prad
tgyroinput['pow_e_line']=prad
