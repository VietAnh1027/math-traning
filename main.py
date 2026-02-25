import random
import pandas as pd
from tabulate import tabulate
import numpy as np

def phepTinh(toanTu: str, n: int, a: int):
	result = {"Câu hỏi": [], "Đáp án nhập": [], "Trạng thái": []}
	if toanTu not in ["*", "/"]:
		print("Sẽ cập nhật sau !")
		return result
	i = 0
	# Tạo khoảng giá trị phù hợp
	value_range = np.arange(1,11)
	current_length = len(value_range)
	if toanTu == "*":
		while i < n:
			if current_length == 0:
				current_length = len(value_range)
			# Lấy ra phần tử được chọn ngẫu nhiên
			idx = random.randint(0,current_length-1)
			b = value_range[idx]
			# Đổi chỗ phần từ được chọn với phần tử cuối cùng trong khoảng được chọn
			value_range[idx], value_range[current_length-1] = value_range[current_length-1], value_range[idx]
			# Bỏ phần tử cuối cùng khỏi khoảng được chọn
			current_length -= 1
			ques = f"{a} {toanTu} {b}"
			result['Câu hỏi'].append(ques)
			answer = input(f"Câu {i+1}: " + ques + " = ").strip()
			result['Đáp án nhập'].append(answer)
			real_result = str(eval(ques))

			if answer == real_result:
				result['Trạng thái'].append("Đúng")
			elif answer == "exit":
				result['Trạng thái'].append("Dừng chương trình")
				break
			else:
				print(" - Đáp án sai !")
				print(f" - Đáp án đúng là {real_result}")
				result['Trạng thái'].append("Sai")
			i+=1
			print(f"Độ dài mảng hiện tại: {current_length}")
			print(value_range)

	if toanTu == "/":
		value_range = value_range*a
		while i < n:
			if current_length == 0:
				current_length = len(value_range)
			idx = random.randint(0,current_length-1)
			b = value_range[idx]
			value_range[idx], value_range[current_length-1] = value_range[current_length-1], value_range[idx]
			current_length -= 1
			ques = f"{b} {toanTu} {a}"
			result['Câu hỏi'].append(f"{b} : {a}")

			answer = input(f"Câu {i+1}: {b} : {a} = ").strip()
			result['Đáp án nhập'].append(answer)
			real_result = str(int(eval(ques)))

			if answer == real_result:
				result['Trạng thái'].append("Đúng")
			elif answer == "exit":
				result['Trạng thái'].append("Dừng chương trình")
				break
			else:
				print(" - Đáp án sai !")
				print(f" - Đáp án đúng là {real_result}")
				result['Trạng thái'].append("Sai")
			i+=1
			print(f"Độ dài mảng hiện tại: {current_length}")
			print(value_range)

	return result

# try:
if __name__ == "__main__":
	n = int(input("Số lượng câu hỏi luyện tập: "))
	a = int(input("Luyện tập bảng mấy ? : "))
	while True:
		select = input("""Có các tùy chọn sau: 
	1. Phép nhân
	2. Phép chia
Nhập lựa chọn của bạn: """).strip()
		if select == "1":
			result = phepTinh("*", n, a)
			break
		elif select == "2":
			result = phepTinh("/", n, a)
			break
		else: print("Hãy chọn lại !")

	df_result = pd.DataFrame(result)
	ques_right = len(df_result[df_result['Trạng thái'] == 'Đúng'])
	ques_wrong = len(df_result[df_result['Trạng thái'] == 'Sai'])
	print("\n", "="*30, "BẢNG KẾT QUẢ", "="*30)
	print(f"""
Số câu hỏi : {n}
Số câu đúng: {ques_right}
Số câu sai : {ques_wrong}""")
	print("=== ĐIỂM SỐ: ",  ques_right* (10/n), " điểm")
	print(tabulate(df_result, headers='keys', tablefmt='grid', showindex=False))
# except:
# 	print("\nTham số nhập không hợp lệ !")