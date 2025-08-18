import os 

def rename_files(folder_path, prefix="file", start_number=1):
    """
    Renames all files in the given folder with numbering.
    
    :param folder_path: Path to the folder containing files.
    :param prefix: Prefix for the renamed files.
    :param start_number: Starting number for numbering.
    """
    if not os.path.isdir(folder_path):
        print(f"❌ Invalid folder: '{folder_path}'")
        print(f"Length of path: {len(folder_path)}")
        print(f"Characters in path: {[c for c in folder_path]}")
        return
    else:
        print(f"✅ Found folder: '{folder_path}'")
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort() # Ensures files are renames in alphabetical order 

    for count, filename in enumerate(files, start=start_number):
        file_ext = os.path.splitext(filename)[1] # Keep the file extension
        new_name = f"{prefix}_{count}{file_ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f'Renamed: {filename} -> {new_name}')
    
    print("\n✅ All files have been renamed.")


# Example usage: 
if __name__ == "__main__": 
    folder = input("Enter folder path: ").strip()
    folder = folder.replace("\\", "/") 
    prefix = input("Enter file prefix (default 'file): ").strip() or "file"
    try: 
        start_num = int(input("Enter starting number (default 1): ").strip() or 1)
    except ValueError: 
        start_num = 1
    

    rename_files(folder, prefix, start_num)