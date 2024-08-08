from command_line.data_structures.array import Array
from command_line.data_structures.generic_tree import GenericTree
from command_line.data_structures.sort import insertion_sort


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0


class Directories:
    def __init__(self):
        self.tree = GenericTree(Directory("library root"))
        self.memory_limit = 0
        self.used_memory = 0

    def mkdir(self, name):
        if self.common_name(name):
            return -1
        else:
            self.tree.add(self.tree.current_node.value, Directory(name))

    def mk_file(self, name, size):
        self.tree.add(self.tree.current_node.value, File(name, size))
        self.tree.current_node.value.size += size
        self.used_memory += size

    def cd(self, name):
        for node in self.tree.current_node.children:
            if node.data.value.name == name:
                self.tree.current_node = node.data

    def parent(self):
        """ cd.. """
        if self.tree.current_node.parent is None:
            return
        parent = self.tree.current_node.parent
        self.tree.current_node = parent

    def delete(self, name):
        if self.tree.current_node.value.name == name:
            return -1
        else:
            for node in self.tree.current_node.children:
                if node.data.value.name == name:
                    self.tree.current_node.children.delete(node.data)

    def sort(self, key):
        arr = self.create_array()
        sorted_arr = insertion_sort(arr, key)
        return sorted_arr

    def set_mem_limit(self, new_limit):
        self.memory_limit = new_limit
        print(self.memory_limit)
        if self.used_memory > self.memory_limit:
            self.free_memory(self.used_memory - self.memory_limit)

    def common_name(self, name):
        for node in self.tree.current_node.children:
            if node.data.value.name == name:
                return True

    def curr_dir(self):
        return self.tree.current_node.value.name

    def create_array(self):
        length = len(self.tree.current_node.children)
        arr = Array(length)
        for node in self.tree.current_node.children:
            arr.add(node.data.value)
        return arr

    def free_memory(self, needed_space):  # needed space is the amount that needs to be deleted
        freed_space = 0
        while freed_space <= needed_space:
            oldest = self.tree.current_node.children.head_node()
            print("oldest files to delete:", oldest.data.value.name, "size:", oldest.data.value.size)
            freed_space += oldest.data.value.size
            self.tree.current_node.children.delete_first()
            print("freed space:", freed_space)
            self.used_memory -= freed_space
            print("used memory:", self.used_memory)
            break

    def sub_dir(self):
        return self.tree.current_node
