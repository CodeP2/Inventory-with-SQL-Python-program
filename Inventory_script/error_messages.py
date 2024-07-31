def data_convertion_error_message(err, user_input, example):
    print(f"""\r#########Error###########
          \r#Incorrect format -> {err}
          \r#Your's Input: >{user_input}<
          \r#Example: {example}
          \r##########################
          """)
    press_enter()


def integer_error_massage(user_input):
    print(f"""\r#########Error###########
          \r#The input is not a number!
          \r#Your input: {user_input}
          \r#Example of a correct input: 1
          \r##########################
          """)
    press_enter()


def menu_choice_error(options):
    print(f"""\r#########Error###########
          \rIncorrect Choice!
          \rcorrect choices are: {options}
          \r##########################
           """)
    press_enter()


def name_too_short_error(user_input):
    print(f"""\r#########Error###########
          \rName of the product is too short!
          \rMinimal product name requirements: 3
          \rYour input: {user_input}
          \r##########################
           """)
    press_enter()


def press_enter():
    input("Press enter to continue...")