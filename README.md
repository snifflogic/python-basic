# python-basic (snifflogic_basic package)

Python SDK for communicating with the Sniff Controller Basic of Sniff Logic

# Usage

Install the module using `pip`

```bash
pip install git+https://github.com/snifflogic/python-basic
```

To run the example, run

```bash
python -m snifflogic_basic.example
```

To use in your own project,

```python
from snifflogic_basic import *
```

And then you can use `Basic` as shown in `example.py`

## Example script

The example is in `example.py`. It will connect to the given `portName` (default is `COM3`) and will show `numPoint` datapoints (default 1000).
![Alt text](image.png)

# Files

- `basic.py` - a class representing the Basic device.
- `example.py` - a script demonstrating how to use the Basic class. You can use from command line as follows:

# Packages

- [pyserial](https://pyserial.readthedocs.io/en/latest/) - for communicating with the Basic.

## Bugs

If you've encountered a bug, please [open an issue](https://github.com/snifflogic/python-basic/issues). Include details about your device, operating system and Python version. Don't forget to attach your code.

## Contribute

Have you implemented something useful that could benefit others? Don't hesitate to submit a pull request.
