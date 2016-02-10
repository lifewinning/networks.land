---
layout: post
title:  "Packets"
category: reference
---

<!--[Step1](http://networks.land/packets/Step1.html)-->

## What is a packet?

Packets are the basic unit of transport of digital communications networks. One could describe them as follows:

```
A sequence of bytes (1's and 0's) that contain a source address, destination address and payload. 
```

What this means is that all the information we send each other over the network is broken down into discrete units.
That information can be an email, a tweet, an image or even a video you want to stream. 

Thanks to Claude Shannon, the creator of Information theory, computers are capable of splitting information into many small packets and more importantly capable of reconstructing the original information from those packets, like a jigsaw puzzle.

Computer networks and information sharing the way we understand it is possible becuase of this process.

Imagine a scenario in which you live in America and  wanted to transfer an image you've clicked with your smart phone to a friend in Japan.

These days images are typically ~ 1MB in size. That means there are 1 million 1's and 0's (that make up the image) that need to be transferred from the US to Japan.
Since the distance between the US and Japan is significant the likelihood that information will get corrupted along the way is significant. If you tried to send this image in one chunk any time you lost information during transfer you would have to re-send the entire image.

To overcome this problem, modern communications networks employ packet switching. **Find good PS definition**

With packet switching that original image is split up into many tiny chunks and sent to the receiver over many different routes.
Once all the information is picked up at the receiver it reconstructed to display the original information.

Going back to the defintion we wrote for a packet in our example the sender address will be the US computers IP address, the receiver address will be the Japan computers IP address and the payload will be a small part of the original image.


<!--

As you can imagine this process is pretty inefficient and there is a lot of room for error which also makes the process slow.


The first place this technique was employed was the telephone system and it is not used in all modern communications networks.

They can be made up of one or more protocols and are sent from one computer to another through routes.

When you type a URL in the address bar of your browser, you are essentially making a request to a remote computer asking it to send you some information that is stored on it.


A basic and generic definition of packets: -->


This general description is true for most commonly used packet formats and certainly those used on the 
internet.


## The OSI Model

Getting data from one computer to another over the internet is a pretty complicated thing to do, (even though we take it for granted).
To reduce the complexity - or at least seperate out the different actors and roles they play - the OSI model was created.


The details of the OSI model are beyond the scope of what we're concerned with but its worth mentioning becuase this model is the map that helps us navigate what the different moving parts of the network are. 

Starting at the physical layer and how the information is physically transferred via electricity or radio waves from one device to another. All the way up to the application layer, which is how we actually interact with the other devices on the network. 

Think about checking your email or social media, working on a document that is in the cloud or just browsing or reading the news. All of these activities require seamless interaction between a variety of computers of different that play different roles. The OSI model defines those roles. 


## Encapsulation

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








- Protocols
	- 
	-  TCP/IP
	-  DNS
	-  HTTP

