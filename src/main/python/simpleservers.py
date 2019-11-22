import subprocess, time

class SimpleServers:

    def __init__(self, *ports):
        self.ports = list(ports)
        self.pids = []
        
    def start(self):
        for port in self.ports:
            process = subprocess.Popen(['python', '-m', 'http.server', str(port), '--bind', '127.0.0.1'])
            # I do not know if there is a better way to do this. If I do not sleep,
            # the unit tests run before the servers are up and running. I have looked
            # for a solution, but nothing I am trying is working except for this.
            time.sleep(1)
            self.pids.append(process.pid)
            
    def stop(self):
        for identifier in self.pids:
            subprocess.call(['kill', str(identifier)])
           
