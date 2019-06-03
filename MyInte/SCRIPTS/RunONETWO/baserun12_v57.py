#-*-Python-*-
# Created by xiangjian at 2015/9/10 15:02
# here, we will run ONETWO in conventional time-dependent evolution mode to get the beam-driven current and heating profile

# For the input files
inputs=[(root['INPUTS']['ONETWOInput']['inone'],'inone'),
        (root['INPUTS']['ONETWOInput']['gfile'],'gfile'),
        (root['INPUTS']['ONETWOInput']['auxiliary']['nubeam.dat'],'nubeam.dat'),
        (root['INPUTS']['ONETWOInput']['auxiliary']['gafit.in'],'gafit.in'),
        (root['INPUTS']['ONETWOInput']['auxiliary']['toray.in'],'toray.in'),
        (root['INPUTS']['ONETWOInput']['auxiliary']['genray.dat'],'genray.dat'),
#        (root['INPUTS']['ONETWOInput']['subjob']['job12.pbs'],'job12.pbs'),
        (root['INPUTS']['ONETWOInput']['subjob']['monitePBS12.sh'],'monitePBS12.sh')
	]
inputs.append(root['INPUTS']['ONETWOInput']['auxiliary']['genray_helicon.dat'])
root['INPUTS']['ONETWOInput']['auxiliary']['nubeam.dat']['nbdrive_naml']['NUBEAM_DT']=root['INPUTS']['ONETWOInput']['inone']['NAMELIS2']['nubeam_back_delt']
#if root['INPUTS']['ONETWOInput']['gfile'] is not None:
#    inputs.append(root['INPUTS']['ONETWOInput']['gfile'])
# correction for the bctime
#root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['bctime'][0]=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['time0']
##----------------------
### output
##----------------------
#igfile=root['SETTINGS']['PHYSICS']['igfile']
#outputs=['iterdb','trpltout.nc','nubeam_12_xplasma_state.cdf','nubeam_12_nubeam_state.cdf','nubeam_12_restart_profs.txt','outone']
outputs=['statefile_1.000000E+06.nc','trpltout.nc','outone','summary','dnubeam_nbi_fld_state.cdf',' toray_5.000000E+00_2_.nc']
#gfileflag=str(root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['timmax']);
#gfile='g0.0'+gfileflag[0]+gfileflag[2:5]+(5-len(gfileflag))*'0';
gfile='g0.99999'
outputs.append(gfile);
##import commands
##newgfile=commands.getoutput('')
##executable = str(root['SETTINGS']['SETUP']['executable'])
#executable = 'chmod 777 monitePBS12.sh ; ./monitePBS12.sh'
#executable = 'pbsMonitor -jq batch -jn 2 -cn 4 -exe onetwo_cfetr -np 8'
nodes=root['SETTINGS']['SETUP']['nodes']
ncore=root['SETTINGS']['SETUP']['ncore']
jobquene=root['SETTINGS']['SETUP']['jobquene']
#executable = 'pbsMonitor -jq '+jobquene+' -jn '+str(nodes)+' -cn '+str(ncore)+' -exe ONETWO_CFETR -np '+str(ncore*nodes)
executable = 'pbsMonitor -jq batch -jn 1 -cn 16 -exe ONETWO_CFETR -np 16'
##executable += " > OMFITlog.txt ; "
#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable,clean='True')
#-----------------------
# load the results
#-----------------------
#root['OUTPUTS']['ONETWOOutput']['iterdb']=OMFITascii('iterdb')
root['OUTPUTS']['ONETWOOutput']['statefile']=OMFITnc('statefile_1.000000E+06.nc')
root['OUTPUTS']['ONETWOOutput']['toray.nc']=OMFITnc('toray_5.000000E+00_2_.nc')
root['OUTPUTS']['ONETWOOutput']['trpltout.nc']=OMFITnc('trpltout.nc')
root['OUTPUTS']['ONETWOOutput']['dnubeam_nbi_fld_state.cdf']=OMFITnc('dnubeam_nbi_fld_state.cdf')
#root['OUTPUTS']['ONETWOOutput']['toray.nc']=OMFITnc('toray.nc')
#root['OUTPUTS']['ONETWOOutput']['nubeam_12_xplasma_state.cdf']=OMFITnc('nubeam_12_xplasma_state.cdf')
#root['OUTPUTS']['ONETWOOutput']['nubeam_12_nubeam_state.cdf']=OMFITnc('nubeam_12_nubeam_state.cdf')
#root['OUTPUTS']['ONETWOOutput']['nubeam_12_restart_profs.txt']=OMFITpath('nubeam_12_restart_profs.txt')
#root['OUTPUTS']['ONETWOOutput']['v12_4.log']=OMFITpath('v12_4.log')
root['OUTPUTS']['ONETWOOutput']['gfile']=OMFITeqdsk(gfile)
root['OUTPUTS']['ONETWOOutput']['outone']=OMFIToutone('outone')
root['OUTPUTS']['ONETWOOutput']['summary']=OMFIToutone('summary')
