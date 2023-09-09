- Dashboard
<a href="{% url 'dashboard' %}">Dashboard</a>

- Quản lý Tin tức
  - Thêm mới tin tức
    <a href="{% url 'add_news' %}">Thêm mới tin tức</a>
  - Danh sách tin tức
    <a href="{% url 'news_list' %}">Danh sách tin tức</a>

- Danh mục/Chuyên mục
  - Quản lý danh mục
    <a href="{% url 'add_category' %}">Quản lý danh mục</a> 
  - Danh sách danh mục
    <a href="{% url 'category_list' %}">Danh sách danh mục</a>

- Quản lý Tác giả/Người viết
  - Thêm tác giả
    <a href="{% url 'add_author' %}">Thêm tác giả</a>
  - Danh sách tác giả
    <a href="{% url 'author_list' %}">Danh sách tác giả</a>

- Thẻ/Tags
  - Quản lý thẻ
    <a href="{% url 'manage_tags' %}">Quản lý thẻ</a>
- Thư viện ảnh/Multimedia
  - Quản lý hình ảnh, video
    <a href="{% url 'manage_media' %}">Quản lý hình ảnh và multimedia</a>
- Thống kê và Báo cáo
  - Thống kê lượt xem
    <a href="{% url 'view_statistics' %}">Thống kê lượt xem</a>
- Cài đặt
  - Quản lý người dùng
    <a href="{% url 'manage_users' %}">Quản lý người dùng</a>
    
- Đăng xuất
<a href="{% url 'logout' %}">Đăng xuất</a>

Trang Dashboard
  - Tổng quan
  - Biểu đồ thống kê
  - Hoạt động gần đây
    - Bài viết mới nhất
    - Tác giả mới thêm
    - Thay đổi danh mục
  - Thông báo và cảnh báo
  - Thống kê lượt xem
  - Tổng quan về tác giả
  - Thống kê dữ liệu
  - Các công cụ quản lý nhanh
    - Tạo mới tin tức
    - Tạo mới danh mục
    - Thêm tác giả mới
  - Thông tin hệ thống
  - Các thông báo quan trọng
  - Báo cáo tổng quan


Giao diện trang thêm mới tin tức thường bao gồm các mục sau:

Tiêu đề: Ô để người dùng nhập tiêu đề cho tin tức.

Nội dung: Trường văn bản lớn để người dùng nhập nội dung chi tiết của tin tức.

Danh mục/Chuyên mục: Một danh sách thả xuống hoặc ô để người dùng chọn danh mục hoặc chuyên mục cho tin tức.

Tác giả/Người viết: Một trường để người dùng chọn tác giả hoặc nhập tên tác giả của tin tức.

Hình ảnh đại diện: Cho phép người dùng tải lên một hình ảnh đại diện cho tin tức.

Thẻ/Tags: Ô để người dùng nhập các thẻ hoặc từ khóa liên quan đến tin tức.

Trạng thái: Một tùy chọn để người dùng chọn trạng thái của tin tức, ví dụ như "Đã xuất bản", "Chờ duyệt", "Nháp", v.v.

Ngày đăng: Một trường cho phép người dùng chọn ngày đăng tin tức.

Nút Lưu: Nút để người dùng lưu tin tức sau khi đã điền đầy đủ thông tin.

Nút Hủy: Nút để người dùng hủy bỏ việc thêm mới tin tức và quay lại trang danh sách tin tức hoặc trang khác.