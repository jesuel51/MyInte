# this script is used to proceed the linear analysis and visulize the result
root['SCRIPTS']['assit']['linstudy.py'].run()
radius=root['SETTINGS']['TEMP']['radius']# all the r/a value correponding to the case
indexrho=root['SETTINGS']['PLOTS']['indexrho'] # the index of rho to be analysised
Gamma_max=linspace(0,0,len(indexrho))
k=root['SETTINGS']['PLOTS']['iview']
root['INPUTS']['GYROInput']['input.profiles']=root['INPUTSRec']['TGYRO'][k]['input.profiles']
root['INPUTS']['GYROInput']['input.profiles.geo']=root['INPUTSRec']['TGYRO'][k]['input.profiles.geo']
count=0
for item in indexrho:
    root['INPUTS']['GYROInput']['input.gyro']['RADIUS']=radius[int(item)]
    root['SCRIPTS']['GYRO']['baserungyro.py'].run()
    root['SCRIPTS']['GYRO']['omegaky.py'].run()
    root['OUTPUTSRec']['GYROOutput'][item]=OMFITtree()
    root['OUTPUTSRec']['GYROOutput'][item]['wr']=root['SETTINGS']['TEMP']['wr']
    root['OUTPUTSRec']['GYROOutput'][item]['wi']=root['SETTINGS']['TEMP']['wi']
    root['OUTPUTSRec']['GYROOutput'][item]['wr_err']=root['SETTINGS']['TEMP']['wr_err']
    root['OUTPUTSRec']['GYROOutput'][item]['wi_err']=root['SETTINGS']['TEMP']['wi_err']
    Gamma_max[count]=max(root['SETTINGS']['TEMP']['wi'])
    count=count+1
# find the maxmium growth rate and the corresponding rho
root['SETTINGS']['TEMP']['indexlin']=indexrho
root['SETTINGS']['TEMP']['Gamma_max']=Gamma_max
plt.close()
root['SCRIPTS']['assit']['linstudy.py'].run()
