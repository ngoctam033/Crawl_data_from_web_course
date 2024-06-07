from extract_html import get_html_files
from soup_methods import extract_html_to_soup
from soup_methods import extract_contents
from soup_methods import remove_duplicates
from clean_data_output import save_file

# Đường dẫn đến thư mục chứa các tệp HTML
path = 'D:\\.CODE\\Crawl_data_from_web_course\\data'

# Gọi hàm get_html_files, để lấy ra tất cả các file html trong thư mục
html_files = get_html_files(path)

#kiểm tra xem html_files có rỗng không
if not html_files:
    print('Không có tệp HTML nào trong thư mục')
    exit()

#gọi hàm extract_html_to_soup để chuyển đổi các file html thành các đối tượng BeautifulSoup
soups = extract_html_to_soup(html_files)
soups = extract_contents(soups, 'div', 'que multichoice deferre', text=False)

contents = remove_duplicates(soups, 'div', 'qtext')
save_file('D:\\.CODE\\Crawl_data_from_web_course\\data', contents, 'cau_hoi_on.html')
# save_file('D:\\.CODE\\Crawl_data_from_web_course\\data', soups, 'cau_hoi.html')

print('Lưu file thành công')