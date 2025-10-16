class SanPham:
    def __init__(self, ten_san_pham, don_gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.don_gia = don_gia
        self.giam_gia = giam_gia

    def tinh_thue_nhap_khau(self):
        return self.don_gia * 0.1

    def hien_thi_thong_tin(self):
        print(f"Tên sản phẩm: {self.ten_san_pham}")
        print(f"Đơn giá: {self.don_gia}")
        print(f"Giảm giá: {self.giam_gia}")
        print(f"Thuế nhập khẩu: {self.tinh_thue_nhap_khau()}")
