import re
import MeCab
import requests
import neologdn

text = open("B2B.txt", "r",encoding="utf-8_sig")
test = open("B2C.txt","a",encoding="utf-8_sig")
url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
r = requests.get(url)
tmp = r.text.split('\r\n')
stopwords = []
#stopwordを取り出す
for i in range(len(tmp)):
    if len(tmp[i]) < 1:
        continue
    stopwords.append(tmp[i])
wakati = MeCab.Tagger(r'-Owakati -d "D:\XAIONDATA\Tabs Adding\mecab-ipadic-neologd"')
punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}【】〕〔『』・■●◎★□○・※．１２３４５６７８９０■「」◆◇＜＞／'
#不要な符号と数字を取り出す
for line in text:
    line = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", line)
    line = re.sub(r'@[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", line)
    line = re.sub(r'&[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", line)
    line = re.sub(r"[%s]+" % punc, "", line)
    line = re.sub('\\n', "", line)
    line = re.sub(r'[0-9]+', "", line)
    new_line = neologdn.normalize(line, repeat=1)
    new_line = wakati.parse(line)
    nums = new_line.split()
    res = []
    for w in nums:
        if not w in stopwords:
            res.append(w)
    fin = " ".join(res)
    write_text = '__label__b' +' ' + fin + '\n'
    test.write(write_text)


text.close()
test.close()