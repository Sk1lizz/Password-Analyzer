import src.models.config as config
import src.utils.create_files as cr
import src.utils.edit_data as gd

test_config = config.config()

config_dict = test_config.get_config_path()

test_cr = cr.create_files(config_dict=config_dict)


print(test_cr.create_file())

dict_cr = test_cr.get_path()

print(dict_cr)

test_gd = gd.edit_data(dict_path=dict_cr)
print(test_gd.add_history("Hello, World!6"))
print(test_gd.get_history(5))
