import os
import shutil
temp_files_name = ["Temp", "Prefetch", "%Temp%"]


def clear_files(folders):
    amount_files_removed = {}
    for key, path in folders.items():
        if key in temp_files_name:
            amount_files_removed[key] = len(os.listdir(path))
            clear_temp_folders(path)
        else:
            amount_files_removed[key] = len(os.listdir(path))
            shutil.rmtree(path)
    return amount_files_removed


def clear_temp_folders(path):
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            try:
                os.remove(item_path)
            except:
                continue
            
    
        
    
    
