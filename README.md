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

```
