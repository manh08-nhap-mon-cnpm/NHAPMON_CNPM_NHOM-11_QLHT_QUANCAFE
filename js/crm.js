// js/crm.js

// UC28: Tích điểm (Ví dụ: 10% giá trị hóa đơn)
function addPoints(customerPhone, billTotal) {
    let customers = JSON.parse(localStorage.getItem('sb_customers')) || [];
    let customer = customers.find(c => c.phone === customerPhone);
    
    if (customer) {
        let points = billTotal * 0.1;
        customer.points += points;
        
        // UC29: Phân hạng thành viên
        if (customer.points >= 1000) customer.rank = "GOLD";
        else if (customer.points >= 500) customer.rank = "SILVER";
        
        localStorage.setItem('sb_customers', JSON.stringify(customers));
        showToast(`Khách ${customer.name} được cộng ${points} điểm!`);
    }
}