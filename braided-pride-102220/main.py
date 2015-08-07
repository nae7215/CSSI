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
import json
import random
from google.appengine.api import urlfetch


da_jinja_environment = jinja2.Environment(  #this is just setting a variable
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<h1> My Playlist App </h1>')
        music = {
            "Taylor Swift": "Bad Blood",
            "Bon Jovi": "Livin' on a Prayer",
            "Ty Dolla $ign": "Blase",
            "Gallant": "Weight in Gold",
            "Rationale": "Fast Lane",
            "Taylor Swift": "Style"
            }
        for key,val in music.items():
            self.response.out.write(key)
            self.response.out.write(" => ")
            self.response.out.write(val)
            self.response.out.write('<br>')
        self.response.out.write('<br>')
        self.response.out.write('<a href=/add>Add a song to your playlist</a>')

class AddHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<h3> Add a song to your playlist:</h3>')
        first_template = da_jinja_environment.get_template('templates/template.html')
        self.response.out.write(first_template.render())

class AddedHandler(webapp2.RequestHandler):
    def get(self):
        new_artist = self.request.get("artist_add")
        new_song = self.request.get("song_add")
        if new_artist and new_song:
            new_artist = new_artist.replace(" ", "+")
            new_song = new_song.replace(" ", "+")
            music[new_artist] = new_song
            self.response.out.write(MainHandler)
        else:
            self.response.out.write("Didn't work")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
    ('/added', AddedHandler)

], debug=True)
