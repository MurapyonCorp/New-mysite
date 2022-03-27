import collections  # python標準ライブラリのパッケージをインストールするときは
import os           # 1行に1つずつ記載する。
import sys

import termcolor  # サードパーティのパッケージをインストールするときはpython標準ライブラリと1行空ける。

import lesson_package # 会社やチームなどの組織が開発したパッケージ

import config
"""
上から「python標準ライブラリ → サードパーティのアプリ → 会社やチーム(自分たち)のパッケージ → ローカルのファイル」という順で書く。
それぞれ複数のパッケージをインストールするときは先頭がアルファベット順位なるように書く。
"""

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print('\n')

print(sys.path)
"""
sys.pathに書かれていない場所のファイルやモジュールは読み込めない。
ローカルのパッケージが一番最初に優先されるため、標準ライブラリやサードパーティと同じようなパッケージをローカルに作ってしまうと
それが最初に読み込まれてしまうため注意が必要になる。
"""