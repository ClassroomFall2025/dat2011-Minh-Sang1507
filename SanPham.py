


class SanPham:
    def __init__(self):
        self.ten_sp = ""
        self.gia = 0.0
        self.giam_gia = 0.0

    def thue_nhap_khau(self):
        return self.gia * 0.1

    def nhap(self):
        self.ten_sp = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.giam_gia = float(input("Nhập giảm giá: "))

    def xuat(self):
        print(f"Tên sản phẩm: {self.ten_sp}")
        print(f"Đơn giá: {self.gia}")
        print(f"Giảm giá: {self.giam_gia}")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau()}")




    