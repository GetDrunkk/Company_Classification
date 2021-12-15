# NAME
company-tagger
 
# About data
 
最後の訓練データ: final_train.txt  
　　テストデータ :final_test.txt

最後の結果:result.txt  
各事業内容に関しての予測、b2bとb2cと判断する確率は内容の下にある

 
# About programs
Preprocessing.py:前処理とテストデータと訓練データ作成するものです。前処理で、mecab-ipadic-neologdという辞書を使ってstopwordsを取り出すこと。最後にラベル追加した。

mecab_test:分かち書きや新しい辞書の使い方などのテスト用プログラムです。

learning.py:Fasttextモデルを訓練する。

Prediction.py:テストデータの検証。

rewrite.py:検証のデータを書き込む。
# Usage
環境の構築
```
pip install -r requirements.txt
```

モデルの訓練
```
python model_learning.py
(compiler):Enter the train text's pathway:
input:トレーニングテキストのpath(ex.D:\XAIONDATA\Tabs Adding\data\train\final_train.txt)
```
訓練したモデルはsrc(プログラムのファイル)に保存

結果の予測
```
python model_prediction.py
(compiler):Enter the model's path
input:モデルのpath(ex.D:\XAIONDATA\Tabs Adding\model\tabs_adding_nlp_last.bin)
(compiler):Enter the test file's path
input:テストテキストのpath(ex.D:\XAIONDATA\Tabs Adding\data\test\final_test.txt)
```
 
# Reference

fasttext  : https://fasttext.cc/docs/en/supervised-tutorial.html  
mecab : https://taku910.github.io/mecab/  
mecab-ipadic-neologd : https://github.com/neologd/mecab-ipadic-neologd  
 