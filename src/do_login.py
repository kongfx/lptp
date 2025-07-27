#    LPTP
#    Copyright (C) 2024-2525  ko114

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
from io import BytesIO

import requests

from . import utils
import getpass, json
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tempfile
def do_login(ka=False)-> tuple[bool,requests.Response, utils.Session]:
    session = utils.Session()
    session.session.get(utils.LUOGU)
    username = input("请输入 UID、用户名或电子邮箱：")
    kr = session.session.get(utils.LUOGU + '/auth/login-methods?login=' + username, headers={
        "x-csrf-token": utils.get_csrf_token(
            session.session, "https://www.luogu.com.cn/auth/login"
        ),
    }, )
    if kr.status_code != 200:
        print('输入不正确。')
        return False, None, None
    password = getpass.getpass('密码（不会显示）：')
    print('获取验证码中...')
    c = session.captcha(ka)
    tfile=tempfile.NamedTemporaryFile(suffix='.png', mode='wb', delete=False)
    Image.open(BytesIO(c)).save(tfile, 'PNG')
    tfile.close()
    img=mpimg.imread(tfile.name)
    import os
    os.unlink(tfile.name)
    plt.imshow(img)
    plt.show()
    captcha = input('输入验证码：')
    s, r = session.login(username, password, captcha)
    if s == 401:
        print('用户名或密码错误。')
    elif s == 400:
        print('验证码错误。')
    elif s == 200:
        print('登录成功。')
        return True, r, session
    else:
        raise Exception('未知错误：' + json.dumps(r, indent=4))
    # print(json.dumps(r, indent=4))
    return False, r, session


if __name__ == '__main__':
    do_login()
