# ASSIGNMENT DAT201 - LẬP TRÌNH PYTHON
# GIAI ĐOẠN 1: THIẾT KẾ MENU VÀ KHUNG SƯỜN HÀM

def nhap_danh_sach_nhan_vien():
    """Y1: Nhập danh sách nhân viên từ bàn phím. (Chưa lưu file)"""
    print(">>> CHỨC NĂNG: Nhập danh sách nhân viên từ bàn phím.")

def xuat_danh_sach_nhan_vien():
    """Y2: Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình."""
    print(">>> CHỨC NĂNG: Đọc thông tin nhân viên từ file và xuất danh sách.")

def tim_nhan_vien_theo_ma():
    """Y3: Tìm và hiển thị nhân viên theo mã nhập từ bàn phím."""
    print(">>> CHỨC NĂNG: Tìm và hiển thị nhân viên theo mã.")

def xoa_nhan_vien_theo_ma():
    """Y4: Xóa nhân viên theo mã nhập từ bàn phím. (Chưa cập nhật file)"""
    print(">>> CHỨC NĂNG: Xóa nhân viên theo mã.")

def cap_nhat_nhan_vien_theo_ma():
    """Y5: Cập nhật thông tin nhân viên theo mã. (Chưa ghi thay đổi vào file)"""
    print(">>> CHỨC NĂNG: Cập nhật thông tin nhân viên theo mã.")

def tim_nhan_vien_theo_khoang_luong():
    """Y6: Tìm các nhân viên theo khoảng lương nhập từ bàn phím."""
    print(">>> CHỨC NĂNG: Tìm nhân viên theo khoảng lương.")

def sap_xep_theo_ho_ten():
    """Y7: Sắp xếp nhân viên theo họ và tên."""
    print(">>> CHỨC NĂNG: Sắp xếp nhân viên theo họ và tên.")

def sap_xep_theo_thu_nhap():
    """Y8: Sắp xếp nhân viên theo thu nhập."""
    print(">>> CHỨC NĂNG: Sắp xếp nhân viên theo thu nhập.")

def xuat_top_5_thu_nhap():
    """Y9: Xuất 5 nhân viên có thu nhập cao nhất."""
    print(">>> CHỨC NĂNG: Xuất 5 nhân viên có thu nhập cao nhất.")
    
def main_menu():
    """Hệ thống menu chính."""
    while True:
        print("\n\n=============== CHƯƠNG TRÌNH QUẢN LÝ NHÂN SỰ RỒNG VIỆT ===============")
        print("1. Nhập danh sách nhân viên")
        print("2. Xuất danh sách nhân viên")
        print("3. Tìm nhân viên theo mã")
        print("4. Xóa nhân viên theo mã")
        print("5. Cập nhật thông tin nhân viên theo mã")
        print("6. Tìm nhân viên theo khoảng lương")
        print("7. Sắp xếp nhân viên theo họ tên")
        print("8. Sắp xếp nhân viên theo thu nhập")
        print("9. Xuất 5 nhân viên có thu nhập cao nhất")
        print("0. Thoát chương trình")
        print("=======================================================================")
        
        chon = input("Vui lòng chọn chức năng (0-9): ").strip()
        
        if chon == '1':
            nhap_danh_sach_nhan_vien()
        elif chon == '2':
            xuat_danh_sach_nhan_vien()
        elif chon == '3':
            tim_nhan_vien_theo_ma()
        elif chon == '4':
            xoa_nhan_vien_theo_ma()
        elif chon == '5':
            cap_nhat_nhan_vien_theo_ma()
        elif chon == '6':
            tim_nhan_vien_theo_khoang_luong()
        elif chon == '7':
            sap_xep_theo_ho_ten()
        elif chon == '8':
            sap_xep_theo_thu_nhap()
        elif chon == '9':
            xuat_top_5_thu_nhap()
        elif chon == '0':
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

# Chạy thử Giai đoạn 1
# if __name__ == "__main__":
#     main_menu()