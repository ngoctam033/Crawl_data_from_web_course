my_project/
│
├── src/
│   ├── main.py             # Chứa mã nguồn chính để crawl dữ liệu
│   └── extract_html.py     # Chứa các hàm để chuyển đổi html file thành đối tượng soup
│
├── tests/
│   ├── test_main.py        # Chứa các bài kiểm tra cho main.py
│   
│
├── html_files/             # Chứa các tệp HTML để crawl dữ liệu
│
├── data/                   # Chứa dữ liệu đã được crawl
│
├── .gitignore              # Liệt kê các tệp và thư mục không được theo dõi bởi Git
├── requirements.txt        # Liệt kê các thư viện Python cần thiết cho dự án
└── README.md               # Mô tả dự án và hướng dẫn sử dụng