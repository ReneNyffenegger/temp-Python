import torch

print(f'CUDA is available       : {torch.cuda.is_available()}'    )
print(f'Available GPUs          : {torch.cuda.device_count()}'    )
print(f'Current device          : {torch.cuda.current_device()}'  )
print(f'Current device location : {torch.cuda.device(0)}'         )
print(f'Name of the device      : {torch.cuda.get_device_name(0)}')
