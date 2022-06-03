class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self,command):
        spaces = ' ' * self.get_level()*2 + '|' +'_'* self.get_level()
        if command == 'name':
            print(spaces + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree(command)
        elif command == 'designation':
            print(spaces + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree(command)
        else:
            print(spaces + self.name + ' ('+self.designation+')')
            if self.children:
                for child in self.children:
                    child.print_tree(command)
    def print_by_level(self,level):
        spaces = ' ' * self.get_level()*2 + '|' +'_'* self.get_level()
        print(spaces+self.name)
        if self.get_level() < level:
            for child in self.children:
                child.print_by_level(level)     
def buld_management_tree():
    root = TreeNode("Nilupul","CEO")
    #this is the CTO tree
    cto = TreeNode('Chinmay','CTO')
    infrasHead = TreeNode('Vishwa','Infrastructure Head')
    cloudManager = TreeNode('Dhaval','Cloud Manager')
    appManager = TreeNode('Abhijit','App Manager')
    infrasHead.add_child(cloudManager)
    infrasHead.add_child(appManager)
    cto.add_child(infrasHead)
    cto.add_child(TreeNode('Aamir', 'Application Head'))
    #HR Head tree
    hrHead = TreeNode('Gels','HR Head')
    hrHead.add_child(TreeNode('Peter','Recruitement Manager'))
    hrHead.add_child(TreeNode('Waqas','Policy Manager'))
    #root Tree

    root.add_child(hrHead)
    root.add_child(cto)
    return root

def main():
    root = buld_management_tree()
    root.print_tree('name')
    root.print_tree('designation')
    root.print_tree('both')
    root.print_by_level(1)
main()