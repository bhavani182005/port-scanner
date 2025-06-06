try:
    import socket
    from tqdm import tqdm
    from concurrent.futures import ThreadPoolExecutor , as_completed

except ImportError as Ie:
    print(f"[ + ] couldn't import {Ie}")

class PortScanner:
    def __init__(self , default_thread_count = 40):
        self.socket_timeout = 0.4
        self.buffer_size = 1024
        self.default_thread_count = default_thread_count

    def banner_grabber(self,soc):
    #funtion for banner grabbing.
        try:
            banner=soc.recv(self.buffer_size).decode()
            if banner:
                return banner
            else:
                return "No banner"
        except Exception:
            return f"Banner Grabbing error"

    def port_scanner(self,domain,port,is_banner_grabbing):
    #function to scan a port.
        try:
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as soc:
                soc.settimeout(self.socket_timeout)
                soc.connect((domain,port))
                if is_banner_grabbing:
                    banner = self.banner_grabber(soc)
                    return (port,banner)
                return port
        except (socket.error,socket.timeout):
            return None
        
    def all_ports_scanner(self,domain,is_banner_grabbing,start = 0,stop = 1024 , ports = None):
    #function to manage the threads and scanning all ports.
        open_ports = []
        if ports is None:
            ports = list(range(start, stop))
        else:
            if ',' in ports[0]:
                ports = ports[0].split(',')
            else:
                ports = ports

        with ThreadPoolExecutor(max_workers=self.default_thread_count) as executor:
            futures = {
                executor.submit(self.port_scanner, domain, int(port), is_banner_grabbing): port
                for port in ports
            }

            for future in tqdm(as_completed(futures), total=len(ports), desc="[ > ] Scanning", ncols=80, colour="green"):
                result = future.result()
                if result is not None:
                    open_ports.append(result)

        return open_ports

