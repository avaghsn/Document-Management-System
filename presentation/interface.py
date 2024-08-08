class Interface:
    def __init__(self, management):
        self.management = management

    def run(self):
        print("--------- < Command List > ---------")
        print("make dir : mkdir dir-name")
        print("make file : mk-file name size")
        print("change dir : cd dir-name")
        print("previous dir : cd..")
        print("del : del dir name | del file name")
        print("sort by name : sort-name")
        print("sort by size: sort-size")
        print("set mem limit : set-limit size")
        print("sub dir : tree")
        print()

        while True:
            print(self.management.curr_dir())

            inp = input(f"> ")
            command = inp.split(' ')

            if command[0] == "mkdir":
                self.mkdir(command[1])
            elif command[0] == "cd":
                self.cd(command[1])
            elif command[0] == "cd..":
                self.parent()
            elif command[0] == "mk-file":
                name, size = command[1], command[2]
                self.mk_file(name, int(size))
            elif command[0] == "del":
                self.delete(command[1])
            elif command[0] == "sort-name":
                self.sort_by_name()
            elif command[0] == "sort-size":
                self.sort_by_size()
            elif command[0] == "set-limit":
                self.set_mem_limit(command[1])
            elif command[0] == "tree":
                self.sub_dir()

    def mkdir(self, name):
        result = self.management.mkdir(name)
        if result == -1:
            print("duplicate directory")

    def mk_file(self, name, size):
        self.management.mk_file(name, size)

    def cd(self, name):
        self.management.cd(name)

    def parent(self):
        """ cd.. """
        self.management.parent()

    def delete(self, name):
        result = self.management.delete(name)
        if result == -1:
            print("can't delete current directory")

    def sort_by_name(self):
        sorted_arr = self.management.sort_by_name()
        for i in range(len(sorted_arr)):
            print(sorted_arr[i].name)

    def sort_by_size(self):
        sorted_arr = self.management.sort_by_size()
        for i in range(len(sorted_arr)):
            print("name:", sorted_arr[i].name, "total size:", sorted_arr[i].size)

    def set_mem_limit(self, limit):
        print(limit)
        self.management.set_mem_limit(int(limit))

    def sub_dir(self):
        """ tree """
        sub_dir = self.management.sub_dir()
        print(" ", sub_dir.value.name)
        for node in sub_dir.children:
            print("   ", node.data.value.name)
