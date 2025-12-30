// js/pos.js

let currentBill = [];

// UC14: Thêm món vào hóa đơn
function addToBill(productName, price) {
    const item = currentBill.find(i => i.name === productName);
    if (item) {
        item.qty++;
    } else {
        currentBill.push({ name: productName, price: price, qty: 1 });
    }
    renderBill();
}

// UC18 & UC19: Tính tiền & Thanh toán
function checkout(discountPercent = 0) {
    let total = currentBill.reduce((sum, item) => sum + (item.price * item.qty), 0);
    let finalAmount = total * (1 - discountPercent / 100);

    // Thực hiện trừ kho tự động (UC23)
    currentBill.forEach(item => {
        autoDeductStock(item.name, item.qty);
    });

    showToast(`Thanh toán thành công: ${finalAmount.toLocaleString()} VNĐ`, "success");
    currentBill = []; // Reset bill
    renderBill();
}