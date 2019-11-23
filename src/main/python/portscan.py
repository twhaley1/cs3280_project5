import sys
import socket
import multiprocessing

def scan(ip, startPort, endPort = None):
    if endPort is None:
        endPort = startPort
    if endPort < startPort:
        raise ValueError
        
    processQueue = multiprocessing.Queue(2 + endPort - startPort)
    print('------------------------------------------------------------')
    processes = startProcesses(processQueue, ip, startPort, endPort)
    waitForProcesses(processQueue, processes)
    print('------------------------------------------------------------')
    
    return getPortDictionary(processQueue)
    
def startProcesses(queue, ip, startPort, endPort):
    processes = []
    for port in range(startPort, endPort + 1):
        process = multiprocessing.Process(target=detectPortStatus, args=(queue, ip, port))
        processes.append(process)
        print(f'Starting scan on Port: {port}')
        process.start()
    return processes
        
def waitForProcesses(queue, processes):
    print('\nWaiting on processes to conclude...')
    for process in processes:
        pid = process.pid
        process.join()
        print(f'Process {pid} Complete.')
    print('Processes complete...\n')
    queue.put(None)
    
def getPortDictionary(queue):
    statusDictionary = {}
    for queueContent in iter(queue.get, None):
        statusDictionary[queueContent[0]] = queueContent[1]
    return statusDictionary

def detectPortStatus(output, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    portOpen = False
    if result == 0:
        portOpen = True
    output.put((port, portOpen))
    
def printList(source):
    for item in source:
        print(item)

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3 or len(args) > 4:
        sys.exit('Invalid Program Arguments...')
        
    contents = {}
    if len(args) == 3:
        contents = scan(str(args[1]), int(args[2]))
    if len(args) == 4:
        contents = scan(str(args[1]), int(args[2]), int(args[3]))
    
    portKeys = list(contents.keys())
    portKeys.sort()
    printableContents = map(lambda key: f'Port: {key} -> Open: {contents[key]}', portKeys)
    printList(printableContents)

