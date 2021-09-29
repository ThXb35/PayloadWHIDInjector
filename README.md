# PayloadWHIDInjector

WHID Payloads for Linux, MacOS and Windows

# List of payloads

| OS      | Name                                     | Description                                                  |
| ------- | ---------------------------------------- | ------------------------------------------------------------ |
| WINDOWS | [DisableAV](Windows/WIN_DisableAV.txt)   | Disables the Windows AV without using command lines          |
| WINDOWS | [RevShell](Windows/WIN_RevShell.txt)     | Runs a reverse shell to a specified server                   |
| WINDOWS | [screenshot](Windows/WIN_screenshot.txt) | Screenshots the remote host and exfils the data to an external VPS |

# Deploy the payloads

The [deployPayloads.py](deployPayloads.py) will automatically deploy every payload from this repository to your wihd injector.

```bash
$ python3 deployPayloads.py
```

