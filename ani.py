import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
 
def animate(_list, generator, title, save, save_frames=1000):
    x_pos=[0.4,1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4,9.4,10.4,11.4,12.4,13.4,14.4,15.4,16.4,17.4,18.4,19.4]
    n = max(_list)+7
    fig, ax = plt.subplots()
    ax.set_title(title)
 
    bar_rects = ax.bar(range(len(_list)), _list, align="edge")  
    ax.set_xlim(0, len(_list))
    ax.set_ylim(0, int(1.1*n))
    text = ax.text(0.01, 0.95, "", transform = ax.transAxes)
    iteration = [0]
    def _animate(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
            plt.xticks(x_pos,labels=_list)
        iteration[0] += 1
        text.set_text(f"No. Iterations: {iteration[0]}")
   
    anim = FuncAnimation(fig, func=_animate,
        fargs=(bar_rects, iteration), frames=generator, interval=10,
        repeat=False, save_count=save_frames)
    plt.show()	