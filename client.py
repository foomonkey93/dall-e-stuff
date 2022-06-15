from docarray import Document
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)



server_url = 'grpc://127.0.0.1:51005'


def gloop(options):
    pick=input("pick a num: ")
    fav = options[int(pick)]

    diffused = fav.post(f'{server_url}', parameters={'skip_rate': 0.5, 'num_images': 36}, target_executor='diffusion').matches
    diffused.plot_image_sprites(fig_size=(10,10), show_index=True)

    return diffused




def runMain():
    prompt=input("say prompt: ")
    da = Document(text=prompt).post(server_url, parameters={'num_images': 3}).matches
    da.plot_image_sprites(fig_size=(10,10), show_index=True)
    keepGoing='y'
    while keepGoing=='y':
        da=gloop(da)
        keepGoing=input("continue, y/n: ")




runMain()