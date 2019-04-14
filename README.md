# Chinesium BLE Dual Temperature probe decoder 'Turata'

I am sure the are multiple variations, but some playing with gatttool
should find the data.

My device seems to start notifying automatically but we have gatttool
ask for notifications on the only listed handle (0x0025) anyway. Then
pipe them into a python script to decode the responses.
