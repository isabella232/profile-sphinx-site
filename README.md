# profile-sphinx-site

A tiny repository to profile a Sphinx site. It is packaged with two things:

1. A small documentation build (copied from the pydata bootstrap theme)
2. A python script that generates this documentation using Sphinx

# How to use the site

1. Install the requirements:

   ```
   pip install requirements.txt
   ```
2. Run py-spy on the build script:

   ```
   py-spy record -o profile.svg -- python build.py
   ```

This will run the profiler a bunch of times...simply ctrl+c when you want it to finish
and then an SVG should exist showing you the flame graph of running the code.
