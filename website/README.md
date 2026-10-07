# La Mela d’oro · Zeitz

Website nhà hàng tiếng Đức, HTML/CSS/JavaScript thuần, không cần framework hay bước build. Toàn bộ website deploy được nằm trong `dist/`.

## Chạy trên máy

Từ folder `website`, chạy:

```sh
python3 -m http.server 4173 --directory dist
```

Mở http://localhost:4173/. Cần HTTP server để tải JSON; không mở `index.html` bằng `file://`.

Có thể deploy thư mục `dist/` lên hosting static thông thường. Bản xem trước hiện dùng Sites và để riêng tư.

## Sửa dữ liệu

- `dist/data/menu.json`: 264 mục, 38 nhóm; chuyển từ toàn bộ 25 ảnh gốc. Mỗi món có mã, mô tả, danh sách lựa chọn `variants`, giá dạng số nguyên `priceCents`, ký hiệu gốc, nguồn ảnh, trang nguồn và trạng thái cần duyệt.
- `dist/data/restaurant.json`: thông tin từ file Word; giờ mở cửa xác minh trực tiếp trên Google Maps ngày 06.10.2026.
- `dist/app.js`: hiển thị menu, tìm kiếm, lọc, giỏ lưu trên thiết bị, ảnh gốc và tương tác.
- `dist/styles.css`: màu thương hiệu và responsive; các biến màu ở đầu file.
- `dist/index.html`: nội dung homepage và metadata SEO. Nếu đổi liên hệ/giờ mở cửa, cập nhật cả nội dung HTML dự phòng và Restaurant JSON-LD trong file này; metadata dùng địa chỉ website đang triển khai.

Giá: `990` = 9,90 €. Nếu có lựa chọn nhiều size/dung tích, mỗi lựa chọn là một phần tử của `variants`. Không tạo giá mặc định cho món chưa đọc được. ID phải duy nhất; số món 950 xuất hiện hai lần trong ảnh gốc (Ginger Ale và Köstritzer Pils), nên ID bao gồm category.

## Những dữ liệu chưa có / cần duyệt

- 11 món đồ uống nóng ở trang 23 bị cắt mất giá. Giữ `variants: []` và `needsReview: true`; website hiện “Preis bitte erfragen”, không thêm vào tổng tiền. Khi có giá chính xác, điền `variants`, đổi `needsReview` thành false và bỏ `reviewReason`.
- Tài liệu không có bảng giải nghĩa allergen/zusatzstoffe. Giữ mã nguyên bản, không tự gán ý nghĩa; khách được hướng dẫn hỏi nhà hàng. Không có nhãn Vegan được xác nhận nên không tạo filter Vegan. Vegetarian và Scharf chỉ dùng những tên/mô tả ghi rõ trên menu.
- Không có email, mạng xã hội, link đặt hàng, link booking, API thanh toán hoặc số WhatsApp trong Word. Website chỉ dùng số điện thoại đã cung cấp, không thêm liên kết giả.
- Không xác nhận dịch vụ Lieferung/Abholung, phí hoặc khu vực giao; không đưa ra các cam kết này.
- Không có dữ liệu chủ thể pháp lý, Impressum hoặc Datenschutz được cung cấp; không tạo nội dung hay link pháp lý giả. Khi nhận tài liệu chính thức, bổ sung các trang và liên kết tương ứng.

## Luồng đặt món

Khách chọn món → xem tổng tiền → có thể sao chép danh sách → gọi +49 3441 2590861 để hỏi và xác nhận. Website không gửi đơn, không xử lý thanh toán và không hiển thị xác nhận đơn giả. Giỏ lưu bằng localStorage của trình duyệt, có nút xóa và kiểm tra dữ liệu lưu không hợp lệ.

## Tài nguyên hình ảnh và font

25 ảnh gốc là menu. Bản cập nhật này bổ sung 7 ảnh thực tế độc lập của khách (1 ảnh trùng được bỏ qua); không có logo riêng. Wordmark được trình bày bằng typography, không được coi là logo có sẵn.

- Hero pizza vẫn là ảnh minh họa do built-in imagegen tạo và có ghi rõ “KI-generiertes Stimmungsbild · Serviervorschlag”; không đại diện cho ảnh món thật của nhà hàng. Khu khám phá, giới thiệu, đặt món và gallery dùng ảnh thực tế khách cung cấp. Nguồn và xử lý ảnh ghi trong `ASSETS.md`.
- Hai crop sushi/tagliatelle từ menu gốc vẫn lưu trong assets để đối chiếu nhưng không dùng trên homepage.
- `dist/assets/original-menu/`: đủ 25 trang menu, dùng làm đối chiếu tùy chọn qua nút Originalkarte; menu HTML là trải nghiệm chính.
- Bebas Neue và Caveat: self-host, giấy phép SIL Open Font License trong `dist/assets/`. Không có asset/font/CSS nào được sao chép từ L’Osteria.

## Kiểm tra đã thực hiện

Các viewport 375, 390, 430, 768, 1440, 1920px; kiểm tra scrollWidth, ảnh tải, menu di động, tìm kiếm theo tên/category, kết quả rỗng, lựa chọn size, cộng/trừ/xóa/clear, tổng tiền, reload persistence, chống dữ liệu localStorage không hợp lệ, ảnh original, filter và reduced motion. Kết quả cùng ảnh chụp nằm trong folder `../review/`.

Blueprint thiết kế: https://losteria.net/de/ (hero full-bleed, mảng đỏ/trắng/đen, typography hẹp đậm, menu khám phá trên ảnh, khu CTA, footer; code và tài nguyên riêng). Giờ mở cửa: https://maps.app.goo.gl/2YcBp9PybKwvrkx46.
