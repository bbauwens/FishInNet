# FishInNet
Fish In Net or (FIN) for short, is a web app where anglers can log their catch so it doesn't turn out to be just another fishing story! The web app will allow the angler to share their location or general area (privacy is still imporant, and keeping those secret spots a secret!!) with pictures. FIN will be a great way to allow the community to come together to not only share their catch but much more! In fact, FIN allows anglers to share the lakes, baits, weather on the day that they caught their trophy. Additionally fish wouldn't be around without conservation efforts, and community groups to come together and bring awareness and interest to new and young anglers! In this case for proof of concept we will be using local fishing lakes to the city of Omaha to better depict our use, and then show our vision for further expansion of the app as listed by suggestions by the community.
//add more


## Installation:
Software Needed/Used for install

-Git: Installed on your local machine.

-Docker: Installed and running on your local machine.


BASH CLI Commands
Setting Up the Django App

(Creates a clone of the repository)
git clone https://github.com/bbauwens/FishInNet.git

(Changes to the directory)
cd FishInNet

(Builds Docker image)
docker compose build

(Create webservice config files)
docker compose run app django-admin startproject webservices .

(Starts containers in background)
docker compose up -d

(Runs migrations)
docker compose exec web python manage.py migrate

(Creates super user admin for use in the admin interface for container)
docker compose exec web python manage.py createsuperuser





## Getting Started:


# License:
The MIT License (MIT)

Copyright (c) Benjamin D. Bauwens 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
