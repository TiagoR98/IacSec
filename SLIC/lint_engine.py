'''
Akond Rahman
Feb 08, 2018
Puppet Lint Engine
'''
import constants
import subprocess
import os
import numpy as np

def generateOutput(path2file):
    ## Add rules to check automatically here
    if(path2file.endswith(constants.PP_EXT)):
        rulesToCheck = [constants.PP_RULE_ALL_IN_ONE]
        lintToolCmd = constants.PP_LINT_TOOL
    elif(path2file.endswith(constants.CH_EXT)):
        rulesToCheck = [constants.CHEF_ALL_RULES, constants.CHEF_SWITCH_RULE]
        lintToolCmd = constants.CHEF_LINT_TOOL
    for rule_ in rulesToCheck:
        try:
           command2exec = lintToolCmd + ' ' + rule_ + ' ' + path2file + ' ' + constants.REDIRECT_APP + ' ' + constants.OUTPUT_TMP_LOG
        #    print command2exec
           subprocess.check_output([constants.BASH_CMD, constants.BASH_FLAG, command2exec])
        except subprocess.CalledProcessError as e_:
           print(constants.EXCEPTION + str(e_))

def getOutputLines():
    file_lines = []
    with open(constants.OUTPUT_TMP_LOG, constants.FILE_OPEN_MODE) as log_fil:
         file_str = log_fil.read()
         file_lines = file_str.split(constants.NEWLINE)
    return file_lines

def getHardCodeCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_HARD in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_HARD in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getSuspCommCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_SUSP in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_SUSP in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getSecretLocaCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_SECRET in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_SECRET in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getMD5UsageCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_MD5 in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_MD5 in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getHTTPUsageCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_HTTP in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_HTTP in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getBindUsageCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_BIND in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_BIND in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getEmptyPwdCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_EMPT in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_EMPT in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getDefaultAdminCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_DEF_ADM in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_DEF_ADM in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getBase64Count(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_BASE64 in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_BASE64 in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getMissingDefaultCount(file_lines):
    cnt2ret = 0
    line2ret = [ s_ for s_ in file_lines if constants.LINT_MIS_DEFAU in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    for s_ in file_lines:
        if constants.LINT_MIS_DEFAU in s_:
           cnt2ret += 1
    if cnt2ret > 0:
        line2ret = list(np.unique(line2ret))
    return cnt2ret, line2ret

### Puppet Missing Default
def getPuppetMissingDefaultCount(file_lines):
    cnt2ret = 0
    line2ret = [ s_ for s_ in file_lines if constants.PUPP_MISS_DEFA in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    for s_ in file_lines:
        if constants.PUPP_MISS_DEFA in s_:
           cnt2ret += 1
    if cnt2ret > 0:
        line2ret = list(np.unique(line2ret))
    return cnt2ret, line2ret
'''
added june 26, 2018
'''

def getHardCodeUserCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_HARD_CODE_UNAME in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_HARD_CODE_UNAME in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getHardCodePassCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_HARD_CODE_PASS in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_HARD_CODE_PASS in s_ for s_ in file_lines)
    return cnt2ret, line2ret


def getIntegCheckCount(file_lines):
    line2ret = [ s_ for s_ in file_lines if constants.LINT_INTEG_VIO in s_]
    line2ret = [str_.split(constants.AT_SYMBOL)[1] for str_ in line2ret if constants.AT_SYMBOL in str_]
    cnt2ret = sum(constants.LINT_INTEG_VIO in s_ for s_ in file_lines)
    return cnt2ret, line2ret


def parseOutput():
    '''
    Initialization
    '''
    rul_hardcode_cnt,  rul_hardcode_lin   = 0, ''
    rul_susp_comm_cnt, rul_susp_comm_lin  = 0, ''
    rul_secr_loca_cnt, rul_secr_loca_lin  = 0, ''
    rul_md5_usage_cnt, rul_md5_usage_lin  = 0, ''
    rul_http_use_cnt,  rul_http_use_lin   = 0, ''
    rul_bind_use_cnt,  rul_bind_use_lin   = 0, ''
    rul_empt_pwd_cnt,  rul_empt_pwd_lin   = 0, ''
    rul_defa_adm_cnt,  rul_defa_adm_lin   = 0, ''
    rul_base64_cnt,    rul_base64_lin     = 0, ''
    rul_mis_case_cnt,  rul_mis_case_lin   = 0, ''
    ## added June 26, 2018
    rul_sec_user_cnt,  rul_sec_user_lin   = 0, ''
    rul_sec_pass_cnt,  rul_sec_pass_lin   = 0, ''
    ## added June 26, 2018
    rul_sec_inte_cnt,  rul_sec_inte_lin   = 0, ''
    ## added June 14, 2019
    rul_pup_dflt_cnt,  rul_pup_dflt_lin   = 0, ''
    '''
    '''
    file_ = open(constants.OUTPUT_TMP_LOG, constants.FILE_OPEN_MODE)
    num_lines = sum(1 for line_ in file_)
    # print 'Genrated a log file of {} lines'.format(num_lines)
    if num_lines > 0:
        file_lines = getOutputLines()
        # print file_lines
        rul_hardcode_cnt,  rul_hardcode_lin   = getHardCodeCount(file_lines)
        rul_susp_comm_cnt, rul_susp_comm_lin  = getSuspCommCount(file_lines)
        rul_secr_loca_cnt, rul_secr_loca_lin  = getSecretLocaCount(file_lines)
        rul_md5_usage_cnt, rul_md5_usage_lin  = getMD5UsageCount(file_lines)
        rul_http_use_cnt,  rul_http_use_lin   = getHTTPUsageCount(file_lines)
        rul_bind_use_cnt,  rul_bind_use_lin   = getBindUsageCount(file_lines)
        rul_empt_pwd_cnt,  rul_empt_pwd_lin   = getEmptyPwdCount(file_lines)
        rul_defa_adm_cnt,  rul_defa_adm_lin   = getDefaultAdminCount(file_lines)
        rul_base64_cnt,    rul_base64_lin     = getBase64Count(file_lines)
        rul_mis_case_cnt,  rul_mis_case_lin   = getMissingDefaultCount(file_lines)
        ## added June 26, 2018
        rul_sec_user_cnt,  rul_sec_user_lin   = getHardCodeUserCount(file_lines)
        rul_sec_pass_cnt,  rul_sec_pass_lin   = getHardCodePassCount(file_lines)

        ## added June 26, 2018
        rul_sec_inte_cnt,  rul_sec_inte_lin   = getIntegCheckCount(file_lines)
        ## added June 14, 2019
        rul_pup_dflt_cnt,  rul_pup_dflt_lin   = getPuppetMissingDefaultCount(file_lines)
    # this will be expanded
    # output2ret = (rul_hardcode_cnt, rul_susp_comm_cnt, rul_secr_loca_cnt, rul_md5_usage_cnt,
    #               rul_http_use_cnt, rul_bind_use_cnt, rul_empt_pwd_cnt, rul_defa_adm_cnt,
    #               rul_base64_cnt, rul_mis_case_cnt)

    output2ret = (rul_hardcode_cnt, rul_susp_comm_cnt, rul_md5_usage_cnt,
                  rul_http_use_cnt, rul_bind_use_cnt, rul_empt_pwd_cnt, rul_defa_adm_cnt,
                  rul_mis_case_cnt, rul_sec_inte_cnt,
                  rul_pup_dflt_cnt
                 )  # // removing base 64 after luke feedback, added puppet default count
    tot_cnt = sum(output2ret)

    output2ret = (rul_hardcode_cnt, rul_susp_comm_cnt, rul_md5_usage_cnt,
                  rul_http_use_cnt, rul_bind_use_cnt, rul_empt_pwd_cnt, rul_defa_adm_cnt,
                  rul_sec_user_cnt, rul_sec_pass_cnt,                  ### added June 26, 2018
                  rul_mis_case_cnt, rul_sec_inte_cnt, rul_pup_dflt_cnt,  ### added June 14, 2019
                  tot_cnt )
    # this will be expanded
    str2ret    = (rul_hardcode_lin, rul_susp_comm_lin, rul_secr_loca_lin, rul_md5_usage_lin,
                  rul_http_use_lin, rul_bind_use_lin, rul_empt_pwd_lin, rul_defa_adm_lin,
                  rul_base64_lin, rul_mis_case_lin, rul_sec_user_lin, rul_sec_pass_lin, rul_sec_inte_lin, rul_pup_dflt_lin) ### added June 26, 2018

    # print str2ret
    return output2ret, str2ret




def runLinter(full_path_file):
    #1. run linter with custom rules
    generateOutput(full_path_file)
    #2. parse output
    all_rul_cnt_out = parseOutput()
    #3. delete temp file
    os.remove(constants.OUTPUT_TMP_LOG)
    ## returns a tuple: first is count, second is line string
    return all_rul_cnt_out
