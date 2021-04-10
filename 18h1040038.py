import random
class person:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender
    def ho_ten(self):
        for i in range(0,self.sinhvien):
            hoten=str(input("nhap ten sinh vien {} : ".format(i)))
            self.name.apperd(hoten)
    def tuoi(self):
        for i in range(0,self.sinhvien):
            tuoi=random(17,25)
            self.age.apperd(tuoi)
    def gioitinh(self):
        for i in range(0,self.gioitinh):
            gioitinh=str(input("nhap gioi tinh{} : ".format(i)))
            self.gender.apperd(gioitinh)
class student(person):
    def __init__(self, Id, Class, Grade):
        self.Id = Id
        self.Class = Class
        self.Grade = Grade
    def Id(self):
        for i in range(0,self.sinhvien):
            nhap_id =int(input("nhap id cho sinh vien thu {} : ".format(i)))
            self.id.append(nhap_id)
            return self.Id
    