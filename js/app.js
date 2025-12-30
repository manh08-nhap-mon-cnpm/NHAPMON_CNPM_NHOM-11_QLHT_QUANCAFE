// js/app.js

// --- 1. KHỞI TẠO DỮ LIỆU (MOCK DATABASE) ---

// Khởi tạo Bàn (UC05)
let tables = JSON.parse(localStorage.getItem('sb_tables')) || [
    { id: 1, name: "Bàn 01", status: "Trống" },
    { id: 2, name: "Bàn 02", status: "Có khách" },
    { id: 3, name: "Bàn 03", status: "Đang dọn" },
    { id: 4, name: "Bàn 04", status: "Trống" }
];

// Khởi tạo Menu (UC10 - UC13)
let menuItems = JSON.parse(localStorage.getItem('sb_menu')) || [
    { id: 101, name: "Caffe Latte", price: 55000, recipe: [{ ing: "Hạt Cafe", qty: 20 }, { ing: "Sữa tươi", qty: 150 }] },
    { id: 102, name: "Caramel Macchiato", price: 65000, recipe: [{ ing: "Hạt Cafe", qty: 20 }, { ing: "Caramel", qty: 30 }] },
    { id: 103, name: "Matcha Latte", price: 60000, recipe: [{ ing: "Bột Matcha", qty: 10 }, { ing: "Sữa tươi", qty: 200 }] }
];

// Khởi tạo Kho (UC21)
let inventory = JSON.parse(localStorage.getItem('sb_inventory')) || [
    { name: "Hạt Cafe", stock: 1000, unit: "g" },
    { name: "Sữa tươi", stock: 5000, unit: "ml" },
    { name: "Caramel", stock: 500, unit: "ml" },
    { name: "Bột Matcha", stock: 200, unit: "g" }
];

let currentCart = [];
let activeTableId = null;

// --- 2. QUẢN LÝ BÀN (PACKAGE 1) ---

function renderTables() {
    const grid = document.getElementById('grid-tables') || document.getElementById('table-grid');
    if (!grid) return;

    const userData = localStorage.getItem('sb_user');
    const user = userData ? JSON.parse(userData) : { role: 'STAFF' };

    grid.innerHTML = tables.map(t => {
        const statusClass = t.status === 'Trống' ? 'border-green-500' : (t.status === 'Có khách' ? 'border-red-500' : 'border-amber-500');
        const statusText = t.status === 'Trống' ? 'text-green-600' : (t.status === 'Có khách' ? 'text-red-600' : 'text-amber-600');
        
        return `
            <div class="table-card bg-white p-8 border-b-[10px] shadow-sm text-center relative group ${statusClass}">
                ${user.role === 'ADMIN' ? `<button onclick="deleteTable(${t.id})" class="absolute top-4 right-4 text-gray-300 hover:text-red-500 opacity-0 group-hover:opacity-100 transition"><i class="fa-solid fa-trash-can"></i></button>` : ''}
                <div class="text-4xl font-black text-[#1e3932] mb-2">${t.name}</div>
                <div class="text-[10px] font-black uppercase tracking-widest ${statusText} mb-6 italic">${t.status}</div>
                <button onclick="openPOS(${t.id})" class="w-full py-3 rounded-full bg-[#007042] text-white font-black text-[10px] hover:bg-[#1e3932] transition uppercase shadow-lg">
                    Phục vụ / POS
                </button>
            </div>
        `;
    }).join('');
}

function saveNewTable() {
    const input = document.getElementById('table-name-input');
    const name = input.value.trim();
    if (!name) return showToast("Nhập tên bàn đi m!");
    
    tables.push({ id: Date.now(), name: name, status: "Trống" });
    syncData('tables');
    input.value = "";
    closeAddModal();
    showToast("Thêm bàn thành công!", "success");
}

function deleteTable(id) {
    if (!confirm("Xóa bàn này hả m?")) return;
    tables = tables.filter(t => t.id !== id);
    syncData('tables');
    showToast("Đã xóa bàn.");
}

// --- 3. POS & THANH TOÁN (UC14 - UC19 + UC23) ---

function openPOS(id) {
    activeTableId = id;
    const table = tables.find(t => t.id === id);
    if (table.status === "Đang dọn") return showToast("Bàn đang dọn dẹp!", "error");

    document.getElementById('pos-table-title').innerText = table.name;
    document.getElementById('modal-pos').classList.remove('hidden');
    currentCart = []; 
    renderMenuPOS();
    renderCart();
}

function renderMenuPOS() {
    const grid = document.getElementById('menu-items');
    if (!grid) return;
    grid.innerHTML = menuItems.map(m => `
        <div onclick="addToCart(${m.id})" class="bg-white p-6 rounded-3xl border border-gray-100 hover:border-[#007042] cursor-pointer shadow-sm transition-all hover:scale-105">
            <div class="font-black text-[#1e3932]">${m.name}</div>
            <div class="text-[#007042] font-bold text-sm">${m.price.toLocaleString()}đ</div>
        </div>
    `).join('');
}

function addToCart(id) {
    const product = menuItems.find(m => m.id === id);
    const existing = currentCart.find(c => c.id === id);
    if (existing) {
        existing.qty++;
    } else {
        currentCart.push({ ...product, qty: 1 });
    }
    renderCart();
}

function renderCart() {
    const list = document.getElementById('cart-items');
    if (!list) return;
    list.innerHTML = currentCart.map(c => `
        <div class="flex justify-between items-center bg-white p-4 rounded-xl shadow-sm border border-gray-50">
            <div>
                <div class="font-bold text-sm text-[#1e3932]">${c.name}</div>
                <div class="text-[10px] text-gray-400 font-bold italic">Số lượng: ${c.qty}</div>
            </div>
            <div class="text-xs font-bold text-[#007042]">${(c.price * c.qty).toLocaleString()}đ</div>
        </div>
    `).join('');
    
    const total = currentCart.reduce((s, c) => s + (c.price * c.qty), 0);
    const totalDisplay = document.getElementById('total-price');
    if (totalDisplay) totalDisplay.innerText = total.toLocaleString() + 'đ';
}

function payBill() {
    if (currentCart.length === 0) return showToast("Chọn món đã m ơi!", "error");

    // UC23: Kiểm tra tồn kho trước khi trừ
    let canProcess = true;
    currentCart.forEach(item => {
        if (item.recipe) {
            item.recipe.forEach(r => {
                const stockItem = inventory.find(i => i.name === r.ing);
                if (!stockItem || stockItem.stock < (r.qty * item.qty)) {
                    showToast(`HẾT HÀNG: ${r.ing} không đủ để pha ${item.name}!`, "error");
                    canProcess = false;
                }
            });
        }
    });

    if (!canProcess) return;

    // UC23: Tiến hành trừ kho thiệt
    currentCart.forEach(item => {
        if (item.recipe) {
            item.recipe.forEach(r => {
                const stockItem = inventory.find(i => i.name === r.ing);
                stockItem.stock -= (r.qty * item.qty);
            });
        }
    });

    // UC06: Đổi trạng thái bàn
    const table = tables.find(t => t.id === activeTableId);
    table.status = "Trống";

    // UC19: Lưu hóa đơn (Giả lập) & Sync
    syncData('tables');
    syncData('inventory');
    
    closePOS();
    showToast("Thanh toán thành công! Điểm đã tích (UC28).", "success");
}

// --- 4. ĐỒNG BỘ & TIỆN ÍCH ---

function syncData(key) {
    if (key === 'tables') localStorage.setItem('sb_tables', JSON.stringify(tables));
    if (key === 'inventory') localStorage.setItem('sb_inventory', JSON.stringify(inventory));
    if (key === 'menu') localStorage.setItem('sb_menu', JSON.stringify(menuItems));
    renderTables();
}

function closePOS() { 
    document.getElementById('modal-pos').classList.add('hidden'); 
}

function openAddModal() { 
    document.getElementById('modal-add-table').classList.remove('hidden'); 
}

function closeAddModal() { 
    document.getElementById('modal-add-table').classList.add('hidden'); 
}

// Gọi render lần đầu khi load trang
if (document.getElementById('grid-tables') || document.getElementById('table-grid')) {
    renderTables();
}