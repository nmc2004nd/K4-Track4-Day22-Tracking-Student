# Bàn giao phần người 1

## Đọc trên máy thứ hai sau khi kéo Git

- Git mang theo `instruction.md`, `runs/nop_bai/video_1.txt`, `video_2.txt`, ghi chú này, bảng điểm và `runs/nguoi_1/video_1_eval_config.json`. Khi người 2 tạo `video_3.txt`–`video_5.txt` trong `runs/nop_bai/`, các file TXT đó cũng được Git nhận.
- `lab_data/`, `TrackEval/`, trọng số `*.pt`, video preview và notebook đã chạy **không** đi theo Git. Tải dữ liệu theo `README.md`, cài môi trường và TrackEval trên máy thứ hai nếu máy đó chưa có. Dùng notebook gốc `on_tap_metrics.ipynb` nếu cần chạy lại.
- Sau khi giải nén dữ liệu, từ gốc repo đặt `export LAB_DATA="$PWD/lab_data/data_lab21"`. Nếu cần chấm lại `video_1`, chép cấu hình đi kèm: `cp runs/nguoi_1/video_1_eval_config.json "$LAB_DATA/video_1/eval_config.json"`.
- Video có vẽ ID của `video_1` và `video_2` chỉ ở máy thứ nhất; nếu cần xem trực tiếp trên máy thứ hai, chuyển riêng ngoài Git hoặc chạy lại từ ảnh.

## Môi trường và dữ liệu trên máy thứ nhất

- Dùng Conda env `ai` theo yêu cầu. Từ thư mục gốc repo: `conda activate ai`.
- Dữ liệu đã giải nén ở `lab_data/data_lab21/`. Đặt `export LAB_DATA="$PWD/lab_data/data_lab21"`, rồi chạy `python scripts/check_data.py --lab-data-root "$LAB_DATA"`.
- TrackEval ở `TrackEval/` trong repo; khi chấm dùng `--trackeval-root TrackEval`.
- Cả năm tracker trong danh sách đã khởi tạo và xử lý một frame thử được trong env `ai` (StrongSort chưa xuất track ngay ở frame đầu, không phải lỗi khởi tạo).
- `pip check` vẫn báo BoxMOT 10.0.42 yêu cầu NumPy 1.23.1, trong khi env `ai` đang có NumPy 2.4.6. ByteTrack và BoTSORT đã chạy đủ các video được giao; ba tracker còn lại mới được thử một frame.
- Gói dữ liệu tải về không có `preview/` và `video_1/eval_config.json`. Đã tạo `eval_config.json` tối thiểu với tên benchmark nội bộ `LAB21` trong thư mục dữ liệu đã được gitignore. Xem video có vẽ ID trong `runs/nop_bai/`.
- Notebook đã chạy bằng kernel của env `ai`; bản có kết quả chỉ lưu trên máy này ở `runs/nguoi_1/on_tap_metrics_da_chay.ipynb`. Ba câu metric: Đúng, Sai, Đúng. Ảnh đầu `video_1`: YOLO có 14/6/5 hộp người ở `conf` 0.15/0.3/0.5.

## `video_1`

- File nộp `runs/nop_bai/video_1.txt` và video `runs/nop_bai/video_1_preview.mp4`: BoTSORT, `conf=0.3`, `iou=0.7`, đủ 600 frame.
- Chấm đúng file nộp bằng `evaluate_practice.py`: **HOTA 29.969, MOTA 19.025, IDF1 29.703**. Bảng đầy đủ để dán vào báo cáo: `runs/nguoi_1/video_1_pedestrian_summary.txt`.
- Các bản đủ frame đã thử: ByteTrack 0.3/0.5: HOTA 26.912, MOTA 17.292, IDF1 25.713; BoTSORT 0.3/0.5: 29.460, 19.811, 29.354; BoTSORT 0.15/0.5: 29.343, 20.731, 29.561. BoTSORT 0.3/0.7 có HOTA và IDF1 cao nhất trong các bản này.
- Các bản thử 150 frame khác: BoTSORT `conf=0.5`, `iou=0.4` và `iou=0.7` (mỗi lượt chỉ đổi một tham số). `conf=0.5` ít hộp hơn rõ rệt; `conf=0.15` thêm người ở xa nhưng cũng tăng hộp giả và lần đổi ID trên bản đủ frame.
- Quan sát: người nhỏ ở xa vẫn dễ bị bỏ sót; nhóm người gần camera được theo dõi liên tục hơn. Bản `iou=0.7` tăng HOTA nhưng có nhiều hộp giả hơn bản `iou=0.5` (611 so với 337 theo bảng chấm).

## `video_2`

- File nộp `runs/nop_bai/video_2.txt` và video `runs/nop_bai/video_2_preview.mp4`: BoTSORT, `conf=0.15`, `iou=0.5`, đủ 1.050 frame. File TXT có 13.821 hàng; có track ở cả frame đầu và frame cuối.
- Trên 150 frame đầu: ByteTrack 0.3/0.5 xuất 1.313 hộp; BoTSORT 0.3/0.5 xuất 1.543 hộp; BoTSORT 0.15/0.5 xuất 1.720 hộp; BoTSORT 0.5/0.5 chỉ 1.125 hộp. Với `conf=0.15`, thử `iou=0.4/0.5/0.7` lần lượt có 1.717/1.720/1.737 hộp.
- Quan sát: cảnh đông, nhiều người nhỏ và bị che khuất phía xa. BoTSORT giữ được thêm một số người so với ByteTrack ở đoạn xem thử; `conf=0.5` bỏ sót nhiều hơn. Ở `conf=0.15`, các frame đã xem không thấy hộp giả nổi bật. Track ID 4 ở mép phải có hộp tại cả 1.050 frame và vị trí gần như không đổi; người rất xa vẫn thường không có ID. Không có nhãn để chấm điểm số cho video này.

## Việc người 2 tiếp tục

Thử tracker, chọn cấu hình và chạy đủ frame cho `video_3`–`video_5` vào cùng `runs/nop_bai/`; điền báo cáo từ ghi chú này cùng quan sát của mình. Không chấm HOTA/MOTA/IDF1 cho `video_2`–`video_5`.
