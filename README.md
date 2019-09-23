# QA Automation Engineer Challenge
First of all I wanted to thank you all for taking the time to consider and review my code challenge!

## How to run
Standing in the root folder, you just need to first build the docker image for the test:
```
docker build . --tag test
```
Note: I added a tag for practicity, it is later used in docker-compose
Then, we run the docker compose file which has the selenium hub and our tests image
```
docker-compose up
```
And that's it! you can view the logs for the test image to see exactly what's happening

## Notes and comments
- I created this whole project in Python (3) because it is the language I am the most comfortable with. The first challenge said that we could use any tool but the rest specified some js frameworks/libraries I am not really confident in or even have experience with at all. Since I didn't have much time to do this, I chose the one that was easier for me.
- For the third challenge, the test does not run on an specific board, as it only does with the first one available. To be completely honest I didn't have much time to create these tests and I could wrap my head around the trello site to select an specific board. The test does run independently on the data provided in /src/utils/data.json file, but it does not specify a board to run in.
- Some comments/things I would add if I had more time/the necessary skills:
  - The test could generate a token by itself, as I provided one in the data.json file 
  - The docker image could be custom, both the selenium ones and the one with the tests. The docker compose file calls docker hub images and while this is a common thing, there are things I would do myself if I could.
  - The setup methods could be more complex, I really simplified the pytest fixtures for the sake of simplicity. They do their job but I am well aware that they are not as optimal.
  
The net work time I employed of this project was around 5-6 hs.
