# This script that advertises a bluetooth low energer beacon for 15 seconds
#import class library time
import time

from bluetooth.ble import BeaconService  #Import a 3rd party control module

#Create an instance of the object from the 3rd party class
#Create variable for BeaconService function
service = BeaconService()


service.start_advertising("11111111-2222-3333-4444-555555555555",1,1,1,200)
#event to start advertising service 
#bluetooth UUID 
#different parameters for which you accept the UUID
time.sleep(15)
#event stop time after 15 seconds

service.stop_advertising()
#event to stop advertising for service 
print("Done.")
#print displays the string Done