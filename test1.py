import src.models.generate as gr

test_gn = gr.generate_password()

print(test_gn.set_setting(russian_letters=False, length=32))

print(test_gn.generate_password())