#to test whether cuda,torch is using gpu
'''import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))'''

#to clear cuda cache
import torch
torch.cuda.empty_cache()

#clear files in a directory
'''import os,glob
files = glob.glob('./transfer/' + '*')
for file in files:
    os.remove(file)'''