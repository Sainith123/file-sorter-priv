import os, shutil, json, datetime


def get_path():
    path = os.popen('pwd').read().split("/")[2:]
    path[0] = path[0].upper()
    path[0] += ":"
    path[-1] = path[-1][:-1]
    return r"\\".join(path)
    
parent_path = get_path()

def check_type(full_path):
    return_type = {
        ".xls" : "excel_path",
        ".xlsx" : "excel_path",
        ".pdf" : "pdf_path",
        ".docx" : "doc_path",
        ".pptx" : "ppt_path",
        ".mkv" : "video_path",
        ".mp4" : "video_path",
        ".zip" : "zip_path",
        ".rar" : "zip_path", 
        ".tar.gz" : "zip_path",
        ".heic" : "image_path", 
        ".jpg" : "image_path", 
        ".png" : "image_path", 
        ".ico" : "image_path", 
        ".jpeg" : "image_path", 
        ".jfif" : "image_path",
        ".webp" : "image_path",
        ".exe" : "exe_path",
        ".appx" : "exe_path",
        ".img" : "exe_path",
        ".bat" : "exe_path",
        ".msi" : "exe_path",
        ".opdownload" : "NULL",
        ".crdownload" : "NULL",
        ".opdownload" : "NULL",
        ".download" : "NULL",
        ".part" : "NULL",
        ".temp" : "NULL",
        ".tmp" : "NULL",
        "log.txt" : "NULL",
        "sort.lnk" : "NULL"
        }

    for i in return_type.keys():
        if full_path.lower().endswith(i):
            return return_type[i]
    return "misc_path"

def check_directory(path):
    return os.path.isdir(os.path.join(parent_path,path)) or check_type(path) == "NULL"

def move_file(start_path,end_path):
    try:
        shutil.move(start_path,end_path)
        with open(os.path.join(parent_path,"log.txt"),"a") as f:
            f.write(f"{datetime.datetime.now()} : Moving {file} into {paths[check_type(file)]}\n")
    except:
        with open(os.path.join(parent_path,"log.txt"),"a") as f:
            f.write(f"{datetime.datetime.now()} : Moving {file} into {paths[check_type(file)]} FAILED\n")

def folders_do_exist():
    
    global paths
    paths = {"image_path":  "IMAGE" ,"pdf_path":  "PDF" ,"doc_path":  "DOCS" ,"misc_path":  "MISC" ,"ppt_path":  "PPT" ,"video_path":  "VIDEO" ,"zip_path":  "ZIP" ,"exe_path":  "EXE" ,"excel_path" : "XLSX"}
    paths = {k:os.path.join(parent_path,v) for k,v in paths.items()}

    for i in paths.values():
        if not os.path.exists(i):
            os.makedirs(i)

    if not os.path.exists(os.path.join(parent_path,"log.txt")):
        with open(os.path.join(parent_path,"log.txt"),"w") as f:
            pass

folders_do_exist()

while True:

    files = [i for i in os.listdir(parent_path) if not check_directory(i)]
    
    if files == []:
        break
    
    for file in files:
        move_file(os.path.join(parent_path,file),paths[check_type(file)])




