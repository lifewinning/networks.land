---
layout: default
title:  "Step 1"
---


####Disclaimer
*This post is a pretty incoherent right now mainly due to the fact that these notes have been made on the various flights and trains I have taken over the past week and I am writing it up after two nights of very little sleep. Apologies to anyone who reads it before I get to clean it up.*

When I was thinking about this section my initial reaction was to just jump right into the stack, followed by the snail mail analogy drive home the beauty of encaspulation and seperation of roles and be like yay innnernet!

But its hard to figure out what the first step should be. I'm still not sure but history seems like an easy start.

So before going any further I think it might be good to lay down some questions that all the stuff in this section solves.
Understanding how TCP/IP works is not difficult because by design they tried to make it as easy as possible! But if you understand what problems it is trying to tackle and that those problems can be tackled in a variety of ways it might help develop a better foundation for why things are the way they are.

##Questions
So here are some questions I have so far:

 * How do you get some information across a great distance?
 * How do you make sure the information you sent is the same that was eventually received ?
 * How do you ensure the message you're sending reaches the right receiver?
 * How do you allow this system to scale? or How do you allow many conversations to take place simultaneously without prohibitive costs?
 * What does redundancy look like in this system

 I know these are very simple and obvious, but right now I feel like they might be a good way to bring attention to important stuff that is now second nature to us.
 I need to do more research into this but Im sure we can find good anecdotes for all those question in the history of the various things that make up these things. Things things things
 
  Bad example, modem stands for MOdulaator DEModulator and was actually around in a nascent form in the 1920s way before arpanet and the likes.

 Along with questions here are other background type things that I think will give a more wholesome picture   
 
##Information theory

  Shannon and Information theory. Basically the first mental model to think about is that information theory is all about the quantification of the amount of 'Information' in a given object. 
  The reason I find this notion fascination is because understanding how much of something there is is an important non trivial step in being able to manipulate and control it. 

   Once you figure out how much of something there is, its possible to start thinking about how much redundancy also existed within that system. 
*Find an example that reflects this idea well.*
   Once you know how much redundancy there is you can start thinking about how to reduce it to make transmitting that thing easier 
   (Its not a coincidence that the questions above are symmetrical to this thought process)

   The Information Age and transition from digital to analog allowed things to be manipulated in ways that wasn't possible before. 
   Similar to how the steam engine blah blah,newton optics blah blah, other big scientific game changers.

##Where in the stack are you?
Introducing this idea that a packet is made up of lots of different parts and the first part in understanding what the interent is requires figuring out what you're looking at and where it is in the stack. When im trying to debug my home router I dont care what http payloads are flying around and similarly when a single webpage isnt loading in my browser I dont think the problem lies in my Wi-Fi.

##Pantone Packets Pocket Guide

A nice learning tool might be a pocket packets reference guide (I love saying that). Sort of a legend that allows you to look up different types of packets and what theyre good for. Personally I love the idea of making it look like [this](https://www.google.co.in/search?q=pantone+color+guide&es_sm=91&source=lnms&tbm=isch&sa=X&ved=0CAcQ_AUoAWoVChMIqI3MlI21xwIV5B2mCh1mcwED&biw=1440&bih=734#imgrc=6FkxyVwacAD0iM%3A) because we get the notion of a stack for free but trading cards would also work.
I think this could be a fun thing to give students when we talk about this stuff. Can design them in a way that its easy for teachers to print out there own etc.

   
