import time
import pyautogui
import pyperclip

import RobotConfig
import RobotDatabase


def getMobiles(page):
    return RobotDatabase.getMobiles(page * 10, 10)


def fillMessage():
    message = RobotDatabase.getMessage()

    pyautogui.hotkey('command', 'a')

    time.sleep(1)

    pyautogui.press('backspace')

    time.sleep(1)

    pyperclip.copy(message)

    time.sleep(1)

    pyautogui.hotkey('command', 'v')


def sendInvite():
    print('发送添加好友请求')

    invite = pyautogui.locateOnScreen('send.png')
    if invite:
        i_x, i_y = invite.left, invite.top
        print(f'图像位于屏幕上的坐标：X={i_x}, Y={i_y}')

        i_pos_x = i_x // 2
        i_pos_y = i_y // 2

        pyautogui.moveTo(i_pos_x + 28, i_pos_y + 25)

        time.sleep(1)

        pyautogui.leftClick()

        time.sleep(2)


def addFriend():
    print('点击添加好友按钮')

    try:
        wechat = pyautogui.locateOnScreen('wechat.png')
        add = pyautogui.locateOnScreen('lastadd.png')
        if add and wechat:
            a_y = wechat.top
            a_x = add.left
            print(f'图像位于屏幕上的坐标：X={a_x}, Y={a_y}')

            a_pos_x = a_x // 2
            a_pos_y = a_y // 2

            pyautogui.moveTo(a_pos_x + 28, a_pos_y + 25)

            time.sleep(1)

            pyautogui.leftClick()

            time.sleep(1)

            fillMessage()

            time.sleep(1)

            sendInvite()
    except Exception as e:
        print(e.__cause__.__str__())
        pass


def del_mobile():
    print('清除手机号')

    del_button = pyautogui.locateOnScreen('del.png')
    if del_button:
        d_x, d_y = del_button.left, del_button.top
        print(f'图像位于屏幕上的坐标：X={d_x}, Y={d_y}')

        d_pos_x = d_x // 2
        d_pos_y = d_y // 2

        pyautogui.moveTo(d_pos_x + 8, d_pos_y + 8)

        time.sleep(1)

        pyautogui.leftClick()

        time.sleep(1)


def input_mobile():
    input_add = pyautogui.locateOnScreen('add.png')
    if input_add:
        in_x, in_y = input_add.left, input_add.top
        print(f'图像位于屏幕上的坐标：X={in_x}, Y={in_y}')

        in_pos_x = in_x // 2
        in_pos_y = in_y // 2

        pyautogui.moveTo(in_pos_x + 25, in_pos_y + 25)

        time.sleep(1)

        pyautogui.leftClick()

        time.sleep(1)

        mobiles = getMobiles(RobotConfig.robotConfig['robot']['db']['page'])
        for mobile in mobiles:
            print("输入手机号：" + mobile)

            pyautogui.write(mobile)

            time.sleep(1)

            pyautogui.press('enter')

            time.sleep(3)

            addFriend()

            time.sleep(3)

            del_mobile()


def click_add():
    new_loc = pyautogui.locateOnScreen('new.png')
    if new_loc:
        n_x, n_y = new_loc.left, new_loc.top
        print(f'图像位于屏幕上的坐标：X={n_x}, Y={n_y}')

        n_pos_x = n_x // 2
        n_pos_y = n_y // 2

        pyautogui.moveTo(n_pos_x + 25, n_pos_y + 25)

        time.sleep(1)

        pyautogui.click(button='right', duration=1)

        time.sleep(1)

        pyautogui.moveTo(n_pos_x + 30, n_pos_y + 30)

        time.sleep(1)

        pyautogui.click(button='left', duration=1)

        time.sleep(1)

        input_mobile()


def locate_org():
    location = pyautogui.locateOnScreen('org.png')
    if location:
        x, y = location.left, location.top
        print(f'图像位于屏幕上的坐标：X={x}, Y={y}')

        pos_x = x // 2
        pos_y = y // 2

        pyautogui.moveTo(pos_x + 25, pos_y + 25)

        time.sleep(1)

        pyautogui.click(button='right', duration=1)

        time.sleep(1)

        pyautogui.moveTo(pos_x + 30, pos_y + 30)

        time.sleep(1)

        pyautogui.click(button='left', duration=1)

        time.sleep(1)

        click_add()
    else:
        print('没有找到')


if __name__ == '__main__':
    pyautogui.click(button='left', duration=0.2)

    time.sleep(1)

    pyautogui.hotkey('command', 'space')

    time.sleep(1)

    appName = "企业微信"

    pyperclip.copy(appName)

    time.sleep(1)

    pyautogui.hotkey('command', 'v')

    time.sleep(1)

    pyautogui.press('enter')

    time.sleep(1)

    locate_org()









