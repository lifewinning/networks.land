---
layout: page
title: Packet Switching Relay Race
category: activities
feedback: packet-switching-relay
image: objects-5.JPG
---

So this game is pretty silly, but surprisingly fun? It is ideally played with 6-8 people, and definitely has a lot of room for expansion or adaptation. 

*Objective: Understand how data is transmitted through that network of networks to your computer via **packet switching*** and understand the components of the HTTP header. 

### Materials 
- Packet switching relay kit
	- At least three different maximum 12-piece puzzles (again, your mileage may vary). We bought blank 12-piece puzzles [here](http://www.amazon.com/dp/B00598K8H8/ref=cm_sw_r_tw_dp_q49Twb0ZD0PMQ)
	- Enough small envelopes to hold a bunch of puzzle pieces (your mileage may vary)
	- Place each puzzle piece into an envelope and label the envelopes with some identifier that indicates which puzzle that piece is part of--in our case we had puzzles A, B, and C, but you could do numbers or names or if you want to be real literal and kind of a jerk to your students, and entire HTTP header.
- At least 4 tables. One table is at the opposite end of the room; all the packet envelopes should be placed on this table. The other three tables are lined up in a row across from that table, each one labeled with a corresponding puzzle ID that you've used on your packet envelopes.
- 3 different colored post-it notes. Each of the 3 tables at the end of the room has a post-it note set on it.
- Projector is handy but not necessarily required

### Activities

- Show students an example of a traceroute to demonstrate how visiting a website actually involves "hopping" across servers throughout the network. The traceroute example simplifies things a little bit--when you open a webpage, it's not exactly one thing that's loading on the screen, it's a whole bunch of little things that are coming from lots of different places and they all take different paths to your computer. (10-15 minutes)

![envelopes](/assets/objects-4.JPG){:.img-responsive}

- Explain how we're going to do a simplified demonstration of how all those little things travel to a computer. Show students one of the "packet envelopes". These represent different pieces of information and, for our purposes, just indicate where the packet needs to go. (Don't tell them there are puzzle pieces in the envelopes!)

- On one wall in the room, make some space to hang name tags for all participants.

- Reminder: the packets should be placed *label down* on one table on one side of the room.

- Students have to take envelopes off the table *one at a time*, read the envelope's label to figure out which table it needs to go to on the other side of the room. (20-30 minutes)

- When the student delivers the envelope, they have to grab a post-it note from the table and bring that post-it back to the packet table. The game facilitator adds that post-it to the wall underneath that student's name. The player who collects the most post-its (i.e., moves the most packets) wins the game. 

- Depending on the number of students you have, there can be 3 dedicated people at the tables receiving the puzzle pieces assembling in real time, or the assembly can happen after the fact. The nice thing about having real-time puzzle assembly is it means there are two winners, a packet winner and a puzzle winner.

![puzzle piece](/assets/objects-2.JPG){:.img-responsive}

- In this example, we made puzzles with drawings of things you might see or do on the internet. We were quite pleased.

![puzzles](/assets/objects-1.JPG){:.img-responsive}

- This entire activity is a very, very simplified approximation of **packet switching**. Explain the concepts behind TCP/IP and why it's cool to students. (10-15 minutes)

- Right now this activity only addresses a single "hop" in the network, maybe the last line of our traceroute from earlier. How could students represent the full complexity of a traceroute? How many more envelopes would they need? Brainstorm expanding the game and making different rules with students. (10-15 minutes)

- It's pretty likely that the rules created for this expanded game would be tedious and really not fun to play. Explain this is why we use computers: because at the end of the day they're not actually that smart, but they can do a bunch of really tedious things really, really fast. 

- **Optional/maybe a bad idea**: It would be theoretically possible to try and incorporate other interesting facets of the HTTP header, like cookies, into these packets. We haven't tried that yet. But if you have ideas we welcome contributions!