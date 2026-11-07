# User stories
As an unregistered angler, I want to view the feed the community is contributing to, so I can stay up to date with catches and conservation efforts.

Acceptance criteria:

-Ability to view the public posts of registered anglers and conservation events.

-Unable to comment or make posts.


As an unregistered angler, I want to create an account to be a part of this community so I can participate in the FishInNet community experience.

Acceptance criteria

-Ability to create an account.

-Angler username must be unique.

-Required fields for registration otherwise account creation will not succeed.

-Ability to see after account creation new abilities such as commenting, creating, and liking posts.

-Password security requirements.


As a registered angler, I want to log into my account, so I can create posts and contribute to the community.

Acceptance criteria

-Ability to log into account and log out.

-Wrong password or username rejects log in.

-Upon logging out, user will need to reauthenticate for an active session.


As a registered angler, I want to create posts and contribute to the community, so I can provide my expertise to the community.


Acceptance criteria

-Ability to create posts and comment.

-Ability to delete a post.

-Posts are connected to authenticated registered angler's account.



As a registered angler, I want to share information about the lake, fishing technique, bait, and weather condition, so other anglers can compare for best fishing experience.


Acceptance criteria

-Ability to share data on lake, fishing technique, bait, and weather condition.

-Posts are connected to authenticated registered angler's account.


As a registered angler, I want to comment and like other anglers posts, so I can connect with the community and provide insight.


Acceptance criteria

-Ability to comment and like with created username.

-Unable to edit or delete other anglers post.

-Commenter / liker is the authenticated user commenting or liking the post.


As a registered angler, I want to control my location data, so I can keep some hotspots private so they aren't overfished.


Acceptance criteria

-Ability to control location data turn off/on

-Ability to select preference on specific, general, or private location.

-Location preference is shown.


As a fishing conservation activist, I want to view conservation events, so I can help participate in impactful help so other generations can enjoy this hobby.


Acceptance criteria

-Ability to view conservation events.

-Unable to edit/create/delete conservation events.


As a MasterAngler (Administrator of the site), I want to be able to edit/create/delete community conservation events, so I can encourage impactful conservation efforts for other generations to enjoy the outdoors.


Acceptance criteria

-MasterAngler is an authenticated and authorized user of the administrator group.

-Ability to edit/create/delete conservation events.

-Ability to set the date for the event.


As a MasterAngler (Administrator of the site), I want to moderate posts and manage user accounts, so I can prevent a negative atmosphere, misleading, or inappropriate data.


Acceptance criteria

-Ability to edit / delete all posts that violate guidelines.

-Ability to delete / ban all accounts that violate guidelines.

-Ability to suspend or restore all accounts.

-MasterAngler is authenticated and authorized user of the administrator group.

-Administrator privileges are only available to authorized and authenticated users of that administrative group.




# Mis-user stories

As a malicious unregistered angler I want to make posts and comments without making an account.

Mitigation Criteria:

-Authentication that user is registered to make a post.

-Accounts not registered are rejected.

As a malicious unregistered angler I want to have the abilities of a registered account.

Mitigation Criteria:

-Authentication prevents ability to see account abilities.

As a malicious registered angler I want to log into / log out of someone else's account.

Mitigation Criteria:

-Authentication rejects ability to log in.

As a malicious registered angler I want to edit, change, or delete someone's account.

Mitigation Criteria:

-Unauthorized account is rejected from others accounts.

As a malicious registered angler I want to edit, change, or delete someone's post.

Mitigation Criteria:

-Unauthorize account is rejected from others posts.

As a malicious registered angler I want to turn on location data and see specific location of private fishing spots.

Mitigation Criteria:

-Different location specific options prevent data shown.

As a malicious fishing conservation activist I want to edit, create, or delete conservation event post.

Mitigation Criteria:

-Account privilege separation prevents this.

As a malicious MasterAngler (Administrator of the site) I want to be able to edit/create/delete conservation events.

Mitigation Criteria:

-Alternative accounts to MasterAngler do not have permissions outside of view only.

-Authentication mechanisms prevent access.

As a malicious MasterAngler (Administrator of the site I want to be able to edit/delete posts, create negative atmosphere and delete or ban accounts. 

Mitigation Criteria:

-Administrators can remove negative atmosphere / false info.

-Administrators approve or deny posts in community posts.





# Diagrams

# Prototype
