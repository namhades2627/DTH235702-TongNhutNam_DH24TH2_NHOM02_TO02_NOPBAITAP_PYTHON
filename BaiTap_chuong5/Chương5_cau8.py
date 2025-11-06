print('Câu 8: Tách lấy tên bài hát')
def get_filename(path):
    return path.split("\\")[-1]

def get_name_without_ext(path):
    filename = get_filename(path)
    return filename.rsplit(".", 1)[0]


path = r"d:\music\muabui.mp3"
print("Đường dẫn:", path)
print("Tên file:", get_filename(path))
print("Tên không đuôi:", get_name_without_ext(path))