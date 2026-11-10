# FishInNet
Fish In Net or (FIN) for short, is a web app where anglers can log their catch so it doesn't turn out to be just another fishing story! The web app will allow the angler to share their location or general area (privacy is still important, and keeping those secret spots a secret!!) with pictures. FIN will be a great way to allow the community to come together to not only share their catch but much more! In fact, FIN allows anglers to share the lakes, baits, and weather on the day of their trophy or first catch! The fishing community wouldn't be around without conservation efforts, and community groups to come together and bring awareness and interest to new and young anglers for years to come, that is why FIN also doubles as a conservation app in addition to sharing for opportunities to make fishing last! In this case, for proof of concept we will be using local fishing lakes to the city of Omaha to better depict our use, and then show our vision for further expansion of the app depicted by further community interests! FishInNet wants to welcome new and old anglers to get them active with a great new/existing hobby and extend efforts to continue the conservation of the hobby!


## Installation:
Software Needed/Used for install

-Git: Installed on your local machine.

-Docker Desktop: Installed and running on your local machine.

-Docker Compose: Installed on your machine


STARTING LINE BELOW:

1. BASH CLI Commands (launch cmd prompt)
Setting Up the Django App

(Creates a clone of the repository)

2. In command prompt run "git clone https://github.com/bbauwens/FishInNet.git"

(Changes to the directory)

3. In command prompt run "cd FishInNet"

(Builds Docker image)

4. In command prompt run "docker compose build"

(Starts containers in background)

5. In command prompt run "docker compose up -d"

(Runs migrations)

6. In command prompt run "docker compose exec app python manage.py migrate"

(Creates super user admin for use in the admin interface for container)

7.In command prompt run "docker compose exec app python manage.py createsuperuser"


## Getting Started:
Once you have completed the above installation the app should now be ready to be accessed.

1. Open browser and go to http://localhost:8000/admin/
(use credentials used above when creating super user)

2. Once logged in you should now be able to:

*View Posts

*Register to FIN

*Sign in if you registered a FIN account

*Share pictures and interact with the FIN community by liking or commenting

*View fishing details on the post such as what kind of bait, lake the fish was caught at, and the weather conditions

*Discover conservation events listed and calendar.


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
