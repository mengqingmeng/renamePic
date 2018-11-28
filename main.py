import pandas as pd
import numpy as np
import os
from PIL import Image
import shutil
import re
current_file_path =  os.path.dirname(os.path.abspath(__file__))
newColName = '更改数量'
def loadExcel(path):
    excel = pd.ExcelFile(path)
    df = pd.read_excel(excel)
    return df

def processDF(df):
    writer = pd.ExcelWriter('renamePicRecording.xlsx')
    df[newColName] = None
    for index,series in df.iterrows():
        fromID = series.values[0]
        toID = series.values[1]
        processCount = renamePic(fromID,toID)
        df.at[index, newColName] = processCount
        # print(result)
        # print(series)
    df.to_excel(writer,'Sheet1')

def renamePic(fromID,toID):
    fromDir = '/Users/mqm/Downloads/1127产品图片汇总'
    # 将图片文件夹下面的图片名存在数组中
    picNames = []
    for _, _, files in os.walk(fromDir):
        # print(len(files)    
        for file in files:
            picNames.append(file)

    renamedPicFloderName = 'renamedPic'
    renamedPicFloderPath = os.path.join(current_file_path,renamedPicFloderName)
    if not os.path.exists(renamedPicFloderPath):
        os.mkdir(renamedPicFloderPath)
    # 查找原图
    re_str = r'^cp\_'+str(fromID)+r'\_\d{1}\.\w*'
    
    count = 0
    for picName in picNames:
        if re.match(re_str,picName):
            count +=1
            # 复制图片并重命名
            srcImg = os.path.join(fromDir,picName)
            dstImg = os.path.join(renamedPicFloderPath,'cp_'+str(toID)+'_'+str(count)+'.png')
            shutil.copyfile(srcImg,dstImg)
            
    return count

    
if __name__ == "__main__":
    path = '/Users/mqm/Downloads/IT用新增产品ID更换.xlsx'
    df = loadExcel(path)
    processDF(df)