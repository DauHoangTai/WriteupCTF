# Solution - yana

- site is hosted on github pages with a custom domain that has a wildcard A record pointing to github pages
- this allows anyone to register a subdomain of yana.wtf by making a github pages site
- This allows us to load the page and bring the success or failure image into the cache
- we can then use fetch with abortcontroller to check if it's cached, and if so, invalidate it
- cache partitioning is bypassed since we're SameSite


# Cheese solution
- monitor crt.sh to find other people's gh pages payloads
- yoink one & modify it
