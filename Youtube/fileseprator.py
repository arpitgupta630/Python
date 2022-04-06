# In this project our task is to seprate diffrent types of file to diffrent folders

import os
import shutil

dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.flac', '.wav', '.wma','.aac'),
    'video_extensions' : ('.mp4', '.avi', '.wmv', '.mkv', '.mov', '.flv', '.mpeg'),
    'document_extensions' : ('.docx', '.pptx', '.pdf', '.xlsx', '.csv', '.txt')
}

user_folder_path = input('Enter folder path: ')

def file_classifier (folder_path, file_extesion):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extesion:
            if file.endswith(extension):
                files.append(file)
    return files

for extension_type, extension_tuple in dict_extensions.items():
    
    new_folder_name = (extension_type.split('_')[0]).title() + ' Folder'
    new_folder_path = os.path.join(user_folder_path, new_folder_name)
    os.mkdir(new_folder_path)
    
    for item in file_classifier(user_folder_path, extension_tuple):
        item_path = os.path.join(user_folder_path, item)
        item_new_path = os.path.join(new_folder_path, item)
        shutil.move(item_path, item_new_path)
        
    