from command_line.data_access.directories import Directories
from command_line.logic.management import Management
from command_line.presentation.interface import Interface

if __name__ == "__main__":
    directories = Directories()
    manage = Management(directories)
    interface = Interface(manage)

    interface.run()
