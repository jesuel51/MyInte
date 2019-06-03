#-*-Python-*-
# this script is used to calcualte the Er profiles according to the input.profiles
##--------------------------
# What are the input files
##--------------------------
#inputs=[(root['INPUTS']['ProfileGenInput']['iterdb'],'iterdb'),
inputs=[(root['INPUTS']['ProfileGenInput']['input.profiles'],'input.profiles'),
        (root['INPUTS']['ProfileGenInput']['cerfile'],'cerfile')]
##----------------------
### output
##----------------------
outputs=['vgen/input.profiles','vgen/input.profiles.geo']
executable ='pbsMonitor -cn 24 -exe profiles_gen -vgen -i input.profiles -cer cerfile -er 2 -vel 2 -in DC -ix 2 -n 24'
##executable += " > OMFITlog.txt ; "
#-----------------------
# Execute Profile_gen
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable,clean='true')    
#-----------------------
# load the results
#-----------------------
root['OUTPUTS']['ProfileGenOutput']['input.profiles']=OMFITgaCode('vgen/input.profiles')
