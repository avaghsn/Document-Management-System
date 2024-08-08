class Management:
    def __init__(self, directories):
        self.directories = directories

    def mkdir(self, name):
        return self.directories.mkdir(name)

    def mk_file(self, name, size):
        return self.directories.mk_file(name, size)

    def cd(self, name):
        self.directories.cd(name)

    def parent(self):
        """ cd.. """
        self.directories.parent()

    def delete(self, name):
        return self.directories.delete(name)

    def sort_by_name(self):
        return self.directories.sort(lambda x: x.name)

    def sort_by_size(self):
        return self.directories.sort(lambda x: int(x.size))

    def set_mem_limit(self, limit):
        self.directories.set_mem_limit(limit)

    def curr_dir(self):
        return self.directories.curr_dir()

    def sub_dir(self):
        return self.directories.sub_dir()
