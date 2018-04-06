import os
import Crypto




def encrypt(key, file_name):
    chunk_size = 64*1024
    output_file = "(encrypted)" + file_name
    file_size = str(os.path.getsize(file_name)).zfill(16)

print("Hello")
