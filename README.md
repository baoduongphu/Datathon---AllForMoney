## 🚀 Hướng dẫn Clone dự án về máy (How to Clone)

Để bắt đầu làm việc với mã nguồn của dự án **Datathon 2026**, bạn cần sao chép repository này về máy tính cá nhân.

### 1. Kiểm tra git đã cài đặt chưa
Hãy đảm bảo máy tính của bạn đã cài đặt **Git**. Bạn có thể kiểm tra bằng lệnh:
```bash
git --version
```
### 2. Mở Terminal/Command Prompt
Di chuyển đến thư mục nơi bạn muốn lưu trữ dự án trên máy tính của mình:

``` Bash
cd duong/dan/den/thu/muc/cua/ban
```

### 3. Chạy lệnh clone
```bash
git clone https://github.com/baoduongphu/Datathon---AllForMoney.git
```
### 4. Truy cập vào thư mục dự án
```bash
cd Datathon---AllForMoney
```
### 5. Tạo môi trường ảo
```bash
python -m venv venv
.\venv\Scripts\activate
```
### 6. Cài đặt môi trường
```bash
pip install -r requirements.txt
```

## 📂 Cấu trúc dự án (Project Structure)

Dự án được tổ chức theo cấu trúc chuẩn để đảm bảo tính tái lập (reproducibility) và dễ dàng quản lý:

```text
datathon-2026-the-gridbreakers/
│
├── data/                       # Chứa dữ liệu đầu vào
│   ├── raw/                    # Dữ liệu gốc từ BTC (orders.csv, sales.csv,...)
│   └── processed/              # Dữ liệu đã làm sạch và tạo đặc trưng (Features)
│
├── notebooks/                  # Chứa toàn bộ các file Jupyter Notebook
│   ├── 0_MCQ_Part1.ipynb       # Code thực hiện và lưu kết quả bài thi Trắc nghiệm (Phần 1)
│   ├── 1_EDA_Analysis.ipynb    # Code thực hiện Trực quan hóa và Phân tích (Phần 2)
│   ├── 2_Feature_Eng.ipynb     # Code kết hợp các bảng, xử lý chuỗi thời gian, kiểm soát leakage
│   └── 3_Forecasting.ipynb     # Code huấn luyện mô hình, tối ưu và giải thích mô hình (SHAP)
│
├── src/                        # Các module Python dùng chung (.py)
│   ├── data_processing.py      # Hàm tiền xử lý dữ liệu tự động
│   └── model_utils.py          # Hàm đánh giá và Cross-validation
│
├── report/                     # Báo cáo kỹ thuật
│   ├── LaTeX_source/           # Mã nguồn theo template NeurIPS
│   └── Report_Final.pdf        # Bản PDF báo cáo cuối cùng (tối đa 4 trang)
│
├── submissions/                # Kết quả dự báo
│   ├── sample_submission.csv   # File mẫu đối chiếu
│   └── final_submission.csv    # File kết quả nộp lên Kaggle
│
├── README.md                   # Hướng dẫn chi tiết dự án
└── requirements.txt            # Danh sách thư viện cần thiết (pip install)
```
