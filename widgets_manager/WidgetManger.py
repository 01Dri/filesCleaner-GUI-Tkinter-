class WidgetManager:
    
    def __init__(self):
        self.widgets: [] = []

    def add_widget(self, widget):
        self.widgets.append(widget)
    
    def create_widget(self, widget):
        self.add_widget(widget)
        return widget
        
    def start(self):
        for idx, wid in enumerate(self.widgets):
            wid.grid(row=idx, column=0, sticky='w', pady=2)

            

