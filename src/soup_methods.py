from bs4 import BeautifulSoup
import re


#tạo hàm để làm sạch html
#input là một đối tượng BeautifulSoup cần làm sạch
#output là một đối tượng BeautifulSoup đã được làm sạch
def clean_html(soup):
    #tạo một list chứa các cặp tên thẻ và class cần xóa
    tags = [['div', 'state'], ['div', 'grade'], ['div', 'questionflag editable'],
             ['h4','accesshide'],['div','qtype_multichoice_clearchoice']]
    #duyệt qua các cặp tên thẻ và class
    for tag in tags:
        #tìm tất cả các thẻ có tên và class tương ứng
        tags = soup.find_all(tag[0], class_=tag[1])
        #duyệt qua các thẻ
        for tag in tags:
            #xóa thẻ
            tag.decompose()
    return soup
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
        soup = clean_html(soup)
        #thêm đối tượng vào list
        soups.append(soup)
    return soups

#tạo hàm để trích xuất nội dung của một đối tượng BeautifulSoup
#input là đối tượng BeautifulSoup, tên thẻ cần trích xuất và class của thẻ
#output là phần html của thẻ cần trích xuất
def extract_content(soup, tag, class_name, text):
    # tạo biểu thức chính quy để tìm kiếm các class bắt đầu bằng class_name
    class_regex = re.compile("^" + class_name)
    #tìm tất cả các thẻ có tên và class tương ứng
    tags = soup.find_all(tag, class_=class_regex)
    #lấy nội dung của mỗi thẻ, khi lấy nội dung của một thẻ thì thực hiện xuống dòng
    if text == True:
        #tạo một list để chứa nội dung văn bản của mỗi tag trong tags
        content = []
        #duyệt qua các thẻ trong tags
        for tag in tags:
            #thêm nội dung của thẻ vào list content
            content = content + [tag.text + '\n']
        return content
    else:
        #tạo một list để chứa các đối tượng soup
        new_soup = []
        #duyệt qua các thẻ trong tags
        for tag in tags:
            #thêm thẻ vào list new_soup
            new_soup = new_soup + [tag.prettify()+ '\n']
        return new_soup

#tạo hàm để trích xuất nội dung của một list các đối tượng BeautifulSoup
#input là list chứa các đối tượng BeautifulSoup, tên thẻ cần trích xuất và class của thẻ
#output là list chứa phần html của các thẻ cần trích xuất
def extract_contents(soups, tag, class_name, text):
    #tạo list để chứa nội dung của các thẻ
    contents = []
    #duyệt qua các đối tượng BeautifulSoup trong list
    for soup in soups:
        #trích xuất nội dung của đối tượng
        content = extract_content(soup, tag, class_name, text)
        #thêm nội dung vào list
        contents = contents + content
    #in ra số phần tử trong contents
    print(len(contents))
    return contents


#tạo một hàm để tìm và xóa những thẻ có nội dung trùng lặp
#input là một đối tượng soups,list các thẻ cần tìm nội dùng trùng lặp cần xóa, class name của thẻ
#output là một đối tuongwj soup sau khi xóa các thẻ trùng lặp
def remove_duplicates(soups, tag, class_name):
    # tạo biểu thức chính quy để tìm kiếm các class bắt đầu bằng class_name
    class_regex = re.compile("^" + class_name)
    #Tạo một mảng để chứa các câu hỏi đã xuất hiện
    seen = []
    #một một mảng tags để chưa các thẻ cần trả về
    tags = []
    #tạo một vòng lặp duyệt qua các phần tử trong mảng soups
    for soup in soups:  
        #chuyển soup thành một đối tượng BeautifulSoup
        soup = BeautifulSoup(soup, 'html.parser')
        #tìm tất cả các thẻ có tên và class tương ứng
        found_tags = soup.find(tag, class_=class_regex)
        #duyệt qua các thẻ
        #kiểm tra xem nội dung của thẻ đã xuất hiện chưa
        if found_tags.get_text() not in  seen:
            #nếu chưa xuất hiện thì thêm nội dung vào mảng seen
            seen = seen + [str(found_tags.get_text())]
            #thêm thẻ vào mảng tags
            tags = tags + [str((soup.prettify() + '\n'))]
        else:
            # #nếu đã xuất hiện thì xóa thẻ
            print('Duplicate found: ', found_tags.text)
            found_tags.decompose()
    #chi biết số phần tử trong mảng tags
    print(len(tags))
    return tags


