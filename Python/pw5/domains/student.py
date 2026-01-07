class Student:
    def __init__(self, sid, name, dob):
        self.__sid = sid
        self.__name = name
        self.__dob = dob

    def get_sid(self):
        return self.__sid
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob