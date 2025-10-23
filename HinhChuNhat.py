class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def get_chu_vi(self):
        return (self.dai + self.rong) * 2

    def get_dien_tich(self):
        return self.dai * self.rong

    def xuat(self):
        print(f"Hình chữ nhật: dài = {self.dai}, rộng = {self.rong}, "
              f"chu vi = {self.get_chu_vi()}, diện tích = {self.get_dien_tich()}")


class Vuong(ChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

    def xuat(self):
        print(f"Hình vuông: cạnh = {self.dai}, "
              f"chu vi = {self.get_chu_vi()}, diện tích = {self.get_dien_tich()}")
