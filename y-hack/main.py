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
from calc import rel_fares

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template("template/home.html")
        self.response.write(my_template.render())

class ResultHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World")
    def post(self):
        budget = self.request.get("budget")
        num = self.request.get("number_of_people")
        origin = self.request.get("org")
        leave = self.request.get("leave_after")
        dic = rel_fares("Deals.csv", budget, num, origin, leave)
        print (budget)
        print (num)
        print (origin)
        print (leave)
        print (dic)
        fill_in = {'results': dic}
        results_template = jinja_environment.get_template("template/results.html")
        self.response.write(results_template.render(fill_in))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultHandler),
], debug=True)
