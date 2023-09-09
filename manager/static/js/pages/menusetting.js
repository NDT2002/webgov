$(document).ready(function () {
    // Xử lý sự kiện khi một phần tử được thả vào vùng chứa widget-content
  function handleDrop(event) {
    event.preventDefault();
    var draggedItemId = event.originalEvent.dataTransfer.getData("text/plain");
    var droppedZone = $(this);

    var clonedElement = $("#" + draggedItemId).clone();
    clonedElement.removeClass("card-widget").addClass("menu-content-item");
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
  $(".menu-struct")
    .on("drop", handleDrop)
    .on("dragover", function (event) {
      event.preventDefault();
    });

  $(".menu-content-item .widget-content")
    .on("drop", handleDrop)
    .on("dragover", function (event) {
      event.preventDefault();
    });

  // Kích hoạt sự kiện bắt đầu kéo cho widget-examp
  $(".card-widget").on("dragstart", handleDragStart);

  // Kích hoạt chọn vùng chứa trong widget-content-item
//   $(".card-body > .widget-content > .widget-content-item > .card-body > .widget-content").on("drop", handleDrop);

  // Kích hoạt sắp xếp cho widget-content
  $(".menu-struct").sortable({
    items: ".menu-content-item",
  });

  // Ngăn chọn văn bản khi kéo
  $(".menu-struct").disableSelection();

  // Xử lý sau khi kết thúc sắp xếp
  $(".menu-struct").on("sortstop", function (event, ui) {
    // ...
  });
});