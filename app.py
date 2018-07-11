users = {}



class Menu():
    def main_menu(self):
        status = ""
        while status != 'q':
            status = input("Are you registersed user? y/n enter q to quit: ")
            if status == "y":
                self.oldUser()
            elif status == "n":
                self.newUser()

    def newUser(self):
        name = input("create login name: ")
        password = input("create login password: ")



        new = {'name': name, 'password': password}

        id = len(users) + 1

        users[id] = new


    def oldUser(self):
        name = input("Enter login name: ")
        password = input("Enter password")

        for user in users:
            if name == users[user]['name'] and password == users[user]['password']:
                print("login successfully.")
                return

        print('user doesent exist or wrong password')
        return


















