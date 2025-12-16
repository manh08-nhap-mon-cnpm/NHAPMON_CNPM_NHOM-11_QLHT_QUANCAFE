function toggleTableStatus(btn, tableId, currentStatus) {
    let newStatus = currentStatus === "empty" ? "using" : "empty";

    fetch("/update-table", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: tableId, status: newStatus })
    }).then(res => res.json())
      .then(data => {
          if(data.success){
              btn.textContent = newStatus === "empty" ? "Trống" : "Đang dùng";
              btn.classList.remove(currentStatus);
              btn.classList.add(newStatus);
          }
      });
}
