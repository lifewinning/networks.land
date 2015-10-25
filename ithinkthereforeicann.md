## I Think Therefore ICANN

### Background

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


### Types of TLDs

- "original" TLDs
	- domains created before ICANN (e.g. .com, .net, .mil)

- ccTLD
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
- gTLD
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
- Domain hacks/Linguistic happenstance for example ".ly"
- Jokes (e.g. winafreebird.com means nothing but is also amazing?)

### Dilemmas for All Domains

- How do you price your domain?
- Are there uses you're not OK with? 
- IPv4 / IPv6 oh noes

### Gameplay notes

- Assumptions
	- fictional, blank slate--none of the countries are real, assumes completely open namespace
- How It Works: 
	- roles and particularities of players assigned to players based on dice throws, documented on paper character forms
	- during each player's turn in a round, they withdraw a situation card (color coded for their particular character) which either gives them a choice of action or just adds/takes away points. 
	- de facto points for all players
		- brands buying namespace gives everyone base set of points
		- "scarcity creep"--with each passing round players get a few more people acquiring domains from them simply because there are less and less cool phrases and domains available
	- if a gTLD player gets an "acquire domain" card and choose to submit an application for a new TLD, other players can contest the acquisition and the game goes to the domain auction. (basically a lightning round where auction participants try to buy the domain)
	- fun fact: the points are mostly meaningless, ICANN always wins 
- Available actions to players
	- ccTLD
		- representative agency for a country
			- apply for ccTLD
			- ban particular uses of TLDs based on national law
			- apply for and acquire internationalized ccTLDs
			- pursue domain hack-type purchases
			- shut down the internet in your own country
			- sell management of ccTLD to outside company (spend the rest of the game basically doing nothing and collecting a portion of sales/point acquisitions)
		- shady dealer "on behalf of" country
	- single-issue gTLD owner
		- nationalist gTLD
			- impose specific uses of the TLD
			- lead secessionist revolts to regain use of your domain
		- cultural/concept gTLD
			- impose specific uses of the TLD
			- contest gTLD hoarder purchases that are too similar to the domain/go to gTLD auction
			- apply for more related gTLDs/expand interests
	- gTLD hoarders
		- apply for more gTLDs
		- contest gTLDs/go to TLD auction
		- impose specific uses of TLDs 


### Gameplay -- Structure

Players are assigned a type of TLD owner--ccTLD, gTLD, or secessionist region seeking a gTLD. Only one player can play as a scessionist region. 

All players begin with a fixed number of points, determined by dice throws. All players have the baseline goal of maintaining 500 points to achieve their gameplay goals. For ccTLDs that means political stability, for gTLDs that means enough points to buy a new domain, and for secessionist regions that means enough political support to obtain their own gTLD. During each round, players select cards that present scenarios that can help them increase their points or will lead them to lose points. 

ccTLD and gTLD players both begin holding 1 TLD. They receive **scarcity bonus** points during each round, the amount of which is determined by a dice throw. These are a reflection of the fact that, as less and less domains are available, certain domains become more acceptable to use or commonly used. gTLDs can buy more TLDs with points over the course of the game. 

Secessionists have only one goal in terms of the game: to get a domain. Once that's achieved, they transition to playing as a gTLD (rather than a ccTLD, as certain governmental secnarios don't really apply to them).  

### Gameplay -- Stories for Cards

#### ccTLDs

- Domain Hack Bonus

This is a set of points reflecting the scenario when a player's TLD becomes more lucrative due to hype around being able to make interesting puns and jokes using it. 

- Contentious Use of Your TLD

This is a scenario in which someone outside of a player's country uses their TLD in a way that doesn't necessarily reflect the country's political or cultural experiences, and the player has to decide whether to allow that use of their TLD or intervene, potentially damaging their TLD's reputation and position on the political stage or damaging their reputation in their country as a political leader. 

**Neat Real-World Example of This**

`.ly`: Violet Blue's "sex-positive URL shortener" vb.ly was deleted by the .ly domain registry in 2010 allegedly for not adhering to regulations for the TLD related to "text referring to adult content and offensive imagery." Basically, pornography is illegal under Libyan law (which is not to say Sharia law, these are different) and although vb.ly was operating outside of Libya, it was still expected to adhere to Libyan law. Later that same year, access to less than four-letter .ly domains became restricted to Libyan residents. 

- Government Collapse!

This is a scenario in which political unrest within your country leads to your country being divided into multiple independent states, leading your current TLD being retired and new rules being established. 

**Neat Real-World Example of This**

`.yu`: - Computer Scientists at the Jožef Stefan Institute in Slovenia, then part of the Socialist Federal Republic of Yugoslavia, registered the .yu domain in 1987. 
  
When SFR Yugoslavia dissolved during the Yugoslav Wars beginning in 1991, the republic broke up into several smaller countries. Slovenia and Croatia quickly registered their own TLDs (.si and .hr, respectively, registered in 1993) but through a weird game of governance hot-potato the new Slovenian government now controlled the .yu TLD. and IANA facilitated the transfer fo the TLD from Slovenian hands to the Federal Republic of Yugoslavia via an association at the University of Belgrade. 

In 2003, the FR Yugoslavia became Serbia and Montenegro, and the .cs ccTLD was registered for the newly named country. However, it didn't really end up going into use. .yu ended up lingering for a while, basically being the only ccTLD that wasn't based on an ISO code. In a way, it kind of didn't make a huge difference since the Serbia and Montenegro split apart in 2006, which led to the creation of the .rs and .me TLDs. In 2007, ICANN handed control of .yu to the Serbian National Register of Internet Domain Names, with the intent of slowly phasing the TLD out and letting the domain expire, which it ultimately did in 2010.  

- Middleman Offer

In this scenario, a ccTLD hands over maintenance and management of their TLD to a third-party operator. They can choose to do this for lots of reasons, though the most common reason is that the country itself lacks the IT infrastructure to actually run a domain registry and needs assistance promoting the TLD. However, this choice comes with caveats--technically the players only receive a percentage of profits from the TLD. 

**Neat Real-World Example**

`.tv`: The domain is currently operated by dotTV, a Verisign company; the Tuvalu government owns twenty percent of the company. In 1999, Tuvalu negotiated a contract leasing its Internet domain name ".tv" to a company formed by idealab for $50 million in royalties over a 12-year period. The Tuvalu government receives a quarterly payment of US$1 million for use of the top-level domain. With the first $1 million payment the government received, Tuvalu was finally able to afford the $100,000 it cost to join the United Nations. Lou Kerner joined .tv as its CEO in January 2000, and the company began selling .tv domain names in April 2000. Verisign acquired .tv in December 2001.

**Another Neat Real-World Example**

A few ccTLDs are managed by middlemen not necessarily by choice or in the service of financial gain or support. Some countries' TLDs were registered early in the TLD creation process, and representatives from that country weren't necessarily able to actually engage in the process. 

`.io`: .io is one of the fastest-growing top-level domains on the internet, a particular favourite among start-ups and technology companies. It refers to the British Indian Ocean Territory, a remote but strategically-important scattering of islands in the middle of the Indian Ocean, also known as the Chagos Archipelago. It consists of seven atolls and over 1,000 tiny islands. 

All Chagossians were driven off the island starting around 1967, when Mauritius was declared independent from the British government and the islands were annexed from Mauritius, and they have not and probably will not ever be allowed to go home. The archipelago's largest island is currently home to a U.S. military base, which has played a pretty cool role in propagating the war on terror.

All this to say, when ccTLDs were being registered Chagossians weren't exactly prepared for it, which is where Paul Kane and the Internet Computer Bureau come in. Kane registered the TLD way back in 1997, and is just now reaping the benefits of the .io TLD. The ICB also manages 2 other British territory TLDs, `.ac` (Ascenion Islands) and `.sh` (St. Helena). Kane has previously stated with regard to the TLDs that "Each of the overseas territories has an account and the funds are deposited there because obviously the territories have expenses that they incur and it’s offsetting that." Whether that's actually true or whether the account Kane describes actually goes to a representative of the Chagossian people is entirely unclear. 

- Political Unrest

While similar to the government collapse scenario, this more typically refers to chaos within a government more like a revolution or coup than confluence of several factions dissolving the nation. Players can choose a few secnarios to resolve or not resolve their conflict. 

**Neat Real-World Examples**

`.sy`: Alongside the humanitarian crisis, one of the ways in which the Syrian conflict has been visible to the outside world is through its effect on the internet both inside and outside the country. In 2012, as the rebel groups were making some of their largest early advances against the government, Syria disappeared from the internet almost entirely. On the 29th of November, almost all networks within Syria became inaccessible from the outside world - and what reports did leak out suggested that mobile and landline links inside the country were down as well.

`.ly`: Libya’s two governments, as well as other splinter groups, are competing over the ability to communicate officially via the internet, and in places it comes down simply to who holds the login details: "the government domains are distributed between the two parties and it depends on who has the password which allows them to change the details of the domain. 

#### Secessionist

- Endorsement Letters

For a non-recognized nation-state or cultural entity to receive a TLD, they have to do a bunch of things. One of those things is submit letters of support from government and cultural bodies, as well as businesses and individuals with a connection to the region or entity seeking a domain. 

**Neat Real-World Examples**

`.cat`: Created in 2005 after extensive lobbying, payment, and the pursuit of letters of support from the Spanish and French governments, this TLD is dedicated to the promotion of Catalonian culture and identity. While it has the potential to be an incredibly lucrative TLD given all the domain hacks that can be applied to it, the requirement that .cat sites promote the Catalonian language in some respect has somewhat limited its expansion. 

`.scot`: Created in 2014 to promote Scottish culture and identity, and kind of a fun detail in the efforts for Scottish secession that came up last year. 

- Third Party Middleman

Sometimes in the process of seeking out a TLD, a secessionist/cultural identity finds themselves scooped. Another gTLD service will basically swoop in and snag the sought-after TLD. This is a huge bummer. 

**Neat Real-World Examples**

`.cymru`: In 2014, the Welsch organization DotCYM got its wish for a Welsh-language domain, but not for control of it. ICANN created both .cymru and the English-language .wales domains, but they were delegated to Nominet, the English company which runs .uk. To add insult to injury, when Nominet launched its sales websites for the new domains, it used Google Translate to produce the Welsh content.

.cymru is also interesting as an example of the limitations of the internet's preferred languages--which is to say, preferred character encodings. Like the minority or unrecognised groups passed over by ISO country codes, minority and non latin languages were also poorly served historically. Some of this has to do with the fact that until the 1980s the internet used ASCII encoding to display text. The expansion of "internationalized" TLDs with Unicode encoding has opened up new possibilities in this space, though honestly the complexity of this topic led us to not really get deep on that for today.

#### gTLD

- Domain Hack Bonus

This is a set of points reflecting the scenario when a player's TLD becomes more lucrative due to hype around being able to make interesting puns and jokes using it. 

- Contentious Use of Your TLD

Similar to the ccTLD scenario, but generally the politics have less to do with cultural identities and more to do with money and power.

**Neat Real-World Examples**

`.sucks`: The Canadian company Momentous acquired the .sucks TLD in 2014 after a private auction between the company and fellow gTLD purveyor Donuts. It's been mired by concerns over defamation and intellectual property for reasons that are probably pretty self-evident (also, Saudi Arabia's Communications and Information Technology Commission filed an objection to the TLD because of the possibility it might be used for pornographic sites, shruggie). 

Momentous, through their subsidiary Vox Populi, in some ways is kind of just running an extortion scheme through this TLD. During the "sunrise" registration period for the TLD they set up a "Trademark Clearinghouse" as a mechanism for allowing corporations to register a .sucks domains in advance--at the price of about $2500 a domain. (Stories about this TLD like to note how Taylor Swift has already acquired taylorswift.sucks, which like, *of course she has*.) 

- Acquisition Round

This is the round where players can obtain more gTLDs. Most gTLDs are owned by a select number of companies, basically because it's a pretty expensive process to even request a TLD let alone receive it. Usually, these gTLDs are registered by wholly owned subsidiaries of the larger companies. 