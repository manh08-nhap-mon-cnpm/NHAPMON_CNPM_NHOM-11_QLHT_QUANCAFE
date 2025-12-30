## HỆ THỐNG QUẢN LÝ QUÁN CAFE

Hệ thống quản lý quán cafe được xây dựng nhằm hỗ trợ chủ quán và nhân viên trong việc quản lý hoạt động kinh doanh hằng ngày một cách hiệu quả, chính xác và dễ sử dụng.  
Hệ thống giúp giảm thiểu sai sót trong quá trình phục vụ, quản lý dữ liệu tập trung và tiết kiệm thời gian vận hành.

---

## 1. Mô tả bài toán

Trong thực tế, nhiều quán cafe quy mô nhỏ và vừa vẫn quản lý thủ công các hoạt động như gọi món, thanh toán, quản lý bàn, nhân viên và doanh thu, dẫn đến dễ xảy ra sai sót và khó kiểm soát.

**Bài toán đặt ra** là xây dựng một hệ thống quản lý quán cafe đơn giản, dễ sử dụng, đáp ứng các chức năng cơ bản như:
- Đăng nhập và phân quyền người dùng
- Quản lý bàn, món ăn, danh mục
- Gọi món và thanh toán
- Xem doanh thu
- Hỗ trợ chủ quán và nhân viên vận hành hiệu quả

Hệ thống được xây dựng dưới dạng ứng dụng web sử dụng Flask (Python) chạy trên môi trường local.

---

## 2. Chức năng chính của hệ thống

- Đăng nhập hệ thống
- Phân quyền người dùng (Admin / Staff)
- Đổi mật khẩu
- Giao diện dashboard theo từng vai trò
- Quản lý dữ liệu quán cafe (mô phỏng)

---

## 3. Công nghệ sử dụng

- Ngôn ngữ lập trình: **Python**
- Framework: **Flask**
- Giao diện: **HTML, CSS, JavaScript**
- Quản lý mã nguồn: **GitHub**

---

## 4. Thành viên nhóm

| STT | Họ và tên | MSSV | Vai trò trong nhóm |
|:--:|:----------------|:--------:|:-------------------|
| 1 | Đường Minh Anh | 24S1020003 | Thành Viên |
| 2 | Nguyễn Anh Thư | 24S1020077 | Thành viên |
| 3 | Trần Phương Anh | 24S1020009 | Thành viên |
| 4 | Phạm Huy Khôi | 24S1020033 | Nhóm trưởng |

---

## 5. Hướng dẫn chạy hệ thống

### Bước 1: Clone project
git clone https://github.com/manh08-nhap-mon-cnpm/NHAPMON_CNPM_NHOM-11_QLHT_QUANCAFE.git
### Bước 2: Di chuyển vào thư mục web
cd NHAPMON_CNPM_NHOM-11_QLHT_QUANCAFE/
### Bước 3: Cài đặt thư viện cần thiết
pip install flask
### Bước 4: Chạy ứng dụng
python main.py
### Bước 5: Truy cập hệ thống
Mở trình duyệt và truy cập:
http://localhost:8000/index.html
### Bước 6: Tài khoản đăng nhập mẫu
#### Admin:
Tên đăng nhập: admin
Mật khẩu: 123
### Staff:
Tên đăng nhập: staff
Mật khẩu: 123
(Có thể thay đổi mật khẩu sau khi đăng nhập)
