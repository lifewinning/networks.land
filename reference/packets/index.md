---
layout: post
title:  "Packets"
category: reference
---

<!--[Step1](http://networks.land/packets/Step1.html)-->

## What is a packet?

Packets are the basic unit of transport of digital communications networks. One could describe them as follows:

```
A sequence of bytes (1's and 0's) that contain a source address, destination address and body. 
```

What this means is that all the information we send each other over the network is broken down into discrete units.
That information can be an email, a tweet, an image or even a video you want to stream. 

##Packets, Networks and the Postal Service
In this post we rely heavily on analogy of packets and the postal service. The reason this analogy is nice is because the basic functionality of a computer network and the physical postal service is the same.

 - Take stuff from one place to another. 
 - In both types of networks the sender and receiver have an address.
 -  The *protocols* (we'll talk about this a bit more later) of the networks are used to route stuff i.e move stuff from the sender to the receiver.


Keeping this in mind we can break a packet can be broken down into two parts:

- Headers
	 - This is the metadata of the packet.
	 - It contains the sender/receiver address
	 - Other information that describes the packet but is not the actual information the sender wants to send the receiver.
	 - In out postal service analogy you can think of this as the envelope of a letter
- Body
	- This is the information the sender wants the receiver to have.
	- You can think of this as the actual letter you want the receiver to have.


This general description is true for most commonly used packet formats and certainly those used on the 
internet.

So as I'm sure you've probably already guessed. The internet doesn't work *exactly* the same as the postal service. The place where it differs most significantly (other than the fact that dogs will not eat your packets) are in two charachteristics. We will discuss both of these in more detail.

 - Packet Switching
 - Encapsulation


## Packet Switching

Packet switching is defined as: *"A mode of data transmission in which a message is broken into a number of parts that are sent independently, over whatever route is optimum for each packet, and reassembled at the destination."*

Going back to our postal service analogy. You can think of packet switching in the following way:

- Write a letter to a friend
- Cut the letter up into many smaller pieces
- Put each piece in an envelope with their address as the destination and yours as the source
- Send each sealed envelope with a different service i.e USPS, FedEx, UPS

While this seems like a bizzare thing to do for snail mail. It actually makes a lot of sense when thinking about computer networks.

Because the Postal Service doesn't treat your packages as replicable and they dont send your mail at the speed of light, if someone in the post office loses/damages your letter by accident that letter is lost forever. The way they overcome this issue is by having processes in check that ensure the likelihood of that happening is small.

However with the Internet the sheer quantity of information and the speed and distances over which its being shared there is no way to avoid having some damage done to your data as it is sent over the network. Luckily, the the way the internets protocols are designed, a receiver can tell when it gets a malformed packet and ask the sender to re-send that information. All of this happens so fast that a person can't even tell.


Now imagine a scenario in which you live in America and wanted to transfer an image you've clicked with your smart phone to a friend in Japan. These days smartphone images are typically ~ 1MB in size. That means there are *1 million 1's and 0's* (that make up the image) that need to be transferred from the US to Japan.

Since the distance between the US and Japan is significant the likelihood that information will get corrupted along the way is significant. If you tried to send this image in one chunk, any time you lost information during transfer you would have to re-send the entire image. This is basically where packet switching comes in. 
Instead of needing to send the entire image in one go, you can split it into smaller pieces. Whats also nice about this method is that it isnt necessary for all the packets to take the same route. So if there is a lot of traffic on one route its easy to switch to another one.


To see this idea be played literally check out our [Packet Switching Relay Race](http://networks.land/activities/what-is-the-internet-made-of/3-be-the-internet.html) activity.

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

So now that we are aware of packet switching and how a message can be sent from one computer to another by breaking it into smaller packets we should look at another charachteristic of the internet that allows it to scale so vastly.


The technical/hard to understand definition of encapsulation:

*In computer networking, encapsulation is a method of designing modular communication protocols in which logically separate functions in the network are abstracted from their underlying structures by inclusion or information hiding within higher level objects.*

What these words are trying to say is that in a computer network, a computer is not only a possible source or destination for a packet but also a middle man for other computers packets! If we didnt have packet encapsulation every packet being transmitted would have to be fully processed by every hop in the network before sending it out again which would lead to a very slow and inefficient (not to mention unsafe) network.

<!--An important thing to keep in mind at the this point is that in a computer network the body of one packet can be a whole other packet. If you're scratching your head right now, I dont blame you but *encapsulation* (putting one packet inside another) is a pretty crucial part of how computer networks work.
-->
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
Lets look a little more closely at the different actors and their motives:

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
	  - While we are all used to this action, its easy to forget that when this happens Alice is actually sending a message to a computer somewhere on that internet that has Bobs inbox stored in it.
	  - In order to get this message from Alices computer to the computer that stores Bobs inbox, the message has to traverse a whole network of computers (the internet!).
	  - Now the computers between Alice and Bob make up the courier service in our previous example. And by using encapsulation only the information that is relevant to getting the message to bob is exposed to the computers along the way.






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
