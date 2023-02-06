import pygame

# The real and imaginary parts of each complex number are calculated based on
# the current pixel position on the screen. The number of iterations required
# for the complex number to diverge is calculated, and the color of the pixel
# is set based on the number of iterations.

# color map function
def color_map(iterations, max_iter):
    # modify to change color mapping
    color = (iterations % 8 * 32, iterations % 16 * 16, iterations % 32 * 4 * 0.2) # RGB values
    return color

pygame.init()
screen = pygame.display.set_mode((640, 640))

# set max iterations -> Higher values for better results but slower performance
max_iter = 512

# set range of values for the real part (x axis) and imaginary
# (y axis) of the complex number to be used to generate fractal
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5

# calculate the step size for each iteration
dx = (xmax - xmin) / screen.get_width()
dy = (ymax - ymin) / screen.get_height()

# Visual representation of the Mandelbrot set. 

# iterate over all pixels on screen and calculate real and imaginary part of complex number
for i in range(screen.get_width()):
    for j in range(screen.get_height()):
        real = xmin + i * dx
        imag = ymin + j * dy

        c = complex(real, imag)
        z = complex(0, 0)

        # counter for iterations
        iterations = 0

        # check if complex number is in the Mandelbrot set
        while abs(z) < 2 and iterations < max_iter:
            z = z * z + c
            iterations += 1

        # set color based on n iterations
        color = color_map(iterations, max_iter)
        screen.set_at((i, j), color)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
