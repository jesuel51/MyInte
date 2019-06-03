# this scripts is used to deploy the 
import os
iview=root['SETTINGS']['PLOTS']['iview']
basedir=root['SETTINGS']['SETUP']['deployDir']
cmd='mkdir '+basedir
os.system(cmd)
itdir=basedir+'/'+str(iview)
cmd='mkdir '+itdir
os.system(cmd)
# deploy all the outputs
os.system(cmd+'/12')
root['OUTPUTSRec']['ONETWOOutput'][iview].deploy(basedir+'/'+str(iview)+'/12')
os.system(cmd+'/efit')
root['OUTPUTSRec']['EFITOutput']['Out'][iview].deploy(basedir+'/'+str(iview)+'/efit')
os.system(cmd+'/PG')
root['OUTPUTSRec']['ProfileGenOutput'][iview].deploy(basedir+'/'+str(iview)+'/PG')
os.system(cmd+'/TGYRO')
root['OUTPUTSRec']['TGYROOutput'][iview].deploy(basedir+'/'+str(iview)+'/TGYRO')
