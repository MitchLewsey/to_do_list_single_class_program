class Create_To_Do():
    def __init__(self):
        self.all_tasks = {}

    def add_task(self, task):
        self.all_tasks.update({task : "Not started"})
    
    def show_tasks(self):
        return [x for x,y in self.all_tasks.items() if y != "Completed"]
    
    def complete_task(self, task):
        self.all_tasks.update({task : "Completed"})
