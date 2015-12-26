---
layout: post
title:  "Packets"
---

[Step1](http://networks.land/packets/Step1.html)

Packets are the basic unit of transport of the internet.
They can be made up of one or more protocols and are sent from one computer to another through routes.
When you type a URL in the address bar of your browser, you are essentially making a request to a remote computer asking it to send you some information that is stored on it.

A basic and generic definition of packets: A sequence of bytes (1's and 0's) that contain a source address, destination address and payload. This general description is true for most commonly used packet formats and certainly those used on the internet.

An important thing to keep in mind at the this point is that the payload of one packet can be a whole other packet. If you're scratching your head right now, I dont blame you but *encapsulation* (putting one packet inside another) is a pretty crucial part of how computer networks work.

To think about this more clearly lets use an example. Alice and Bob went to college together but after graduating Alice took up a job in India while Bob moved to New York. They've done a good job staying in touch and almost ten years after graduating its Bobs 30th birthday and Alice wants to surprise him with a nice birthday present. 

She knows both his home address and work address but decides to mail the present to his work address because he is not home for long periods of time and he also lives alone which mean there is no one to get his mail for him when he is not around. 

Bob works for Vandalay Industries in their corporate office which is located at:
			420 West 4th Street, 
 			6th Floor,
 			New York
 			10003

Now lets think about the what happens from the time Alice mails the present to when Bob receives it.

 - Alice wraps Bobs present and addresses it to:

							 	Robert Weiner, 
						 		IT Department,
							 	Vandalay Industries,
							 	421 West 4th Street,
							 	New York 
							 	10003
							 	U.S.A


- Alice then chooses a courier service and drops the package off to them. 
- The courier service sees the address and puts it on a plane with all the other packages that are intended for New York.
- Once the package arrives in the New York, the local office sends it out for delivery with all the other packages intended for Manhattan.
- When the delivery messenger gets to 420 West 4th Street he realises many companies have an office in that building.
- He looks up which floor Vandalay Industries is on and delivers the package to the reception
- The receptionist accepts the package and sees it is for Bob who works in IT and goes and delivers it to him.

This mundane example actually covers the concept of encapsulation really well. 
Lets look a little more closely to the different actors and their motives:

- Alice: 
	- She wants to get a package delivered to Bob.
	- She doesn't need to know the details of how Bob will receive the package.
- Courier Service office in India: 
	- Wants to deliver the package to New York
	- Doesnt need to know about Bob, his office or his birthday present
- Courier Service office in New York: 
	- Wants to deliver the package to Bobs office.
	- Doesnt need to know about Bob or his birthday present.
- Vandalay Industries receptionist: 
	- Receives package from the service and wants to deliver it to Bob
	- Doesnt care that its Bob's birthday present.

Now lets compare this to what it would look like if Alice was to send Bob an E-mail.


  - Alice writes the email and sends it to Bobs email address
	  - While we are all used to this action, its esay to forget that when this happens Alice is actually sending a message to a computer somewhere on that internet that has Bobs inbox stored in it.
	  - In order to get this message from Alices computer to the computer that stores Bobs inbox, the message has to traverse a whole network of computers (the internet!).
	  - Now the computers between Alice and Bob make up the courier service in our previous example. And by using encapsulation only the information that is relevant to getting the message to bob is exposed to the computers along the way.









This can be broken down further

- Protocols
	-  TCP/IP
	- 	DNS
	- 	

