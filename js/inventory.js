// js/inventory.js

// UC24: Công thức (Recipe) - Món -> Nguyên liệu
const recipes = {
    "Caffe Latte": [
        { ingredient: "Hạt Cafe", amount: 20 }, 
        { ingredient: "Sữa tươi", amount: 150 }
    ],
    "Caramel Macchiato": [
        { ingredient: "Hạt Cafe", amount: 20 },
        { ingredient: "Caramel", amount: 30 }
    ],
    "Matcha Latte": [
        { ingredient: "Bột Matcha", amount: 10 },
        { ingredient: "Sữa tươi", amount: 200 }
    ]
};

// Khởi tạo dữ liệu kho (UC21)
let inventory = JSON.parse(localStorage.getItem('sb_inventory')) || [
    { name: "Hạt Cafe", stock: 1000, unit: "g" },
    { name: "Sữa tươi", stock: 5000, unit: "ml" },
    { name: "Caramel", stock: 500, unit: "ml" },
    { name: "Bột Matcha", stock: 200, unit: "g" }
];

// 1. Hàm hiển thị bảng kho hàng (Dùng cho trang inventory.html)
function renderInventoryTable() {
    const tbody = document.getElementById('inventory-table');
    if (!tbody) return;

    tbody.innerHTML = inventory.map(item => `
        <tr class="border-b border-gray-50 hover:bg-gray-50 transition">
            <td class="p-6 font-bold text-gray-700">${item.name}</td>
            <td class="p-6 font-black ${item.stock < 100 ? 'text-red-500' : 'text-[#007042]'}">${item.stock}</td>
            <td class="p-6 text-gray-400 font-bold text-xs uppercase">${item.unit}</td>
            <td class="p-6">
                <span class="px-4 py-1 rounded-full text-[10px] font-black uppercase ${item.stock > 100 ? 'bg-green-100 text-green-600' : 'bg-red-100 text-red-600'}">
                    ${item.stock > 100 ? 'Ổn định' : 'Sắp hết'}
                </span>
            </td>
            <td class="p-6">
                <button onclick="importStock('${item.name}')" class="text-[#007042] hover:underline font-bold text-xs">Nhập thêm</button>
            </td>
        </tr>
    `).join('');
}

// UC22: Nhập thêm hàng thủ công
function importStock(name) {
    const amount = prompt(`Nhập số lượng ${name} muốn thêm:`);
    if (amount && !isNaN(amount)) {
        const item = inventory.find(i => i.name === name);
        item.stock += parseInt(amount);
        saveInventory();
        renderInventoryTable();
        showToast(`Đã nhập thêm ${amount} ${item.unit} ${name}`, "success");
    }
}

// UC23: Trừ kho tự động khi thanh toán
function autoDeductStock(itemName, quantity) {
    const recipe = recipes[itemName];
    if (!recipe) return true; // Không có công thức thì bỏ qua

    let canDeduct = true;
    
    // Kiểm tra xem đủ hàng không
    recipe.forEach(r => {
        const invItem = inventory.find(i => i.name === r.ingredient);
        if (!invItem || invItem.stock < (r.amount * quantity)) {
            canDeduct = false;
        }
    });

    if (!canDeduct) {
        showToast(`Không đủ nguyên liệu để pha ${itemName}!`, "error");
        return false;
    }

    // Tiến hành trừ
    recipe.forEach(r => {
        const invItem = inventory.find(i => i.name === r.ingredient);
        invItem.stock -= (r.amount * quantity);
    });

    saveInventory();
    return true;
}

function saveInventory() {
    localStorage.setItem('sb_inventory', JSON.stringify(inventory));
}

// Hàm quay về đúng Dashboard dựa trên quyền (Sửa lỗi nhảy dashboard cũ)
function goToDashboard() {
    const user = JSON.parse(localStorage.getItem('sb_user'));
    if (user && user.role === 'ADMIN') {
        window.location.href = 'admin-dashboard.html';
    } else {
        window.location.href = 'staff-dashboard.html';
    }
}

// Khởi tạo khi load trang
if (document.getElementById('inventory-table')) {
    renderInventoryTable();
}