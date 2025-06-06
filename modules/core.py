try:
    from modules.command_line.cli import CommandLine
    from modules.scanner.port_scanner import PortScanner

except ImportError as Ie:
    print(f"[ + ] Error: couldn't import {Ie}")

class PortScannerCore:
    def __init__(self):
        self.commandline = CommandLine()
    
    def main(self):
        arguments = self.commandline.get_arguments()
        print(arguments)
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

            results = portscanner.all_ports_scanner(domain = target_domain,is_banner_grabbing = is_banner_grabbing_enabled,ports = ports)
            
            if results:
                for result in results:
                    print(f" Result : {result}")
            else:
                print(f"[ + ] No Ports are open for target '{arguments.domain}'")

        else:
            print(f"[ ! ] Missing required arguments:\nUsage : portscanner --domain <domain> [options] \nUse --help for more helpfull information. \n")
            exit(1)