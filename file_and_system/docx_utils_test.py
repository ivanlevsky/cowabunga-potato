from python_common.global_param import GlobalParam
from file_and_system.docx_utils import *
from graphic.matplotlib_utils import *
from io import BytesIO


# docx_file = GlobalParam.get_word_report() +'demo1.docx'
# write_docx_table_style_example()
# save_docx_file(docx_file)

# docx_file = GlobalParam.get_word_report() +'demo2.docx'
# read_docx_template_file(docx_file)
# save_docx_file(docx_file)


def insert_matplotlib_image_example_1():
    plt.cla()
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    y = [1, 6, 4, 3, 2, 2, 3, 4]
    lx = np.add(x, 0.5)
    mplt, lines = draw_lines_in_two_dimensional('线图和柱图', lx, y, 'x', 'y')
    set_line_style(mplt, lines[0], '-')
    set_line_marker(mplt, lines[0], 'o')
    set_line_color(mplt, lines[0], 'orange')
    plt.bar(x, y, color='lightblue', label='bar', width=1, linewidth=0.2, edgecolor='black', align='edge')
    plt.grid()
    plt.legend()
    # plt.show()
    memfile = BytesIO()
    plt.savefig(memfile)
    return memfile


def insert_matplotlib_image_example_2():
    plt.cla()
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    fracs = [15, 30, 45, 10]

    # Adapt radius and text size for a smaller pie
    # Valid font size are xx-small, x-small, small, medium, large, x-large, xx-large, larger, smaller, None
    patches, texts, autotexts = plt.pie(fracs, labels=labels,
                                        autopct='%0.2f%%',
                                        textprops={'size': 'smaller'},
                                        shadow=True, radius=0.5,
                                        explode=(0.05, 0.07, 0.02, 0.04))

    autotexts[0].set_color('white')
    plt.title('饼图')
    plt.legend(title='animal')
    # plt.show()
    memfile = BytesIO()
    plt.savefig(memfile)
    return memfile

def insert_matplotlib_image_example_3():
    plt.cla()
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    recipe = ["225 g flour",
              "90 g sugar",
              "1 egg",
              "60 g butter",
              "100 ml milk",
              "1/2 package of yeast"]

    data = [225, 90, 50, 60, 100, 5]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title("Matplotlib bakery: A donut")
    # fig.show()
    # plt.show()
    # ax.plot.show()
    memfile = BytesIO()
    plt.savefig(memfile)
    return memfile

docx_file = GlobalParam.get_word_report() + 'demo3.docx'
picture_file = GlobalParam.get_test_image_path() + 'pic111.png'
write_docx_template_example()
# add_doc_picture(picture_file)
add_doc_picture(insert_matplotlib_image_example_1())
add_doc_picture(insert_matplotlib_image_example_2())
add_doc_picture(insert_matplotlib_image_example_3())
save_docx_file(docx_file)
# //未完成：插入word无边框图
