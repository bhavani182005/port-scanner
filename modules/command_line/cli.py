try:
    import argparse

except ImportError as Ie:
    print(f"[ + ] couldn't import {Ie}")

class CommandLine:
    def get_banner(self):
        banner = """
                             ____            _     ____                                  
                            |  _ \\ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
                            | |_) / _ \\| '__| __| \\___ \\ / __/ _` | '_ \\| '_ \\ / _ \\ '__|
                            |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
                            |_|   \\___/|_|   \\__| |____/ \\___\\__,_|_| |_|_| |_|\\___|_|  

                                                                                        v1.0.0 

                                        Author : Bhavani E  |  GitHub : @bhavani182005
                                        ``````                 ```````
                                            This is a tool to scan open ports 
                """
        return banner

    def get_help_menu(self):
        help_menu = """
            [Description]: This is a simple port scanner which can be used to identify the open ports developed by Bhavani E.
                        Usage : portscanner.py -d domain/ip  -p [ range (ex: 1-1000) ] [ options ]   
                
                        [Options]
                            -d , --domain                        : Domain/ip to scan [ Mandatory ]
                            -p , --ports (80,443,8080,8088)      : Only specified port(s) to scan. If no ports specified all ports will scanned.
                            -p-                                  : To scan all the ports
                            -b , --banner-grabbing               : Enable banner grabbing
                            -v , --verbose                       : To enable verbose mode.
                            -t , --threads                       : Threads (default : 40)
                            -h , --help                          : help


    """
        return help_menu
    
    def get_arguments(self):
        argument_parser=argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False)
        try:
            argument_parser.add_argument("-d","--domain")
            argument_parser.add_argument("-p","--ports",nargs='+')
            argument_parser.add_argument("-t","--threads",type=int)
            argument_parser.add_argument("-b","--banner-grabbing",action="store_true")
            argument_parser.add_argument("-v","--verbose",action="store_true")
            argument_parser.add_argument("-h","--help",action="store_true")

            arguments = argument_parser.parse_args()

            return arguments
        
        except argparse.ArgumentError:
            print(f"[ ! ] Value needed for the argument Please use -h to get more information.")
            exit()
            
        except argparse.ArgumentTypeError:
            print(f"\n [ ! ] Please use -h to get more information.")
            exit()
        
        except Exception as e:
            print(f"\n [ ! ] Unexpected Argument Error:{e}")
            exit()