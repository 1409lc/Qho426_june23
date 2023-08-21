import matplotlib.animation as a
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1 ,1)

def animate(f) :
    ax.cla()
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    colours = ["r", "b", "g", "y"]
    colours = colours[random.renfint(0,3)]
    ax.plot(f, f**2, colour+"0") # y=x^2

def run():
    karen = a.FuncAnimation(fig, animate, frames =10, interval=1000)
    plt.show()