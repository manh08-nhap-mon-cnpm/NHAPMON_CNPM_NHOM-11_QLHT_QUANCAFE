# ----- TABLES -----
try:
    from src.tables.list_tables import list_tables
    from src.tables.create_table import create_table
    from src.tables.update_table import update_table
    from src.tables.delete_table import delete_table
    from src.tables.update_table_status import update_table_status
except Exception as e:
    # Nếu import lỗi, tạo hàm thay thế để chương trình không crash hoàn toàn
    def _not_impl(*args, **kwargs):
        print("⚠️  Module bàn chưa cài đặt hoặc import thất bại.")
    list_tables = _not_impl
    create_table = _not_impl
    update_table = _not_impl
    delete_table = _not_impl
    update_table_status = _not_impl

# ----- MENU -----
try:
    from src.menu.add_item import add_item
    from src.menu.update_item import update_item
    from src.menu.delete_item import delete_item
    from src.menu.list_items import list_items
except Exception:
    def _not_impl(*args, **kwargs):
        print("⚠️  Module món (menu) chưa cài đặt hoặc import thất bại.")
    add_item = _not_impl
    update_item = _not_impl
    delete_item = _not_impl
    list_items = _not_impl

# ----- AUTH -----
try:
    from src.auth.login import login
    from src.auth.change_password import change_password
    from src.auth.assign_role import assign_role
except Exception:
    def _not_impl(*args, **kwargs):
        print("⚠️  Module auth chưa cài đặt hoặc import thất bại.")
    login = _not_impl
    change_password = _not_impl
    assign_role = _not_impl


# ---------------- Helpers ----------------
def input_int(prompt, allow_empty=False):
    """
    Nhận một số nguyên từ input.
    Nếu allow_empty True và user enter rỗng -> trả về None.
    Lặp lại yêu cầu nếu input không phải số nguyên.
    """
    while True:
        s = input(prompt).strip()
        if s == "" and allow_empty:
            return None
        try:
            return int(s)
        except ValueError:
            print("❌ Vui lòng nhập một số nguyên hợp lệ (hoặc enter để bỏ qua).")


def input_str(prompt, allow_empty=False):
    s = input(prompt).strip()
    if s == "" and allow_empty:
        return None
    return s
    """Nhận chuỗi; trả về None nếu rỗng và allow_empty True."""
    s = input(prompt).strip()
    if s == "" and allow_empty:
        return None
    return s


def safe_call(fn, *args, **kwargs):
    """
    Gọi hàm của các module bên ngoài với try/except để tránh crash chương trình.
    In lỗi nếu có.
    """
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        print(f"❌ Lỗi khi thực hiện thao tác: {e!s}")


# ---------------- MENU TABLES ----------------
def menu_tables():
    while True:
        print("\n=== QUẢN LÝ BÀN ===")
        print("1. Xem danh sách bàn")
        print("2. Tạo bàn mới")
        print("3. Cập nhật thông tin bàn")
        print("4. Xóa bàn")
        print("5. Cập nhật trạng thái bàn")
        print("0. Quay lại")
        ch = input("Chọn: ").strip()

        if ch == "1":
            safe_call(list_tables)

        elif ch == "2":
            name = input_str("Tên bàn: ")
            if not name:
                print("❌ Tên bàn không được rỗng.")
                continue
            seats = input_int("Số ghế: ")
            if seats is None or seats <= 0:
                print("❌ Số ghế phải là số nguyên dương.")
                continue
            safe_call(create_table, name, seats)

        elif ch == "3":
            tid = input_int("ID bàn: ")
            if tid is None:
                print("❌ ID bàn là bắt buộc.")
                continue
            name = input_str("Tên mới (enter bỏ qua): ", allow_empty=True)
            seats = input_int("Số ghế mới (enter bỏ qua): ", allow_empty=True)
            # Nếu seats là None -> truyền None; nếu có thì kiểm tra dương
            if seats is not None and seats <= 0:
                print("❌ Số ghế phải là số nguyên dương.")
                continue
            safe_call(update_table, tid, name, seats)

        elif ch == "4":
            tid = input_int("ID bàn cần xóa: ")
            if tid is None:
                print("❌ ID bàn là bắt buộc.")
                continue
            confirm = input_str(f"Bạn có chắc muốn xóa bàn {tid}? (y/n): ").lower()
            if confirm == "y":
                safe_call(delete_table, tid)
            else:
                print("Hủy xóa.")

        elif ch == "5":
            tid = input_int("ID bàn: ")
            if tid is None:
                print("❌ ID bàn là bắt buộc.")
                continue
            status = input_str("Trạng thái mới (ví dụ: free/occupied/reserved): ")
            if not status:
                print("❌ Trạng thái không được rỗng.")
                continue
            safe_call(update_table_status, tid, status)

        elif ch == "0":
            break

        else:
            print("Sai lựa chọn. Vui lòng nhập lại.")


# ---------------- MENU MENU (MÓN) ----------------
def menu_menu():
    while True:
        print("\n=== QUẢN LÝ MÓN ===")
        print("1. Danh sách món")
        print("2. Thêm món")
        print("3. Cập nhật món")
        print("4. Xóa món")
        print("0. Quay lại")
        ch = input("Chọn: ").strip()

        if ch == "1":
            safe_call(list_items)

        elif ch == "2":
            name = input_str("Tên món: ")
            if not name:
                print("❌ Tên món không được rỗng.")
                continue
            # Giá có thể là int hoặc float, chấp nhận số thực
            price_raw = input_str("Giá: ")
            try:
                price = float(price_raw)
                if price < 0:
                    raise ValueError
            except Exception:
                print("❌ Giá phải là một số không âm.")
                continue
            category = input_int("ID danh mục: ")
            if category is None:
                print("❌ ID danh mục là bắt buộc.")
                continue
            safe_call(add_item, name, price, category)

        elif ch == "3":
            mid = input_int("ID món: ")
            if mid is None:
                print("❌ ID món là bắt buộc.")
                continue
            name = input_str("Tên mới (enter bỏ qua): ", allow_empty=True)
            price_raw = input_str("Giá mới (enter bỏ qua): ", allow_empty=True)
            price = None
            if price_raw is not None:
                try:
                    price = float(price_raw)
                    if price < 0:
                        raise ValueError
                except Exception:
                    print("❌ Giá phải là một số không âm.")
                    continue
            cate = input_int("Danh mục mới (enter bỏ qua): ", allow_empty=True)
            safe_call(update_item, mid, name, price, cate)

        elif ch == "4":
            mid = input_int("ID món cần xóa: ")
            if mid is None:
                print("❌ ID món là bắt buộc.")
                continue
            confirm = input_str(f"Bạn có chắc muốn xóa món {mid}? (y/n): ").lower()
            if confirm == "y":
                safe_call(delete_item, mid)
            else:
                print("Hủy xóa.")

        elif ch == "0":
            break

        else:
            print("Sai lựa chọn. Vui lòng nhập lại.")


# ---------------- MENU AUTH ----------------
def menu_auth():
    while True:
        print("\n=== QUẢN LÝ TÀI KHOẢN ===")
        print("1. Đăng nhập")
        print("2. Đổi mật khẩu")
        print("3. Gán quyền")
        print("0. Quay lại")
        ch = input("Chọn: ").strip()

        if ch == "1":
            u = input_str("Username: ")
            p = input_str("Password: ")
            if not u or not p:
                print("❌ Username và Password không được rỗng.")
                continue
            safe_call(login, u, p)

        elif ch == "2":
            uid = input_int("User ID: ")
            if uid is None:
                print("❌ User ID là bắt buộc.")
                continue
            old = input_str("Mật khẩu cũ: ")
            new = input_str("Mật khẩu mới: ")
            if not old or not new:
                print("❌ Cả mật khẩu cũ và mới đều phải nhập.")
                continue
            safe_call(change_password, uid, old, new)

        elif ch == "3":
            uid = input_int("User ID: ")
            if uid is None:
                print("❌ User ID là bắt buộc.")
                continue
            role = input_str("Quyền: ")
            if not role:
                print("❌ Quyền không được rỗng.")
                continue
            safe_call(assign_role, uid, role)

        elif ch == "0":
            break

        else:
            print("Sai lựa chọn. Vui lòng nhập lại.")


# ---------------- MAIN ----------------
def main():
    while True:
        print("\n===== MENU CHÍNH =====")
        print("1. Quản lý bàn")
        print("2. Quản lý món")
        print("3. Tài khoản / phân quyền")
        print("0. Thoát")

        ch = input("Chọn chức năng: ").strip()

        if ch == "1":
            menu_tables()
        elif ch == "2":
            menu_menu()
        elif ch == "3":
            menu_auth()
        elif ch == "0":
            print("Thoát.")
            break
        else:
            print("Sai lựa chọn. Vui lòng nhập lại.")


if __name__ == "__main__":
    main()
