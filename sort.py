import os, shutil, datetime


def get_path():
    os.path
    return os.getcwd()
    
parent_path = get_path()

def check_type(full_path):
    return_type = {

        ".xls" : "excel_path",
        ".xlsx" : "excel_path",
        ".xlsm" : "excel_path",
        ".ods" : "excel_path",

        ".fnt" : "font_path",
        ".fon" : "font_path",
        ".otf" : "font_path",
        ".ttf" : "font_path",

        ".bin" : "disk_path",
        ".dmg" : "disk_path",
        ".iso" : "disk_path",
        ".toast" : "disk_path",
        ".vcd" : "disk_path",

        ".pdf" : "pdf_path",
        ".epub" : "pdf_path",
        ".ris" : "pdf_path",

        ".ics" : "invites_path",
        ".zoom" : "invites_path",

        ".docx" : "doc_path",
        ".doc" : "doc_path",
        ".docs" : "doc_path",

        ".pptx" : "ppt_path",
        ".ppt" : "ppt_path",
        ".pps" : "ppt_path",
        ".odp" : "ppt_path",
        ".key" : "ppt_path",

        ".mkv" : "video_path",
        ".mp4" : "video_path",
        ".3g2" : "video_path",
        ".3gp" : "video_path",
        ".avi" : "video_path",
        ".flv" : "video_path",
        ".h264" : "video_path",
        ".m4v" : "video_path",
        ".vof" : "video_path",
        ".swf" : "video_path",
        ".rm" : "video_path",
        ".mpeg" : "video_path",
        ".mov" : "video_path",
        ".mpg" : "video_path",
        ".wmo" : "video_path",

        ".zip" : "zip_path",
        ".rar" : "zip_path", 
        ".tar.gz" : "zip_path",
        ".7z" : "zip_path",
        ".arj" : "zip_path", 
        ".deb" : "zip_path",
        ".rpm" : "zip_path",
        ".z" : "zip_path",
        ".pkg" : "zip_path",

        ".heic" : "image_path", 
        ".jpg" : "image_path", 
        ".png" : "image_path", 
        ".ico" : "image_path", 
        ".jpeg" : "image_path", 
        ".jfif" : "image_path",
        ".webp" : "image_path",
        ".ai" : "image_path",
        ".bmp" : "image_path",
        ".gif" : "image_path",
        ".ps" : "image_path",
        ".psd" : "image_path",
        ".svg" : "image_path",
        ".tif" : "image_path",
        ".tiff" : "image_path",
        
        ".exe" : "exe_path",
        ".appx" : "exe_path",
        ".apk" : "exe_path",
        ".bat" : "exe_path",
        ".msi" : "exe_path",
        ".apk" : "exe_path",
        ".cgi" : "exe_path",
        ".com" : "exe_path",
        ".gadget" : "exe_path",
        ".jar" : "exe_path",
        ".w2f" : "exe_path",

        ".aif" : "audio_path",
        ".cda" : "audio_path",
        ".mid" : "audio_path",
        ".midi" : "audio_path",
        ".mp3" : "audio_path",
        ".mpa" : "audio_path",
        ".ogg" : "audio_path",
        ".wav" : "audio_path",
        ".wma" : "audio_path",
        ".wpl" : "audio_path",

        ".opdownload" : "NULL",
        ".crdownload" : "NULL",
        ".opdownload" : "NULL",
        ".download" : "NULL",
        ".part" : "NULL",
        ".temp" : "NULL",
        ".tmp" : "NULL",
        "log.txt" : "NULL",
        "sort.lnk" : "NULL",

        ".c" : "c_path",
        ".h" : "c_path",

        ".cpp" : "cpp_path",

        ".java" : "java_path",
        ".class" : "java_path",

        ".py" : "python_path",

        ".ipynb" : "jupyter_path",

        ".js" : "js_path",

        ".ts" : "ts_path",

        ".bat" : "cmd_path",
        ".sh" : "cmd_path",
        ".cmd" : "cmd_path",

        ".css" : "css_path",

        ".htm" : "html_path",
        ".html" : "html_path",
        ".xhtml" : "html_path",

        ".cs" : "cs_path",

        ".php" : "php_path",

        ".swift" : "swift_path",

        ".wb" : "binary_path",

        ".blend1" : "3d_path",

        ".txt" : "notes_path"

        }

    for i in return_type.keys():
        if full_path.lower().endswith(i):
            return return_type[i]
    return "misc_path"  #stores the file in miscellaneous path 

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

    paths = {
        "image_path":  "IMAGE" ,
        "pdf_path":  "PDF" ,
        "doc_path":  "DOCS" ,
        "misc_path":  "MISC" ,
        "ppt_path":  "PPT" ,
        "video_path":  "VIDEO" ,
        "zip_path":  "ZIP" ,
        "exe_path":  "EXE" ,
        "excel_path" : "XLSX",
        "audio_path" : "AUDIO",
        "code_path" : "CODE",
        "c_path" : "CODE/C",
        "cpp_path" : "CODE/C++",
        "cs_path" : "CODE/C#",
        "java_path" : "CODE/Java",
        "js_path" : "CODE/JavaScript",
        "ts_path" : "CODE/TypeScript",
        "cmd_path" : "CODE/CMD",
        "html_path" : "CODE/HTML",
        "binary_path" : "CODE/Binary",
        "php_path" : "CODE/PHP",
        "swift_path" : "CODE/Swift",
        "css_path" : "CODE/CSS",
        "jupyter_path" : "CODE/Jupyter",
        "python_path" : "CODE/Python",
        "disk_path" : "DISK IMAGES",
        "3d_path" : "3D",
        "notes_path" : "NOTES",
        "invites_path" : "INVITES",
        "font_path" : "FONTS"
        }

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