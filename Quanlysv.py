
from SinhvienPoly import SinhVienIT, SinhVienBiz, SinhVienPoly
class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def __nhap_float(self, message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

    def nhap_danh_sach_sv(self):
        while True:
            ho_ten = input("Nhập họ tên sinh viên (hoặc Enter để dừng): ").strip()
            if ho_ten == "":
                break

            nganh = input("Ngành học (IT/Biz): ").strip().lower()
            if nganh == "it":
                java = self.__nhap_float("Điểm Java: ")
                html = self.__nhap_float("Điểm HTML: ")
                css = self.__nhap_float("Điểm CSS: ")
                sv = SinhVienIT(ho_ten, java, html, css)
            elif nganh == "biz":
                marketing = self.__nhap_float("Điểm Marketing: ")
                sales = self.__nhap_float("Điểm Sales: ")
                sv = SinhVienBiz(ho_ten, marketing, sales)
            else:
                print("Ngành không hợp lệ!")
                continue

            self.dssv.append(sv)

    def xuat_danh_sach_sv(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng.")
        else:
            print("\n--- Danh sách sinh viên ---")
            for sv in self.dssv:
                sv.xuat()

    def xuat_sv_gioi(self):
        print("\n--- Sinh viên giỏi ---")
        ds_gioi = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
        if not ds_gioi:
            print("Không có sinh viên giỏi.")
        else:
            for sv in ds_gioi:
                sv.xuat()

    def sap_xep_theo_diem(self):
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print("Đã sắp xếp danh sách theo điểm giảm dần.")
        self.xuat_danh_sach_sv()
        def them_sinh_vien(self):
         ho_ten = input("Nhập họ tên: ")
        diem = float(input("Nhập điểm: "))



    







