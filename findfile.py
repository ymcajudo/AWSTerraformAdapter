import os
import glob
import jsonfile
import time

tf_cmd = jsonfile.read_json_file('D:/00.tmp/03.jsonFile/public_variables.json')

# 특정 폴더 경로와 파일 이름 설정
folder_path = tf_cmd['var_downloadpath']

file_name = tf_cmd['var_downloadfilename']

def find_file(folder_path, file_name):
    # 폴더 내의 모든 파일 경로 가져오기
    all_files = glob.glob(os.path.join(folder_path, '*'))

    # 파일 이름과 일치하는 파일 찾기
    for file_path in all_files:
        if os.path.isfile(file_path) and os.path.basename(file_path) == file_name:
            #return file_path
            return True

    # 일치하는 파일이 없는 경우 None 반환
    return None

# 파일 찾기 함수 호출
if __name__ == "__main__":

    # 결과 출력
    while True:
        result = find_file(folder_path, file_name)
        if result:
            print(f'파일이 존재합니다: {result}')
        else:
            print('파일을 찾을 수 없습니다.')
        time.sleep(1)
            
