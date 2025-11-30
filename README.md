Friends asked me to sketch out the architecture of website to exchange retal houses between two main tenants.

In such system we consider:
- the properties (the rental house/rental contract)
- the tenants (who submit their property)
- property owner (approvers)
- administrative user of the website

A deal is struck when 2 parties agree to exchange and
when the property owner(s) agree that the exchange is valid.
- no stance yet on when a property has multiple owners (how does that approval work - lets leave this constraint out in first iteration)

The system is only designed to bring tenants together and to "lock" the intention of their exchange.

The website - in terms of dialogue - should be "similar" to funda.nl, which means: 
- the property is the central object 
- the property goes through state phases.
- tenants and property owners change the state of the properties

The system is designated for the Dutch market.

Property owners are automatically signed up via a chamber of commerce land and enabled after an approval by the owner itself. This could be via a signup link and an explanation that a tenant wants to exchange his contract with another tenant.

Tenants will signup manually via email-verification and subsequently are asked to perform a 0.01cent iDEAL transaction, to "validate", that they are living in the property they want to exchange.
Refunding could be an option.
iDEAL transaction will reveal zipcode, housenumber and "tenant" itself (could still be bogus, but that's okay)

This registration is not a 100% guarantee from a legal perspective at all. The purpose is: the registration captures who is behind the transaction and the supposed tenant and if there is a mismatch, the party is already rejected in an early phase. It is to reduce noise by identifying the person who performed the payment. Final validation is performed by the property owner.

This will reduce annoyance under property owners and prevents a website full of bogus assets/lending contracts. Keep in mind: the owner of the property knows its tenants, so if something sips through, the owner of this website will contacted by the property owner and take action (block/removal)

Can you sketch out such a system.
What are the object-models, state-diagrams and overall architecture sketch.
Can you give advise on the front-end and back-end (Flask/FastCGI) and database. I would expect either MongoDB or MySQL/PostGresSQL. Given the simplicity of the datamodel and the RestAPI support, my initial direction would be MongoDB (RestAPI and JSON are nowadays tightly coupled).

Could you fleshout userstories for Signup and user acquiring a property and tenant approving a property.
7 days after an approval, the property should be not visible/removed from the website.

