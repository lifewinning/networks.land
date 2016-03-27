---
layout: post
title:  "Packets"
category: reference
---

<!--[Step1](http://networks.land/packets/Step1.html)-->

## What is a packet?

Packets are the basic unit of transport for digital communications networks. One could describe them as follows:

```
A sequence of bytes (1's and 0's) that contain a source address, destination address and body. 
```

This means that all the information we send each other over the network is broken down into discrete units. That information can be an email, a tweet, an image, or even a video you want to stream.


## Packets, Networks and the Postal Service


We think of packets as being similar to your mail carrier because both a computer network and the postal service share a basic functionality.

 - Both take stuff from one place to another. 
 - In both types of networks the sender and receiver have an address.
 -  The *protocols* (we'll talk about this a bit more later) of the networks are used to route stuff i.e move stuff from the sender to the receiver.


Keeping this in mind, a packet can be broken down into two parts:

- Headers
	 - This is the metadata of the packet.
	 - It contains the sender/receiver address
	 - It also contains other information that describes the packet, but is not the actual information the sender wants to send to the receiver.
	 - In our postal service analogy you can think of this as the envelope of a letter
- Body
	- This is the information the sender wants the receiver to have.
	- You can think of this as the actual letter you want the receiver to have.


This general description is true for most commonly used packet formats and certainly those used on the 
internet.

As I'm sure you've probably already guessed, the internet doesn't work *exactly* the same as the postal service. There are two places where packets differ considerably from the postal service (other than the fact that dogs won’t eat your packets). These are:

 - Packet Switching
 - Encapsulation


## Packet Switching

Packet switching is defined as: *"A mode of data transmission in which a message is broken into a number of parts that are sent independently, over whatever route is optimum for each packet, and reassembled at the destination."*

Going back to our postal service analogy, you can think of packet switching in the following way:

- Write a letter to a friend
- Cut the letter up into many smaller pieces
- Put each piece in an envelope with their address as the destination and yours as the source
- Send each sealed envelope with a different service i.e USPS, FedEx, UPS

While this seems like a bizarre thing to do for snail mail, it actually makes a lot of sense when thinking about computer networks.

The Postal Service doesn't treat your packages as replicable and they don't send your mail at the speed of light, so if someone in the post office loses/damages your letter by accident that letter is lost forever. To prevent this from happening the postal service has processes in check that ensure the likelihood of your mail reaching you.

With the Internet, however, the sheer quantity of information and the speed and distances over which it's being shared means there is no way to avoid having some damage done to your data as it is sent over the network. Luckily, the the way the internet's protocols are designed, a receiver can tell when it gets a malformed packet and ask the sender to re-send that information. All of this happens so fast that a person can't even tell.


Now imagine a scenario in which you live in America and want to transfer an image you've clicked with your smart phone to a friend in Japan. These days smartphone images are typically ~ 1MB in size. That means there are *1 million 1's and 0's* (that make up the image) that need to be transferred from the US to Japan.

Since the distance between the US and Japan is significant, the likelihood that information will get corrupted along the way is significant. If you tried to send this image in one chunk, any time you lost information during the transfer you would have to re-send the entire image. This is where packet switching comes in. 
Instead of needing to send the entire image in one go, you can split it into smaller pieces. It also isnt necessary for all the packets to take the same route, so if there is a lot of traffic on one route it's easy to switch to another one.


To further understand how this works check out our [Packet Switching Relay Race](http://networks.land/activities/what-is-the-internet-made-of/3-be-the-internet.html) activity.

<!--![blocks](/assets/ps-1.JPG){:.img-responsive}-->
<!--
Thanks to Claude Shannon, the creator of Information theory, computers are capable of splitting information into many small packets and more importantly capable of reconstructing the original information from those packets, like a jigsaw puzzle. 

Computer networks and information sharing the way we understand it is possible because	of this process.
-->



<!--Imagine a scenario in which you live in America and  wanted to transfer an image you've clicked with your smart phone to a friend in Japan.

These days images are typically ~ 1MB in size. That means there are *1 million 1's and 0's* (that make up the image) that need to be transferred from the US to Japan.

Since the distance between the US and Japan is significant the likelihood that information will get corrupted along the way is significant. If you tried to send this image in one chunk any time you lost information during transfer you would have to re-send the entire image.



To overcome this problem, modern communications networks employ packet switching. 

With packet switching that original image is split up into many tiny chunks and sent to the receiver over many different routes.
Once all the information is picked up at the receiver it reconstructed to display the original information.

Going back to the defintion we wrote for a packet in our example the sender address will be the US computers IP address, the receiver address will be the Japan computers IP address and the body will be a small part of the original image.
-->




## Encapsulation

Now that we understand packet switching and how a message can be sent from one computer to another by breaking it into smaller packets, we should look at another characteristic of the internet that allows it to scale so vastly.


The technical/hard to understand definition of encapsulation:

*In computer networking, encapsulation is a method of designing modular communication protocols in which logically separate functions in the network are abstracted from their underlying structures by inclusion or information hiding within higher level objects.*

In plain English this means that in a computer network, a computer is not only a possible source or destination for a packet but also a middleman for other computers packets! If we didn't have packet encapsulation every packet being transmitted would have to be fully processed by every hop in the network before sending it out again, which would lead to a very slow and inefficient (not to mention unsafe) network.


To think about this more clearly let's use an example. Alice and Bob went to college together, but after graduating Alice took up a job in India while Bob moved to New York. They've done a good job staying in touch and almost ten years after graduating it's Bobs 30th birthday and Alice wants to surprise him with a nice birthday present. 

She knows both his home address and work address but decides to mail the present to his work address because he is not home for long periods of time and he also lives alone which mean there is no one to get his mail for him when he is not around. 

Bob works for Vandalay Industries which is located at:
			420 West 4th Street, 
 			6th Floor,
 			New York
 			10003

So what happens from the time Alice mails the present to when Bob receives it?

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
- Once the package arrives in New York, the local office sends it out for delivery with all the other packages intended for Manhattan.
- When the delivery messenger gets to 420 West 4th Street he realises many companies have offices in that building.
- He looks up which floor Vandalay Industries is on and delivers take the package to reception
- The receptionist accepts the package and sees it is for Bob who works in IT and delivers it to him.

This mundane example actually covers the concept of encapsulation really well. 
Lets look a little more closely at the different actors and their motives:

- Alice: 
	- She wants to get a package delivered to Bob.
	- She doesn't need to know the details of how Bob will receive the package.
- Courier Service office in India: 
	- Wants to deliver the package to New York.
	- Doesn't need to know about Bob, his office, or his birthday present
- Courier Service office in New York: 
	- Wants to deliver the package to Bobs office.
	- Doesn't need to know about Bob or his birthday present.
- Vandalay Industries receptionist: 
	- Receives package from the service and wants to deliver it to Bob
	- Doesn't care that its Bob's birthday present.

Now lets compare this to what it would look like if Alice was to send Bob an E-mail.


  - Alice writes the email and sends it to Bobs email address
	  - Since we are all familiar with this action, it's easy to forget that when this happens Alice is actually sending a message to a computer somewhere on that internet that has Bob's inbox stored in it.
	  - In order to get this message from Alice's computer to the computer that stores Bob's inbox, the message has to traverse a whole network of computers (the internet!).
	  - The computers between Alice and Bob make up the courier service in our previous example. And by using encapsulation only the information that is relevant to getting the message to Bob is exposed to the computers along the way.


So to summarise, information can be sent over a computer network from a sender to receiver by using their unique addresses (IP address) on the network. In order to reach the receiver the information has to be traverse the computer networks (Internet).

 Because these networks are spread over large physical distances there is often information corruption along the way In order to minimise this, large chunks of information are broken up into small discrete packets which have a higher likelihood of not getting corrupted. 

Thanks to packet encapsulation computers along the way only have to look at the envelope (packet headers) to direct the message to the recipient without requiring any knowledge of what is inside. 





<!--- Protocols
	- 
	-  TCP/IP
	-  DNS
	-  HTTP-->

<!--

As you can imagine this process is pretty inefficient and there is a lot of room for error which also makes the process slow.


The first place this technique was employed was the telephone system and it is not used in all modern communications networks.

They can be made up of one or more protocols and are sent from one computer to another through routes.

When you type a URL in the address bar of your browser, you are essentially making a request to a remote computer asking it to send you some information that is stored on it.


A basic and generic definition of packets: -->
