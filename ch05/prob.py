# -*- coding:utf-8 -*-
from pprint import pprint

musician = [
    "Nirvana",
    "Rancid",
    "Slipknot",
    "赤い公園",
    "ポルカドットスティングレイ",
    "岸田教団&THE明星ロケッツ"
]

location = [
    (35.0001664, 136.6940303),  # Aichi
    (35.7980492, 136.4041298),  # Gifu
    (37.6398921, 137.6463404)   # Niigata
]

my = {
    "height": 168,
    "weight": 62,
    "color": "blue"
}

music = {
    "Nirvana": ["Blew", "School", "Lithium"],
    "Rancid": ["Maxwell Murder", "The 11th Hour", "Roots Radicals"],
    "Slipknot": ["742617000027", "Eyeless", "Liberate"],
    "赤い公園": ["絶対的な関係", "NOW ON AIR", "闇夜に提灯"],
    "ポルカドットスティングレイ": ["テレキャスター・ストライプ", "エレクトリック・パブリック", "一大事"],
    "岸田教団&THE明星ロケッツ": ["ワイヤーステップ", "Memory", "少女綺想曲"]
}

if __name__ == '__main__':
    pprint(musician)
    pprint(location)
    pprint(my)
    pprint(music)
