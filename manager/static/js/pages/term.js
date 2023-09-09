$(document).ready(function () {
    // Lấy tham chiếu đến phần tử input và nút lưu sử dụng jQuery
  const nameInput = $("#name");
  const saveButton = $("#save-btn");
  saveButton.prop("disabled", true);


  // Bắt sự kiện thay đổi nội dung của input
  nameInput.on("input", function() {
    // Lấy giá trị hiện tại của input
    const currentValue = $(this).val();

    // Kiểm tra giá trị và cập nhật trạng thái của nút lưu
    if (currentValue.trim() === "") {
      saveButton.prop("disabled", true);
    } else {
      saveButton.prop("disabled", false);
    }
  });
  
});