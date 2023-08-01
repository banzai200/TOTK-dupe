import nxbt, time

macro = """
X 0.1s
0.2s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
B Y 0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
A 0.1s
0.1s
PLUS 0.1s
"""

# Start the NXBT service
nx = nxbt.Nxbt()

# Create a Pro Controller and wait for it to connect
def dupe(num):
    #nx.press_buttons(controller_index, [nxbt.Buttons.HOME])
    time.sleep(2)
# Run a macro on the Pro Controller
    number = 0
    while number < num:
        number = number + 1
        print(number)
        nx.macro(controller_index, macro)

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)
nx.press_buttons(controller_index, [nxbt.Buttons.L, nxbt.Buttons.R])
nx.press_buttons(controller_index, [nxbt.Buttons.A])
time.sleep(3)
ye = 0
while ye < 1:
    dupe(50)
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_UP])
    ye = ye + 1
    print('copy number ' + str(ye))