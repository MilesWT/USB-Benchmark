import os
import time
data = "I liek sneks"
with open('output_file', 'w') as fout:
    fout.seek(0)
    start = time.clock()
    fout.write(data) # replace 1024 with size_kb if not unreasonably large
    end = time.clock()
    fout.truncate()
print("File written in "+str(end-start)+" Seconds")
