## dplearning
#概要
Ruby on rails と python を組み合わせて、アップロードした画像にラベルとそのラベルの重要度(注目度のようなもの)を付与するアプリケーションです。
ラベルと重要度の付与には深層学習を用いて、付与を行います。railsではアップロードされた画像とタイトル、ファイルパス、付与されたラベルと重要度を画像ごとに一つのページに表示するようにしました。

#実行環境
python
バージョン：3.6.8
モジュール：numpy,keras,json,cv2,tensorflow
ruby
バージョン：2.4.0
rails
バージョン：5.2.2
Gemに関してはGemfile参照

#実行方法
ファイルパスを適切なパスに変更
railsでサーバーを起動
ブラウザからアクセスすることで、indexページに移動します。Add Newからアップロードページに移動します。アップロードした画像(ページ)はindexの[delete]で削除できます。

予測可能なラベルは以下の116個になります。
'airplane', 'baby', 'background', 'ball', 'baseball', 'bat', 'bathroom', 'beach', 'bear', 'bed', 'bench', 'bike', 'bird', 'blue', 'board', 'boat', 'bowl', 'boy', 'building', 'bus', 'cake', 'camera', 'car', 'cat', 'cell', 'chair', 'child', 'city', 'clock', 'computer', 'couch', 'counter', 'couple', 'desk', 'dirt', 'display', 'dog', 'elephant', 'fence', 'field', 'fire', 'floor', 'food', 'frisbee', 'fruit', 'giraffe', 'girl', 'glass', 'grass', 'ground', 'group', 'head', 'hill', 'horse', 'hydrant', 'keyboard', 'kitchen', 'kite', 'laptop', 'light', 'living', 'luggage', 'man', 'middle', 'mirror', 'motorcycle', 'mountain', 'ocean', 'orange', 'park', 'parking', 'person', 'phone', 'photo', 'picture', 'pizza', 'plane', 'plate', 'player', 'pole', 'racket', 'refrigerator', 'road', 'room', 'sandwich', 'shirt', 'sidewalk', 'sink', 'skateboard', 'sky', 'slope', 'snow', 'soccer', 'station', 'street', 'suit', 'surfboard', 'table', 'tennis', 'tie', 'toilet', 'tower', 'track', 'traffic', 'train', 'tree', 'truck', 'umbrella', 'vase', 'view', 'wall', 'water', 'wave', 'window', 'woman', 'zebra'
