
Lets start with model of Products
with attributes: ID
                 Short Description,
				 Long Description,
				 Minimun Amount Of Products Per Sale,
				 Cost Price,
				 Sale Price,
and model of Sales
with attributes:ID,
                Short Description,
				Long Description,
				Sale Price,
				Date of Sale,
				Number of Document,
			    where Short and Long Description, and Sale Price it's from Products model so that they a foreign keys.
This will be our first step of database migrations
 so our tables are Products and sales