from datetime import datetime


def diff_func1(list1, list2):
    start_time = datetime.now()
    error = list2.copy()
    for i in range(len(list1) - 1, -1, -1):
        for j in range(len(list2) - 1, -1, -1):
            if list2[j].__eq__(list1[i]):
                list2.pop(j)
                list1.pop(i)
                break
    for ls in list2:
        if error.__contains__(ls):
            print('line ' + str(error.index(ls)) + ", " + ls, end='')

    end_time = datetime.now()
    print(end_time - start_time)


def diff_func2(list1, list2):
    start_time = datetime.now()
    error = []
    for i in range(0, len(list2) - 1, 1):
        for j in range(0, len(list1) - 1, 1):
            if list1[j] == list2[i]:
                break
            else:
                if j == len(list2) - 2:
                    error.append("line: " + str(i) + " , " + list2[i])

    for ls in error:
        print(ls, end='')

    end_time = datetime.now()
    print(end_time - start_time)



with open(r"C:\Users\ivanovsky\Desktop\nds list1.txt", "r") as text_file1:
    text_lines1 = text_file1.readlines()
with open(r"C:\Users\ivanovsky\Desktop\nds list2.txt", "r") as text_file2:
    text_lines2 = text_file2.readlines()


diff_func1(text_lines1.copy(), text_lines2.copy())
diff_func2(text_lines1.copy(), text_lines2.copy())

