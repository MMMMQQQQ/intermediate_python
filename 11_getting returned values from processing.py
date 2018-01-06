from multiprocessing import Pool

def job(num):
    return num*2

if __name__=='__main__':
    # how many process that we will define
    p=Pool(processes=20)
    data=p.map(job,range(20))
    data2=p.map(job,[1,2,3])
    p.close()
    print(data)
    print(data2)