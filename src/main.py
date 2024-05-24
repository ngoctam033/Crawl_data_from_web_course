from extract_html import get_html_files
from soup_methods import extract_html_to_soup
from soup_methods import extract_contents
from clean_data_output import save_file
from clean_data_output import clean_text
import re

# Đường dẫn đến thư mục chứa các tệp HTML
path = 'D:\\.CODE\\Crawl_data_from_web_course\\html_files'

# Gọi hàm get_html_files
html_files = get_html_files(path)

#kiểm tra xem html_files có rỗng không
if not html_files:
    print('Không có tệp HTML nào trong thư mục')
    exit()

#gọi hàm extract_html_to_soup để chuyển đổi các file html thành các đối tượng BeautifulSoup
soups = extract_html_to_soup(html_files)

#gọi hàm extract_content để trích xuất nội dung của các đối tượng BeautifulSoup
#với tham số đầu vào là tên thẻ cần trích xuất và class của thẻ
contents = extract_contents(soups, 'div', 'que multichoice deferre')

# Chuyển contents thành một chuỗi
contents = ''.join([''.join(sublist) for sublist in contents if sublist])

#lam sach du lieu
cleaned_text = clean_text(contents)

#luu noi dung vao file txt
save_file('D:\\.CODE\\Crawl_data_from_web_course\\data', cleaned_text, 'output2.txt')