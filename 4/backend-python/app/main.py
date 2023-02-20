from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods="GET",
    allow_headers=["*"]
)

class Menu():
    def __init__(self, id, title, category, price, image_url):
         self.id = id
         self.title = title
         self.category = category
         self.price = price
         self.image_url = image_url

albums = [ 
    Menu(1, "ピザ", "Italian", "2000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Pizza.jpg?sp=r&st=2023-02-19T14:19:21Z&se=2025-04-30T22:19:21Z&spr=https&sv=2021-06-08&sr=b&sig=nTeyIH2EsiqqyHqLofbD8VajWr2ViAq6vp3n%2FvilbEA%3D"),
    Menu(2, "パスタ", "Italian", "2000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Pasta.jpg?sp=r&st=2023-02-19T14:20:18Z&se=2025-03-31T22:20:18Z&spr=https&sv=2021-06-08&sr=b&sig=G%2Fb17Wd9oNNr98tyVHhkWJ0xJUVkYyskOd3SIwclKFU%3D"),
    Menu(3, "リゾット", "Italian", "1500 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Risotto.jpg?sp=r&st=2023-02-19T14:20:39Z&se=2025-03-31T22:20:39Z&spr=https&sv=2021-06-08&sr=b&sig=x9sQCqj96%2FvhjX0VJjgWXM6rKKUFQ1R8FVncOACvahQ%3D"),
    Menu(4, "ジェラート", "Italian", "500 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Gelato.jpg?sp=r&st=2023-02-19T14:21:01Z&se=2025-01-31T22:21:01Z&spr=https&sv=2021-06-08&sr=b&sig=3OwRCjoi1LkrPFPFGa2xr2qOt3VT6yc7lPHOSe7rlsQ%3D"),
    Menu(5, "ドルチェ", "Italian", "500 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Dolce.jpg?sp=r&st=2023-02-19T14:21:26Z&se=2025-02-28T22:21:26Z&spr=https&sv=2021-06-08&sr=b&sig=W7AwBs5Z%2FGYezFvaR7CihMZ%2FLibQQHAwmJnZaODhqvc%3D"),
    Menu(6, "ラザニア", "Italian", "1500 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Lasagna.jpg?sp=r&st=2023-02-19T14:21:45Z&se=2025-04-30T22:21:45Z&spr=https&sv=2021-06-08&sr=b&sig=hRwMpOSbMt%2Fwz9Ta1oNWIzN1q4e9qwuB8i9ha9FQPi8%3D"),
    
    Menu(7, "火鍋", "Chinese", "2000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/HotPot.jpg?sp=r&st=2023-02-19T14:22:04Z&se=2024-12-31T22:22:04Z&spr=https&sv=2021-06-08&sr=b&sig=L9XzMjeGaCMii6hq3jJDIqDWcMVJrxJ3nxk9rmIJVRI%3D"),
    Menu(8, "麻婆豆腐", "Chinese", "1500 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/MapoTofu.jpg?sp=r&st=2023-02-19T14:22:24Z&se=2025-01-31T22:22:24Z&spr=https&sv=2021-06-08&sr=b&sig=iU6BF1%2B%2Fyuozayuf3GJzZOQtNL74mOlwtIWT6nAG2uU%3D"),
    Menu(9, "北京ダック", "Chinese", "3000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/RoastedDuck.jpg?sp=r&st=2023-02-19T14:22:43Z&se=2025-03-31T22:22:43Z&spr=https&sv=2021-06-08&sr=b&sig=f0U%2FzLzIwSTfD555E6yaLtsM4julH43JkUZGObAoAJg%3D"),
    Menu(10, "点心", "Chinese", "1000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/DimSum.jpg?sp=r&st=2023-02-19T14:23:00Z&se=2025-02-28T22:23:00Z&spr=https&sv=2021-06-08&sr=b&sig=HPzRb%2BVCWmqRP%2FRuhdjmYZU4%2FcjwLznsnDB9CBh92CM%3D"),
    Menu(11, "炒飯", "Chinese", "1000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/FriedRice.jpg?sp=r&st=2023-02-19T14:23:27Z&se=2025-03-31T22:23:27Z&spr=https&sv=2021-06-08&sr=b&sig=fvsuA3E00dzyZ2cgdYyN70Dy5qB2IBAlSvOhKM46cGM%3D"),
    Menu(12, "揚げ春巻", "Chinese", "1000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/EggRoll.jpg?sp=r&st=2023-02-19T14:23:48Z&se=2025-01-31T22:23:48Z&spr=https&sv=2021-06-08&sr=b&sig=2ocVG04rzpz9yDkWwx8u32w7Nd0u38fuZhI59oYOGoY%3D"),
    
    Menu(13, "らーめん", "Japanese", "1000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Ramen.jpg?sp=r&st=2023-02-19T14:24:06Z&se=2025-03-31T22:24:06Z&spr=https&sv=2021-06-08&sr=b&sig=Vtxchhh4KR3SuSd2L%2Fm1OV1LCJ059Kj8fbQE0VjpxYk%3D"),
    Menu(14, "すし", "Japanese", "3000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Sushi.jpg?sp=r&st=2023-02-19T14:24:23Z&se=2025-02-28T22:24:23Z&spr=https&sv=2021-06-08&sr=b&sig=wfWTVn7omGehJmqzR%2BxC2fju%2FcbuAnW%2F7Y5JAvM9dSg%3D"),
    Menu(15, "てんぷら", "Japanese", "3000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Tempura.jpg?sp=r&st=2023-02-19T14:24:40Z&se=2025-02-28T22:24:40Z&spr=https&sv=2021-06-08&sr=b&sig=rAaa%2BuGRm23EmE8%2FFBVvTIfk3aWdzsLNUZippeUS%2BEA%3D"),
    Menu(16, "うな重", "Japanese", "3000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Unaju.jpg?sp=r&st=2023-02-19T14:24:57Z&se=2025-01-31T22:24:57Z&spr=https&sv=2021-06-08&sr=b&sig=6oTgBJ5kBf4mUmRLz3gh%2BNXhTIAatfh5vGRACB%2F9lWQ%3D"),
    Menu(17, "お好み焼き", "Japanese", "1000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/Okonomiyaki.jpg?sp=r&st=2023-02-19T14:25:14Z&se=2025-02-28T22:25:14Z&spr=https&sv=2021-06-08&sr=b&sig=2JQMKwTlEQF91vbQuSAdM8Z4rKhUrX%2BempfMDLevYwU%3D"),
    Menu(18, "焼き魚", "Japanese", "1000 JPY", "https://nonprodsharestorage.blob.core.windows.net/imgs/GrilledFish.jpg?sp=r&st=2023-02-19T14:25:44Z&se=2024-12-31T22:25:44Z&spr=https&sv=2021-06-08&sr=b&sig=dzP5fIiJ%2BW9Lp3%2FJjbS9ujw67y%2FKuSu6Eq%2FcxNxPrvk%3D")
]

@app.get("/")
def read_root():
    return {"Azure Container Apps Python Sample API"}


@app.get("/menus")
def get_albums():
    return albums
