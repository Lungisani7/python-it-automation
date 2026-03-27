import shutil

def get_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)

    print("=== DISK USAGE REPORT ===")
    print(f"Path: {path}")
    print(f"Total: {total // (1024**3)} GB")
    print(f"Used: {used // (1024**3)} GB")
    print(f"Free: {free // (1024**3)} GB")

if __name__ == "__main__":
    get_disk_usage()
