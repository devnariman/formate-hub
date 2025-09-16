from PIL import Image
import os


class convertor():
    def __init__(self , file_name , formate , path):
        self.f_name = file_name
        self.format = formate
        self.path = path
        self.get_input_path()
        # self.download_path = 

    def get_input_path(self ):
        current_path = os.getcwd()
        parent_path = os.path.dirname(current_path)
        media_path = os.path.join(parent_path, "media")
        print(media_path)
        input()
    


