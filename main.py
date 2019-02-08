import time, glob
def pertence(path, t):
    with open(path) as f:
        n = f.readline()
        t = int(f.readline())
        for p in range(t):
            if n == f.readline():
                return ("True", str(p), str(time.time()-t))
        return ("False", "-1", str(time.time()-t))
                

for file in glob.glob("*.csv"):
    with open("resposta-" + file.replace("csv", "txt"), "w") as f:
        result = pertence(file, time.time())
        f.write("\n".join(result))