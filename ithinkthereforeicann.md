## I Think Therefore ICANN

### Background

####Why do we need domain names?

- DNS allows us to translate computer IP addresses to human readable urls. Its easier to remember google.com than 139.130.4.5. When the Internet was small the network maintained a plain text file called HOSTS.txt	which was the master list of the mappings of hosts to IP addresses. As the network scaled this approach became impractical. The DNS protocol was created to deal with this problem.
- Domain names make the internet a whole lot easier and a whole lot more fun, but the process that creates them entails a lot of weird complicated things
- During the late 70s and early 80s In the early days of the HOSTS.txt

####How does it work?

- The mappings of domain names to IP addresses are stored in a distributed network of servers. DNS is stored in a reverse tree like heirarchal structure. 
- Another example of such a structure is when you look for a book in the library. If you told the librarian the authors name they will most likely first lookup the last name and then try and then sort for the first name. DNS works similarly but instead of one librarian imagine you had a network of librarians all focusing on specific sub sections of the titles.
- Lets take an example. When you try to connect to example.com the first thing you computer does is talk to the DNS servers to ask it what the IP address for example.com is. When the DNS server sees this request it tries to resolve it from right to left. This means it will look up see which servers it knows that have information on .com domain names and pass the request on to those. 

####The DNS centralised vs decentralised paradox
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