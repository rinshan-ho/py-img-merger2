import settings
import cv2
import sys


class img:
    def __init__(self, path):
        # デフォルト値の設定
        self.name = settings.name
        self.ext = settings.ext
        self.method = settings.method
        self.std = settings.std

        self.imgs=path
        self.imgs.sort(key=str.casefold) # DDされたファイルをAtoZソート
        # imgsをimreadし再格納
        for i, img in enumerate(self.imgs):
            self.imgs[i] = cv2.imread(img) # type -> <class 'numpy.ndarray'>

    def set(self):
        # 設定を変える場合
        name = input(f'name ')
        if(name!=''): self.name = name
        ext = input(f'ext ')
        if(ext!=''): self.ext = ext
        method = input(f'method ')
        if(method!=''): self.method = method
        std = input(f'std ')
        if(std!=''): self.std = std

    def merge(self):
        match self.method:
            case '0' | 0 : self.hconcat()
            case '1' | 1 : self.vconcat()
    def hconcat(self):
        match self.std:
            case '0' | 0 :
                self.height = min(img.shape[0] for img in self.imgs)
            case '1' | 1 :
                self.height = max(img.shape[0] for img in self.imgs)
            case _:
                pass
        img_list_resize = [cv2.resize(img, (int(img.shape[1] * self.height / img.shape[0]), self.height)) for img in self.imgs]
        self.img_merged = cv2.hconcat(img_list_resize)
    def vconcat(self):
        match self.std:
            case '0' | 0 :
                self.width = min(img.shape[0] for img in self.imgs)
            case '1' | 1 :
                self.width = max(img.shape[0] for img in self.imgs)
            case _:
                pass
        img_list_resize = [cv2.resize(img, (self.width, int(img.shape[0] * self.width / img.shape[1]))) for img in self.imgs]
        self.img_merged = cv2.vconcat(img_list_resize)

    def output(self):
        cv2.imwrite(f'./{self.name}.{self.ext}', self.img_merged)
        print(f'./{self.name}.{self.ext}')


# 実行
if(sys.argv[1:]): 
    img = img(sys.argv[1:])
    img.set()
    img.merge()
    img.output()
else:
    print("画像をDDしてください\n")
    input("終了します")