import pyautogui
from time import sleep
import pyperclip

sleep_time = 0.3
duration = 0.5
scroll = -250


def open_wechat():
    # 找到并打开托盘
    up_button_location = pyautogui.locateCenterOnScreen('./image/up_button.png')
    pyautogui.click(up_button_location)
    sleep(sleep_time)
    # 点击微信
    wechat_button_location = pyautogui.locateCenterOnScreen('./image/wechat_button.png')
    pyautogui.click(wechat_button_location)
    sleep(sleep_time)


def send_message(target, message, duplicate=False, times=1):
    # 打开微信
    open_wechat()
    # 点击搜索
    search_button_location = pyautogui.locateCenterOnScreen('./image/search_button.png')
    pyautogui.click(search_button_location)
    sleep(sleep_time)
    # 输入目标联系人
    pyperclip.copy(target)  # 聊天的内容
    pyautogui.hotkey('ctrl', 'v')
    sleep(sleep_time + 0.5)
    # 点击下方第一个联系人
    pyautogui.move(0, 60)
    pyautogui.click()
    if not duplicate:
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    # 输入消息
    else:
        while times > 0:
            pyperclip.copy(message)  # 聊天的内容
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            times -= 1


def pyq_like(total_number):
    pyq_button_location = pyautogui.locateCenterOnScreen('./image/pyq.png')
    print(pyq_button_location)

    if pyq_button_location is None:
        open_wechat()
        sleep(sleep_time)
        pyq_button_location = pyautogui.locateCenterOnScreen('./image/pyq.png')
        pyautogui.click(pyq_button_location)
    else:
        pyautogui.click(pyq_button_location)

    # 开始点赞
    # 移动到空白处
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('./image/wechat_portrait.png'), duration=duration)
    pyautogui.move(0, 100, duration=duration)
    more_button_location_old = 0
    more_button_location_new = pyautogui.locateCenterOnScreen('./image/more.png')
    while total_number > 0:
        print("-"*100)
        print("“展开”按钮旧坐标：" + str(more_button_location_old))
        print("“展开”按钮新坐标：" + str(more_button_location_new))
        if more_button_location_new is None or more_button_location_old == more_button_location_new:
            pyautogui.scroll(scroll)
            sleep(sleep_time)
            more_button_location_new = pyautogui.locateCenterOnScreen('./image/more.png')
            print("更改新坐标为" + str(more_button_location_new))
        elif more_button_location_old != more_button_location_new:
            # 点赞
            pyautogui.moveTo(more_button_location_new, duration=duration)
            sleep(sleep_time)
            pyautogui.click()
            print("点击“展开”按钮")
            sleep(sleep_time + 0.5)
            like_button_location = pyautogui.locateCenterOnScreen('./image/like.png')
            if like_button_location is None:
                pyautogui.scroll(scroll)
                sleep(sleep_time)
                more_button_location_new = pyautogui.locateCenterOnScreen('./image/more.png')
                continue
            sleep(sleep_time + 0.5)
            pyautogui.moveTo(like_button_location, duration=duration)
            sleep(sleep_time + 0.5)
            pyautogui.click()
            print("点击“点赞”按钮")
            sleep(sleep_time + 0.5)
            total_number -= 1
            pyautogui.scroll(scroll)
            more_button_location_old = more_button_location_new
