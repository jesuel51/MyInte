#-*-Python-*-
# Created by xiangjian at 2015/09/10 15:02

# What are the input files

inputs=[(root['INPUTS']['EFITInput']['rtest'],'rtest'),
        (root['INPUTS']['EFITInput']['g0file'],'g0file'),
        (root['INPUTS']['EFITInput']['exeEFIT.sh'],'exeEFIT.sh'),
	]
#if root['INPUTS']['EFITInput']['gfile'] is not None:
#    inputs.append(root['INPUTS']['EFITInput']['gfile'])
##----------------------
### output
##----------------------
#gfileinput=str(root['INPUTS']['EFITInput']['gfile'])[-8:]
#syscmd='cp'+ gfileinput+'g0file'
#root['INPUTS']['EFITInput']['rtest']['PROFILE_EXT']['GEQDSK_EXT']='FILES/'+gfileinput
root['INPUTS']['EFITInput']['rtest']['IN1']['ISHOT']=0
root['INPUTS']['EFITInput']['rtest']['IN1']['ITIME']=0
outputs=['g000000.00000','a000000.00000']
executable = 'chmod 777 exeEFIT.sh ; ./exeEFIT.sh'
#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable,clean='true')
#-----------------------
# load the results
#-----------------------
root['OUTPUTS']['EFITOutput']['gfile']=OMFITeqdsk('g000000.00000')
root['OUTPUTS']['EFITOutput']['afile']=OMFITeqdsk('a000000.00000')
