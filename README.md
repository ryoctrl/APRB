# 概要

Haar-like顔認識でアニメ顔を識別してTwitterのUserStreamから流れてくる画像をRTするBot.

## Description
1. UserStreamAPIから画像付きのTweetをとってくる
1. 今後の貼ってのためとりあえず全部保存する
1. 画像を顔認識にかける
1. アニメ顔が認識された場合、保存した顔像を他のディレクトリに移動しTwitterAPIにRTリクエストを送る

## Requirement
Python 3.x(recommend: 2.6.15)
OpenCV 2.0

## Usage
	
	$ git clone https://github.com/ryoctrl/APRB.git
	$ cd APRB
	$ cp .env_default .env
	$ vi .env # .envにTwitterのAPI情報を入力
	$ vi config.ini #user = に.envに入力したAccoutNameを入力 
	$ python src/main.py

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[tcnksm](https://github.com/tcnksm)
