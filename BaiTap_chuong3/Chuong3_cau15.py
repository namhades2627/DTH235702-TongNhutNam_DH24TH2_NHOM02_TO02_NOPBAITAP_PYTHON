temp = {
    "(a) range(5)": range(5),
    "(b) range(5, 10)": range(5, 10),
    "(c) range(5, 20, 3)": range(5, 20, 3),
    "(d) range(20, 5, -1)": range(20, 5, -1),
    "(e) range(20, 5, -3)": range(20, 5, -3),
    "(f) range(10, 5)": range(10, 5),
    "(g) range(0)": range(0),
    "(h) range(10, 101, 10)": range(10, 101, 10),
    "(i) range(10, -1, -1)": range(10, -1, -1),
    "(j) range(-3, 4)": range(-3, 4),
    "(k) range(0, 10, 1)": range(0, 10, 1),
}
for label, r in temp.items():
    print(f"{label} → {list(r)}")