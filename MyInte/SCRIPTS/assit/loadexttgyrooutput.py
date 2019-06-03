outputs=['out.tgyro.alpha',
         'out.tgyro.flux_e','out.tgyro.flux_i','out.tgyro.flux_i2','out.tgyro.flux_i3','out.tgyro.flux_target',
         'out.tgyro.power_e','out.tgyro.power_i',
         'out.tgyro.profile','out.tgyro.profile2','out.tgyro.profile3',
         'out.tgyro.mflux_e','out.tgyro.mflux_i','out.tgyro.mflux_i2','out.tgyro.mflux_i3',
         'out.tgyro.gyrobohm','out.tgyro.gradient',
         'out.tgyro.geometry.1','out.tgyro.nu_rho',
         'out.tgyro.residual','out.tgyro.control',
         'out.tgyro.geometry.2','out.tgyro.run',
         'input.profiles.gen','input.tgyro.gen'
         ]
## load the result
dir_pre=root['SETTINGS']['extpath']['tgyro']
for item in outputs:
    root['OUTPUTS']['TGYROOutput'][item]=OMFITasciitable(dir_pre+'/'+item)
