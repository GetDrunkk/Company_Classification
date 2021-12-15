# coding: UTF-8
import fasttext as ft

print("Enter the model's path")
path_of_model = input()
model = ft.load_model(path_of_model)

print("Enter the test file's path")
path_of_test = input()

result_of_data = model.test(path_of_test)
print("The result of data :")
print(f'Sample:{result_of_data[0]}  Precision:{result_of_data[1]}  Recall:{result_of_data[2]}')
