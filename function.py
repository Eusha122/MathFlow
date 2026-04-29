import numpy as np
import matplotlib.pyplot as plt

# base grid
x = np.linspace(-10, 10, 1000)

allowed = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "exp": np.exp,
    "log": np.log,
    "sqrt": np.sqrt,
    "abs": np.abs
}

plt.ion()

while True:
    expr = input("\nEnter function (use x OR x,y) or 'exit': ")

    if expr.lower() == "exit":
        break

    plt.clf()

    try:
        ##y=f(x)
        if "y" not in expr:
            allowed_1d = {"x": x, **allowed}
            y = eval(expr, {"__builtins__": None}, allowed_1d)

            plt.plot(x, y, color="blue", linewidth=2)
            plt.title(f"y = {expr}")

            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)

        #f(x,y)=0 
        else:
            X, Y = np.meshgrid(x, x)
            allowed_2d = {"x": X, "y": Y, **allowed}

            Z = eval(expr, {"__builtins__": None}, allowed_2d)

            plt.contour(X, Y, Z, levels=[0], colors="red")
            plt.title(f"{expr} = 0")

        
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")

        plt.draw()
        plt.pause(0.01)

    except Exception as e:
        print("Error:", e)

plt.ioff()
plt.show()