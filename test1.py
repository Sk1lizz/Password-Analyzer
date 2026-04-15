import src.utils.create_files as create_file
import src.models.config as cfg
import src.utils.edit_data as edit_data


if __name__ == "__main__":
    test_cfg = cfg.config()

    path = test_cfg.get_config_path()

    test_cr = create_file.create_files(config_dict=path)

    test_cr.create_file()

    path = test_cr.get_path()

    edit = edit_data.edit_data(path)
    