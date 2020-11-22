import pyautogui
import time
import os
import datetime

# ページ数（とるスクリーンショットの画像数）
page = 2

#(ここでどこのPC画面をとるか設定する)
# 取得左上座標
x1, y1 = 150, 280
# 取得右下座標
x2, y2 = 1000, 1000
# スクショ間隔(秒)
span = 1
# 出力フォルダ頭文字
foldername1 = "screenshot"
# 出力ファイル頭文字
filename = "picture"

# ここからスクリーンショット取得処理

# 待機時間2秒
# (この間にスクショを取得するウィンドウをアクティブにする)
time.sleep(2)

# 出力フォルダ作成(フォルダ名：頭文字_年月日時分秒)
folder_name = foldername1 + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
os.mkdir(folder_name)

# ページ数分スクリーンショットをとる
for p in range(page):
    # 出力ファイル名(頭文字_連番.png)
    out_filename = filename + "_" + str(p+1).zfill(4) + '.png'
    ####################################
    # スクリーンショット取得・保存処理 
    # キャプチャ範囲： 左上のx座標, 左上のy座標, 幅, 高さ
    s = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    # 出力パス： 出力フォルダ名 / 出力ファイル名
    s.save(folder_name + '/' + out_filename)
    # 右矢印キー押下
    pyautogui.keyDown('right')
    # 次のスクリーンショットまで待機
    time.sleep(span)