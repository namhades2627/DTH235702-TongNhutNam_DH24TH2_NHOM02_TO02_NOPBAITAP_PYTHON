print("====Chương trình giải phương trình bậc 2====");
a = float(input("Nhập a: "));
b = float(input("Nhập b: "));
c = float(input("Nhập c: "));
delta = b**2 - 4*a*c;
if delta > 0:
    x1 = (-b + delta**0.5) / (2*a);
    x2 = (-b - delta**0.5) / (2*a);
    print("Phương trình có 2 nghiệm phân biệt:");
    print("Nghiệm thứ nhất: x1 =", x1);
    print("Nghiệm thứ hai: x2 =", x2);
elif delta == 0:
    x = -b / (2*a);
    print("Phương trình có nghiệm kép:");
    print("Nghiệm: x =", x);
else:
    print("Phương trình vô nghiệm.");