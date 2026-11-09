 # User stories
### As an unregistered angler, I want to view the feed the community is contributing to, so I can stay up to date with catches and conservation efforts.

Acceptance criteria:

-Ability to view the public posts of registered anglers and conservation events.

-Unable to comment or make posts.



### As an unregistered angler, I want to create an account to be a part of this community so I can participate in the FIN community experience.

Acceptance criteria

-Ability to create an account.

-Angler username must be unique.

-Required fields for registration otherwise account creation will not succeed.

-Ability to see after account creation new abilities such as commenting, creating, and liking posts.

-Passwords must contain at least 8 characters, with one character being capitalized and one being a special character.

-Unregistered angler must retype password to confirm it matches the previous to confirm account creation.


### As a registered angler, I want to log into my account, so I can create posts and contribute to the FIN community.

Acceptance criteria

-Ability to log into account and log out.

-Wrong password or username rejects log in.

-Upon logging out user session will no longer be active, user will need to reauthenticate for an active session.



### As a registered angler, I want to create posts and contribute to the FIN community, so I can provide my expertise, trophies, experience to the community.


Acceptance criteria

-Ability to create posts and comment.

-Ability to edit and delete the angler's own post.

-Posts are connected to authenticated registered angler's account.




### As a registered angler, I want to share information about the lake, fishing technique, bait, and weather condition, so I can show other anglers the best fishing experience.


Acceptance criteria

-Ability to share data on lake, fishing technique, bait, and weather condition.

-Posts are connected to authenticated registered angler's account.



### As a registered angler, I want to comment and like other anglers posts, so I can connect with the community and provide insight on fishing experience and insights.


Acceptance criteria

-Ability to comment and like with created angler account.

-Anglers are restricted to one like to one authenticated angler account making the like.

-Anglers can remove their one authenticated angler account like at any time.

-Unable to edit or delete other anglers post.

-The angler commenter or liker is the authenticated user commenting or liking the post.



### As a registered angler, I want to control my FIN location data, so I can keep some hotspots private so they aren't overfished.


Acceptance criteria

-Ability to control location data turn off and on

-Ability to select preference on specific, general, or private fishing location.

-Fishing location preference is shown.

-Selected fishing location privacy settings are enforced by the system.

-Fishing private locations are not exposed to unauthorized anglers.



### As a fishing conservation activist, I want to view FIN conservation events, so I can help participate in impactful help so other generations can enjoy this hobby.


Acceptance criteria

-Ability to view FIN conservation events.

-Unable to edit/create/delete FIN conservation events.



### As a MasterAngler (Administrator of the site), I want to be able to edit/create/delete FIN community conservation events, so I can encourage impactful conservation efforts for other generations to enjoy the outdoors.


Acceptance criteria

-MasterAngler is an authenticated and authorized user of the administrator FIN group.

-Ability to edit/create/delete conservation events.

-Ability to set the date for the FIN event.



### As a MasterAngler (Administrator of the site), I want to moderate posts and manage user accounts, so I can prevent a negative FIN atmosphere, misleading, or inappropriate data.


Acceptance criteria

-Ability to edit / delete all posts that violate FIN guidelines.

-Ability to delete / ban all accounts that violate FIN guidelines.

-Ability to suspend or restore all accounts.

-MasterAngler is authenticated and authorized user of the FIN administrator group.

-Administrator privileges are only available to authorized and authenticated users of that FIN administrative group.




# Mis-user stories

### As a malicious unregistered angler I want to make posts and comments without making an account so I can submit misleading and inappropriate posts.

Mitigation Criteria:

-Authentication is verified with a registered account to prove that user is allowed to make a post or comment.

-Unregistered accounts are restricted to view-only permissions.

-Only authenticated and authorized anglers are able to make posts and comments.



### As a malicious unregistered angler I want to gain the abilities of a registered account so I can be anonymous and post freely to avoid accountability.

Mitigation Criteria:

-Authentication prevents ability to see registered account capabilities.

-Authorization restrictions prevent unauthenticated anglers from being able to use authenticated angler abilities.

-Posts can be reported and moderated if they violate the FIN community guidelines.



### As a malicious registered angler I want to gain unauthorized access to another anglers account so I can impersonate and access their private account information.

Mitigation Criteria:

-Authentication verifies user's credentials before successful log in.

-Anglers can log out which terminates their sessions.

-Login attempts are protected from brute force attempts 

-Anglers are notified by the verified and authorized system of invalid login attempts after three incorrect logins.

-Login messages will not say if it was a username issue or password issue.

-No identifying information from a registered email will display if user forgets username, they will need to enter their email and if it matches one in the records it will send to that email but not give a confirmation if it sent successfully.



### As a malicious registered angler I want to gain unauthorized access so I can edit, change, or delete an angler's account or take full control.

Mitigation Criteria:

-Accounts must be authenticated before being able to access account privleges.

-Accounts can only be edited by their own authenticated session and are unable to edit others accounts unless administrator.

-Verification of an account's authorization to make changes to account are checked.


### As a malicious registered angler I want to edit, change, or delete someone's post so I can influence the information share with the FIN community.

Mitigation Criteria:

-Only authorized angler accounts are able to edit, change or delete their own posts.

-Only MasterAngler accounts can moderate other users' posts.

-Unauthorized requests to edit change or delete someone's post are rejected by the system.



### As a malicious registered angler I want to turn on location data and see specific location of private fishing spots so I can find and exploit the fishing location.

Mitigation Criteria:

-Different location specific options prevent data shown which prevent exact locations exposure.

-Private location information is not returned to unauthorized accounts.

-Anglers can control their location whether they want it on or off.



### As a malicious registered angler, I want to upload a malicious or wrong formatted image so I can exploit FIN application or it's community.

Mitigation Criteria:

-File format restrictions to JPEG/JPG, PNG, HEIC/HEIF.

-File size restrictions to less than 8 Megabyte.

-Uploaded images will be verified and validated before being put in database.


### As a malicious fishing conservation activist I want to edit, create, or delete conservation event post so I can exploit the conservation community.

Mitigation Criteria:

-Fishing conservation activist accounts are read only permission and prevent any editing.

-Only authorized MasterAngler accounts can edit, create, or delete conservation event posts.

-Unauthorized change requests to edit, create, or delete are rejected by the system.



### As a malicious registered angler, I want to gain unauthorized access to MasterAngler account so I can be able to edit/create/delete conservation events to prevent FIN community conservation efforts.

Mitigation Criteria:

-Alternative account controls to MasterAngler do not have permissions to adjust conservation efforts controls.

-Authentication and authorization mechanisms prevent non MasterAngler accounts from making changes.

-Audit logs are recorded at changes to the FIN community conservation efforts page by MasterAngler account name and timestamp.



### As a malicious MasterAngler (Administrator of the site) I want to be able to edit/delete posts, create negative atmosphere and delete or ban accounts so I can can disrupt the community. 

Mitigation Criteria:

-MasterAngler accounts can remove negative atmosphere / false info that do not follow FIN community guidelines.

-MasterAngler accounts only can edit or deny posts in community posts.

-MasterAngler accounts permissions are authenticated with assigned MasterAngler account.





# Diagrams

![FIN C4 Diagram](./FIN%20C4%20Diagram.drawio.png)

# Prototype
