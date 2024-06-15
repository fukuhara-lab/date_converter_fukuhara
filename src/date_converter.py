import re
from datetime import datetime

def convert_date(input_date):
    try:
        # YYYY.MM.DD形式の日付を確認し、変換
        if re.match(r'\d{4}\.\d{1,2}\.\d{1,2}', input_date):
            date = datetime.strptime(input_date, '%Y.%m.%d')
            return date.strftime('%Y-%m-%d')
        
        # YYYY/MM/DD形式の日付を確認し、変換
        elif re.match(r'\d{4}/\d{1,2}/\d{1,2}', input_date):
            return datetime.strptime(input_date, '%Y/%m/%d').strftime('%Y-%m-%d')
        
        # 日本の元号（平成、令和、昭和）を含む日付を確認し、西暦に変換
        elif re.match(r'(平成|令和|昭和)(\d+)年(\d+)月(\d+)日', input_date):
            era, year, month, day = re.search(r'(平成|令和|昭和)(\d+)年(\d+)月(\d+)日', input_date).groups()
            year = int(year)
            if year == 0:
                return "Unknown format"  # 0年は存在しない
            month = int(month)
            day = int(day)
            era_start = {'平成': 1989, '令和': 2019, '昭和': 1926}
            year = era_start[era] + year - 1
            return datetime(year, month, day).strftime('%Y-%m-%d')
        
        # R/H/S（令和/平成/昭和の省略形）と"スラッシュ"で区切られた日付を確認し、西暦に変換
        elif re.match(r'(R|H|S)(\d+)/(\d+)/(\d+)', input_date):
            era, year, month, day = re.search(r'(R|H|S)(\d+)/(\d+)/(\d+)', input_date).groups()
            year = int(year)
            if year == 0:
                return "Unknown format"  # 0年は存在しない
            month = int(month)
            day = int(day)
            era_start = {'R': 2019, 'H': 1989, 'S': 1926}
            year = era_start[era] + year - 1
            return datetime(year, month, day).strftime('%Y-%m-%d')
        
        # R/H/S（令和/平成/昭和の省略形）と"ハイフン"で区切られた日付を確認し、西暦に変換
        elif re.match(r'(R|S|H)(\d+)-(\d+)-(\d+)', input_date):
            era, year, month, day = re.search(r'(R|S|H)(\d+)-(\d+)-(\d+)', input_date).groups()
            year = int(year)
            if year == 0:
                year = 1  # 元号の初年度を1年とする
            month = int(month)
            day = int(day)
            era_start = {'R': 2019, 'H': 1989, 'S': 1926}
            year = era_start[era] + year - 1
            return datetime(year, month, day).strftime('%Y-%m-%d')
        
        # YYYYMMDD形式の日付を確認し、変換
        elif re.match(r'\d{8}', input_date):
            return datetime.strptime(input_date, '%Y%m%d').strftime('%Y-%m-%d')
        
        # 一致するフォーマットがない場合は未知の形式として処理
        else:
            return "Unknown format"
    
    except ValueError:
        # datetime.strptime() が無効な日付に対して ValueError を投げる場合
        return "Unknown format"
