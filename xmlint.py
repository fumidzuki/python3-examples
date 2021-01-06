#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
XMLファイルを読み込むことができるかの確認処理を実施します。

【Install（インストール）】

py -m pip install lxml

【Usage（使用方法）】

py xmlint.py ファイルパス、または、ディレクトリパス
"""

import sys
import os
import pathlib
from lxml import etree


def main():

    # 引数を取得する。
    args = sys.argv

    if len(args) <= 1:
        print('引数が不足しています。ファイル、または、ディレクトリを指定してください。')
        sys.exit()

    # ファイル有無を確認する。
    target_directory = pathlib.Path(args[1])
    if target_directory.exists() == False:
        print('ファイル、または、ディレクトリが存在しましせん。対象パス：{}'.format(target_directory))
        sys.exit()

    # ファイルの読み込みを実施して確認処理を実施する。
    p = pathlib.Path(target_directory)
    if p.is_file():
        validate(p.resolve())
    else:
        for file_path in p.glob("**/*.xml"):
            validate(file_path)
    print('処理が完了しました。')


def validate(path):
    try:
        etree.parse(str(path))
    except Exception as e:
        print('XMLファイルの読み込み処理に失敗しました。ファイル名：{}'.format(path))
        print(e)


if __name__ == '__main__':
    main()
