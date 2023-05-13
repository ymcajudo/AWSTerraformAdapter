import json

#실행할 명령 선택: json file을 읽을 땐 file_read, 쓸 땐 file_write
#jsoncmd = 'file_write'
jsoncmd = 'file_read'

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

jsonFilePath = read_json_file('D:/00.tmp/03.jsonFile/public_variables.json')        
file_path = jsonFilePath['var_cmdFolder']

def filemodify(jsoncmd):
    
    if jsoncmd == 'file_write':
     #file_path = jsonFilePath['var_cmdFolder']      #D:/00.tmp 폴더에 data.json이라는 파일을 만듦
     data = {
         'var_command': 'apply',                     #var_command: apply or destroy
         'var_region': 'ap-northeast-2'
     }
    
     write_json_file(file_path, data)

# Usage example
    elif jsoncmd == 'file_read':
        #file_path = 'D:/00.tmp/data.json'       #D:/00.tmp 폴더에 data.json이라는 파일을 읽음
        try:
            json_data = read_json_file(file_path)
            return(json_data['var_region'])
        except FileNotFoundError:
            print('\nThere is no file in the folder')
    else:
        print('Select commands')

if __name__ == "__main__":
    print(filemodify(jsoncmd))