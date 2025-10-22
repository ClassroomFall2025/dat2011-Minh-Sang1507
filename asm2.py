import json
from functools import cmp_to_key

# Cấu hình file
FILE_NAME = "nhan_vien_data.json"

# --- LỚP CƠ SỞ ---
class NhanVien:
    """Lớp cơ sở mô tả Nhân viên Hành chính."""
    def __init__(self, ma, ho_ten, luong):
        self.ma = ma
        self.ho_ten = ho_ten
        self.luong = luong
        self.chuc_vu = "Hành chính"

    def get_thu_nhap(self):
        """Thu nhập được tính bằng tổng các khoản thu (Lương tháng đối với NV Hành chính)[cite: 37]."""
        return self.luong

    def get_thue_thu_nhap(self):
        """Tính thuế thu nhập theo phương pháp lũy tiến[cite: 38]."""
        thu_nhap = self.get_thu_nhap()
        if thu_nhap < 9000000:
            return 0  # Dưới 9 triệu: không đóng thuế [cite: 40]
        elif 9000000 <= thu_nhap <= 15000000:
            return thu_nhap * 0.10  # Từ 9-15 triệu: đóng 10% [cite: 42]
        else: # thu_nhap > 15000000
            return thu_nhap * 0.12  # Trên 15 triệu: đóng 12% [cite: 44]

    def xuat_thong_tin(self):
        """Xuất thông tin cơ bản của nhân viên."""
        thu_nhap = self.get_thu_nhap()
        thue = self.get_thue_thu_nhap()
        print(f"| Mã: {self.ma:<4} | Họ tên: {self.ho_ten:<20} | Chức vụ: {self.chuc_vu:<15} |")
        print(f"| Lương Cố định: {self.luong:,.0f} VND")
        print(f"| THU NHẬP: {thu_nhap:,.0f} VND | THUẾ: {thue:,.0f} VND |")
        
    def to_dict(self):
        """Chuyển đối tượng thành dictionary để lưu vào JSON."""
        return {
            "ma": self.ma,
            "ho_ten": self.ho_ten,
            "luong": self.luong,
            "chuc_vu": self.chuc_vu
        }

# --- LỚP CON 1: NHÂN VIÊN TIẾP THỊ ---
class TiepThi(NhanVien):
    """Lớp mô tả Nhân viên Tiếp thị (có thêm doanh số và hoa hồng)[cite: 34]."""
    def __init__(self, ma, ho_ten, luong, doanh_so, ti_le_hoa_hong):
        super().__init__(ma, ho_ten, luong) # luong là lương cố định tháng [cite: 25]
        self.doanh_so = doanh_so
        self.ti_le_hoa_hong = ti_le_hoa_hong
        self.chuc_vu = "Tiếp thị"
        
    # Ghi đè phương thức getThuNhap() [cite: 70]
    def get_thu_nhap(self):
        """Thu nhập = Lương cố định + Hoa hồng (doanh số * tỉ lệ)[cite: 25]."""
        hoa_hong = self.doanh_so * self.ti_le_hoa_hong
        return self.luong + hoa_hong

    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        hoa_hong = self.doanh_so * self.ti_le_hoa_hong
        print(f"| Doanh số: {self.doanh_so:,.0f} | Tỉ lệ HH: {self.ti_le_hoa_hong*100}% | Hoa hồng: {hoa_hong:,.0f} VND |")
        
    def to_dict(self):
        # Mở rộng dictionary từ lớp cha
        data = super().to_dict()
        data.update({
            "doanh_so": self.doanh_so,
            "ti_le_hoa_hong": self.ti_le_hoa_hong
        })
        return data

# --- LỚP CON 2: TRƯỞNG PHÒNG ---
class TruongPhong(NhanVien):
    """Lớp mô tả Trưởng phòng (có thêm lương trách nhiệm)[cite: 35]."""
    def __init__(self, ma, ho_ten, luong, luong_trach_nhiem):
        super().__init__(ma, ho_ten, luong) # luong là lương tháng cố định [cite: 25]
        self.luong_trach_nhiem = luong_trach_nhiem
        self.chuc_vu = "Trưởng phòng"
        
    # Ghi đè phương thức getThuNhap() [cite: 70]
    def get_thu_nhap(self):
        """Thu nhập = Lương tháng + Lương trách nhiệm[cite: 25]."""
        return self.luong + self.luong_trach_nhiem
    
    def xuat_thong_tin(self):
        super().xuat_thong_tin()
        print(f"| Lương Trách nhiệm: {self.luong_trach_nhiem:,.0f} VND |")
        
    def to_dict(self):
        # Mở rộng dictionary từ lớp cha
        data = super().to_dict()
        data.update({
            "luong_trach_nhiem": self.luong_trach_nhiem
        })
        return data