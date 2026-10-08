# Phân công lab tracking — 2 người, làm lần lượt trên hai máy

Hai người làm lần lượt trên hai máy và bàn giao qua Git. Chạy các lệnh từ thư mục gốc của repo. Chỉ thay tracker và ngưỡng detector `--conf`, `--iou`; giữ nguyên detector, kích thước ảnh, lớp người và mô hình Re-ID.

## Người 1 — chuẩn bị, `video_1` và `video_2`

1. Kích hoạt môi trường Conda `ai` đã có theo yêu cầu, cài các thư viện lab và TrackEval. Tải, giải nén dữ liệu; đặt `LAB_DATA` trỏ tới thư mục chứa `video_1` … `video_5`; chạy `python scripts/check_data.py --lab-data-root "$LAB_DATA"`.
2. Mở `on_tap_metrics.ipynb` bằng kernel của môi trường `ai`: đọc MOTA / IDF1 / HOTA và chạy YOLO trên một ảnh `video_1`.
3. Chạy baseline `video_1` với ByteTrack, `--conf 0.3 --iou 0.5` và tối đa 150 frame để xem nhanh ID trên video thử.
4. Với từng `video_1` và `video_2`, thử ít nhất một tracker theo chuyển động (`bytetrack` hoặc `ocsort`) và một tracker có Re-ID (`botsort`, `strongsort` hoặc `deepocsort`). Với tracker tốt hơn, thử các giá trị `conf` và `iou` gợi ý trong `HUONG_DAN.md`, mỗi lượt chỉ đổi một tham số. Ghi cấu hình đã thử nhưng loại và lỗi nhìn thấy.
5. Chọn cấu hình cho từng video; chạy lại **đủ frame**, không dùng `--max-frames`, lưu vào `runs/nop_bai/` thành `video_1.txt` và `video_2.txt`.
6. Chạy `scripts/evaluate_practice.py` với `runs/nop_bai/video_1.txt`. Điền hai hàng `video_1`, `video_2`, điểm HOTA / MOTA / IDF1 của `video_1` và phần phân tích tương ứng vào `submission_template/BAO_CAO_mau.md`.
7. Commit và push `instruction.md`, hai file TXT trong `runs/nop_bai/`, báo cáo đang viết dở và ghi chú `runs/nguoi_1/BAN_GIAO.md` để người 2 kéo về. Không đưa dữ liệu gốc, trọng số hoặc video preview lên Git.

## Người 2 — `video_3` đến `video_5` và báo cáo

1. Pull các thay đổi của người 1 trên máy thứ hai; thiết lập môi trường và `LAB_DATA` trên máy này; đọc `instruction.md`, báo cáo đang viết dở và `runs/nguoi_1/BAN_GIAO.md`.
2. Với từng `video_3`, `video_4`, `video_5`, xem video gốc và thử ít nhất một tracker theo chuyển động cùng một tracker có Re-ID. Điều chỉnh `conf` hoặc `iou` từng tham số một; ghi lỗi ID, bỏ sót người và hộp giả quan sát được.
3. Chọn cấu hình cho từng video; chạy lại **đủ frame**, không dùng `--max-frames`, lưu cùng `runs/nop_bai/` thành `video_3.txt`, `video_4.txt`, `video_5.txt`.
4. Điền tiếp `submission_template/BAO_CAO_mau.md`: cấu hình, quan sát và một cấu hình đã thử nhưng loại cho `video_3`–`video_5`; rà soát phần người 1 đã điền. Chỉ `video_1` có bảng HOTA / MOTA / IDF1.
5. Commit và push ba file TXT mới cùng báo cáo đã hoàn thành để người 1 cũng kéo về được.

## Kiểm tra chung trước khi nộp

- `runs/nop_bai/` có đủ `video_1.txt` … `video_5.txt`, đúng tên và đủ frame.
- Báo cáo có thông tin của cả năm video; `video_2` … `video_5` chỉ đánh giá bằng mắt, không điền điểm số.
- Nếu máy chậm, giảm số lượt thử tham số trên video đông; vẫn chạy đủ frame cho cả năm file nộp.
