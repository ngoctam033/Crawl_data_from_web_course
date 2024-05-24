import re


#tạm một hàm để lưu file
#imput là đường dẫn file và nội dung cần lưu, tên file.
def save_file(file_path, data, file_name):
    with open(file_path + '\\' + file_name, 'w', encoding='utf-8') as file:
        for content in data:
            for line in content:
                file.write(line)

#tạo hàm để thực hiện làm sạch dữ liệu
#input là biến chứa dữ liệu cần làm sạch, các biểu thức chính quy cần sử dụng để làm sạch dữ liệu
#output là biến chứa dữ liệu đã được làm sạch
def clean_text(text):

    # Sử dụng biểu thức chính quy để tìm và xóa các chuỗi không mong muốn
    cleaned_text = re.sub('Câu trả lời đã được lưuĐạt điểm 1,0', '', text)
    cleaned_text = re.sub('Xóa cờ', '', cleaned_text)
    cleaned_text = re.sub('Đặt cờ', '', cleaned_text)
    cleaned_text = re.sub('Clear my choice', '', cleaned_text)
    cleaned_text = re.sub('Select one:', '\n', cleaned_text)
    cleaned_text = re.sub('Chưa trả lời', '', cleaned_text)
    cleaned_text = re.sub('Đạt điểm 1,0', '', cleaned_text)
    cleaned_text = re.sub('Đoạn văn câu hỏi', '', cleaned_text)
    cleaned_text = re.sub(' Câu hỏi ', 'Câu hỏi ', cleaned_text)

    return cleaned_text

#tạo hàm để lọc ra câu hỏi bị trung tring file text
#input là nội dung file text
#output là nội dung file text sau khi lọc
# def remove_duplicates(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

    
#     #tạo một kiểu dữ liệu set để lưu các câu hỏi đã xuất hiện
#     seen = set()