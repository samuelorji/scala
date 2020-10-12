# scala-zone-content
Repository used for storing content and metadata of Scala Zone lessons. 
 - Every commit to `develop` brach updates the cloud storage content on development environment.
 - Every commit to `stage` brach updates the cloud storage content on production environment.
 - Every commit to `master` brach updates the cloud storage content on production environment.
 
# Updating content
In order to update content on the website, you shall update the branch corresponding to the environment you intend to update. After the triggered GH action flow succeedes, you have to call the /api/courses/update endpoint on the frontend URL to pull new content from cloud storage. For this call to succeed, you need to make this request authenticated with keycloak token with admin role. 
 
