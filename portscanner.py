try:
    from modules.command_line.cli import CommandLine
    from modules.core import PortScannerCore

except ImportError as Ie:
    print(f"[ + ] Error: couldn't import {Ie}")

class PortScannerHandler:
    def __init__(self):
        self.commandline = CommandLine()
        self.core = PortScannerCore()

    def start(self):
        banner = self.commandline.get_banner()
        print(banner)

        self.core.main()

if __name__ == "__main__":
    scanner = PortScannerHandler()
    scanner.start()
