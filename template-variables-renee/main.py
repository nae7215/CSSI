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

da_jinja_environment = jinja2.Environment(  #this is just setting a variable
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        first_template = da_jinja_environment.get_template('templates/landing.html')
        user_cat_type = self.request.get("cat")
        number_of_cats = self.request.get("num")
        my_template_variables = {"cat_type": user_cat_type, "number": number_of_cats }
        self.response.out.write(first_template.render(my_template_variables)) #.render makes the template a string; the variables MUST BE A DICTIONARY!!!

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
