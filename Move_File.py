import os
import shutil

from_dir= "/Users/umaranims/Downloads"
to_dir="/Users/umaranims/Desktop"
to_dir2="/Users/umaranims/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)


    if extension == '':
        continue

    elif extension in ['.gif','.png','jpg','.jpg','.jfif']:
        path1= from_dir + '/' + file_name
        path2= to_dir + '/' + "Image_File"
        path3 = to_dir + '/' + "Image_File" + '/' + file_name  
        
        if os.path.exists(path2):
            print("Moving" + file_name + "......")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + "......")

            shutil.move(path1,path3)

    
    else:
        path4= from_dir + '/' + file_name
        path5= to_dir2 + '/'+ "pdf_File"
        path6 = to_dir + '/' + "pdf_File" + '/' + file_name  
        
        if os.path.exists(path5):

            print("Moving" + file_name + "......")

            shutil.move(path4,path6)

        else: 
            os.makedirs(path5)
            print("Moving" + file_name + "......")

            shutil.move(path4,path6)
        
    



        
        
        




