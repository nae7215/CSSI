#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        eightball_template = jinja_environment.get_template('templates/eightball.html')
        self.response.out.write(eightball_template.render())


# import random

# handler = "Will I have a good day today?"
#
# class FortuneHandler(webapp2.RequestHandler):
#     def get(self):
#         fortunes = ['It is certain',
#         'It is decidedly so',
#         'Without a doubt',
#         'Yes definitely',
#         'You may rely on it',
#         'As I see it, yes',
#         'Most likely',
#         'Outlook good',
#         'Yes',
#         'Signs point to yes',
#         'Reply hazy try again',
#         'Better not tell you now',
#         'Ask again later',
#         'Cannot predict now',
#         'Concentrate and ask again',
#         "Don't count on it",
#         'My reply is no',
#         "My sources say no",
#         "Outlook not so good",
#         "Very doubtful",]
#         self.response.write(handler + '<br> </br>'  + fortunes[random.randint(0,19)])

# class ExcusesHandler(webapp2.RequestHandler):
#     def get(self):
#         tasks = ['task 1', 'task 2', 'task 3']
#         excuses = ['excuse 1', 'excuse 2', 'excuse 3']
#         self.response.write("I didn't " + tasks[random.randint(0,2)] + " because " + excuses[random.randint(0,2)])


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/fortune', FortuneHandler)
], debug=True)
