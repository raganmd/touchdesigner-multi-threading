# TouchDesigner Multi-Threading

A look at how to use multiple threads in python with TouchDesigner
## Contributing Programers / Artists ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## Three Examples 

`text_pyThreads`  
A simple example of creating a function that runs in another thread. As noted in the forum reference post it's important to consider what operations can potentially create race conditions in Touch. The suggested consideration here is to avoid the use of any operations that will interact with a touch Object. Looking more closely at this example we can see here that we're using only Pythonic approaches to editing an external file. In our first example we use a simple text file approach to ensure that we have the simplest possible exploration of a concept.

`text_pyThreads_openCV`  
In the opeCV example we look at how one might consider taking the approach of working with image processing through the openCV library. While this example only creates a random red circle, with a little imagination we might see how this would be useful for doing an external image processing pass - finding image features, identifying colors, etc. Running this as a for loop makes it easy to see how this process can block TouchDesigner's main thread, and why it would be useful to have a means of executing this function in a way that minimizes impact on the running project.

`text_pyThreads_queue`  
While the example `pyThreads_opneCV` is an excellent start, that doesn't help us if we need to know when an outside operation has completed. The use of Queue helps resolve this issue. A Queue object can be placed into storage and act as an interchange between threads. It's marked as a thread safe operation, and in our case is used to help track when we're working function is "Processing" or "Ready". You'll notice that the complications here are that we have a less than ideal need to use an execute DAT to run a frame start script to check for our completed status each frame. This is less than ideal but a reasonable solution for an otherwise blocking operation. Notice that the execute DAT will disable the operation of the frame start script after it's "Ready". This kind of approach helps to ensure that the execute DAT only runs the frame start script when necessary and not every frame. 

## Forum Example  
[Forum Example 1](https://www.derivative.ca/Forum/viewtopic.php?f=4&t=5396&p=28538&hilit=multithreading+example&sid=d472f763f47c228695ff7b567f22afd8#p28538)
`python_threading_sample.toe`  

An example from the forum used to sort out the essential pieces of working with multiple threads, queues, and how to approach this issue without crashing Touch. Many thanks to the original authors for their work helping to shed some light on this murkey part of working in TouchDesigner.