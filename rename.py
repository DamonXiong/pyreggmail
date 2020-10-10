import os


def renameFile():
    fileList = os.listdir(r"H:\01.Company\01.CCB\验收测试\s160_innputpin")
    print(fileList)
    # get current work path
    currentpath = os.getcwd()
    print("Current is " + currentpath)
    # change current work path
    os.chdir(r"H:\01.Company\01.CCB\验收测试\s160_innputpin")
    for fileName in fileList:
        print("Original is " + fileName)
        # delete 0123456789 in file name
        os.rename(fileName, fileName.replace('_00', '_0'))
        print("Changed is " + fileName.replace('_00', '_0'))
    os.chdir(currentpath)


renameFile()
