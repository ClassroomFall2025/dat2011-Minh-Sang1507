class SinhvienPoly:
    def __init__(self, ho_ten, nganh_hoc):
        self.ho_ten = ho_ten.strip()
        self.nganh_hoc = nganh_hoc.strip()

    def get_diem(self):
        
        return 0.0

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem is None:
            return "Không xác định"
        if diem >= 9:
            return "Xuất sắc"
        elif diem >= 8:
            return "Giỏi"
        elif diem >= 7:
            return "Khá"
        elif diem >= 5:
            return "Trung bình"
        elif diem >= 0:
            return "Yếu"
        else:
            return "Không xác định"

    def __str__(self):
        diem = self.get_diem()
        diem_str = f"{diem:.2f}" if isinstance(diem, (int, float)) else "N/A"
        return f"{self.ho_ten:20s} | {self.nganh_hoc:6s} | {diem_str:6s} | {self.get_hoc_luc():12s}"

    def xuat(self):
        print(self.__str__())


class SinhvienIT(SinhvienPoly):
    def __init__(self, ho_ten, nganh_hoc, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, nganh_hoc)
        self.diem_java = float(diem_java)
        self.diem_html = float(diem_html)
        self.diem_css = float(diem_css)

    def get_diem(self):
        # (2*java + html + css)/4
        return (2 * self.diem_java + self.diem_html + self.diem_css) / 4.0


class SinhvienBiz(SinhvienPoly):
    def __init__(self, ho_ten, nganh_hoc, diem_marketing, diem_sales):
        super().__init__(ho_ten, nganh_hoc)
        self.diem_marketing = float(diem_marketing)
        self.diem_sales = float(diem_sales)

    def get_diem(self):
    
     return (2 * self.diem_marketing + self.diem_sales) / 3.0

