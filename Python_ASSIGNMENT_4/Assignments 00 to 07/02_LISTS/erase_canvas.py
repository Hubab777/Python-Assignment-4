import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()
        self.cells = []  # Keep track of cell IDs
        self.eraser = None

        self.create_grid()

        # Wait for a click to place the eraser
        self.canvas.bind("<Button-1>", self.place_eraser)

    def create_grid(self):
        rows = CANVAS_HEIGHT // CELL_SIZE
        cols = CANVAS_WIDTH // CELL_SIZE
        for row in range(rows):
            for col in range(cols):
                left_x = col * CELL_SIZE
                top_y = row * CELL_SIZE
                right_x = left_x + CELL_SIZE
                bottom_y = top_y + CELL_SIZE
                cell = self.canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue', outline='black')
                self.cells.append(cell)

    def place_eraser(self, event):
        if self.eraser is not None:
            return  # Eraser already placed

        # Create pink eraser rectangle
        x, y = event.x, event.y
        self.eraser = self.canvas.create_rectangle(
            x, y, x + ERASER_SIZE, y + ERASER_SIZE, fill='pink'
        )

        # Start tracking mouse movement
        self.canvas.bind("<Motion>", self.move_eraser)

    def move_eraser(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        self.erase_objects(x, y)

    def erase_objects(self, x, y):
        # Define eraser area
        left_x = x
        top_y = y
        right_x = x + ERASER_SIZE
        bottom_y = y + ERASER_SIZE

        # Check overlap with cells
        overlapping = self.canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
        for obj in overlapping:
            if obj != self.eraser:
                self.canvas.itemconfig(obj, fill='white')

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
