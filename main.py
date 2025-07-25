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
import argparse
import json

from src import do_login, fetch_problem, htmllib, render, utils


def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('pid', help='题目编号')
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('--login', action='store_true')
    parser.add_argument('-o', '--output', default='<pid>.html')

    args = parser.parse_args()

    return args


def main(pid, quiet=False, output='<pid>.html'):
    output=pid+".html" if output=="<pid>.html" else output
    session = utils.Session(json.load(open('cookies.json')))
    if not quiet:
        print('下载题目中')
    problem=fetch_problem.fetch_problem(session, pid)
    if not quiet:
        print('渲染题目中')
    result=render.template.render(problem=problem)
    if not quiet:
        print(f'渲染完成，文件将保存至 {output}。')
    with open(output, 'w') as f:
        f.write(result)




def login():
    print('欢迎使用洛谷题目导出系统。在第一次使用时请先登录您的洛谷账号。\n'
          '如果您的账号设置了 2FA，请您在登录后手动修改 cookies.json 中的 __client_id。')
    valid, resp, session = do_login.do_login()
    while not valid:
        print('登录失败。请重新登录。')
        valid, resp, session = do_login.do_login()
    json.dump(session.session.cookies.get_dict(), open('cookies.json', 'w'))

if __name__ == '__main__':
    args = arg()
    if args.login:
        login()
    else:
        main(args.pid, quiet=args.quiet, output=args.output)
