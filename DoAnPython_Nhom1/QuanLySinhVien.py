import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

# ====== Kết nối MySQL ======
def connect_db():
    # Sử dụng thông tin kết nối của bạn
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="qlsv",
        database="QuanLySinhVien"
    )

# ====== Hàm canh giữa cửa sổ ======
def center_window(win, w=700, h=550):
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    win.geometry(f'{w}x{h}+{x}+{y}')

# ====== Cửa sổ chính ======
root = tk.Tk()
root.title("Quản lý sinh viên")
center_window(root, 700, 550)
root.resizable(False, False)

# ====== Tiêu đề ======
lbl_title = tk.Label(root, text="QUẢN LÝ SINH VIÊN", font=("Arial", 18, "bold"))
lbl_title.pack(pady=10)

# ====== Frame nhập thông tin ======
frame_info = tk.Frame(root)
frame_info.pack(pady=5, padx=10, fill="x")

# --- Hàng 1: Mã SV, Họ lót ---
tk.Label(frame_info, text="Mã số SV").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_maso = tk.Entry(frame_info, width=25)
entry_maso.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tk.Label(frame_info, text="Họ lót").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_holot = tk.Entry(frame_info, width=25)
entry_holot.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# --- Hàng 2: Tên, Phái ---
tk.Label(frame_info, text="Tên").grid(row=1, column=2, padx=5, pady=5, sticky="w")
entry_ten = tk.Entry(frame_info, width=25)
entry_ten.grid(row=1, column=3, padx=5, pady=5, sticky="w")

tk.Label(frame_info, text="Giới tính").grid(row=2, column=0, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar(value="Nam")
frame_gender = tk.Frame(frame_info)
tk.Radiobutton(frame_gender, text="Nam", variable=gender_var, value="Nam").pack(side=tk.LEFT)
tk.Radiobutton(frame_gender, text="Nữ", variable=gender_var, value="Nữ").pack(side=tk.LEFT, padx=10)
frame_gender.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# --- Hàng 3: Ngày sinh, Khoa (Combobox) ---
tk.Label(frame_info, text="Ngày sinh").grid(row=2, column=2, padx=5, pady=5, sticky="w")
date_entry = DateEntry(frame_info, width=22, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
date_entry.grid(row=2, column=3, padx=5, pady=5, sticky="w")

tk.Label(frame_info, text="Khoa").grid(row=0, column=2, padx=5, pady=5, sticky="w")
cbb_khoa = ttk.Combobox(frame_info, values=[ "CNTT", "Du Lịch Và Văn Hóa Nghệ Thuật", "Nông Nghiệp - Tài Nguyên Thiên Nhiên", "Sư Phạm",
    "Kinh Tế - Quản Trị Kinh Doanh", "Kỹ Thuật - Công Nghệ - Môi Trường", "Ngoại Ngữ", "Luật - Khoa Học Chính Trị "], width=22)
cbb_khoa.grid(row=0, column=3, padx=5, pady=5, sticky="w")

# --- Hàng 4: Lớp (Nhập tay) ---
tk.Label(frame_info, text="Lớp").grid(row=0, column=4, padx=5, pady=5, sticky="w")
entry_lop = tk.Entry(frame_info, width=25) 
entry_lop.grid(row=0, column=5, padx=5, pady=5, sticky="w")


# ==========================================================
# (Phần code Cửa sổ điểm rèn luyện không thay đổi)
# ==========================================================
def tao_cua_so_diem(maso_cua_sv, hoten_cua_sv):
    win_diem = tk.Toplevel(root)
    win_diem.title(f"Quản lý điểm cho sinh viên: {hoten_cua_sv} ({maso_cua_sv})")
    center_window(win_diem, 800, 600)
    win_diem.grab_set() 

    # --- Các hàm xử lý cho điểm học tập và điểm rèn luyện (giữ nguyên) ---
    # ... (code cửa sổ điểm giữ nguyên như cũ) ...


# ==========================================================
# (Hàm xử lý xem điểm không thay đổi)
# ==========================================================
def xu_ly_xem_diem():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn sinh viên để xem điểm")
        return
    
    item = tree.item(selected[0])
    maso = item['values'][0]
    hoten = f"{item['values'][1]} {item['values'][2]}"
    
    tao_cua_so_diem(maso, hoten)

# ==========================================================
# (Chức năng CRUD sinh viên)
# ==========================================================
def clear_input():
    entry_maso.config(state='normal')
    entry_maso.delete(0, tk.END)
    entry_holot.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    gender_var.set("Nam")
    date_entry.set_date("2003-01-01")
    cbb_khoa.set("")
    entry_lop.delete(0, tk.END)

def load_data():
    for i in tree.get_children():
        tree.delete(i)
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sinhvien")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi tải dữ liệu", f"Lỗi: {err}")

#
# >>>>> HÀM TÌM KIẾM MỚI <<<<<
#
def tim_kiem_sv():
    search_maso = entry_maso.get()
    if not search_maso:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập MSSV cần tìm vào ô Mã số SV.")
        return

    # Xóa dữ liệu cũ trên bảng
    for i in tree.get_children():
        tree.delete(i)
    
    try:
        conn = connect_db()
        cur = conn.cursor()
        # Dùng LIKE để tìm kiếm tương đối (ví dụ: gõ "123" sẽ ra "12345")
        query = "SELECT * FROM sinhvien WHERE maso LIKE %s"
        cur.execute(query, ('%' + search_maso + '%',))
        
        rows = cur.fetchall()
        
        if not rows:
            messagebox.showinfo("Không tìm thấy", f"Không tìm thấy sinh viên nào có mã số chứa '{search_maso}'.")
        else:
            for row in rows:
                tree.insert("", tk.END, values=row)
                
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi tìm kiếm", f"Lỗi: {err}")

def them_sv():
    maso = entry_maso.get()
    holot = entry_holot.get()
    ten = entry_ten.get()
    phai = gender_var.get()
    ngaysinh = date_entry.get()
    khoa = cbb_khoa.get()
    lop = entry_lop.get() 

    if maso == "" or holot == "" or ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập đủ thông tin Mã SV, Họ lót, Tên")
        return

    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO sinhvien (maso, holot, ten, phai, ngaysinh, khoa, lop) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, 
            (maso, holot, ten, phai, ngaysinh, khoa, lop))
        conn.commit()
        load_data()
        clear_input()
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        conn.close()

def xoa_sv():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn sinh viên để xóa")
        return
    
    confirm = messagebox.askyesno("Xác nhận xóa", "Bạn có chắc chắn muốn xóa sinh viên này không?")
    if not confirm:
        return

    maso = tree.item(selected)["values"][0]
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM sinhvien WHERE maso=%s", (maso,))
        conn.commit()
        load_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        conn.close()


def sua_sv():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn sinh viên để sửa")
        return
    
    values = tree.item(selected)["values"]
    if len(values) < 7:
        messagebox.showerror("Lỗi dữ liệu", "Dữ liệu bảng và CSDL không khớp.")
        return
        
    clear_input()
    
    entry_maso.insert(0, values[0])
    entry_maso.config(state='disabled') 
    entry_holot.insert(0, values[1])
    entry_ten.insert(0, values[2])
    gender_var.set(values[3])
    date_entry.set_date(values[4])
    cbb_khoa.set(values[5])
    entry_lop.insert(0, values[6])

def luu_sv():
    maso = entry_maso.get()
    if maso == "":
        messagebox.showwarning("Chưa chọn", "Không có sinh viên nào đang được chọn để lưu")
        return

    holot = entry_holot.get()
    ten = entry_ten.get()
    phai = gender_var.get()
    ngaysinh = date_entry.get()
    khoa = cbb_khoa.get()
    lop = entry_lop.get() 

    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE sinhvien SET holot=%s, ten=%s, phai=%s, ngaysinh=%s, khoa=%s, lop=%s
            WHERE maso=%s
        """, (holot, ten, phai, ngaysinh, khoa, lop, maso))
        conn.commit()
        load_data()
        clear_input()
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi", f"Lỗi: {err}")
    finally:
        conn.close()


# ==========================================================
# (Frame nút - ĐÃ CẬP NHẬT)
# ==========================================================
frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

# --- Hàng nút 1: Các chức năng chính ---
tk.Button(frame_btn, text="Thêm", width=8, command=them_sv).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="Lưu", width=8, command=luu_sv).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_btn, text="Sửa", width=8, command=sua_sv).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_btn, text="Tìm kiếm", width=8, command=tim_kiem_sv, bg="#E8F8F5").grid(row=0, column=3, padx=5, pady=5) # <<< NÚT MỚI
tk.Button(frame_btn, text="Hủy", width=8, command=clear_input).grid(row=0, column=4, padx=5, pady=5)
tk.Button(frame_btn, text="Xóa", width=8, command=xoa_sv).grid(row=0, column=5, padx=5, pady=5)
tk.Button(frame_btn, text="Thoát", width=8, command=root.quit).grid(row=0, column=6, padx=5, pady=5)

# --- Hàng nút 2: Các chức năng phụ ---
# Tạo một frame con để các nút phụ có thể canh giữa
frame_btn_sub = tk.Frame(root)
frame_btn_sub.pack(pady=5)

tk.Button(frame_btn_sub, text="Xem Điểm", width=12, command=xu_ly_xem_diem, bg="#D5F5E3").pack(side=tk.LEFT, padx=10)
tk.Button(frame_btn_sub, text="Tải lại DS", width=12, command=load_data).pack(side=tk.LEFT, padx=10) # <<< NÚT MỚI

# ==========================================================
# (Bảng Treeview - ĐÃ SỬA)
# ==========================================================
lbl_ds = tk.Label(root, text="Danh sách sinh viên", font=("Arial", 10, "bold"))
lbl_ds.pack(pady=5, anchor="w", padx=10)

columns = ("maso", "holot", "ten", "phai", "ngaysinh", "khoa", "lop")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)

tree.heading("maso", text="Mã SV")
tree.heading("holot", text="Họ lót")
tree.heading("ten", text="Tên")
tree.heading("phai", text="Phái")
tree.heading("ngaysinh", text="Ngày sinh")
tree.heading("khoa", text="Khoa")
tree.heading("lop", text="Lớp")
    
tree.column("maso", width=80, anchor="center")
tree.column("holot", width=120)
tree.column("ten", width=70)
tree.column("phai", width=50, anchor="center")
tree.column("ngaysinh", width=90, anchor="center")
tree.column("khoa", width=120)
tree.column("lop", width=80)

tree.pack(padx=10, pady=5, fill="both", expand=True)

# ====== Load dữ liệu ban đầu ======
load_data()
root.mainloop()
