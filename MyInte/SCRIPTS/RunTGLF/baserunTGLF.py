##===================================
### input
##==================================
inputs=[(root['INPUTS']['TGLFInput']['input.tglf'],'input.tglf'),
        (root['INPUTS']['TGLFInput']['jobtglf.pbs'],'jobtglf.pbs'),
        (root['INPUTS']['TGLFInput']['monitePBStglf.sh'],'monitePBStglf.sh')
	]
##----------------------
### output
##----------------------
outputs=['out.tglf.run']
if root['SETTINGS']['SETUP']['tglf_flag']=='nonlin':
    root['INPUTS']['TGLFInput']['input.tglf']['USE_TRANSPORT_MODEL']=True
    outputs.append('out.tglf.flux_spectrum')
    outputs.append('out.tglf.gbflux')
else:
    root['INPUTS']['TGLFInput']['input.tglf']['USE_TRANSPORT_MODEL']=False
#executable ='chmod 777 monitePBStglf.sh ; ./monitePBStglf.sh'
#executable ='pbsMonitor -jq batch -cn 1 -exe tglf -e . -n 1'
#executable ='pbsMonitor -jq parallel11 -cn 4 -jn 2 -exe tglf -e . -n 4'
executable ='pbsMonitor  -exe tglf -e . -n 1'
ret_code=OMFITx.executable(root,inputs=inputs, outputs=outputs, executable=executable)
#-----------------------
# load the results
#-----------------------
root['OUTPUTS']['TGLFOutput']=OMFITtree()
for item in outputs:
    root['OUTPUTS']['TGLFOutput'][item]=OMFITasciitable(item)
