time_in_second = int(input('please input a time in seconds: '))
minuts = time_in_second // 60
seconds = time_in_second % 60
hours = minuts // 60
minuts_for_answer = minuts % 60
print(f"{hours:02.0f}:{minuts_for_answer:02.0f}:{seconds:02.0f}")

