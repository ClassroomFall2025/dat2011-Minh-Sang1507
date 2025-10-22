
from SinhvienPoly import SinhvienIT, SinhvienBiz, SinhvienPoly

class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def nhap_danh_sach_sinh_vien(self):
        print("\n--- Nhập danh sách sinh viên ---")
        while True:
            hoten = input("Nhập họ tên sinh viên (nhấn Enter để dừng): ").strip()
            if hoten == "":
                print("Kết thúc nhập danh sách.")
                break

            nganh = input("Nhập ngành học (IT/BIZ): ").strip().lower()
            if "it" in nganh:
                diem_java = self._nhap_float("Nhập điểm Java: ")
                diem_html = self._nhap_float("Nhập điểm HTML: ")
                diem_css = self._nhap_float("Nhập điểm CSS: ")
                sv = SinhvienIT(hoten, "IT", diem_java, diem_html, diem_css)
                self.dssv.append(sv)
                print(f"Đã thêm: {hoten} - IT")

            elif "biz" in nganh or "marketing" in nganh or "sale" in nganh:
                diem_marketing = self._nhap_float("Nhập điểm Marketing: ")
                diem_sales = self._nhap_float("Nhập điểm Sales: ")
                sv = SinhvienBiz(hoten, "BIZ", diem_marketing, diem_sales)
                self.dssv.append(sv)
                print(f"Đã thêm: {hoten} - BIZ")

            else:
                print("Ngành không hợp lệ. Vui lòng nhập lại (IT hoặc BIZ).")

    def _nhap_float(self, thong_bao):
        while True:
            try:
                val = float(input(thong_bao))
                if 0 <= val <= 10:
                    return val
                else:
                    print("Điểm phải trong khoảng 0 đến 10.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

    def xuat_danh_sach_sinh_vien(self):
        print("\n--- Danh sách sinh viên ---")
        if not self.dssv:
            print("Danh sách sinh viên rỗng.")
            return
        print(f"{'Họ tên':20s} | {'Ngành':6s} | {'Điểm':6s} | {'Học lực':12s}")
        print("-" * 54)
        for sv in self.dssv:
            sv.xuat()

    def xuat_danh_sach_sinh_vien_gioi(self):
        print("\n--- Danh sách sinh viên có học lực GIỎI hoặc XUẤT SẮC ---")
        ds_gioi = [sv for sv in self.dssv if sv.get_hoc_luc() in ["Giỏi", "Xuất sắc"]]
        if not ds_gioi:
            print("Không có sinh viên giỏi.")
            return
        print(f"{'Họ tên':20s} | {'Ngành':6s} | {'Điểm':6s} | {'Học lực':12s}")
        print("-" * 54)
        for sv in ds_gioi:
            sv.xuat()

    def sap_xep_dssv(self):
        print("\n--- Sắp xếp danh sách sinh viên theo điểm giảm dần ---")
        if not self.dssv:
            print("Danh sách sinh viên rỗng.")
            return
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print("Đã sắp xếp xong.")
        self.xuat_danh_sach_sinh_vien()
