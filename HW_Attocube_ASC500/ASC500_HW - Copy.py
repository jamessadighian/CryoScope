# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:49:03 2022

@author: James Sadighian
"""
import sys
import os
from ScopeFoundry import HardwareComponent
import time

try:
    asc500path=r"C:\Users\James Sadighian\Desktop\ASC500_Python_Control-master"
    sys.path.insert(0, asc500path)
    from lib import ASC500
except Exception as err:
    print('Could not load modules needed for AttoCube ASC500: {}'.format(err))

class ASC500HW(HardwareComponent):
    
    name = 'asc500'

    def setup(self):

        
        self.name = 'ASC500'
        self.asc500=0

        
        # Define your hardware settings here.
        # These settings will be displayed in the GUI and auto-saved with data files
        self.settings.New('x_range', dtype=float, unit='um')
        self.settings.New('y_range', dtype=float, unit='um')
        self.settings.New('Columns', dtype=float, vmin=1, vmax=500)
        self.settings.New('Lines', dtype=float, vmin=1, vmax=500)
        self.settings.New('pixel_size', dtype=float, unit='um')
        self.settings.New('sampTime', dtype=float, unit='s')

        
        
        
    def connect(self):
        binPath = asc500path+os.sep+"Installer\ASC500CL-V2.7.13" +os.sep
        dllPath = asc500path+os.sep+"64bit_lib\ASC500CL-LIB-WIN64-V2.7.13\daisybase\lib" +os.sep
        
        self.asc500 = ASC500(binPath, dllPath)
        self.asc500.base.startServer()
        time.sleep(3)
        
        self.settings.x_range.connect_to_hardware(
            read_func=self.getXRange,
            # write_func=self.setXRang
            )
        
        self.settings.y_range.connect_to_hardware(
            read_func=self.getYRange,
            # write_func=self.setYRange
            )
        
        self.settings.Columns.connect_to_hardware(
            read_func=self.asc500.scanner.getNumberOfColumns,
            write_func=self.asc500.scanner.setNumberOfColumns
            )
        
        self.settings.Lines.connect_to_hardware(
            read_func=self.asc500.scanner.getNumberOfLines,
            write_func=self.asc500.scanner.setNumberOfLines
            )
        
        self.settings.pixel_size.connect_to_hardware(
            read_func=self.asc500.scanner.getPixelSize,
            write_func=self.asc500.scanner.setPixelSize
            )
        
        self.settings.sampTime.connect_to_hardware(
            read_func=self.asc500.scanner.getSamplingTime,
            write_func=self.asc500.scanner.setSamplingTime
            )
        
        self.asc500.scanner.setXEqualY(1)
        # LQ = self.settings.as_dict()
        
        # #Connect settings to hardware:
        # LQ['Columns'].hardware_read_func = self.asc500.scanner.getNumberOfColumns()      
        # LQ['Lines'].hardware_read_func = self.asc500.scanner.getNumberOfLines()
        # LQ['pixel_size'].hardware_read_func = self.asc500.scanner.getPixelSize()
        # LQ['sampTime'].hardware_read_func = self.asc500.scanner.getSamplingTime()
        
        # LQ['Columns'].hardware_set_func = self.setcolumns
        # self.asc500.scanner.setNumberOfColumns()   
        # LQ['Lines'].hardware_set_func = self.asc500.scanner.setNumberOfLines()
        # LQ['pixel_size'].hardware_set_func = self.asc500.scanner.setPixelSize()
        # LQ['sampTime'].hardware_set_func = self.asc500.scanner.setSamplingTime()
        
        #Take an initial sample of the data.
        self.read_from_hardware()
        
        
    def disconnect(self):
        #Disconnect the device and remove connections from settings
        print('abc')
        self.settings.disconnect_all_from_hardware()    #james can you find this in the scopefoundry code...is this necessary????
        if hasattr(self, 'ASC500'):
            print('def')
            #disconnect hardware
            #clean up hardware object
            self.asc500.base.stopServer()
            del self.asc500
            self.asc500 = None
    
    def getXRange(self):
        return self.settings['pixel_size']*self.settings['Columns']
        
        
    def getYRange(self):
        return self.settings['pixel_size']*self.settings['Lines']
    # def setXRange:
    #     self.settings
    # def setYRange:
        


