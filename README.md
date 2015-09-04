# pyhotplate
A visualization script for the hotplate problem

I recommend using pypy to run the script, as it can speed things up quite a lot, perhaps by a factor of 3 or more.
The generator requires you to install PyPNG.  You can do that with `pip`:  `pip install pypng`.  

The script pulls data from STDIN as a series of whitespace separated *integers* (it doesn't support floats!).
This means that if your heatmap generator were named `heatmap`, and it output 4096x4096 integer values you could do something like:

    ./heatmap | pypy hotplate.py
    
You'll likely need to modify the script to get it to work for your particular program (you're on your own here!).  

Please submit a pull request if you have any bugfixes or other awesome ideas.

Here is an example output:

![Example Visualization](example_heatmap.png?raw=true)

