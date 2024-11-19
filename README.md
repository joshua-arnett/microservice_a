# microservice_a

My project:

I’m developing a program which takes someone’s favorite (or just randomly selected) hockey team and then notifies them if there’s a game available to attend depending on the date and time they’re in a certain location. It will also provide transportation, weather and ticket price updates.

I’m using a text-based python format to make it as simple as possible.

At this stage I’m looking for a microservice which scrapes a given teams schedule and returns the date, time and location to match it against the user selection which for this is only a date range and preferred team. The program will then only notify the user that a match exists based on their location.

This would be followed, if the user selects to do more research with the current projected weather, ticket price and transportation costs. 

Lastly, an update service if the costs or game start change.
