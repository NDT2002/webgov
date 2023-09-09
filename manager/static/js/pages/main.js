$(document).ready(function () {
  
  // Xử lý sự kiện khi một phần tử được thả vào vùng chứa widget-content
  function handleDrop(event) {
    event.preventDefault();
    var draggedItemId = event.originalEvent.dataTransfer.getData("text/plain");
    var droppedZone = $(this);

    var clonedElement = $("#" + draggedItemId).clone();
    clonedElement.removeClass("widget-examp").addClass("widget-content-item");
    clonedElement.attr("draggable", "false");
    clonedElement.find(".select-box, .btn-block").remove();

    droppedZone.append(clonedElement);
  }

  // Xử lý sự kiện khi bắt đầu kéo để chuyển dữ liệu về phần tử đang kéo
  function handleDragStart(event) {
    var originalElement = $(this);
    var clonedElement = originalElement.clone();

    event.originalEvent.dataTransfer.setData("text/plain", clonedElement.attr("id"));
  }

  // Kích hoạt sự kiện kéo và thả cho widget-created
  $(".widget-created > .card-body > .widget-content")
    .on("drop", handleDrop)
    .on("dragover", function (event) {
      event.preventDefault();
    });

  // Kích hoạt sự kiện bắt đầu kéo cho widget-examp
  $(".widget-examp").on("dragstart", handleDragStart);

  // Kích hoạt chọn vùng chứa trong widget-content-item
  $(".card-body > .widget-content > .widget-content-item > .card-body > .widget-content").on("drop", handleDrop);

  // Kích hoạt sắp xếp cho widget-content
  $(".widget-content").sortable({
    items: ".widget-content-item",
  });

  // Ngăn chọn văn bản khi kéo
  $(".widget-content").disableSelection();

  // Xử lý sau khi kết thúc sắp xếp
  $(".widget-content").on("sortstop", function (event, ui) {
    // ...
  });

  $(".widget-created .card-title").each(function () {
    // Lấy nội dung của tiêu đề card
    var cardTitle = $(this).text();
    var widgetId = $(this).closest(".widget-created").attr("id"); // Lấy ID của widget-created

    // Thêm tiêu đề card và ID widget-created làm tùy chọn vào phần tử select
    $("<option>", {
      value: widgetId,
      text: cardTitle,
    }).appendTo(".select-box .custom-select");
  });

  $(".card-widget .btn-block").click(function (e) {
    e.preventDefault();
    var container = $(this).closest(".card-body");
    // Lấy giá trị của tùy chọn được chọn trong phần tử gần nhất
    var selectedValue = "#" + container.find(".custom-select").val();
    console.log($(selectedValue + " .widget-content").text());
    var widget = $(this).closest(".card-widget");

    // Tạo một bản clone của phần tử container
    var clone = widget.clone();
    clone.removeClass("widget-examp").addClass("widget-content-item");

    clone.attr("draggable", "false");
    // Loại bỏ phần select và nút thêm trong bản sao
    clone.find(".select-box, .btn-block").remove();
    $(selectedValue + " .widget-content").append(clone);
  });
    var saveBtn=$('#save-btn');
    
});
