# Phân công lab tracking — 2 người, làm lần lượt trên một máy

Hai người dùng chung một máy và bàn giao sau khi người 1 hoàn tất phần việc của mình. Chạy các lệnh từ thư mục gốc của repo. Chỉ thay tracker và ngưỡng detector `--conf`, `--iou`; giữ nguyên detector, kích thước ảnh, lớp người và mô hình Re-ID.

## Người 1 — chuẩn bị, `video_1` và `video_2`

1. Kích hoạt môi trường Conda `ai` đã có theo yêu cầu, cài các thư viện lab và TrackEval. Tải, giải nén dữ liệu; đặt `LAB_DATA` trỏ tới thư mục chứa `video_1` … `video_5`; chạy `python scripts/check_data.py --lab-data-root "$LAB_DATA"`.
2. Mở `on_tap_metrics.ipynb` bằng kernel của môi trường `ai`: đọc MOTA / IDF1 / HOTA và chạy YOLO trên một ảnh `video_1`.
3. Chạy baseline `video_1` với ByteTrack, `--conf 0.3 --iou 0.5` và tối đa 150 frame để xem nhanh ID trên video thử.
4. Với từng `video_1` và `video_2`, thử ít nhất một tracker theo chuyển động (`bytetrack` hoặc `ocsort`) và một tracker có Re-ID (`botsort`, `strongsort` hoặc `deepocsort`). Với tracker tốt hơn, thử các giá trị `conf` và `iou` gợi ý trong `HUONG_DAN.md`, mỗi lượt chỉ đổi một tham số. Ghi cấu hình đã thử nhưng loại và lỗi nhìn thấy.
5. Chọn cấu hình cho từng video; chạy lại **đủ frame**, không dùng `--max-frames`, lưu vào `runs/nop_bai/` thành `video_1.txt` và `video_2.txt`.
6. Chạy `scripts/evaluate_practice.py` với `runs/nop_bai/video_1.txt`. Ghi bảng HOTA / MOTA / IDF1, cấu hình đã chọn và quan sát để bàn giao cho người 2.

## Người 2 — `video_3` đến `video_5` và báo cáo

1. Nhận máy, xác nhận môi trường và `LAB_DATA` vẫn dùng được; đọc ghi chú và số liệu của người 1.
2. Với từng `video_3`, `video_4`, `video_5`, xem video gốc và thử ít nhất một tracker theo chuyển động cùng một tracker có Re-ID. Điều chỉnh `conf` hoặc `iou` từng tham số một; ghi lỗi ID, bỏ sót người và hộp giả quan sát được.
3. Chọn cấu hình cho từng video; chạy lại **đủ frame**, không dùng `--max-frames`, lưu cùng `runs/nop_bai/` thành `video_3.txt`, `video_4.txt`, `video_5.txt`.
4. Điền `submission_template/BAO_CAO_mau.md`: cấu hình, quan sát và một cấu hình đã thử nhưng loại cho cả năm video; bảng HOTA / MOTA / IDF1 chỉ cho `video_1`; giải thích lựa chọn tracker cho ít nhất hai video.

## Kiểm tra chung trước khi nộp

- `runs/nop_bai/` có đủ `video_1.txt` … `video_5.txt`, đúng tên và đủ frame.
- Báo cáo có thông tin của cả năm video; `video_2` … `video_5` chỉ đánh giá bằng mắt, không điền điểm số.
- Nếu máy chậm, giảm số lượt thử tham số trên video đông; vẫn chạy đủ frame cho cả năm file nộp.
