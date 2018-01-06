import multiprocessing

def spawn(num,num2):
    print('Spawned:{}{}'.format(num,num2))

# this ensure that the function will be run only the scipte itself runs, but onlysomething else call it
if __name__=='__main__':
    for i in range(100):
        p=multiprocessing.Process(target=spawn,args=(i,i+1))
        p.start()
        # this is used to wait for the process to be completed
        p.join()
