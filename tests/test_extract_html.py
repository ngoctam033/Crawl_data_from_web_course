import unittest
from bs4 import BeautifulSoup
import sys
sys.path.append('D:\.CODE\Crawl_data_from_web_course')
from src.extract_html import extract_html
import os

class TestExtractHtml(unittest.TestCase):
    def test_extract_html(self):
        # Tạo một tệp HTML tạm thời để kiểm tra
        with open('test.html', 'w', encoding='utf-8') as file:
            file.write('<html><body><h1>Hello, world!</h1></body></html>')

        # Sử dụng hàm extract_html để lấy dữ liệu từ tệp
        result = extract_html('test.html')

        # Kiểm tra xem kết quả có phải là một đối tượng BeautifulSoup hay không
        self.assertIsInstance(result, BeautifulSoup)

        # Xóa tệp HTML tạm thời sau khi kiểm tra
        os.remove('test.html')


if __name__ == '__main__':
    unittest.main()