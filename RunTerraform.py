from python_terraform import *
import jsonfile

tf_cmd = jsonfile.read_json_file('D:/00.tmp/03.jsonFile/public_variables.json')     #프로그램에 사용할 전역변수

def exeTerraformbyPython(exeCmd):
    #tf = Terraform(working_dir='D:/00.tmp')
    tf = Terraform(working_dir = tf_cmd['var_workingDir'])
    
    if exeCmd == 'init':
        return_code, output, err = tf.init(capture_output=True)
    elif exeCmd == 'plan':
        return_code, output, err = tf.plan(capture_output=True)
    elif exeCmd == 'apply':
        return_code, output, err = tf.apply(capture_output=True,skip_plan=True)
    elif exeCmd == 'destroy':
        return_code, output, err = tf.destroy(capture_output=True,auto_approve=True, force=None)
    
    print(output)
    print(err)
    #print(return_code)       

if __name__ == "__main__":
    exeCmd = 'init'               #tf.init, tf.plan, tf.apply, tf.destroy
    exeTerraformbyPython(exeCmd)
