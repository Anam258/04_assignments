import tkinter as tk

# Canvas size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40  # Size of each grid cell

def create_grid(canvas):
    """ Creates a grid of blue cells on the canvas. """
    cells = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cells = []
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            # Draw rectangle for each cell
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
            row_cells.append(rect)  # Store the rectangle in the row list
        cells.append(row_cells)  # Store the row of rectangles
    return cells

def erase(event):
    """ Changes the color of grid cells under the eraser to white. """
    x, y = event.x, event.y  # Get the x, y coordinates of the mouse
    row = y // CELL_SIZE  # Find the row based on y position
    col = x // CELL_SIZE  # Find the column based on x position

    # Ensure the row and column are within the bounds of the grid
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        # Change the color of the grid cell to white
        canvas.itemconfig(grid[row][col], fill="white")

def main():
    global canvas, grid

    # Create main window
    root = tk.Tk()
    root.title("Eraser on Canvas")

    # Create canvas
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Draw grid
    grid = create_grid(canvas)

    # Bind mouse movement to the eraser
    canvas.bind("<B1-Motion>", erase)

    # Run application
    root.mainloop()

# Required line to run the program
if __name__ == '__main__':
    main()
