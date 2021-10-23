def trapezoid_area(top, bottom, height):
    try:
        top, bottom, height = int(top), int(bottom), int(height)
        area = (top + bottom)*height*0.5
        return area
    except:
        return '整数を入力してください'

# if __name__ == '__main__':
#     top, bottom, height = input().split()
#     print(trapezoid_area(top, bottom, height))