# This is a sample Python script.
import asyncio

from sms_postman.views import app_sms


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# async def print_hi():
#     # app = await send_sms()
#     # app = sms_routing()
#     # Use a breakpoint in the code line below to debug your script.
#     # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#     return app_sms

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # asyncio.run(print_hi())
    app_sms.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
