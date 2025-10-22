class SinhVienPoly:
    def __init__(self, ho_ten, nganh_hoc):
        self.ho_ten = ho_ten.strip()
        self.nganh_hoc = nganh_hoc.strip()

    def get_diem(self):
        # Phương thức trừu tượng, sẽ được ghi đè ở lớp con
        return 0.0

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 6.5:
            return "Trung bình"
        elif diem < 7.5:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngành học: {self.nganh_hoc}")
        print(f"Điểm: {self.get_diem():.2f}")
        print(f"Học lực: {self.get_hoc_luc()}")

    def __str__(self):
        return f"{self.ho_ten} | {self.nganh_hoc} | {self.get_diem():.2f} | {self.get_hoc_luc()}"
class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, "IT")
        self.diem_java = float(diem_java)
        self.diem_html = float(diem_html)
        self.diem_css = float(diem_css)

    def get_diem(self):
        return (2 * self.diem_java + self.diem_html + self.diem_css) / 4
class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, diem_marketing, diem_sales):
        super().__init__(ho_ten, "Biz")
        self.diem_marketing = float(diem_marketing)
        self.diem_sales = float(diem_sales)

    def get_diem(self):
        return (2 * self.diem_marketing + self.diem_sales) / 3










