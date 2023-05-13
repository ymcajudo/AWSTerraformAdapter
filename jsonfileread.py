from hcl2.parser import parse_string

def read_terraform_file(file_path):
    with open(file_path, 'r') as file:
        terraform_code = file.read()
    parsed_data = parse_string(terraform_code)
    return parsed_data

# Usage example
if __name__ == "__main__":
    file_path = 'D:/00.tmp/01.tf_File/maintest.tf'      
    parsed_data = read_terraform_file(file_path)
    print(parsed_data)