try:
    from time import perf_counter
    from modules.command_line.cli import CommandLine
    from modules.scanner.port_scanner import PortScanner

except ImportError as Ie:
    print(f"[ + ] Error: couldn't import {Ie}")

class PortScannerCore:
    def __init__(self):
        self.commandline = CommandLine()
    
    def main(self):
        ports = None
        arguments = self.commandline.get_arguments()
        if arguments.help:
            print(self.commandline.get_help_menu())
            exit()
        
        if arguments.verbose:
            print("[ + ] Verbose mode is activated")

        if arguments.banner_grabbing and arguments.verbose:
            print("[ + ] Banner grabbing is enabled")

        if arguments.domain:
            portscanner = PortScanner(arguments=arguments)

            target_domain = arguments.domain
            is_banner_grabbing_enabled = arguments.banner_grabbing
            
            if arguments.ports:
                ports = arguments.ports

            if arguments.verbose:
                print("[ + ] port scanning started ")

            scan_start_time = perf_counter()
            results = portscanner.all_ports_scanner(domain = target_domain,is_banner_grabbing = is_banner_grabbing_enabled,ports = ports)
            scan_end_time = perf_counter()

            print(f"\n[ + ] Scan Completed in {scan_end_time-scan_start_time} sec \n")

            if arguments.banner_grabbing:
                print("Port              Status              Banner\n")
            else:
                print("Port              Status")
            if results:
                for result in results:
                    if isinstance(result,tuple):
                        port , banner = result
                    else:
                        port = result
                        banner = None

                    if arguments.banner_grabbing:
                        print(f"{str(port).ljust(5)}          -   Open   -          ", end="")
                    else:
                        print(f"{str(port).ljust(5)}      -       Open")

                    if arguments.banner_grabbing:
                        if isinstance(banner, dict):
                            status = banner.get("Status") or banner.get("Status-Line") or next(iter(banner.values()))
                            print(status.strip())
                            for key, value in banner.items():
                                if key not in ['Status', 'Status-Line']:
                                    print(f"{' '*37}{key}: {value.strip()}")

                        elif isinstance(banner, str):
                            print(banner.strip())

                        else:
                            print("No banner")     

            else:
                print(f"[ + ] No Ports are open for target '{arguments.domain}'")

        else:
            print(f"[ ! ] Missing required arguments:\nUsage : portscanner --domain <domain> [options] \nUse --help for more helpfull information. \n")
            exit(1)

def main():
    Commandline = CommandLine()
    print(Commandline.get_banner())
    portscanner = PortScannerCore()
    portscanner.main()