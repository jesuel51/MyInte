#-*-Python-*-
# Created by xiangjian at 2015/05/03 15:06
#-*-Python-*-
# Created by xiangjian at 2015/05/03 15:06
##--------------------------
# What are the input files
##--------------------------
#inputs=[(root['INPUTS']['ProfileGenInput']['iterdb'],'iterdb'),
#ccw=root['SETTINGS']['PHYSICS']['ccw']
inputs=[(root['INPUTS']['ProfileGenInput']['statefile'],'statefile_2.000000E+06.nc'),
        (root['INPUTS']['ProfileGenInput']['gfile'],'g000000.00000'),
	]
##----------------------
### output
##----------------------
outputs=['input.profiles','input.profiles.geo']
executable =' pbsMonitor -exe profiles_gen -i statefile_2.000000E+06.nc -g g000000.00000'
#executable = executable+' -ipccw '+str(ccw[0])+' -btccw '+str(ccw[1])
##executable += " > OMFITlog.txt ; "
#-----------------------
# Execute Profile_gen
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable,clean='true')    
#-----------------------
# load the results
#-----------------------
root['OUTPUTS']['ProfileGenOutput']['input.profiles']=OMFITgaCode('input.profiles')
root['OUTPUTS']['ProfileGenOutput']['input.profiles.geo']=OMFITgaCode('input.profiles.geo')
# w0=root['INPUTS']['ProfileGenInput']['cerfile']['data']
# w0=map(list,zip(*w0));
# root['OUTPUTS']['ProfileGenOutput']['input.profiles']['omega0']=array(w0[-1])*1.e3
#if root['SETTINGS']['PHYSICS']['iabsq']==1:
#    root['OUTPUTS']['ProfileGenOutput']['input.profiles']['q']=abs(root['OUTPUTS']['ProfileGenOutput']['input.profiles']['q'])
