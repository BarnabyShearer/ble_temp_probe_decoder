DEVICE_MAC=44:A6:E5:36:7C:65

run:
	gatttool -b ${DEVICE_MAC} --char-write-req --handle=0x0025 --value=0100 --listen | ./disp.py

reset:
	sudo hciconfig hci0 down
	sudo hciconfig hci0 up

scan:
	sudo hcitool lescan
