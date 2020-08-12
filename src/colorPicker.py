import cv2
from sklearn.cluster import KMeans
from typing import List


class ColorPicker:
    def __init__(self, img):
        self.img = img

    def convertToHex(self, cluster) -> List[str]:
        # 16進数に変換
        cluster_arr = cluster.cluster_centers_.astype(
            int, copy=False
        )
        res: List[str] = []
        # rgb to hex
        for rgb in cluster_arr:
            color_hex = '#%02x%02x%02x' % tuple(rgb)
            res.append(color_hex)
        return res

    def main(self) -> List[str]:
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img = img.reshape(
            (img.shape[0] * img.shape[1], 3)
        )
        # KMeans法でクラスター化
        cluster = KMeans(n_clusters=4)
        cluster.fit(X=img)
        # rgb から Hexに変換
        res: List[str] = self.convertToHex(cluster)
        return res
