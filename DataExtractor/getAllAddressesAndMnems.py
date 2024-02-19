import os
import json

def read_shared_config(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        address = data.get('wallet', '')
        mnem = data.get('mnem', '')
        return address, mnem

def main():
    output_file = 'Accounts.txt'
    with open(output_file, 'w') as output:
        folder_names = [folder_name for folder_name in os.listdir('C:\\VmSharedFolder') if folder_name.isdigit()]
        folder_names.sort(key=lambda x: int(x))
        for folder_name in folder_names:
            folder_path = os.path.join('C:\\VmSharedFolder', folder_name)
            shared_config_path = os.path.join(folder_path, 'sharedConfig.json')
            if os.path.exists(shared_config_path):
                address, mnem = read_shared_config(shared_config_path)
                output.write(f"{folder_name} - \"{address}\" - \"{mnem}\"\n")
    print(f"Data has been written to {output_file}")

if __name__ == "__main__":
    main()
    
