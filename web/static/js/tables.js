function updateTable(id, status) {
    fetch("/tables/update", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({id, status})
    })
    .then(r => r.json())
    .then(d => {
        if(d.success){
            alert("Đổi trạng thái thành công");
            location.reload();
        }
    })
}
