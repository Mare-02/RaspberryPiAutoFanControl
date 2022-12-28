# RaspberryPiAutoFanControl
Python script for Raspberry Pi to automatically control a PWM Fan

1. Connect the Fans PWM cable to Pin 18

2. Open the terminal and type
```
sudo crontab -e
```

3. It will ask you what editor you want to use.
Just press 1 to use Nano

4. add this lime at the bottom ("<path>" is the path to the file):
```
@reboot python3 <path>/autoFanControl.py
```

5. DONE!
