# db design

DB Design
Design decision, this is not a fully multi-tenant app because there's some part
that is not completely separated. Despite that I have created a Provider model
that will be used to query each co. details from the db. Therefore the starting point
is the Provider, each model has to be linked to the provider. It is an expensive approach
but the requirements of the application demands it.

The user model for employees and providers will be different, they will have completely different
control levels.

14/12/23
I have disabled the feature to enable new clients from registering directly and use the app because the
app heavily relies on Mpesa api. I have also noted many vendors are ditching mpesa for mobile banking services
due to cost associated therefore I have to provide various payment options for receiving cash. I might develop a
payment app seperately that is integrated with banks and mpesa services.

15/12/23
The userserilizer will be used to create the partner instance but first they must be registered
The endpoint will return a token that will identify the client devices so
that they can create the partner instance.
