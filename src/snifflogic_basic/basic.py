import serial


class Basic:
    """Class representing the Sniff Controller Basic
    """

    def __init__(self,port: str) -> None:
        """Initialize the Basic at port `port`

        Args:
            port (str): The name of the port the Basic is connected at
            In Windows, will look like `COM4`
            In Mac, will look like `/dev/tty.usbserial-A6004byf`

        Raises:
            IOError: If could not connect to the Basic. Check that the port
            given is indeed the correct port and that the LED on the Basic is ON.
        """
        try:
            self.ser = serial.Serial(port)
        except:
            raise IOError("Could not connect to given port")

    def parse_data(self,raw_data:str):
        """Parse the given raw data string and return pressure in Pascal

        Args:
            raw_data (String): the raw data received from the basic via serial port

        Returns:
            double: the pressure value in Pascal
        """
        data = int(raw_data.split()[0])
        data = -data/1000
        return data

    def get_data(self) -> float:
        """Get single pressure value from the Sniff Controller Basic 

        Returns:
            float: pressure in Pascal
        """
        data = self.ser.readline()
        self.ser.reset_input_buffer()
        data = self.parse_data(data)
        return data
    
    def close(self):
        """close communication with the Basic
        """
        self.ser.close()
