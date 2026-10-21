# Lộ trình học Forex (từ cơ bản đến tự làm tool quản lý rủi ro)

Mục tiêu cuối: **hiểu thị trường, có kế hoạch giao dịch riêng, giao dịch kỷ luật, và tự code tool khóa giao dịch** (giới hạn số lệnh/ngày, giới hạn lỗ/ngày theo Equity).

Cách học: **lý thuyết → bài tập → review → áp dụng vào "Hệ thống giao dịch" của riêng mình**. Mỗi bài chỉ 1 khái niệm chính.
Ban ngày (ở công ty): đọc chữ + bài tập tính toán. Buổi tối/cuối tuần: xem chart, backtest, demo.

> 📝 **Cập nhật v2:** đổi thứ tự Giai đoạn 3 (Price Action trước), MA/RSI chỉ đọc lướt, bỏ luật "lãi đủ thì đóng hết lệnh", backtest bằng Bar Replay, bài 7.4 tính theo Equity, thêm bài bonus Auto-Risk Check.

---

## 🎯 Project xuyên suốt: Hệ thống giao dịch cá nhân
Mỗi giai đoạn lắp thêm 1 mảnh vào file `TRADING_PLAN.md`:
1. Cặp tiền + khung thời gian sẽ trade
2. Luật vào lệnh
3. Luật SL / TP
4. Luật rủi ro: % rủi ro mỗi lệnh, số lệnh tối đa/ngày, **lỗ tối đa/ngày**, và **"đạt +X R trong ngày thì không mở thêm lệnh mới"** (lệnh đang chạy cứ để chạy theo SL/TP, không tự cắt)
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

### 1.4. Đòn bẩy & Margin ✅ *(Đã hoàn thành)*
- **Lý thuyết:** đòn bẩy, margin, free margin, margin level, stop out.
- **Bài tập:** tính margin cần thiết với đòn bẩy 1:100 cho 0.5 lot; giải thích vì sao đòn bẩy cao làm cháy tài khoản nhanh.

### 1.5. Swap & Phiên giao dịch ✅ *(Đã hoàn thành)*
- **Lý thuyết:** swap (phí qua đêm), phiên Á/Âu/Mỹ, giờ nào biến động mạnh.
- **Bài tập:** lập bảng giờ các phiên theo giờ Việt Nam; chọn phiên phù hợp lịch của bạn.

---

## Giai đoạn 2: Quản lý vốn & rủi ro (QUAN TRỌNG NHẤT)

### 2.1. Rủi ro mỗi lệnh & tính khối lượng lệnh ✅ *(Đã hoàn thành)*
- **Lý thuyết:** quy tắc 1-2%, công thức `Lot = (Vốn x %rủi ro) / (số pip SL x giá trị 1 pip/lot)`.
- **Bài tập:** vốn 1000 USD, rủi ro 1%, SL 20 pip, tính lot. Tự đổi 5 bộ số khác nhau.

### 2.2. Tỷ lệ R:R & Kỳ vọng lợi nhuận ✅ *(Đã hoàn thành)*
- **Lý thuyết:** R:R, winrate, kỳ vọng (expectancy), cách đo kết quả bằng đơn vị **R** (1R = số tiền rủi ro mỗi lệnh).
- **Bài tập:** thắng 40% với R:R 1:2, kỳ vọng dương hay âm? Thử thêm 3 tổ hợp winrate/R:R.

### 2.3. Drawdown & chuỗi thua ✅ *(Đã hoàn thành)*
- **Lý thuyết:** drawdown, vì sao chuỗi thua là bình thường, cần lãi bao nhiêu % để hòa vốn sau khi lỗ X%.
- **Bài tập:** thua 10 lệnh liên tiếp với rủi ro 2% còn bao nhiêu vốn; lỗ 20% cần lãi bao nhiêu % để về hòa.
- **Lý thuyết thêm:** vì sao **không** đặt "mục tiêu lãi cố định mỗi ngày" (ép vào lệnh xấu khi ngày không có kèo; cắt mất những cú thắng lớn).
- **Áp dụng vào project:** chốt luật rủi ro (% mỗi lệnh, lỗ tối đa/ngày, số lệnh tối đa/ngày, đạt +X R thì ngừng mở lệnh mới).

---

## Giai đoạn 3: Phân tích kỹ thuật – Price Action (tối xem chart 30-45 phút)

> Thứ tự: **Cấu trúc → Vùng giá → Đa khung → Nến (cò súng) → ATR**. Nến chỉ có ý nghĩa khi giá đã ở đúng vùng.

### 3.1. Cấu trúc thị trường ✅ *(Đã hoàn thành)*
- **Lý thuyết:** đỉnh/đáy cao hơn/thấp hơn, uptrend/downtrend/sideway, Swing High/Low, BOS (phá cấu trúc tiếp diễn), CHoCH (đổi cấu trúc/đảo chiều).
- **Quy tắc vẽ (chốt cứng, không đổi trong 1 tháng):** Swing High/Low cần ít nhất 2 cây thấp hơn/cao hơn mỗi bên. Ghi quy tắc vào `TRADING_PLAN.md`, không tự sửa sau khi thua lệnh.
- **Phân biệt Trending vs Ranging:** Trending = HH/HL hoặc LH/LL rõ ràng → dùng BOS/CHoCH. Ranging = đỉnh đáy ngang hàng → dùng chiến lược mua S bán R, không tìm BOS.
- **Bài tập:** đánh dấu cấu trúc trên 30 đoạn chart quá khứ (5 phút/chart), phân loại trending hay ranging, lưu thành thư viện ảnh để xem lại.

### 3.2. Vùng giá quan trọng (Support/Resistance & Supply/Demand) ✅ *(Đã hoàn thành)*
- **Lý thuyết:** vùng hỗ trợ/kháng cự; Supply/Demand là cách vẽ chặt hơn (vùng có impulse mạnh rời đi + chưa được test lại = ưu tiên); Role Reversal; false breakout.
- **Quy tắc vẽ (chốt cứng):** vẽ theo thân nến (không phải bóng nến); ưu tiên vùng trên H4/D1; vùng quá cũ (giá đã test lại 3+ lần) giảm ưu tiên. Ghi vào `TRADING_PLAN.md`, không vẽ lại vùng sau khi thua.
- **Checklist chất lượng vùng (đếm được):**
  1. Chưa hoặc ít được test lại (fresh)
  2. Có impulse mạnh rời khỏi vùng
  3. Trùng với khung lớn hơn (H4/D1 xác nhận H1)
  4. Có confluence: round number, swing cũ, vùng overlap S/R và SD
  5. Thời gian giá ở trong vùng ngắn (giá rời nhanh)
- **Bài tập:** vẽ cùng 1 chart bằng 2 cách (S/R ngang và SD theo impulse); chọn cách nào rõ ràng hơn với bạn rồi bỏ cách kia; tìm 3 ví dụ false breakout.

### 3.3. Khung thời gian (Multi-timeframe) ✅ *(Đã hoàn thành)*
- **Lý thuyết:** khung lớn (D1/H4) xác định xu hướng và vùng; khung nhỏ (H1/M15) tìm điểm vào.
- **Luật bias (chốt cứng):** chỉ tìm lệnh theo hướng D1/H4. H1/M15 chỉ dùng để xác nhận entry, không dùng để xác định hướng. Pullback trên H1 trong uptrend D1 = cơ hội Buy, không phải tín hiệu Sell.
- **Bài tập:** chọn 1 cặp, xác định trend ở D1/H4/H1, ghi nhận xét.

### 3.4. Nến Nhật làm tín hiệu
- **Lý thuyết:** OHLC, thân nến, bóng nến; chỉ học 3 mẫu: Pinbar (từ chối giá), Engulfing (nhấn chìm), Fakey (phá vỡ giả + xác nhận).
- **Quy tắc cứng:** nến chỉ hợp lệ khi nằm tại vùng S/R đã xác định trước. Nến cùng mẫu giữa khoảng trống = bỏ qua.
- **Bài tập:** chụp 5 nến đẹp tại vùng quan trọng + 5 nến cùng mẫu nằm giữa khoảng trống; so sánh kết quả sau đó; ghi rõ với từng nến "được phép vào lệnh không? Vì sao?"

### 3.4b. Liquidity — Thanh khoản & Stop Hunt
- **Lý thuyết:** giá thường đi săn thanh khoản (stop loss đám đông) trước khi chạy thật; Equal Highs/Equal Lows = ổ thanh khoản hay bị quét; Inducement (dụ vào lệnh rồi quét); bản chất false breakout chính là liquidity sweep.
- **Không cần học:** order block, FVG, ICT đầy đủ — giữ đơn giản.
- **Bài tập:** tìm 3 ví dụ Equal High/Low bị quét trên chart quá khứ; xác định giá quét xong đi đâu.

### 3.5. ATR (độ biến động) & đặt SL
- **Lý thuyết:** ATR đo biến động, dùng làm "đệm" để SL không bị quét oan.
- **Bài tập:** tính SL = 1.5 x ATR cho 3 cặp tiền, so sánh khoảng cách SL.

### 3.6. Confluence — Đồng thuận điều kiện
- **Lý thuyết:** setup A+ cần tối thiểu bao nhiêu điều kiện đồng thuận? Ví dụ: cấu trúc đúng hướng D1 + vùng mạnh chưa test nhiều + nến tín hiệu hợp lệ + ATR hợp lý + không gần tin lớn. Càng nhiều điều kiện đồng thuận thì xác suất càng cao — nhưng số lệnh ít hơn. Tìm điểm cân bằng phù hợp với bạn.
- **Bài tập:** tự viết "Setup A+ của tôi cần tối thiểu X điều kiện", đưa vào `TRADING_PLAN.md`.

### 3.7. MA & RSI (đọc lướt, ~15 phút mỗi cái, không bắt làm bài tập sâu)
- **Lý thuyết:** MA/RSI đo cái gì, hay sai khi nào (sideway, trễ). Chỉ để biết chúng là gì.
- **Bài tập:** viết 2-3 dòng mỗi cái. Nếu sau này hệ thống của bạn không dùng thì bỏ qua hẳn.

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
- **Lý thuyết:** biến "cảm giác" thành điều kiện đúng/sai rõ ràng (cấu trúc nào, vùng nào, nến tín hiệu nào).
- **Bài tập:** viết luật vào lệnh Buy và Sell, người khác đọc phải làm theo được.

### 5.2. Luật SL, TP & quản lý lệnh
- **Lý thuyết:** đặt SL ở đâu (sau vùng + đệm ATR), TP ở đâu (vùng đối diện/cấu trúc), có dời SL về hòa vốn không, chốt một phần.
- **TP Management theo phản ứng giá:** khi giá tiếp cận vùng TP, đọc phản ứng — giá đâm thẳng qua (momentum mạnh) thì để chạy tiếp; giá khựng lại, xuất hiện nến đảo chiều thì cân nhắc chốt một phần hoặc dời SL về hòa vốn. Không tự cắt sớm vì sợ, không gồng mù khi giá đã cảnh báo.
- **Bài tập:** bổ sung vào luật; thử áp dụng trên 10 tình huống chart quá khứ.

### 5.3. Kế hoạch giao dịch 1 trang
- **No-trade rules (bắt buộc có trong kế hoạch):** không vào lệnh giữa vùng (mid-range, không có S/R rõ); không vào lệnh khi spread/volatility bất thường; không vào lệnh trong vòng 15-30 phút trước/sau tin lớn; không vào lệnh khi H4 và D1 xung đột chưa rõ hướng. Ghi thành danh sách cụ thể, dễ kiểm tra trước mỗi lệnh.
- **Bài tập:** gộp toàn bộ luật vào `TRADING_PLAN.md`: cặp tiền, khung, giờ trade, điều kiện vào, SL/TP, rủi ro, giới hạn ngày, và danh sách No-trade rules.

### 5.4. Backtest bằng Bar Replay
- **Lý thuyết:** backtest là gì, lỗi hay gặp (chọn lọc lệnh đẹp, **nhìn trước tương lai**). Không kéo chart tĩnh đã chạy xong; dùng **Bar Replay (TradingView)** hoặc FX Blue Trading Simulator để nến chạy từng cây, che phần bên phải.
- **Bài tập:** backtest tối thiểu **30 lệnh** (tốt nhất 50) vào bảng tính (ngày, vào, SL, TP, kết quả theo R); tính winrate và kỳ vọng.

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

> Mặc định dùng **MT5 (MQL5)**. Chỉ đổi sang cTrader (C#) nếu bạn đã quen C# và sàn của bạn hỗ trợ.

### 7.1. Cú pháp MQL5 cơ bản
- **Lý thuyết:** biến, hàm, `OnInit`, `OnTick`, `OnTimer`.
- **Bài tập:** viết EA in ra số dư và equity lên chart.

### 7.2. Đọc lịch sử lệnh & đếm lệnh trong ngày
- **Lý thuyết:** `HistorySelect`, `PositionsTotal`, múi giờ server broker, lưu **balance đầu ngày**.
- **Bài tập:** EA hiển thị "hôm nay đã vào X lệnh, lãi/lỗ Y%".

### 7.3. Khóa giao dịch theo số lệnh/ngày
- **Lý thuyết:** class `CTrade`, đóng lệnh mới mở khi vượt giới hạn, lưu trạng thái "đã khóa" bằng `GlobalVariableSet` (tắt/bật lại EA vẫn còn khóa).
- **Bài tập:** vượt X lệnh/ngày thì lệnh mới bị đóng ngay và gửi thông báo.

### 7.4. Khóa giao dịch theo lỗ tối đa/ngày (tính theo Equity)
- **Lý thuyết:** kiểm tra liên tục (`OnTimer` mỗi 1 giây), dùng **Equity** chứ không chỉ Balance để bắt cả lệnh đang âm:
  `Daily Drawdown % = (Balance đầu ngày − Equity hiện tại) / Balance đầu ngày × 100`
- **Bài tập:** chạm -Y% thì đóng toàn bộ vị thế, xóa lệnh chờ, và khóa đến hôm sau. **Chạy trên tài khoản demo trước.**

### 7.5. Khóa mở lệnh mới khi đã đạt +X R trong ngày
- **Bài tập:** khi lãi trong ngày đạt +X R thì chặn lệnh mới (đóng lệnh mới mở ngay), **không đụng vào lệnh đang chạy**. Gửi thông báo "hôm nay đủ rồi".

### 7.6. (Bonus) Auto-Risk Check
- **Bài tập:** khi có lệnh mới, EA tính (khoảng cách Entry→SL × lot): nếu vượt % rủi ro cho phép, hoặc lệnh không có SL sau ~10 giây thì tự đóng/giảm lot. Chống bấm nhầm lot.
- *(Chỉ làm sau khi 7.3-7.5 chạy ổn.)*

> Nếu sau này thấy mình hay tự tắt EA khi cay cú → mới cân nhắc chạy trên VPS hoặc thêm thông báo Telegram. Chưa cần ở giai đoạn đầu.

---

## 🏆 Đích đến cuối khóa
1. Có `TRADING_PLAN.md` hoàn chỉnh, luật rõ ràng.
2. Có backtest Bar Replay 30-50 lệnh với kỳ vọng dương.
3. Có ít nhất 1-2 tháng nhật ký demo, tuân thủ luật ổn định.
4. Có EA khóa giao dịch theo số lệnh, lỗ tối đa/ngày (Equity) và chặn lệnh mới khi đạt +X R, chạy ổn trên demo.

---
**Tiến độ được cập nhật trong `FOREX_PROGRESS.md`.** Khi sẵn sàng, nói "Bắt đầu Bài 1.4".