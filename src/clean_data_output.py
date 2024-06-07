import re


#tạm một hàm để lưu file
#imput là đường dẫn file và nội dung cần lưu, tên file.
def save_file(file_path, data, file_name):
    with open(file_path + '\\' + file_name, 'w', encoding='utf-8') as file:
        for content in data:
            file.write(str(content))

#tạo hàm để thực hiện làm sạch dữ liệu
#input là biến chứa dữ liệu cần làm sạch, các biểu thức chính quy cần sử dụng để làm sạch dữ liệu
#output là biến chứa dữ liệu đã được làm sạch


#tạo hàm để lọc ra câu hỏi bị trung tring file text
#input là nội dung file text
#output là nội dung file text sau khi lọc
# def remove_duplicates(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

    
#     #tạo một kiểu dữ liệu set để lưu các câu hỏi đã xuất hiện
#     seen = set()