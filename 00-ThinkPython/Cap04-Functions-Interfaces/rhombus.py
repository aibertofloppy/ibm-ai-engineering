import turtle

def rhombus(side_length, angle):
    """
    Draws a rhombus using turtle graphics.

    Parameters:
    side_length (int or float): Length of each side.
    angle (int or float): Interior angle in degrees.
    """
    for _ in range(2):
        turtle.forward(side_length)
        turtle.left(angle)
        turtle.forward(side_length)
        turtle.left(180 - angle)

# Example usage
turtle.speed(1)  # Slower drawing for visualization
rhombus(50, 60)
turtle.done()