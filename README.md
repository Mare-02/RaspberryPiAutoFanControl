# RaspberryPiAutoFanControl
Python script for Raspberry Pi to automatically control a PWM Fan

```
sudo crontab -e
```

It will ask you what editor you want to use.
Just press 1 to use Nano

add this lime at the bottom ("path" is the path of the file):
```
@reboot python3 path/autoFanControl.py
```

DONE!
