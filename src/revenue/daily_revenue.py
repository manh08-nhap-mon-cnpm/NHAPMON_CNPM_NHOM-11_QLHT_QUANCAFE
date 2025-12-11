# -*- coding: utf-8 -*-
from src.core.database import load_db

def daily_revenue(date=None):
    payments = load_db("payments")
    total = sum(int(p.get("total", 0)) for p in payments)
    print(f"Doanh thu (tổng) hiện có: {total} đ (số thanh toán: {len(payments)})")

