# python-pianywhere-serial-api
This is the python API for controlling features of the PiAnywhere mobile data board including power managment, sms messaging and calendar fucntions. [PiAnywhere Store](https://www.pianywhere.com)

# Basic Usage

The PiAnywhere API communications over the UART serial connection on the raspberry pi. When you create an instance of the PiAnywhere python API it will begin communications over the UART port. In order for this to work effectivly other devices cannot also use this serial line.

```python
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

```python
pianywhere = PiAnywhere("/dev/ttyS0")

pianywhere.send_command(command)

pianywhere.send_command_with_check(command, check)

pianywhere.add_sms_responder(number)

pianywhere.remove_sms_responder(number)

pianywhere.clear_sms_responders()

pianywhere.send_sms_message(number, message)

pianywhere.get_all_sms_messages()

pianywhere.get_unread_sms_messages()

pianywhere.get_sms_message(id)

pianywhere.set_wake_datetime(datetime)
```
