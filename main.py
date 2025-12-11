# main.py

# 1. Nhập (Import) các hàm từ các file của bạn
# Giả sử cấu trúc thư mục của bạn là:
# /project_root
#   |-- main.py
#   |-- src
#       |-- tables
#           |-- create_table.py
#           |-- update_table.py
#           |-- delete_table.py
#           |-- list_tables.py
#           |-- update_table_status.py

from src.tables.create_table import create_table
from src.tables.update_table import update_table
from src.tables.delete_table import delete_table
from src.tables.list_tables import list_tables
from src.tables.update_table_status import update_table_status


# 2. Sử dụng khối 'if __name__ == "__main__":' để chạy code test

if __name__ == "__main__":
    print("====================================")
    print("🚀 BẮT ĐẦU KIỂM TRA TÍNH NĂNG QUẢN LÝ BÀN")
    print("====================================\n")

    # --- 1. TB04 – Xem danh sách bàn (List Tables) ---
    print("--- CHẠY TEST: TB04 – Xem danh sách bàn ---")
    list_tables()
    print("------------------------------------\n")


    # --- 2. TB01 – Tạo bàn mới (Create Table) ---
    print("--- CHẠY TEST: TB01 – Tạo bàn mới ---")
    create_table("A01", 4)
    create_table("B05", 8)
    # Lưu ý: Trong thực tế, hàm này sẽ trả về ID bàn vừa tạo
    print("------------------------------------\n")


    # Giả sử chúng ta có một ID bàn để thử nghiệm các chức năng khác
    TEST_TABLE_ID = 123


    # --- 3. TB05 – Cập nhật trạng thái bàn (Update Table Status) ---
    print(f"--- CHẠY TEST: TB05 – Cập nhật trạng thái bàn cho ID {TEST_TABLE_ID} ---")
    # Trạng thái có thể là: 'Trống', 'Đang dùng', 'Đã đặt'
    update_table_status(TEST_TABLE_ID, "Đang dùng")
    print("------------------------------------\n")


    # --- 4. TB02 – Cập nhật thông tin bàn (Update Table Info) ---
    print(f"--- CHẠY TEST: TB02 – Cập nhật thông tin bàn cho ID {TEST_TABLE_ID} ---")
    update_table(TEST_TABLE_ID, name="VIP-01", seats=10) # Đổi tên và số ghế
    print("------------------------------------\n")


    # --- 5. TB03 – Xóa bàn (Delete Table) ---
    print(f"--- CHẠY TEST: TB03 – Xóa bàn ID {TEST_TABLE_ID} ---")
    delete_table(TEST_TABLE_ID)
    print("------------------------------------\n")


    print("====================================")
    print("✅ HOÀN TẤT KIỂM TRA CÁC TÍNH NĂNG")
    print("====================================")
