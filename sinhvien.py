class Sinhvien:
   

    def __init__(self, tensv, namsinh, truong):
        self.ten_sv = tensv
        self.namsinh = namsinh
        self.truong = truong
    def xoa(self):
        pass
    def sua(self):
        pass  
    def xuat_thong_tin(self):
        print(f"sinhvien: {self.ten_sv}, namsinh: {self.namsinh}, truong: {self.truong}") 
    def __str__(self):
        return f"sinhvien: {self.ten_sv}, namsinh: {self.namsinh}, truong: {self.truong}"



