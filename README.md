# QA Automation Engineer Challenge
First of all I wanted to thank you all for taking the time to consider and review my code challenge!

## How to run
NOTE: I'm assuming you have docker up to date and running on your computer.

Standing in the root folder, you just need to run the docker compose file:
```
docker-compose up
```
And that's it! docker compose will take care of pulling the images and running the containers. 

NOTE: this process my take some time depending on your internet connection. Also the building of the test image will take a little bit when installing the numpy Python package, but don't worry, this is a normal behavior, since this package needs to be compiled while creating the image. Hang in there!

There are two containers, one for a selenium standalone chrome server, and the other containing the tests. Both logs will appear on your terminal at the same time. If you want to see the logs for the test container alone you have to run the following command:
```
docker logs digitalhubuae_tests_1
```

## Notes and comments
- I created this whole project in Python (3) because it is the language I am the most comfortable with. The first challenge said that we could use any tool but the rest specified some js frameworks/libraries I am not really confident in or even have experience with at all. Since I didn't have much time to do this, I chose the one that was easier for me.
- For the third challenge, the test does not run on an specific board, as it only does with the first one available. To be completely honest I didn't have much time to create these tests and I couldn't wrap my head around the trello site to select an specific board. The test does run independently on the data provided in /src/utils/data.json file, but it does not specify a board to run in.
- **Important note:** if for any reason the test fails, try running `docker-compose up` again in the root directory. This is because the test container needs the chrome one to be up before it tries to connect to it, logically. I added a small sleep time on the setup method of front end tests for this not to happen. Again, this could be solved in a more fancy way, but I just wanted to make sure it ran successfuly. It should not fail since I added this, but I found that it still sometimes does. Better safe than sorry. (you can also take 20 seconds out of the final running time :) )
- If you need the credentials for the account used, they are the following:
```
email: qacodechallenge@gmail.com
password: p4ssw0rd
```
- Some comments/things I would add if I had more time/the necessary skills:
  - The test could generate a token by itself, as I provided one in the data.json file 
  - The docker image could be custom, both the selenium ones and the one with the tests. The docker compose file calls docker hub images and while this is a common thing, there are things I would do myself if I could.
  - Also, on the subject of the docker images, the data.json file could be mounted in a volume so that it does not require for the image to be built every time you need to run tests. But I made it this way for the sake of simplicity.
  - If needed, a selenium grid service could be mounted, so that the tests are run in both chrome and firefox at the same time, to say the least. You can also implement a lot of different scenarios with this setup, but again, for simplicity reasons, I only created a selenium standalone server.
  - The setup methods could be more complex, I really simplified the pytest fixtures for the sake of simplicity. They do their job but I am well aware that they are not as optimal.
  - The logging is made through STDOUT (print statements). Of course a more complex logging could be made, but this was the most optimal and lightweight way to implement it for this project.
  
The net work time I employed on this project was around 5-6 hs.
