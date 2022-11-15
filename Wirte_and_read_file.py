"""This simple program can be used to fetch data from any given URL using the GET method, write it to disk and user can also
read the content saved on the console or screen"""

import itertools
import os.path
import tempfile
import time
import uuid

import requests


class ExtractSaveRead:
    def __init__(self, *args, **kwargs):
        self.url = kwargs['url']
        self.__dict__.update(kwargs)
        self.__dict__.update(args)

    @classmethod
    def get_data(cls, url):
        cls.url = url
        response = requests.get(url, stream=True)
        response.encoding = "utf-8"
        saved = response.text  # initialized for user to see fetched content.

        if os.path.exists('response.txt'):
            """save new response according to time"""
            with open(f'response_{int(time.time_ns())}''.txt', 'w+b') as save_file:
                for lines in response.iter_lines(chunk_size=128):
                    save_file.write(lines)
        else:
            with open('response.txt', 'w+b') as save_file:
                for lines in response.iter_lines(chunk_size=128):
                    save_file.write(lines)
                    # print(saved)  # for users to see the content been saved

    @classmethod
    def read_data(cls):
        with open('response.txt', 'r+t') as read_file:
            read_file.seek(0)
            content_check = read_file.read(1)
            if not content_check and os.path.isfile('response.txt'):
                print(f'No content to be read, please check : {os.getcwdb()} if fle present')
            else:
                read_file.seek(0)
                size_to_read = 300
                file_content = read_file.read(size_to_read)
                while len(file_content) > 0:
                    print(f'{file_content}')
                    file_content = read_file.read(size_to_read)


ExtractSaveRead.get_data(input("Please enter the URl: "))  # you can hard code the 'url' here if you wish.
ExtractSaveRead.read_data()

"""Extra Points"""
"""Example of url to use for text: https://restful-booker.herokuapp.com/booking
"""

"""save new response using unique temporary folder and file name"""
# f1, filename = tempfile.mkstemp(prefix='response', suffix='.txt')
# with open(f1, 'wb') as save_file:

"""save new response with a unique uuid"""
# filename = 'response' + str(uuid.uuid4()) + '.txt'
# with open(filename, 'wb') as save_file:


"""save new response with a new extension

rsplit(), which operates on the string in reverse order, 
with 1 as an argument, will split the string on the last 
occurrence of the delimiter i.e. ('.')."""

# base_file = 'response.txt'
# name, ext = base_file.rsplit('.', 1)
# print(name) --> response  i.e splited from .txt
# new_extension = "csv"
# unique_id = int(time.time_ns())
# new_file = f'{name}_{unique_id}.{new_extension}'
# with open(new_file, 'wb') as save_file:
