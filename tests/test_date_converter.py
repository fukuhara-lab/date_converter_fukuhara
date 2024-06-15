import sys
import os

# 現在のスクリプトのディレクトリへのパスを取得し、Pythonの検索パスに追加する
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.date_converter import convert_date

@pytest.mark.parametrize("input_date, expected_output", [
    # 基本的なフォーマット
    ('1995.2.4', '1995-02-04'),
    ('2008/12/23', '2008-12-23'),
    ('平成5年2月6日', '1993-02-06'),
    ('R3/08/30', '2021-08-30'),
    ('20180506', '2018-05-06'),
    # 追加テスト
    ('1985.02.22', '1985-02-22'),
    ('2012/12/3', '2012-12-03'),
    ('昭和63年2月6日', '1988-02-06'),
    ('H11-2-6', '1999-02-06'),
    ('S63/2/6', '1988-02-06'),
    ('19991206', '1999-12-06'),
    # エッジケース
    ('令和1年5月1日', '2019-05-01'),  # 令和元年の特例
    ('昭和1年12月25日', '1926-12-25'),  # 昭和の開始
    ('平成31年4月30日', '2019-04-30'),  # 平成の最終日
    # 異常系
    ('20200631', 'Unknown format'),  # 存在しない日付
    ('R0/1/1', 'Unknown format'),  # 令和元年以前の不正な表記
    ('2020/02/30', 'Unknown format'),  # 存在しない日 (2月30日)
    ('198a/12/05', 'Unknown format'),  # 不正な年の表記
    ('1995.13.40', 'Unknown format')  # 存在しない月と日
])

def test_convert_date(input_date, expected_output):
    assert convert_date(input_date) == expected_output
