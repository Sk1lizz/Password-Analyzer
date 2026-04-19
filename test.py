#import src.views.main_window as window
from src import create_files
from src import config

import src as window

if __name__ == "__main__":
    cfg = config()

    path = cfg.get_config_path()

    cr = create_files(config_dict=path)

    cr.create_file()

    path = cr.get_path()
    main = window.main()

    main.set_config(path)

    main.start()