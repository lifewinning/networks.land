# networks.land
Resources for and documentation of lesson plans and activities for explaining internet infrastructure to people. 

## TODO

+ add images to lesson plans? (possibly add an `image` tag to YAML so index of lesson plans will have an image too?s)
+ edit copy on lesson plans so they can clearly stand alone
+ style guide on resources and lesson plans: some have horizontal rule line breaks, some don't, some are more narrative, some are full of bullet points--tbh I don't really care what it looks like but we just need to pick something legible and stick with it
+ add PDF versions of each lesson plan
+ edit copy on TLD game so it makes any kind of sense
+ longer "about" copy with images (this can be the last thing really)

## Site Structure Things That I'll Probably Forget To Explain If I Don't Write It Down

Because we are lazy and CMSes are dumb, most of the sub-foldering and structuring of these pages ended up being a matter of some kind of janky YAML choices. 

If a markdown file is supposed to appear on the website, it needs YAML front matter. If it's in this repo more for reference, it shouldn't have front matter. 

Each page should have the following front matter defined: 

```
layout
title
category 
```

Right now, these are the available options to add for `category`:

+ `reference`: documentation that defines and explains high-level concepts in human speak (or attempts to)
+ `activities`: lesson plans and game rules--the stuff we actually made
+ `header`: basically this is a page that either acts as an index for other pages or a page that needs to appear in the header nav (the "about" page, for example, which has no subpages, or the "resources" page). 
+ if a page is a category: "header" page and is going to have subpages, its YAML is a little different and looks like this: 

```
layout
title
category
permalink
header
```

+ the `permalink` tag is just to make things look pretty. 
+ the `header` tag is there basically to be able to match sub-category pages to this page using this lazy snippet: 


```
{% for p in site.pages %}
	{% if p.category == page.header %}
	<a class="page-link" href="{{ p.url | prepend: site.baseurl }}">{{ p.title }}</a>
	{% endif %}
{% endfor %}
```

+ if a page doesn't have subpages, it doesn't need the `header` tag. 

I am undecided right now whether we need sub-sub pages (e.g., should all the "what is the internet made of" lesson plans actually be broken out?)



for batching image resize with imagemagick

<!--`for file in *.jpg; do convert $file -resize 1024 ../images-ouput/$file; done`-->
`python convert.py` for batch converting images in `non-web-stuff/images-raw`