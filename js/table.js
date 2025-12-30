// Dữ liệu mẫu (Giả lập Database)
let tables = JSON.parse(localStorage.getItem('sb_tables')) || [
    { id: 1, name: "Bàn 01", status: "Trống" },
    { id: 2, name: "Bàn 02", status: "Có khách" },
    { id: 3, name: "Bàn 03", status: "Đang dọn" }
];

// Hàm thông báo Toast (Tái sử dụng)
function showToast(msg, type = 'success') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    const color = type === 'success' ? 'bg-[#007042]' : 'bg-red-600';
    toast.className = `${color} text-white px-8 py-4 rounded-2xl shadow-2xl mb-3 flex items-center gap-3 font-bold animate-in`;
    toast.innerHTML = `<i class="fa-solid fa-info-circle"></i> <span>${msg}</span>`;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

// UC05: Hiển thị danh sách bàn
function renderTables() {
    const grid = document.getElementById('table-grid');
    const user = JSON.parse(localStorage.getItem('sb_user'));
    
    grid.innerHTML = tables.map(t => {
        let statusColor = t.status === 'Trống' ? 'border-green-500' : (t.status === 'Có khách' ? 'border-red-500' : 'border-amber-500');
        let statusText = t.status === 'Trống' ? 'text-green-600' : (t.status === 'Có khách' ? 'text-red-600' : 'text-amber-600');
        
        return `
            <div class="table-card bg-white p-10 shadow-sm border-b-[10px] ${statusColor} text-center relative group">
                ${user.role === 'ADMIN' ? `
                    <button onclick="deleteTable(${t.id})" class="absolute top-4 right-4 text-gray-300 hover:text-red-500 opacity-0 group-hover:opacity-100 transition">
                        <i class="fa-solid fa-trash-can"></i>
                    </button>
                ` : ''}

                <div class="text-4xl font-black text-[#1e3932] mb-2">${t.name}</div>
                <div class="text-[10px] font-black uppercase tracking-widest ${statusText} mb-6 italic">${t.status}</div>
                
                <button onclick="changeStatus(${t.id})" class="w-full py-3 rounded-full bg-gray-100 text-[#1e3932] font-black text-[10px] hover:bg-[#007042] hover:text-white transition uppercase">
                    Đổi trạng thái
                </button>
            </div>
        `;
    }).join('');
}

// UC01: Tạo bàn mới
function submitCreateTable() {
    const name = document.getElementById('input-table-name').value.trim();
    if (!name) return showToast("Không được để trống tên bàn!", "error");
    if (tables.find(t => t.name === name)) return showToast("Tên bàn đã tồn tại!", "error");

    const newTable = {
        id: Date.now(),
        name: name,
        status: "Trống"
    };
    tables.push(newTable);
    saveData();
    closeModal();
    showToast(`Đã tạo ${name} thành công!`);
}

// UC04: Xóa bàn
function deleteTable(id) {
    const table = tables.find(t => t.id === id);
    if (table.status === 'Có khách') return showToast("Không thể xóa bàn đang có khách!", "error");
    
    if (confirm("Mày có chắc muốn xóa bàn này không?")) {
        tables = tables.filter(t => t.id !== id);
        saveData();
        showToast("Đã xóa bàn!");
    }
}

// UC06: Logic đổi trạng thái
function changeStatus(id) {
    const table = tables.find(t => t.id === id);
    const flow = { "Trống": "Có khách", "Có khách": "Đang dọn", "Đang dọn": "Trống" };
    table.status = flow[table.status];
    saveData();
}

// Lưu Database cục bộ
function saveData() {
    localStorage.setItem('sb_tables', JSON.stringify(tables));
    renderTables();
}

// UI Modals
function openModal() { document.getElementById('modal-add').classList.remove('hidden'); }
function closeModal() { document.getElementById('modal-add').classList.add('hidden'); }