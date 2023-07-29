# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:27:17 2022

@author: James Sadighian
"""

from ScopeFoundry import BaseMicroscopeApp
from TimeTagger import (Scope, createTimeTagger, freeTimeTagger)

class CryoScope(BaseMicroscopeApp):

    # this is the name of the microscope that ScopeFoundry uses 
    # when storing data
    name = 'cryo_microscope'
    
    # You must define a setup function that adds all the 
    #capablities of the microscope and sets default settings
    def setup(self):
        #Add App wide settings

        #Add hardware components
        #Notice that ScopeFoundry Hardware components always have the suffix “HW”.
        #from ScopeFoundryHW.virtual_function_gen.vfunc_gen_hw import VirtualFunctionGenHW #tells python where to find the hardware component folder.file.py.class
        #self.add_hardware(VirtualFunctionGenHW(self)) #creates an instance of the hardware (an active copy in memory), and then adds it to your App
        from HW_Swabian.SwabianTT import TimeTaggerHW
        self.add_hardware(TimeTaggerHW(self, name='timetagger'))
        from HW_Attocube_ASC500.ASC500_HW import ASC500HW
        self.add_hardware(ASC500HW(self))
        #print("Adding Hardware Components")
        print("uWu daddy i finished adding the hardware components")
        
        
        #Add measurement components
        #Notice that ScopeFoundry Measurement class names always have the suffix “Measure”.
        from HW_Swabian.swabian_counthist_measure import SwabianHistogram
        self.add_measurement(SwabianHistogram(self))       
        from HW_Swabian.swabian_triple_measure import SwabianTriple
        self.add_measurement(SwabianTriple(self))
        from HW_Swabian.swabian_filewriter_measure import SwabianFilewriter
        self.add_measurement(SwabianFilewriter(self))
        # from HW_Swabian.swabian_cryoFLIM_measure import SwabianCryoFLIM
        # self.add_measurement(SwabianCryoFLIM(self))     

        # from HW_Attocube_ASC500.ASC500_Scan import ASC500_Scan
        # self.add_measurement(ASC500_Scan(self))
        from HW_Swabian.swabian_scan import Swabian_Scan
        self.add_measurement(Swabian_Scan(self))
        
        
        # print("Creating Measurement objects")
        print("uWu daddy i finished creating the measurement objects")
        # Connect to custom gui

        # load side panel UI

        # show ui
        self.ui.show()
        self.ui.activateWindow()


if __name__ == '__main__':
    import sys
    
    app = CryoScope(sys.argv)
    sys.exit(app.exec_())