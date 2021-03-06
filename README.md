[pianywhere_4g]: https://github.com/Altitude-Tech/python-pianywhere-serial-api/blob/master/pianywhere_4g.png "PiAnywhere 4G Board"

# PiAnywhere Serial API for Python
This is the python API for controlling features of the PiAnywhere mobile data board including power managment, sms messaging and calendar fucntions. Hardware found at the [PiAnywhere Store](https://www.pianywhere.com).

![alt text][pianywhere_4g]

# Basic Usage

The PiAnywhere API communications over the UART serial connection on the raspberry pi. When you create an instance of the PiAnywhere python API it will begin communications over the UART port. In order for this to work effectivly other devices cannot also use this serial line.

```python
from pianywhere import PiAnywhere

# Create serial connection to PiAnywhere
pianywhere = PiAnywhere("/dev/ttyS0")

# Send SMS message from the baord
pianywhere.send_sms_message("my_number", "Hello from your PiAnywhere")
```
# Error Handling

The PiAnywhere API will throw a number of exceptions depending on the conditions, catching these exceptions is critical to using the API.

```python
try:
    number = "phone number"
    pianywhere.add_sms_responder(number)
    pianywhere.send_sms_message(number, "You have been added to the pianywhere sms responder!")
    
except PIANYWHERE_ERROR_RESPONSE:
    # The modem could not process the command send
    pass
    
except PIANYWHERE_NO_CARRIER:
    # No carrier was detected, likely a problem with the SIM card
    pass
    
except PIANYWHERE_BAD_RESPONSE:
    # The UART response was incorrect, could not be processed
    pass
    
except PIANYWHERE_BUFFER_OVERFLOW:
    # Too much data requested, caused an internal buffer overflow
    pass
    
except PIANYWHERE_BAD_COMMAND:
    # Your command was not recognised as valid
    pass
```

## API Reference
Basic Setup:
```python
# If your are using the raspberry pi 1/2 or zero
rpi2 = "/dev/ttyAMA0"

# If you are using the raspberry pi 3
rpi3 = "/dev/ttyS0"

pianywhere = PiAnywhere(rpi3)
```
Sending raw commands directly to PiAnywhere and the modem:
```python
pianywhere.send_command(command)

pianywhere.send_command_with_check(command, check)
```
SMS functions:
```python
pianywhere.add_sms_responder(number)

pianywhere.remove_sms_responder(number)

pianywhere.clear_sms_responders()

pianywhere.send_sms_message(number, message)

pianywhere.get_all_sms_messages()

pianywhere.get_unread_sms_messages()

pianywhere.get_sms_message(id)
```
Wake and sleep mode commands:
```python
pianywhere.set_wake_datetime(datetime)

pianywhere.set_sleep_datetime(datetime)

pianywhere.get_pianywhere_date()
```
Modem control commands:
```python
pianywhere.powerkey_modem()

pianywhere.reset_modem()
```
