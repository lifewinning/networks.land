# Point Arena Workshops

###Logistics

- Dates: October 11-18 OR October 11-22?
- I need to email Ben (friend with property up there) about possibly staying at his place

###Things We Need To Give Blake/Tech Center team:

- Short description
- Headcount of how many participants
- Materials needs

###Useful things about Point Arena

- Is in very close proximity to the Manchester Cable Station, a submarine cable landing site for the [U.S.-Japan Cable](http://www.submarinecablemap.com/#/submarine-cable/japan-u-s-cable-network-jus)

- Partly as a reuslt of this proximity, has become basically the ground zero for rural broadband WISP [Further Reach](http://furtherreach.net/), a project of [DeNovo Group](http://denovogroup.org/main/celerate-project/). AFAIK that operates captive portal style.

- So there's lots of cable cones and lots of microwave antennae that are easy to just point at. 

- Also home to the amazing [Point Arena Tech Center](http://www.arenatechcenter.org/), they're the ones who are basically able to facilitate us doing a thing. 

###Demographic/Audience

- Per Blake: apathy is kind of a huge obstacle for working with the kids in the area. The primary industries of the region are tourism and weed, little incentive to get into tech stuff. 

- Also considering that some of them don't even have internet at home it's not like this stuff translates into things they can do outside of the tech center

- But they did a Minecraft camp this summer that has been super popular and successful, so there's definitely interest from some kids?

- Lack of home network connection != lack of internetting, though--it's mostly just mobile and apps based. (TLDR that thing about the internet basically turning into TV, everyting is terrible) Getting them to pay attention and not look at stuff on YouTube is, apparently, a thing.

###Other Possible Collaborators

- Sam Kronick/Disk Cactus--frequently aforementioned infrastructure friend running a studio in Oakland, is insanely stoked to be involved, has useful Point Arena connections.
	- 	Im down. Will let you lead on this as you know him.

- Jenna Burrell--professor at Berkeley iSchool, doing cool things, hasn't responded to my email. 

###Braindump of Ideas

- Maybe let's not plan on doing more than 3 actual *things* given lead time and the amount of time we'll even be there? 

- A field trip to the beach and to the cable landing site is kind of mandatory. In an ideal world weather permitting we could also do some kind of activity *on* the beach? 

- Was thinking about what an obstacle course/game for illustrating packet switching might look like? 2 teams, each trying to deliver packets to different endpoints, then have to assemble the packets into the requested file on arrival. 

- Also! The distinction between packets and streaming, the web and apps. 

- I've probably griped about badly done infrastructure crowdmaps too much to fairly suggest this but they're actually pretty fun on the hyperlocal level. 

- (This would be also fun to play ON A BEACH but mid-October in California might not be the best in terms of weather)

- Doing things with and on LANs both a practical consideration (unreliable internet access) and a good way to  illustrate key concepts. 

- Bearing in mind that thing about how they're alreeady "connected" at least via mobile, trying to incentivize interest by doing something with DIY networks. I.E. here are tools for building a space to do stuff and talk with your friends that your parents can't access. 

- We have to work on the TLD RPG anyway for Radical Networks?

###SM Notes
- Feels like a series of workshops about the internet and its infrastructure (duh). Im working on the assumption that we are going to do these at the tech center and they will be after school workshops.

	*Those assumptions are pretty much correct. If we do a fieldtrip that will involve a little more effort (the cable's not far away but it's not walking distance from the tech center). But 3 workshops, roughly 2-3 hours?*

- Seperating the transport and data layer makes sense

- So one day on physical stuff, the next on packet switching and how that infrastructure is put to use, and finally using these principals to make a mobile friendly DIY network.

	*I think the more we can clearly link each workshops' activities to one another the better--i.e. being able to refer back to the transport layer piece during the data layer piece ("remember when you had to run around and piece together that puzzle thing? this is like that!").*  

 	*One thing that a friend who has done a lot of work with teaching kids suggested is to structure workshops with one anchor activity and then building out around it? So like, if the group is only able to really get through one piece of the thing they'll still have fun, and if there's a couple of super-advanced kids who get through it really fast there's other activities for them to do.*

 - Fieldtrip/crowdmap
	-  Given time contraints I dont know if we can do both. Can we integrate them in the same day somehow?

		*We could just stretch it out over the three days, so we give them images of stuff to look for and have a map up for all 3 days that we just add stuff to (and probably frontload a little bit in the days prior)* 

 - Packet Switching obstacle course
 	- LOVE this idea. Currently thinking of mechanisms that can be used for the course. Maybe you dont know your endpoint at the start and both teams have to take multiple hops to get to the final endpoint. 
 - DIY Network
  	- We should talk to them more before diving deep into this one. Nothing we can make is going to be as fancy as the apps they're used to so the main incentives are personalization and platform control. 
 
 	*Yeah, we won't be making them a brand new Facebook or something. It we give them a cool thing to do on the network (games, chat, a place to store photos) that might help. How advanced do we want to get on the personalization angle? Like do we build a GUI for stuff on the network or do we crash-course them in ssh and command-line text editing? This isn't a thing that needs to be decided for Blake it's more just a thing I'm thinking about.*

 	*I'm going to shoot an email to Zean from Further Reach about whether he'd have time/want to help teach some of the transport layer stuff specifically looking at the microwave network. I mean, he personally trenched some of that fiber and configured those networks, so he's probably the best person to explain them.* 
