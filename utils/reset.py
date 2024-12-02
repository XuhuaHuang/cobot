# %% [markdown]
# Reset `MyCobot 280 Pi` to Initial Position

# %%
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

# %%
mc: MyCobot = MyCobot(port=PI_PORT, baudrate=str(PI_BAUD))

if mc.is_controller_connected() != 1:
    print("Cobot controller is not connected")
    exit(1)

# %%
print("Printing angles before reset")
print(mc.get_angles())

# %%
mc.send_angles(angles=[0, 0, 0, 0, 0, 0], speed=30)

# %%
print("Printing angles after reset")
print(mc.get_angles())
