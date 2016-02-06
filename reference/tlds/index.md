---
layout: post
title:  "Top-Level Domains"
category: reference
---

####Why do we need domain names?

- DNS allows us to translate computer IP addresses to human readable urls. Its easier to remember google.com than 139.130.4.5. When the Internet was small the network maintained a plain text file called HOSTS.txt	which was the master list of the mappings of hosts to IP addresses. As the network scaled this approach became impractical. The DNS protocol was created to deal with this problem.
- Domain names make the internet a whole lot easier and a whole lot more fun, but the process that creates them entails a lot of weird complicated things
- Paul Mockapetris designed the Domain Name System at the University of California, Irvine in 1983, and wrote the first implementation at the request of Jon Postel from ISI. The Internet Engineering Task Force published the original specifications in RFC 882 and RFC 883 in November 1983, which have remained the standard for naming Internet hosts

####How does it work?

- The mappings of domain names to IP addresses are stored in a distributed network of servers. DNS is stored in a reverse tree like heirarchal structure. 
- Another example of such a structure is when you look for a book in the library. If you told the librarian the authors name they will most likely first lookup the last name and then try and then sort for the first name. DNS works similarly but instead of one librarian imagine you had a network of librarians all focusing on specific sub sections of the titles.
- Lets take an example. When you try to connect to example.com the first thing you computer does is talk to the DNS servers to ask it what the IP address for example.com is. When the DNS server sees this request it tries to resolve it from right to left. This means it will look up see which servers it knows that have information on .com domain names and pass the request on to those. 


####The DNS centralised vs decentralised paradox
- *Not sure how Galloway-esque we want to go here*
###ICANN
- The Internet Corporation for Assigned Names and Numbers is the body that is responsible for coordinating the maintenance and methodologies of the root name servers and associated databases of the internet.

- They also are responsible for policy development for internationalization of the DNS system, introduction of new generic top-level domains (TLDs), and the operation of root name servers. The numbering facilities ICANN manages include the Internet Protocol address spaces for IPv4 and IPv6, and assignment of address blocks to regional Internet registries. 
<!-- - While TCP/IP is designed to be a decentralised system it is hard for  -->

# Types of Top-Level Domains

- **"original" TLDs**: These are the domains created before the introduction of ICANN. They are the oldest of the top-level domains. 

| **domain** | **use-case** | **who manages it**|
|-----------------------------------------------|
|.com | | |
|.net | | |
|.org| | |
|.edu| | |  
| .mil| | |

- **Country-Code TLDs (ccTLD)**
	- Definitions/Types
		- traditionally use 2 or 3-letter country codes for domains
			- 3-letter codes are reserved for future use but not all are currently in use (which is why no one can get the .and TLD)
		- internationalized (IDN) ccTLDS
			- use native language characters instead of Latin characters
			- not necessarily formal country abbreviations, can also be colloquial terms for countries ( e.g., the domain .السعودية is a colloquial short-form name for Saudi Arabia in Arabic)
	- Acquisition/creation process
		- Initially Jon Postel just used the ISO country-code standards and IANA accepted applications kind of on a goodwill basis, assuming people who represented countries actually did so (see .ly history for example of how this creates dilemmas)
		- ATM all the ISO codes are basically "reserved", to be implemented basically if/when a country representative requests
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
- **Generic Top-Level Domain gTLD**
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

### Dilemmas for All Domains

- How do you price your domain?
- Are there uses you're not OK with? 
- IPv4 / IPv6 oh noes

***

# Top-Level Domain Stories

##.ly
 -	**Deception**
 	- In 1997 Kalil Elwihesi applied for to IANA for responsibility of .ly (the ISO code for libya). He registered it with a libyan address even though he lived in the UK and for several years sold the domain name and kept the profits. The IANA assumed this was going to the Libyan government

 - **Civil Unrest**
  - On March 31 2011, Hadi Naser, CEO of Libyan Spider, came into work to discover all his domains were offline. He quickly discovered that the outage was deliberate: the US-based company which distributed all his content, **Softlayer, had shut him down, apparently on orders from the US Government**. In February, the mass arrest of human rights campaigners in the eastern city of Benghazi had sparked violent protests across the country; in March the UN Security Council authorised NATO air raids on the country. Naser, who taught himself to code while working at an auto spare parts shop, thought he was finished: "It’s hard for me to explain how those three days went for me. I had been working for 10 years and then someone comes and shuts down everything. Completely destroyed 10 years of work... For 3 days I wasn’t able to talk or act or move or think. It’s like if I die it would be better than this thing happening to me."
 - Unfortunately as there are two governments now in Libya, there is a dispute now over the ownership of the current domains which belong to the the government entities." Libya’s two governments, as well as other splinter groups, are competing over the ability to communicate officially via the internet, and in places it comes down simply to who holds the login details: "the government domains are distributed between the two parties and it depends on who has the password which allows them to change the details of the domain.

## .scot
 - 	Scotland needed to get a "letter of no objection" from the UK government because ICANN originally used the ISO list of countries to determine which countries should have a TLD and sctoland doesn't feature in that list.
 
## .cymru
 - Like the minority or unrecognised groups passed over by ISO country codes, minority and non latin languages were also poorly served historically. 
 - Some of this has to do with the fact that until the 1980s the internet used ASCII encoding to display text. ASCII is a 8-bit encoding system that only had remove for characters from the english language. In the early 1980s the unicode standard was developed which is 16-bits long and allowed for the inclusion of all language symbols.
 - In 2014, DotCYM got its wish for a Welsh-language domain, but not for control of it. ICANN created both .cymru and the English-language .wales domains, but they were delegated to Nominet, the English company which runs .uk. To add insult to injury, when Nominet launched its sales websites for the new domains, it used Google Translate to produce the Welsh content.
  
## .yu
 
  - Computer Scientists at the Jožef Stefan Institute in Slovenia, then part of the Socialist Federal Republic of Yugoslavia, registered the .yu domain in 1987. For Yugoslav computer users it had always been difficult to access any international networks: as a non-aligned country in the Cold War, they were not readily welcomed by the European and American networks of the 1970s, nor by their Soviet counterparts. These networks were largely academic: run by other universities and research institutes, based on huge mainframe computers, and running on proprietary, and mostly American, technology. But in the the 1980s a new network started to emerge: ARPANET, which became the Internet we know today.
  
  When SFR Yugoslavia dissolved during the Yugoslav wars beginning in 1991, the republic broke up into several smaller countries. Slovenia and Croatia quickly registered their own TLDs (.si and .hr, respectively, registered in 1993) but through a weird game of governance hot-potato the new Slovenian government now controlled the .yu TLD. and IANA facilitated the transfer fo the TLD from Slovenian hands to the Federal Republic of Yugoslavia via an association at the University of Belgrade. 

  In 2003, the FR Yugoslavia became Serbia and Montenegro, and the .cs ccTLD was registered for the newly named country. However, it didn't really end up going into use. .yu ended up lingering for a while, basically being the only ccTLD that wasn't based on an ISO code. In a way, it kind of didn't make a huge difference since the Serbia and Montenegro split apart in 2006, which led to the creation of the .rs and .me TLDs. In 2007, ICANN handed control of .yu to the Serbian National Register of Internet Domain Names, with the intent of slowly phasing the TLD out and letting the domain expire, which it ultimately did in 2010.  
  
## .io
  - .io is one of the fastest-growing top-level domains on the internet, a particular favourite among start-ups and technology companies. It's also one of the most expensive. To the ear of the tech-savvy, “io” sounds like “input/output”, and it’s used for everything from business software and databases to bitcoin and blogs. But like all the other domains we’ve looked at, .io is also a place: a country-code top-level domain, or ccTLD, which refers to a particular place on the Earth's surface. In this case, that place is the British Indian Ocean Territory, a remote but strategically-important scattering of islands in the middle of the Indian Ocean, also known as the Chagos Archipelago. It consists of seven atolls and over 1,000 tiny islands, and not many people have ever heard of it.

## .sy
 - In July, the Free Syrian Army was formed by defecting officers from the Syrian Armed Forces, and a state of civil war has existed in the country ever since. Hundreds of thousands of Syrians have been killed or imprisoned on both sides, while almost three million have fled across the borders, one of the largest forced migrations since World War Two. 80,000 people are currently housed in the Zaatari refugee camp in Jordan alone.

 - Alongside the humanitarian crisis, one of the ways in which the conflict has been visible to the outside world is through its effect on the internet both inside and outside the country. In 2012, as the rebel groups were making some of their largest early advances against the government, Syria disappeared from the internet almost entirely. On the 29th of November, almost all networks within Syria became inaccessible from the outside world - and what reports did leak out suggested that mobile and landline links inside the country were down as well.

##.george
 - registered by Wal Mart

##.cat

 - Before .cat was available, and given the reluctance of certain Catalan institutions, companies, and people, to use .es, .ad, .fr, .it domains (depending on the state respectively) for their domains, alternatives emerged.[3] An example of this was the website for the city of Girona in Catalonia, which preferred to use a .gi domain ("http://www.ajuntament.gi/", the word "ajuntament" meaning both "city council" and "town hall"), even though .gi is the country code for Gibraltar, instead of the corresponding .es as a Spanish local authori

## .tv
 - The domain is currently operated by dotTV, a Verisign company; the Tuvalu government owns twenty percent of the company. In 1999, Tuvalu negotiated a contract leasing its Internet domain name ".tv" to a company formed by idealab for $50 million in royalties over a 12-year period.[1] The Tuvalu government receives a quarterly payment of US$1 million for use of the top-level domain. With the first $1 million payment the government received, Tuvalu was finally able to afford the $100,000 it cost to join the United Nations. Lou Kerner joined .tv as its CEO in January 2000, and the company began selling .tv domain names in April 2000. Verisign acquired .tv in December 2001