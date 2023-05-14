import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler      #본 파이썬 코드명을 watchdog.py라고 하면 에러뜸. watchdog 이외 이름으로 정의
import jsonfilemodify
import jsonfile
import RunTerraform
import shutil
import findfile

"""
실행방법----------------------------------
1. D:\00.tmp\04.testweb에서 testweb_apply.html 또는 testweb_destroy.html 파일을 웹 브라우저에서 열기
2. 위 1의 웹 브라우저에서 버튼 클릭
3-1. 위 2에서 apply이면 AWS에 instance 생성(apply)
3-2. 위 2에서 destroy이면 AWS에 instance 삭제(destroy)
참고: 테스트 관련 파일은 D:\00.tmp 에 있고, 같은 폴더에 압축 파일(00.tmp.zip)로 백업
"""

tf_cmd = jsonfile.read_json_file('D:/00.tmp/03.jsonFile/public_variables.json')     #프로그램에 사용할 전역변수

# Define the event handler
class NewFileHandler(FileSystemEventHandler):
    
    def on_created(self, event):                                #해당 폴더에 파일 생성(create)
        
        #테스트 케이스 선택
        json_data = jsonfile.read_json_file(tf_cmd['var_cmdFolder'])        #public_variables.json에서 var_cmdFolder의 data.json 읽기
        tfCreate = json_data['var_command']

        if not event.is_directory:
            print("\n==============================================")
            print(">>> Input command: " + json_data['var_command'])          #입력된 명령어
            print("==============================================\n")
            if tfCreate == 'apply':             #Make VMs
                shutil.copy(tf_cmd['var_sampleFile_tf'], tf_cmd['var_testFile_tf'])
                tfchange(tf_cmd['var_testFile_tf'])
                RunTerraform.exeTerraformbyPython('init')               #Terraform commands: tf.init, tf.plan, tf.apply, tf.destroy
                RunTerraform.exeTerraformbyPython('plan')
                RunTerraform.exeTerraformbyPython('apply')
                shutil.move(tf_cmd['var_cmdFolder'], tf_cmd['var_cmdMove'])
            elif tfCreate == 'destroy':
                RunTerraform.exeTerraformbyPython('init')               #Terraform commands: tf.init, tf.plan, tf.apply, tf.destroy
                RunTerraform.exeTerraformbyPython('destroy')
                shutil.move(tf_cmd['var_cmdFolder'], tf_cmd['var_cmdMove'])
                
    def on_deleted(self, event):                                    ##해당 폴더에 파일 삭제(delete)
        if not event.is_directory:
            print("\n===========================================")
            print(">>> A file deleted: ", fName(event.src_path))
            print("===========================================\n")
#--------------------------------------------------------

#Find out the name of a file
def fName(strFileName):
    for i in range(len(strFileName)):
        if strFileName[i] == "\\":
            return strFileName[i+1:len(strFileName)]                #파일 이름 리턴
    
# Define the function to watch a folder
def watch_folder(path):
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    
    #테스트 웹페이지에서 만든 data.json 파일이 download folder에 있으면 watch하는 폴더로 이동 시켜서 이벤트 발생
    if findfile.find_file(tf_cmd['var_downloadpath'], tf_cmd['var_downloadfilename']) :
        time.sleep(1)
        shutil.move(tf_cmd['var_download'], tf_cmd['var_cmdFolder'])   
 
    try:
        while True:
            time.sleep(1)
            #초당 1회 모니터링 하다가 새로운 data.json이 들어오면 실행(watch하는 폴더로 이동해서 이벤트 발생)
            if findfile.find_file(tf_cmd['var_downloadpath'], tf_cmd['var_downloadfilename']) :
                shutil.move(tf_cmd['var_download'], tf_cmd['var_cmdFolder'])  
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Folder watch Example usage
def tfchange(file_path):
    jsoncmd = 'file_read'                           #json 파일 읽기
    replacements = {
        "${var_region}": jsonfile.filemodify(jsoncmd)       #tf 파일에 변수값(${var_region})을 us-east-2, ap-northeast-2(서울)로 변경
    }
 
    # File modification example usage
    jsonfilemodify.change_strings_in_file(file_path, replacements)

if __name__ == "__main__":
    tf_cmd = jsonfile.read_json_file('D:/00.tmp/03.jsonFile/public_variables.json')     #프로그램에 사용할 전역변수
    folder_path = tf_cmd['var_watchFolder']       #D:/00.tmp 폴더의 파일 생성/삭제/이동 등 이벤트 모니터링
    watch_folder(folder_path)       #파이썬에서는 디렉토리 심볼이 "\"이 아니라 "/"
    
    
