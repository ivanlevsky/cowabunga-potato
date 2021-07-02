import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
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


def draw_two_dimensional(title, x_input, y_input, x_labal, y_label):
    line_list = plt.plot(x_input, y_input)
    plt.title(title)
    plt.xlabel(x_labal)
    plt.ylabel(y_label)
    return plt, line_list


def show_matplot_image(matplot_object):
    matplot_object.show()


def animate(num, data, line, point_x_line, point_y_line, point):
    # if len(data[..., :num])!=0:
    if len(data[..., :num][0]) != 0:
        px = data[...,:num][0][-1]
        py = data[...,:num][1][-1]
        point_x_line.set_data([px-0.5, px+0.5], [py, py])
        point_y_line.set_data([px, px], [py-0.5, py+0.5])
        point.set_data(px,py)
        line.set_data(data[...,:num])
    return line,


def test_2d_formula_animation(formula_title, formula_input,  formula_output):
    fig_2d = plt.figure()
    data = np.array([formula_input, formula_output])
    line, = plt.plot([], [], "r-")
    point_x_line, = plt.plot([], [], "b-")
    point_y_line, = plt.plot([], [], "g-")
    point, = plt.plot([], [], "ro")
    plt.axis([-2.0, 2.0, -2.0, 2.0])
    plt.grid(True)
    plt.title(formula_title)
    line_2d_ani = animation.FuncAnimation(fig_2d, animate, frames=105, fargs=(data, line, point_x_line, point_y_line,
                                                                              point), interval=10)
    return plt, line_2d_ani


def save_animation_as_gif_image(write_animation, animation_name):
    """
    use animation.writers.list() to list writer current machine supported
    """
    write_animation.save(''.join((animation_name,'.gif')), writer=animation.PillowWriter(fps=40))


def test_function():
    line_list = plt.plot([-3, -2, 5, 0], [1, 6, 4, 3])
    return plt, line_list


# -----------------test line , line style-----------------------------------
# x=[0, 1, 2, 3, 4, 5]
# y=[0, 1, 2, 3, 4, 5]
# mplt, lines = draw_two_dimensional('Square function', x, y, 'x', 'y')
# set_line_style(mplt, lines[0], '-')
# set_line_marker(mplt, lines[0], '*')
# set_line_color(mplt, lines[0], 'c')
# show_matplot_image(mplt)
# ------------------2d animation----------------------------------
# x = np.linspace(-2, 2, 50)
# y = np.sqrt(1-(x**2/4))
# x = np.concatenate((x, -x), axis=0)
# y = np.concatenate((y, -y), axis=0)
# mplt, test_ani = test_2d_formula_animation('test', x, y)
# show_matplot_image(mplt)
# save_animation_as_gif_image(test_ani, 'ellipse')
# -----------------3d animation-----------------------------------
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# r = np.linspace(0, 1, 20)
# p = np.linspace(0, 2*np.pi, 20)
# R, P = np.meshgrid(r, p)
# Z = ((R**2 - 1)**2)
# X, Y = R*np.cos(P), R*np.sin(P)
# mplot = [ax.plot_surface(X, Y, Z, cmap="rainbow")]
# ax.set_zlim(0,1)
# ax.set_xlabel(r'$\phi_\mathrm{real}$')
# ax.set_ylabel(r'$\phi_\mathrm{im}$')
# ax.set_zlabel(r'$V(\phi)$')
# def animate_3d(num, zx, zy, ani_plot):
#     ani_plot[0].remove()
#     zz = ((R**2 - num/50)**2)
#     ani_plot[0] = ax.plot_surface(zx, zy, zz, cmap="rainbow")
#     ax.view_init(45,100+abs(num-50))
#     return ani_plot[0],
#
# line_ani = animation.FuncAnimation(fig, animate_3d, frames=50, fargs=(X, Y, mplot), interval=10)
# plt.show()

