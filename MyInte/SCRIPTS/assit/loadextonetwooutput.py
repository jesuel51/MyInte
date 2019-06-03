outputs=['trpltout.nc','outone','dnubeam_nbi_fld_state.cdf','g0.99999','statefile_1.000000E+06.nc','toray_5.000000E+00_2_.nc','summary']
## load the result
dir_pre=root['SETTINGS']['extpath']['onetwo']
if dir_pre[-1]!='/':
    dir_pre=dir_pre+'/'
for item in outputs:
    if item.find('.nc')!=-1 or item.find('.cdf')!=-1:
        root['OUTPUTS']['ONETWOOutput'][item]=OMFITnc(dir_pre+item);
    elif item.find('g',0,1)!=-1:
        root['OUTPUTS']['ONETWOOutput'][item]=OMFITeqdsk(dir_pre+item);
    elif item=='outone':
        root['OUTPUTS']['ONETWOOutput'][item]=OMFIToutone(dir_pre+item);
    else:
        root['OUTPUTS']['ONETWOOutput'][item]=OMFITpath(dir_pre+item);
#root['OUTPUTS']['ONETWOOutput']['trpltout.nc']=OMFITnc(dir_pre+'trpltout.nc')
#root['OUTPUTS']['ONETWOOutput']['dnubeam_nbi_fld_state.cdf']=OMFITnc(dir_pre+'dnubeam_nbi_fld_state.cdf')
#root['OUTPUTS']['ONETWOOutput']['outone']=OMFIToutone(dir_pre+'outone')
