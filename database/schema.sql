-- database/schema.sql
PRAGMA foreign_keys = ON;

-- 1. Bàn
CREATE TABLE IF NOT EXISTS tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    seats INTEGER NOT NULL CHECK(seats > 0),
    status TEXT DEFAULT 'trống' CHECK(status IN ('trống', 'đang dùng', 'đã đặt', 'đang dọn'))
);

-- 2. Danh mục
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- 3. Món ăn/uống
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL CHECK(price >= 0),
    category_id INTEGER,
    image_url TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- 4. Nguyên liệu
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    quantity REAL DEFAULT 0,
    unit TEXT NOT NULL  -- ví dụ: kg, lít, cái, gói
);

-- 5. Nhân viên
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('admin', 'quản lý', 'thu ngân', 'phục vụ')),
    phone TEXT,
    password_hash TEXT NOT NULL
);

-- 6. Tài khoản (liên kết với employees)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    employee_id INTEGER,
    role TEXT DEFAULT 'phục vụ',
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- 7. Hóa đơn
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_id INTEGER,
    employee_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'đang gọi' CHECK(status IN ('đang gọi', 'đã thanh toán', 'hủy')),
    total REAL DEFAULT 0,
    discount REAL DEFAULT 0,
    final_amount REAL DEFAULT 0,
    FOREIGN KEY (table_id) REFERENCES tables(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- 8. Chi tiết hóa đơn
CREATE TABLE IF NOT EXISTS bill_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1 CHECK(quantity > 0),
    price_at_time REAL NOT NULL,
    FOREIGN KEY (bill_id) REFERENCES bills(id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES menu_items(id)
);

-- 9. Phiếu nhập hàng
CREATE TABLE IF NOT EXISTS import_forms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier TEXT,
    employee_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount REAL DEFAULT 0,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- 10. Chi tiết nhập hàng
CREATE TABLE IF NOT EXISTS import_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    form_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (form_id) REFERENCES import_forms(id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);

-- Dữ liệu mẫu (chạy lần đầu)
INSERT OR IGNORE INTO categories (name) VALUES ('Cà phê'), ('Trà sữa'), ('Nước ép'), ('Topping'), ('Khác');

INSERT OR IGNORE INTO tables (name, seats) VALUES 
('Bàn 01', 4), ('Bàn 02', 4), ('Bàn 03', 6), ('Bàn 04', 2), ('Bàn VIP', 10);

INSERT OR IGNORE INTO employees (name, role, phone, password_hash) VALUES 
('Admin', 'admin', '0901234567', 'hashed_password_here');  -- sẽ thay bằng bcrypt sau

INSERT OR IGNORE INTO users (username, password_hash, role) VALUES 
('admin', 'hashed_password', 'admin');
