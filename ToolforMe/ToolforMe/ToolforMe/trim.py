# -*- coding: utf-8 -*-
import sys
from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(description='size')
parser.add_argument("filename",help ='file name' )
parser.add_argument("size",help = 'size')
parser.add_argument("up",help = 'up')
parser.add_argument("right",help='right')
args = parser.parse_args()
#トリミング前の画像の格納先
ORIGINAL_FILE_DIR = "./" + args.filename + "/" 
#トリミング後の画像の格納先
TRIMMED_FILE_DIR = "./" + args.filename + "_cut_data/"

def trim(path,size,up,right):
  im = Image.open(path)
  l = size
  w,h = im.size
  left,top = int(w - l)/2 + right,int(h - l)/2 + up
  right,bottom = int(w + l)/2 + right,int(h + l)/2 + up
  im_trimmed = im.crop((left,top,right,bottom))
  return im_trimmed

def main():
  if os.path.isdir(TRIMMED_FILE_DIR) == False:
    os.makedirs(TRIMMED_FILE_DIR)

  #画像ファイル名を取得
  files = os.listdir(ORIGINAL_FILE_DIR)
  #特定の拡張子のファイルだけを採用。実際に加工するファイルの拡張子に合わせる
  files = [name for name in files if name.split(".")[-1] in ["png","jpg"]]

  for val in files:
    #オリジナル画像へのパス
    path = ORIGINAL_FILE_DIR + val
    #トリミングされたimageオブジェクトを取得
    size = int(args.size)
    up = int(args.up)
    right = int(args.right)
    im_trimmed = trim(path,size,up,right)
    #トリミング後のディレクトリに保存。ファイル名の頭に"cut_"をつけている
    im_trimmed.save(TRIMMED_FILE_DIR+"cut_"+val, quality=95) #qualityは95より大きい値は推奨されていないらしい

if __name__=="__main__":
    main()

