// js/auth.js

// 1. Hàm Toast (Hiện thông báo lỗi/thành công)
function showToast(message, type = 'error') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const toast = document.createElement('div');
    const bg = type === 'success' ? 'bg-[#007042]' : 'bg-red-600';
    toast.className = `${bg} text-white px-8 py-4 rounded-2xl shadow-2xl flex items-center gap-4 font-bold text-sm border border-white/20 mb-3 transition-all duration-300`;
    toast.innerHTML = `<i class="fa-solid ${type === 'success' ? 'fa-check-double' : 'fa-circle-exclamation'}"></i> <span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => { toast.remove(); }, 3000);
}

// 2. Hàm Login (UC37 & UC36)
function handleLogin() {
    const userField = document.getElementById('u');
    const passField = document.getElementById('p');
    
    const user = userField.value.trim().toLowerCase();
    const pass = passField.value.trim();

    if (!user || !pass) {
        showToast("Vui lòng điền đủ Partner ID và mật khẩu!");
        return;
    }

    // Kiểm tra tài khoản bị khóa (UC47)
    if (localStorage.getItem(`locked_${user}`)) {
        showToast("Tài khoản bị khóa. Liên hệ Admin!", "error");
        return;
    }

    // Logic kiểm tra tài khoản
    let role = "";
    if (user === 'admin' && pass === '123') role = "ADMIN";
    else if (user === 'staff' && pass === '123') role = "STAFF";

    if (role) {
        // Lưu session (UC36)
        localStorage.setItem('sb_user', JSON.stringify({
            name: user,
            role: role,
            time: new Date().toLocaleTimeString()
        }));
        localStorage.setItem(`attempts_${user}`, 0); // Reset số lần sai

        showToast("Đăng nhập thành công!", "success");

        // Nhảy trang dựa trên quyền (Tách biệt Dashboard)
        setTimeout(() => {
            if (role === "ADMIN") window.location.href = "admin-dashboard.html";
            else window.location.href = "staff-dashboard.html";
        }, 1000);
    } else {
        // Xử lý đếm sai (UC47)
        let attempts = parseInt(localStorage.getItem(`attempts_${user}`)) || 0;
        attempts++;
        localStorage.setItem(`attempts_${user}`, attempts);
        
        if (attempts >= 3) {
            localStorage.setItem(`locked_${user}`, true);
            showToast("Sai 3 lần. TÀI KHOẢN ĐÃ BỊ KHÓA!", "error");
        } else {
            showToast(`Sai mật khẩu! Còn ${3 - attempts} lần thử`, "error");
        }
    }
}