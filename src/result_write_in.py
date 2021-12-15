import fasttext as ft
#各データの予測した結果を記入　
text = open("data/test/final_test.txt", "r", encoding="utf-8_sig")
sample = open("data/result/result.txt","w+", encoding="utf-8_sig")
model = ft.load_model('model/tabs_adding_nlp_last.bin')
FP = 0
FN = 0
for line in text:
    if line[0] != "_":
        continue
    rs = line.rstrip('\n')
    aline = rs[11:]
    res = model.predict(aline,k=2)
    if res[0][0][9] == line[9] :
        new_line = "TURE" + "  " + line
        sample.write(new_line)
        r = res[0][0] + " " + res[0][1] + "\n"
        sample.write(r)
        k = str(res[1][0]) + " " + str(res[1][1])+ "\n"
        sample.write(k)
        sample.write("\n")
    else:
        new_line = "FALSE" + "  " + line
        sample.write(new_line)
        r = res[0][0] + res[0][1]+ "\n"
        sample.write(r)
        k = str(res[1][0]) + " " + str(res[1][1])+ "\n"
        sample.write(k)
        sample.write("\n")


''' 
    if line[9] == 'b':
        fpn = 'P'
        b+=1
    else:
        fpn = 'N'
        c+=1
    if rewrite_ans == 'F' and fpn == 'P':
        FP += 1
    elif rewrite_ans == 'F' and fpn == 'N':
        FN += 1
'''


#print(FN)
#print(FP)
text.close()
sample.close()
