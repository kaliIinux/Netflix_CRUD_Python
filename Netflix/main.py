import inquirer
from usuário import Login, menu_users
from Filme import menu_films


def menu_main():

    while True:
        
        questions = [
        inquirer.List('option',
                        message="What do you want to do?",
                        choices=['LOGIN', 'USER SETTINGS', 'EXIT'],
                    ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['option']
        
        if choice == 'EXIT':
            print("\x1b[2J\x1b[1;1H", end="")
            exit()

        elif choice == 'LOGIN':
            
            if Login() == True:
                print("\x1b[2J\x1b[1;1H", end="")
                menu_films()  
        
        elif choice == 'USER SETTINGS':
            print("\x1b[2J\x1b[1;1H", end="")
            menu_users()
        
        else:
            exit()

menu_main()
