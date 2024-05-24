#import thư viện để làm việc với các file html
import os

#tạo hàm để lấy danh sách tất cả các file html trong thư mục
#input là đường dẫn của thư mục 'html-files'
#output là một list chứa đường dẫn của các file html
def get_html_files(path):
    # Tạo list để chứa đường dẫn của các file html
    html_files = []
    # Duyệt qua các file trong thư mục và các thư mục con
    for root, dirs, files in os.walk(path):
        for file in files:
            # Kiểm tra xem file có phải là file html không
            if file.endswith('.html'):
                # Nếu là file html thì thêm đường dẫn của file vào list
                html_files.append(os.path.join(root, file))
    return html_files
