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
from . import utils
from .htmllib import clean_html as cl
from .htmllib import md

class Problem:
    def __init__(self, problem: dict):
        self.pid = problem['pid']
        self.title = problem['title']
        self.data = problem
        self.name = problem['content']['name']
        self.locale = problem['content']['locale']
        self.background = cl(md(problem['content']['background']))
        self.description = cl(md(problem['content']['description']))
        self.formatI = cl(md(problem['content']['formatI']))
        self.formatO = cl(md(problem['content']['formatO']))
        self.hint = cl(md(problem['content']['hint']))
        self.samples = problem['samples']


def fetch_problem(session: utils.Session, problem_id: str) -> Problem:
    response = session.session.get(utils.LUOGU + 'problem/' + problem_id)
    response.raise_for_status()
    problem = response.json()['data']['problem']
    return Problem(problem)
