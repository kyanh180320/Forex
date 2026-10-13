# Lộ trình học Forex (từ cơ bản đến tự làm tool quản lý rủi ro)

Mục tiêu cuối: **hiểu thị trường, có kế hoạch giao dịch riêng, giao dịch kỷ luật, và tự code tool khóa giao dịch** (giới hạn số lệnh/ngày, giới hạn % lãi/lỗ/ngày).

Cách học: **lý thuyết → bài tập → review → áp dụng vào "Hệ thống giao dịch" của riêng mình**. Mỗi bài chỉ 1 khái niệm chính.
Ban ngày (ở công ty): đọc chữ + bài tập tính toán. Buổi tối/cuối tuần: xem chart, backtest, demo.

---

## 🎯 Project xuyên suốt: Hệ thống giao dịch cá nhân
Mỗi giai đoạn lắp thêm 1 mảnh vào file `TRADING_PLAN.md`:
1. Cặp tiền + khung thời gian sẽ trade
2. Luật vào lệnh
3. Luật SL / TP
4. Luật rủi ro (% mỗi lệnh, số lệnh tối đa/ngày, lỗ tối đa/ngày, lãi mục tiêu/ngày)
5. Nhật ký giao dịch (bảng tính)

---

## Giai đoạn 1: Khái niệm nền (chỉ đọc chữ + tính tay)

### 1.1. Forex là gì & Cặp tiền ✅ *(Đã hoàn thành)*
- **Lý thuyết:** thị trường forex, ai tham gia, cặp tiền, base/quote, cách đọc giá (bid/ask).
- **Bài tập:** giải thích bằng lời EURUSD = 1.0850 nghĩa là gì; liệt kê 7 cặp chính.

### 1.2. Pip, Lot & giá trị pip ✅ *(Đã hoàn thành)*
- **Lý thuyết:** pip là gì, các loại lot (standard/mini/micro), giá trị 1 pip.
- **Bài tập:** EURUSD từ 1.0850 lên 1.0900, mua 0.1 lot, lãi bao nhiêu pip, bao nhiêu USD.

### 1.3. Spread & các loại lệnh ✅ *(Đã hoàn thành)*
- **Lý thuyết:** spread, Buy/Sell, Market/Limit/Stop, Stop Loss, Take Profit.
- **Bài tập:** giải thích vì sao mở lệnh xong đã lỗ nhẹ; cho 3 tình huống, chọn loại lệnh phù hợp.

### 1.4. Đòn bẩy & Margin
- **Lý thuyết:** đòn bẩy, margin, free margin, margin level, stop out.
- **Bài tập:** tính margin cần thiết với đòn bẩy 1:100 cho 0.5 lot; giải thích vì sao đòn bẩy cao làm cháy tài khoản nhanh.

### 1.5. Swap & Phiên giao dịch
- **Lý thuyết:** swap (phí qua đêm), phiên Á/Âu/Mỹ, giờ nào biến động mạnh.
- **Bài tập:** lập bảng giờ các phiên theo giờ Việt Nam; chọn phiên phù hợp lịch của bạn.

---

## Giai đoạn 2: Quản lý vốn & rủi ro (QUAN TRỌNG NHẤT)

### 2.1. Rủi ro mỗi lệnh & tính khối lượng lệnh
- **Lý thuyết:** quy tắc 1-2%, công thức `Lot = (Vốn x %rủi ro) / (số pip SL x giá trị 1 pip/lot)`.
- **Bài tập:** vốn 1000 USD, rủi ro 1%, SL 20 pip, tính lot. Tự đổi 5 bộ số khác nhau.

### 2.2. Tỷ lệ R:R & Kỳ vọng lợi nhuận
- **Lý thuyết:** R:R, winrate, kỳ vọng (expectancy).
- **Bài tập:** thắng 40% với R:R 1:2, kỳ vọng dương hay âm? Thử thêm 3 tổ hợp winrate/R:R.

### 2.3. Drawdown & chuỗi thua
- **Lý thuyết:** drawdown, vì sao chuỗi thua là bình thường, cần lãi bao nhiêu % để hòa vốn sau khi lỗ X%.
- **Bài tập:** thua 10 lệnh liên tiếp với rủi ro 2% còn bao nhiêu vốn; lỗ 20% cần lãi bao nhiêu % để về hòa.
- **Áp dụng vào project:** chốt luật rủi ro (% mỗi lệnh, lỗ tối đa/ngày, số lệnh tối đa/ngày).

---

## Giai đoạn 3: Phân tích kỹ thuật cơ bản (tối xem chart 30-45 phút)

### 3.1. Nến Nhật
- **Lý thuyết:** OHLC, thân nến, bóng nến, một số mẫu nến cơ bản (chỉ 3-4 mẫu).
- **Bài tập:** chụp 5 cây nến ở các vị trí khác nhau trên chart quá khứ, mô tả nó nói gì.

### 3.2. Trend & cấu trúc thị trường
- **Lý thuyết:** đỉnh/đáy cao hơn/thấp hơn, uptrend/downtrend/sideway.
- **Bài tập:** đánh dấu trend trên 10 đoạn chart quá khứ, tự đối chiếu.

### 3.3. Support/Resistance & Cung cầu
- **Lý thuyết:** vùng hỗ trợ/kháng cự, vùng cung cầu, vì sao giá phản ứng ở vùng.
- **Bài tập:** vẽ vùng trên 1 cặp tiền, hôm sau kiểm tra giá có tôn trọng vùng không.

### 3.4. Khung thời gian (Multi-timeframe)
- **Lý thuyết:** khung lớn xác định xu hướng, khung nhỏ tìm điểm vào.
- **Bài tập:** chọn 1 cặp, xác định trend ở D1/H4/H1, ghi nhận xét.

### 3.5. Moving Average (MA)
- **Lý thuyết:** SMA/EMA đo cái gì, dùng khi nào, hay sai khi nào (sideway).
- **Bài tập:** viết 3 dòng tổng kết; quan sát MA50 trên 5 đoạn chart.

### 3.6. RSI
- **Lý thuyết:** RSI đo cái gì, quá mua/quá bán, phân kỳ, hay sai khi nào.
- **Bài tập:** tìm 3 chỗ RSI báo đúng và 3 chỗ RSI báo sai.

### 3.7. ATR (độ biến động)
- **Lý thuyết:** ATR đo biến động, dùng để đặt SL hợp lý.
- **Bài tập:** tính SL = 1.5 x ATR cho 3 cặp tiền, so sánh khoảng cách SL.

---

## Giai đoạn 4: Phân tích cơ bản & tin tức

### 4.1. Lãi suất & Ngân hàng trung ương
- **Lý thuyết:** Fed, ECB, BOJ...; lãi suất ảnh hưởng đồng tiền thế nào.
- **Bài tập:** giải thích vì sao Fed tăng lãi suất thường làm USD mạnh lên.

### 4.2. Lạm phát & số liệu kinh tế (CPI, NFP)
- **Lý thuyết:** CPI, NFP, GDP; "số thực tế vs dự báo".
- **Bài tập:** chọn 1 tin đã ra, xem giá phản ứng thế nào, ghi lại.

### 4.3. Đọc lịch kinh tế & né tin
- **Lý thuyết:** mức độ ảnh hưởng (thấp/vừa/cao), spread giãn lúc ra tin, có nên trade lúc ra tin.
- **Bài tập:** 1 tuần liền, mỗi ngày ghi dự đoán 1 tin quan trọng, tối kiểm tra lại.
- **Áp dụng vào project:** thêm luật "không vào lệnh trước/sau tin lớn X phút".

---

## Giai đoạn 5: Xây hệ thống giao dịch riêng

### 5.1. Viết luật vào lệnh
- **Lý thuyết:** biến "cảm giác" thành điều kiện đúng/sai rõ ràng.
- **Bài tập:** viết luật vào lệnh Buy và Sell, người khác đọc phải làm theo được.

### 5.2. Luật SL, TP & quản lý lệnh
- **Lý thuyết:** đặt SL ở đâu, TP ở đâu, có dời SL về hòa vốn không, chốt một phần.
- **Bài tập:** bổ sung vào luật; thử áp dụng trên 10 tình huống chart quá khứ.

### 5.3. Kế hoạch giao dịch 1 trang
- **Bài tập:** gộp toàn bộ luật vào `TRADING_PLAN.md`: cặp tiền, khung, giờ trade, vào, SL/TP, rủi ro, giới hạn ngày.

### 5.4. Backtest tay
- **Lý thuyết:** backtest là gì, lỗi hay gặp (chọn lọc lệnh đẹp, nhìn trước tương lai).
- **Bài tập:** backtest 50-100 lệnh vào bảng tính (ngày, vào, SL, TP, kết quả theo R); tính winrate và kỳ vọng.

---

## Giai đoạn 6: Demo → Tiền thật

### 6.1. Mở tài khoản demo & nhật ký giao dịch
- **Bài tập:** trade demo theo đúng kế hoạch, ghi nhật ký mỗi lệnh (lý do vào, có theo luật không, cảm xúc).

### 6.2. Review hằng tuần
- **Bài tập:** cuối tuần liệt kê lệnh vi phạm luật, lỗi lặp lại, một điều cải thiện cho tuần sau.

### 6.3. Tiêu chí lên tiền thật
- **Lý thuyết:** khi nào đủ điều kiện (ví dụ: tối thiểu 1-2 tháng demo, tỷ lệ tuân thủ luật cao, kỳ vọng dương).
- **Bài tập:** tự viết tiêu chí của mình; nếu lên tiền thật thì dùng **vốn nhỏ**, rủi ro nhỏ.

---

## Giai đoạn 7: Tự code tool khóa giao dịch (MQL5 / nền tảng bạn dùng)

> Chọn nền tảng trước: MT5 (MQL5), MT4 (MQL4), hoặc cTrader (C#).

### 7.1. Cú pháp MQL5 cơ bản
- **Lý thuyết:** biến, hàm, `OnInit`, `OnTick`, `OnTimer`.
- **Bài tập:** viết EA in ra số dư và equity lên chart.

### 7.2. Đọc lịch sử lệnh & đếm lệnh trong ngày
- **Lý thuyết:** `HistorySelect`, `PositionsTotal`, múi giờ server broker.
- **Bài tập:** EA hiển thị "hôm nay đã vào X lệnh, lãi/lỗ Y%".

### 7.3. Khóa giao dịch theo số lệnh/ngày
- **Lý thuyết:** class `CTrade`, đóng lệnh mới mở khi vượt giới hạn, lưu trạng thái "đã khóa" (`GlobalVariableSet`).
- **Bài tập:** vượt X lệnh/ngày thì lệnh mới bị đóng ngay và gửi thông báo.

### 7.4. Khóa giao dịch theo % lãi/lỗ trong ngày
- **Bài tập:** lỗ chạm -Y% hoặc lãi đạt +Z% so với balance đầu ngày thì đóng hết lệnh và khóa đến hôm sau. **Chạy trên tài khoản demo trước.**

---

## 🏆 Đích đến cuối khóa
1. Có `TRADING_PLAN.md` hoàn chỉnh, luật rõ ràng.
2. Có backtest tay 50-100 lệnh với kỳ vọng dương.
3. Có ít nhất 1-2 tháng nhật ký demo, tuân thủ luật ổn định.
4. Có EA khóa giao dịch theo số lệnh và % lãi/lỗ, chạy ổn trên demo.

---
**Tiến độ được cập nhật trong `FOREX_PROGRESS.md`.** Khi sẵn sàng, nói "Bắt đầu Bài 1.1".
