import subprocess 
import multiprocessing

def script1():
    cmd1 = 'FaceMesh.py'
    p = subprocess.Popen(cmd1, shell = True)
    out, err  = p.communicate()


def script2():
    cmd2 = 'Gui.py'
    p = subprocess.Popen(cmd2, shell = True)
    out, err  = p.communicate()

p1  =  multiprocessing.Process(target= script1)
p2  =  multiprocessing.Process(target= script2)

if __name__ == '__main__' :
    p1.start()
    p2.start()
    p1.join()
    p2.join()

