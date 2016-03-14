---
layout: post
title:  "Top-Level Domains"
category: reference
permalink: reference/top-level-domains/
---

This section is an overview of *top-level domains*, or the things you see at the end of a URL in a browser. Domain names make using the internet a whole lot easier and a whole lot more fun, but the process that creates them entails a lot of weird complicated things. 

### Why do we need domain names?

- Devices connected to a network using TCP/IP all have an **IP address**, a unique numerical ID. Numerical labels are great for letting computers talk to computers, but try to imagine having to remember something like 170.149.159.130 every time you wanted to visit a website. 
- DNS allows us to translate computer IP addresses to human readable urls, mapping those IPs to domain names.
- When the Internet was small, the network (which is to say, probably a graduate student working on the network) maintained a plain text file called HOSTS.txt which was the master list of the mappings of hosts to IP addresses. As the network scaled, this approach became impractical. The DNS protocol was created to deal with this problem.
- Paul Mockapetris designed the Domain Name System at the University of California, Irvine in 1983, and wrote the first implementation at the request of [Jon Postel](http://www.wired.com/2012/10/joe-postel/). The Internet Engineering Task Force published the original specifications in RFC 882 and RFC 883 in November 1983, which have remained the standard for naming Internet hosts.

### How does it work?

- The mappings of domain names to IP addresses are stored in a distributed network of servers. DNS is stored in a reverse tree like heirarchal structure. 
- Since that last sentence meant literally nothing, here is an analogy: imagine you're looking for a book in the library. If you told the librarian the authors name, they will most likely first look up the last name and then try and then sort for the first name. DNS works similarly but instead of one librarian imagine you had a network of librarians all focusing on specific sub sections of the titles.
- Did that help? Not really? OK. Let's try something more like a "real world" example. 
- Like example.com. When you try to connect to example.com, the first thing your computer does is talk to the DNS servers (a computer that sort of acts as a domain-to-IP directory) to ask it what the IP address for example.com is. When the DNS server sees this request, it tries to resolve the request from right to left. 
- This means it will look up see which servers it knows that have information on **.com** domain names and pass the request on to those servers, which will then look up or send along the request for the **example** part of example.com. 

### Who Is Responsible For DNS?

In the end, we have no one to blame but ourselves. Well, also the fact that today's systems of internet governance were born more out of happenstance and kind of limited foresight on how big and complex the network would become. 

#### ICANN
- The Internet Corporation for Assigned Names and Numbers (ICANN) is the body that is responsible for coordinating the maintenance and methodologies of the root name servers and associated databases of the internet. A lot of this work happens via the The Internet Assigned Numbers Authority (IANA).
- It was created in 1998 basically as the U.S. government realized that they didn't really know what the fuck they were doing. Well, it's a little more complicated than that, but we'll get into this more later.
- They also are responsible for policy development for internationalization of the DNS system, introduction of new generic top-level domains (TLDs), and the operation of root name servers. The numbering facilities ICANN manages include the Internet Protocol address spaces for IPv4 and IPv6, and assignment of address blocks to regional Internet registries. 
- 

### Types of Top-Level Domains

For reference: IANA maintains a database of all TLDs [here](https://www.iana.org/domains/root/db).

#### The "original" TLDs 

These are the domains created before the introduction of ICANN. They are the oldest of the top-level domains, and while some have retained their original use-cases many are now just taken as sort of given, de facto domains. 

<div  markdown="1" class="row row-eq-height">
	
<div  markdown="1" class="col-md-4">
	
###.com 
**Use Case**: "commercial"--can be used by anyone, sort of through the weirdness of early internet history became the default top-level domain for commercial or personal use. 

**Managed By**: Initially managed by Network Solutions, Inc. as a contractor to the U.S. government, it's now managed by Verisign, Inc. 

</div>

<div  markdown="1" class="col-md-4">

###.net 

**Use Case**: "network"--originally intended for distributed networks of computers.

**Managed By**: Verisign, Inc.

</div>

<div  markdown="1" class="col-md-4">

###.org 

**Use Case**: "organization"--originally intended for non-profit organizations only (and used by many non-profits for this reason), it's also appropriated by less benevolent initiatives (see [internet.org](http://internet.org)) 

**Managed By**: the Public Interest Registry, a domain registrar created by the non-profit organization Internet Society.

</div>

<div  markdown="1" class="col-md-4">

###.edu

**Use Case**: "educational"--although, since we are dealing with a U.S. hegemony here, what's considered an "educational" means more "institutions of education" than "educational". As of 2001 the domain is actually only for United States education institutions accredited by any accreditation agency recognized by the U.S. Department of Education. 

**Managed By**: Educause, a nonprofit dedicated to supporting higher education IT initiatives, is responsible for the TLD, although they actually contract out this work to...surprise! Verisign again. 

</div>

<div  markdown="1" class="col-md-4">

###.gov 

**Use Case**: U.S. state and federal agencies 

**Managed By**: The General Services Administration contracts out maintenance of this TLD to Verisign.

</div>

<div  markdown="1" class="col-md-4">

###.mil

**Use Case**: United States military 

**Managed By**: The U.S. Department of Defense

</div>
</div>


### Country-Code TLDs (ccTLD)

- Definitions/Types
	- traditionally use 2 or 3-letter country codes for domains
		- 3-letter codes are reserved for future use but not all are currently in use (which is why no one can get the .and TLD)
	- internationalized (IDN) ccTLDS
		- use native language characters instead of Latin characters
		- not necessarily formal country abbreviations, can also be colloquial terms for countries ( e.g., the domain .السعودية is a colloquial short-form name for Saudi Arabia in Arabic)
- Acquisition/creation process
	- Initially Jon Postel just used the ISO country-code standards and IANA accepted applications kind of on a goodwill basis, assuming people who represented countries actually did so (see .ly history for example of how this creates dilemmas)
	- Currently, all the ISO codes are basically "reserved", to be implemented basically if/when a country representative requests
	- Internationalized ccTLDs processed through applications
- Ownership/Management
	- can be managed by a national telecommunications authority
	- ...or "partner" with companies that manage the domain and pay out royalties to countries
		- .io, .ac, .sh -- Internet Computer Bureau
		- Verisign management of .tv
- Political Incidents/Implications
	- the Internet Computer Bureau example--countries with complicated political status who continue to be unable to see the benefits of their domains
	- what happens when countries come apart? the .yu example when the former Yugoslavia fell apart
	- cultural/political clashes (vb.ly indcident and decency laws, Turkmenistan domains)

#### Generic Top-Level Domain gTLD

<!-- Add here a history of the whole gTLD mess and how we got here -->

- Definitions/Types
	- sponsored gTLD: represents a concept or term, non-geographic  
	- geographic gTLD
		- represents a geographic region or cultural identity
			- city/region (.nyc)
			- cultural identity (.cat)
			- places that might like more sovereignty than they have (.wales, .scot)
		- varied requirements w/r/t relationship to place
- Acquisition process
	- Application fee is $185,000--$5K of which is paid to reserve a space *for* your application, the remainder paid when the application's actually submitted
	- Why is it so expensive? According to ICANN: 
		> The total fee per applicant takes into account close to $US13 million invested by ICANN since October 2007 to put the design of the implementation program in place. It includes allocated staff time, direct consulting expenses and other fixed costs.
	- The application basically needs to make the case for why a domain should exist--what, if any, demographic it serves, how it will benefit the name space, 
	- Two weeks after the application deadline, ICANN publishes the total list of applications. At that point domain applications can be contested
	- Things that can't be registered as gTLDs: existing 2 or 3-letter ISO country codes (.and, for example), registered trademark products (not even by the owner of the trademark), 	
- Ownership
	- individual institutional stakeholders for very narrow, specific participants (.museum, .aero)
	- representatives of a regional/cultural concern (.cat)
	- colonial powers fucking over regional/cultural concerns (.wales)
	- large companies seeking general control over namespaces (e.g. Donuts just buying all the weird domains for all the things)
- Political Incidents/Implications
	- what if your regional/cultural entity secedes? (.scot, .cat)
	- capacity to be used for straight trolling (.sucks)
	- what does it even mean to "own" these terms/phrases?

### Why People Buy Domains

- Political Application
- Commerce
- Brand Identity
- Domain hacks/Linguistic happenstance/Poetics (e.g. [notall.technology/actually](http://notall.technology/actually))
- Jokes (e.g. [winafreebird.com](http://winafreebird.com) means nothing but is also amazing?)


