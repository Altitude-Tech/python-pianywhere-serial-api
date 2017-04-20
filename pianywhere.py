from serial import Serial
import time
from pianywhere_exception import *

class PiAnywhere():

    MAX_UART_BUFFER = 128

    def __init__(self):
        self.uart = Serial("/dev/ttyS0")
        self.uart.baudrate = 9600
        self.uart.timeout = 1

    def __exit__(self):
        self.uart.close()

    def send_command(self, command):
        self.uart.write(command)
        response = self.uart.read(MAX_UART_BUFFER)
        return response

    def send_command_with_check(self, command, check):
        if not(command.startswith( ("AT+", "PI+"))):
            raise PIANYWHERE_BAD_COMMAND()

        self.uart.write(command.append("/r/n"))
        response = self.uart.read(self.MAX_UART_BUFFER);

        if(check in response):
            return true
        elif("ERROR" in response):
            raise PIANYWHERE_ERROR_RESPONSE()
        elif("NO CARRIER" in response):
            raise PIANYWHERE_NO_CARRIER()
        elif("BUFFER OVERFLOW" in response):
            raise PIANYWHERE_BUFFER_OVERFLOW()
        else:
            raise PIANYWHERE_BAD_RESPONSE()

    def add_sms_responder(self,number):
        return self.send_command_with_check("PI+SETRESPONDER=%s" % number, "OK")

    def remove_sms_responder(self, number):
        return self.send_command_with_check("PI+UNSETRESPONDER=%s" % number, "OK")

    def clear_sms_responders(self):
        return self.send_command_with_check("PI+CLEARRESPONDERS", "OK")

    def send_sms_message(self, number, message):
        self.send_command_with_check("AT+", "OK")

    def get_all_sms_messages(self):
        self.send_command_with_check("AT+", "OK")

    def get_unread_sms_messages(self):
        self.send_command_with_check("AT+", "OK")

    def get_sms_message(self, id):
        self.send_command_with_check("AT+", "OK")

    def set_wake_datetime(self, datetime):
	self.send_command_with_check("PI+WAKEON=%s" % datetime, "OK")

    def set_sleep_datetime(self, datetime):
        self.send_command_with_check("PI+SLEEPON=%s" % datetime, "OK")

    def get_pianywhere_date(self):
        datetime = send_command_with_check("PI+DATETIME", "OK")
	return time.strptime(datetime, '%b %d %Y %I:%M%p')

    def powerkey_modem(self):
        self.send_command_with_check("AT+", "OK")

    def reset_modem(self):
        self.send_command_with_check("AT+", "OK")
