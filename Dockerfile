# 使用するPythonのベースイメージ
FROM python:3.8-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトファイルのコピー
COPY . /app

# コンテナ起動時にpytestを実行
CMD ["pytest", "-v"]
