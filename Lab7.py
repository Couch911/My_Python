import string

def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Файл", file_name, "не вдалося відкрити")
        return None
    else:
        print("Файл", file_name, " відкрито")
        return file


file1_name = "TF4_1.txt"
file2_name = "TF4_2.txt"

file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    file_1_w.write("Цей файл заповнено випадковим текстом, цей текстом.\n")
    file_1_w.write("Ще цей файл трохи текстом.\n")
    print("Інформацію  записано у TF4_1.txt")
    file_1_w.close()
    print("Файл TF4_1.txt закрито\n")

file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r is not None and file_2_w is not None:
    text = file_2_r.read()

    for ch in string.punctuation + "—«»…":
        text = text.replace(ch, " ")

    words = text.split()
    counts = {}

    for w in words:
        length = len(w)
        counts[length] = counts.get(length, 0) + 1

    for length in sorted(counts):
        file_2_w.write(f"Слів з {length} символів: {counts[length]}\n")

    file_2_r.close()
    file_2_w.close()
    print("Файли TF4_1.txt і TF4_2.txt закрито\n")

print("Вміст TF4_2.txt:")
file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    for line in file_3_r:
        print(line.strip())

    print("Файл TF4_2.txt закрито")
    file_3_r.close()
