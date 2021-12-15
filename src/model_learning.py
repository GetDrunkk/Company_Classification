import fasttext

print("Enter the train text's pathway:")
train_path = input()
model = fasttext.train_supervised(input=train_path,epoch=500, lr=0.5, dim=300, minCount=1)
model.save_model("tabs_adding_nlp.bin")