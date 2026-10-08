# Báo cáo lab: chọn tracker cho 5 video

**Nhóm:** PayToWin **Thành viên:** Nguyễn Mạnh Cường - 2A202602823
                                   Đỗ Mạnh Đoan      - 2A2026028xx

Detector cố định: `yolo26n.pt`, ảnh 640 px, Re-ID `osnet_x0_25_msmt17`. Không đổi các mục này trong bài nộp chính.

## 1. Cấu hình đã chọn

Mỗi video: tracker bạn nộp, `conf`, `iou`, điều bạn **nhìn thấy** trên video, và một cấu hình đã thử rồi loại.

| Video | Tracker | conf | iou | Quan sát khi xem video | Đã thử nhưng loại |
|---|---|---|---|---|---|
| video_1 (quảng trường, tĩnh, ban ngày) | botsort | 0.3 | 0.7 | Nhóm người gần camera được theo dõi liên tục hơn; người nhỏ ở xa vẫn dễ bị bỏ sót. | bytetrack, `conf=0.3`, `iou=0.5`: HOTA và IDF1 thấp hơn trên `video_1`. |
| video_2 (phố đêm, tĩnh, rất đông) | botsort | 0.15 | 0.5 | Trong các đoạn đã xem, giữ được thêm một số người ở xa hoặc bị che khuất; người rất xa vẫn có thể thiếu ID. | botsort, `conf=0.5`, `iou=0.5`: bỏ sót nhiều người hơn trong 150 frame đầu. |
| video_3 (camera di động, ảnh nhỏ) | | | | | |
| video_4 (trong nhà, camera di chuyển) | | | | | |
| video_5 (trên xe bus, giao lộ đông) | | | | | |

## 2. Số liệu video_1

Dán bảng HOTA / MOTA / IDF1 do `scripts/evaluate_practice.py` in ra.

| HOTA | MOTA | IDF1 |
|---:|---:|---:|
| 29.969 | 19.025 | 29.703 |

Kết quả chấm `runs/nop_bai/video_1.txt`; bảng đầy đủ ở `runs/nguoi_1/video_1_pedestrian_summary.txt`.

`video_2` đến `video_5` không có nhãn trong gói lab. Không điền số cho các video đó.

## 3. Phân tích

Với **ít nhất hai video** (nên gồm một video bạn chỉ đánh giá bằng mắt), viết 3–5 câu:

- Tracker đã chọn giữ ID tốt hơn, hay ít hộp giả hơn, ở điểm nào bạn nhìn thấy?
- Cảnh đó (đứng yên / chuyển động, đông / thưa, sáng / tối, trong nhà / ngoài trời) khiến tracker này hợp hơn tracker kia như thế nào?

**video_1.** Camera đứng yên và người gần camera đủ lớn nên BoTSORT duy trì ID ở nhóm này tốt hơn trong video đã xem. Người nhỏ ở xa vẫn hay bị bỏ sót, dù đã thử giảm `conf`. So với ByteTrack ở `conf=0.3`, `iou=0.5`, bản BoTSORT đã nộp có HOTA 29.969 so với 26.912 và IDF1 29.703 so với 25.713. Bản `iou=0.7` tăng HOTA và IDF1 nhưng cũng có nhiều hộp giả hơn bản `iou=0.5`, nên đây là điểm còn phải đánh đổi.

**video_2.** Cảnh đêm rất đông, nhiều người nhỏ hoặc bị che khuất khiến tracker dễ bỏ sót hoặc mất ID. Ở các đoạn đã xem, BoTSORT với `conf=0.15` giữ thêm được một số người so với ByteTrack; thử `conf=0.5` làm mất nhiều hộp người hơn. Vẫn có người ở rất xa không được gán ID. Video này không có nhãn nên nhận xét chỉ dựa trên quan sát, không có điểm HOTA, MOTA hay IDF1.

## 4. Nếu có thêm thời gian

Một hoặc hai câu: bạn sẽ thử tiếp điều gì (Re-ID khác, quét `conf` mịn hơn, xem frame gây lỗi…).
