--- I need to use faiss-gpu. now, this project run with faiss-cpu
--- If you want to learn whether faiss-cpu and faiss-gpu works, you can look flowing code:
"""
# CUDA'nın kullanılabilirliğini kontrol etme
gpu_count = faiss.get_num_gpus()
if gpu_count > 0:
    print(f"CUDA destekli GPU sayısı: {gpu_count}")
else:
    print("CUDA kullanılabilir değil, CPU üzerinde çalışıyor.")

"""

--- 