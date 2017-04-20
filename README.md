# python-pianywhere-serial-api
This is the python API for controlling features of the PiAnywhere mobile data board including power managment, sms messaging and calendar fucntions.

## Basic Usage

```python
pianywhere = PiAnywhere()
pianywhere.send_sms_message("my_number", "Hello from your PiAnywhere")
```
