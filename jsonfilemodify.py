import jsonfile

def change_strings_in_file(file_path, replacements):
    #with open(file_path, 'r', encoding="UTF-8") as file:       #한글 때문에 파일 열때 에러 발생시 적용
    with open(file_path, 'r') as file:
        text = file.read()

    modified_text = change_strings(text, replacements)

    with open(file_path, 'w') as file:
        file.write(modified_text)

def change_strings(text, replacements):
    for old_string, new_string in replacements.items():
        text = text.replace(old_string, new_string)
    return text

# Usage example
if __name__ == "__main__":
    
    tf_cmd = jsonfile.read_json_file('D:/00.tmp/03.jsonFile/public_variables.json')
    tf_cmd['var_sampleFile_tf']

    file_path = tf_cmd['var_sampleFile_tf']

    jsoncmd = 'file_read'                           #json 파일 읽기

    replacements = {
      #"${var_region}": "ap-northeast-2"            #tf 파일에 변수값(${var_region})을 us-east-2, ap-northeast-2(서울)로 변경
      #"${var_region}": "us-east-2"
      "${var_region}": jsonfile.filemodify(jsoncmd)
    }

    change_strings_in_file(file_path, replacements)

    print('\n Done!!')
