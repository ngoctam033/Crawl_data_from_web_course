from bs4 import BeautifulSoup
import re

#tạo hàm để chuyển đổi html file sang đối tượng BeautifulSoup
#tham số đầu vào là đường dẫn của file html
#hàm trả về đối tượng BeautifulSoup
def extract_html(path):
    #mở file html
    with open(path, 'r', encoding='utf-8') as file:
        #đọc dữ liệu từ file
        data = file.read()
        #tạo đối tượng BeautifulSoup từ dữ liệu đọc được
        soup = BeautifulSoup(data, 'html.parser')
    return soup

#tạo một hảm để trả về một list chứa các đối tượng BeautifulSoup
#input là list chứa đường dẫn của các file html
#output là list chứa các đối tượng BeautifulSoup
def extract_html_to_soup(files):
    #tạo list để chứa các đối tượng BeautifulSoup
    soups = []
    #duyệt qua các file trong list
    for file in files:
        #tạo đối tượng BeautifulSoup từ file
        soup = extract_html(file)
        #thêm đối tượng vào list
        soups.append(soup)
    return soups

#tạo hàm để trích xuất nội dung của một đối tượng BeautifulSoup
#input là đối tượng BeautifulSoup, tên thẻ cần trích xuất và class của thẻ
#output là phần html của thẻ cần trích xuất
def extract_content(soup, tag, class_name):
    # tạo biểu thức chính quy để tìm kiếm các class bắt đầu bằng class_name
    class_regex = re.compile("^" + class_name)
    #tìm tất cả các thẻ có tên và class tương ứng
    tags = soup.find_all(tag, class_=class_regex)
    #lấy nội dung của mỗi thẻ, khi lấy nội dung của một thẻ thì thực hiện xuống dòng
    content = [tag.text + "\n" for tag in tags]
    # print(content)
    return content

#tạo hàm để trích xuất nội dung của một list các đối tượng BeautifulSoup
#input là list chứa các đối tượng BeautifulSoup, tên thẻ cần trích xuất và class của thẻ
#output là list chứa phần html của các thẻ cần trích xuất
def extract_contents(soups, tag, class_name):
    #tạo list để chứa nội dung của các thẻ
    contents = []
    #duyệt qua các đối tượng BeautifulSoup trong list
    for soup in soups:
        #trích xuất nội dung của đối tượng
        content = extract_content(soup, tag, class_name)
        #thêm nội dung vào list
        contents.append(content)
    return contents