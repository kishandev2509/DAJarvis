import multiprocessing
import requests

def downloadFile(url, name):
    r = requests.get(url)
    open(f"del\\file{name}.jpg","wb").write(r.content)




if __name__ == '__main__':
    url = "https://picsum.photos/5000/3250"

    pross=[]

    for i in range(1000):
        p = multiprocessing.Process(target=downloadFile,args=[url,i])
        p.start()
        pross.append(p)

    for p in pross:
        p.join()