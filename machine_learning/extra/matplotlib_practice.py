import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# metplotlib default not support chinese,need set font,windows fonts dir c:/windows/fonts
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

def set_line_style(matplot_object, line_object, style):
    """{'': '_draw_nothing', ' ': '_draw_nothing', '-': '_draw_solid', '--': '_draw_dashed', '-.': '_draw_dash_dot',
    ':': '_draw_dotted', 'None': '_draw_nothing'} """
    matplot_object.Line2D.set_linestyle(line_object, style)


def set_line_marker(matplot_object, line_object, marker):
    """markers = {'.': 'point', ',': 'pixel', 'o': 'circle', 'v': 'triangle_down', '^': 'triangle_up',
    '<': 'triangle_left', '>': 'triangle_right', '1': 'tri_down', '2': 'tri_up', '3': 'tri_left', '4': 'tri_right',
    '8': 'octagon', 's': 'square', 'p': 'pentagon', '*': 'star', 'h': 'hexagon1', 'H': 'hexagon2', '+': 'plus',
    'x': 'x', 'D': 'diamond', 'd': 'thin_diamond', '|': 'vline', '_': 'hline', 'P': 'plus_filled', 'X': 'x_filled',
    0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup',
    7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase',
    'None': 'nothing', None: 'nothing', ' ': 'nothing', '': 'nothing'} """
    matplot_object.Line2D.set_marker(line_object, marker)


def set_line_color(matplot_object, line_object, color):
    """one of {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}, they are the single character short-hand notations for blue,
    green, red, cyan, magenta, yellow, black, and white. """
    matplot_object.Line2D.set_color(line_object, color)


def draw_formula_two_dimensional(formula_title, formula_input, formula_output, formula_string):
    line_list = plt.plot(formula_input, formula_output)
    plt.title(formula_title)
    plt.xlabel('x')
    plt.ylabel(formula_string)
    return plt, line_list


def show_matplot_image(matplot_object):
    matplot_object.show()


def animate(num, data, line, point_x_line, point_y_line, point):
    # if len(data[..., :num])!=0:
    if len(data[..., :num][0]) != 0 :
        px = data[...,:num][0][-1]
        py = data[...,:num][1][-1]
        point_x_line.set_data([px-0.5, px+0.5], [py, py])
        point_y_line.set_data([px, px], [py-0.5, py+0.5])
        point.set_data(px,py)
        line.set_data(data[...,:num])
    return line,


def test_2d_formula_animation(formula_title, formula_input,  formula_output):
    fig = plt.figure()
    data = np.array([formula_input, formula_output])
    line, = plt.plot([], [], "r-")
    point_x_line, = plt.plot([], [], "b-")
    point_y_line, = plt.plot([], [], "g-")
    point, = plt.plot([], [], "ro")
    plt.axis([-2.0, 2.0, -2.0, 2.0])
    plt.grid(True)
    plt.title(formula_title)
    line_ani = animation.FuncAnimation(fig, animate, frames=105, fargs=(data, line, point_x_line, point_y_line,
                                                             point), interval=10)
    return plt, line_ani


def save_animation_as_gif_image(write_animation, animation_name):
    """
    use animation.writers.list() to list writer current machine supported
    """

    write_animation.save(''.join((animation_name,'.gif')), writer=animation.PillowWriter(fps=40))


def test_function():
    line_list = plt.plot([-3, -2, 5, 0], [1, 6, 4, 3])
    return plt, line_list


# mplt, lines = draw_formula_two_dimensional('Square function', x, y, 'y = x**2')
# mplt, lines = test_function()
# set_line_style(mplt, lines[0], ':')
# set_line_marker(mplt, lines[0], '*')
# set_line_color(mplt, lines[0], 'c')
# show_matplot_image(mplt)

x = np.linspace(-2, 2, 50)
y = np.sqrt(1-(x**2/4))
x = np.concatenate((x, -x), axis=0)
y = np.concatenate((y, -y), axis=0)
mplt, test_ani = test_2d_formula_animation('test', x, y)
# show_matplot_image(mplt)
save_animation_as_gif_image(test_ani, 'ellipse')
