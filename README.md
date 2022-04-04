# Video Analysis

Attempting to analyze video from a Raspberry Pi for fun. The inspiration behind comes from a few sources.
First, I had a question about whether I could calculate the speed of a vehicle from a video. This way we could do some very interesting analysis such as tracking the average speed 
of vehicle going down our street, or finding outliers.

The second reason is for tracking usage of mountain bike trails. I have looked at quite a few ways to track usage of mountain bike trails and the problem always comes back to "how do you recognize 
a person on a bike?" This is interesting because animals may also use the trails and mess up the results, so something like a motion detector would get false positives. In retrospect, I should have 
narrowed down the scope of that particular project. Oh well.

For this we are going to have a few objectives. Not all of them are critical.

** Video Streaming **
1.) Stream video from an input device on computer (webcam) - critical
2.) Stream video from an input device on local network  (local wifi)
3.) Stream video from an input device over internet

** Video processing **
1.) Process video on local machine - critical
2.) Ability to identify people and vehicles - critical
3.) Ability to count the instances of people - important
4.) Ability to track the speed of vehicles across an video.

** Data Storage **
1.) Store the instance of people
2.) Store the speed of vehicles
3.) Correlate speed and images of vehicles

** Data Display **
1.) Display number of people spotted over time
2.) Display the average speed of vehicles over time
3.) Find speed outliers in vehicle data
 
# Dev Diary

That's right, we're creating a dev diary for this project!

## Day 1

Initial Ideation and proof of concept. For the first go, I'll be starting with just trying to find people. Mainly because
I have a camera built into my computer that looks at a person all the time.

We will, of course, be using my favorite source of learning: https://pythonprogramming.net/loading-images-python-opencv-tutorial/

